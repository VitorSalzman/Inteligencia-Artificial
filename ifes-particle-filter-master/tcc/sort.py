"""
    SORT: A Simple, Online and Realtime Tracker
    Copyright (C) 2016 Alex Bewley alex@dynamicdetection.com
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from __future__ import print_function

from numba import jit
import os.path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from skimage import io
from scipy.optimize import linear_sum_assignment
import glob
import time
import argparse

class Particle:

    def __init__(self, pos_x, pos_y, velocity, theta, weight):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocity = velocity
        self.theta = theta
        self.weight = weight
        self.resample_weights = (0, 0)

class ParticleBoxTracker(object):

    """
    This class represents the internel state of individual tracked objects observed as bbox.
    """
    count = 0
    def __init__(self, bbox):
        """
        Initialises a tracker using initial bounding box.
        """
        self.id = ParticleBoxTracker.count
        ParticleBoxTracker.count += 1
        self.state = convert_bbox_to_z(bbox)
        #self.objclass = bbox[6]

        self.time_since_update = 0
        self.history = []
        self.hits = 0
        self.hit_streak = 0
        self.age = 0

        self.min_vel = -500.0
        self.max_vel = 500.0
        self.num_of_particles = 100
        self.velo_stdev = 200.0
        self.theta_stdev = 0.5
        self.delta_time = 0.05
        self.particles = [Particle(self.state[0], self.state[1], np.random.uniform(low = self.min_vel, high = self.max_vel), np.random.uniform(low = -np.pi, high = np.pi), 1./self.num_of_particles) for i in range(self.num_of_particles)]

    def copy_particle(self, particle):
        """
        Create a copy of a particle
        """
        return Particle(particle.pos_x, particle.pos_y, particle.velocity, particle.theta, particle.weight)

    def mean_pos(self, particles):
        """
        Get the mean position of the particles.

        Parameters
        ----------
        state : ndarray
            Array of Particles

        Returns
        -------
        ndarray

        """
        sum_x = 0.
        sum_y = 0.

        for particle in particles:
            sum_x += particle.pos_x
            sum_y += particle.pos_y

        return (sum_x/self.num_of_particles, sum_y/self.num_of_particles)

    def mean_weight(self, particles):
        """
        Get the mean weight of the particles.

        Parameters
        ----------
        state : ndarray
            Array of Particles

        Returns
        -------
        ndarray
        """
        sum_weight = 0.

        for particle in particles:
            sum_weight += particle.weight

        return sum_weight/self.num_of_particles

    def calculate_weight(self, particle, center):
        """
        Calculates the weight of the particle by the distance from the center of bbox

        """
        dist_x = particle.pos_x - center[0]
        dist_y = particle.pos_y - center[1]

        dist = np.sqrt((dist_x*dist_x)+(dist_y*dist_y))

        return np.exp(-dist)

    def get_particle_by_reference_weight(self, reference, particles):
        """
        Get a particle in the distribution using a reference weight
        """
        if reference >= 1:
            return particles[self.num_of_particles-1]
        else:
            for i in range(self.num_of_particles):
                if reference >= particles[i].resample_weights[0] and reference < particles[i].resample_weights[1]:
                    return particles[i]

    def resample(self, particles):
        """
        Creating a new sample sorting particles with weigth importance
        """
        for i in range(self.num_of_particles):
            # Setting the boundings of particles
            if i == 0:
                particles[i].resample_weights = (0,particles[i].weight)
            else:
                particles[i].resample_weights = (particles[i-1].resample_weights[1],particles[i-1].resample_weights[1]+particles[i].weight)

        reference = np.random.random() # First particle will be  random particle

        k = self.mean_weight(particles) # Mean of the weights

        new_sample = []
        for i in range(self.num_of_particles):

            if reference > 1: # Making a "circular" effect on the array
                reference -= 1

            new_particle = self.copy_particle(self.get_particle_by_reference_weight(reference,particles))
            new_sample.append(new_particle)
            reference += k

        return new_sample

    def motion_model(self, particles):
        """

        """
        for particle in particles:
            new_theta = particle.theta + np.random.normal(0., self.theta_stdev)

            new_velocity = particle.velocity + np.random.normal(0., self.velo_stdev)
            if (new_velocity > self.max_vel):
                new_velocity = self.max_vel
            elif (new_velocity < self.min_vel):
                new_velocity = self.min_vel

            new_x = particle.pos_x + (particle.velocity * self.delta_time * np.cos(particle.theta))
            new_y = particle.pos_y + (particle.velocity * self.delta_time * np.sin(particle.theta))

            particle.pos_x = new_x
            particle.pos_y = new_y
            particle.velocity = new_velocity
            particle.theta = new_theta

        return particles

    def observation_model(self, particles, measurement):
        """
        """
        sum_weight = 0.0

        for particle in particles:
            particle.weight = self.calculate_weight(particle, measurement)
            sum_weight += particle.weight

        # Normalizing the weights
        for particle in particles:
            particle.weight = particle.weight/sum_weight

        return particles

    def get_state(self):
      """
      Returns the current bounding box estimate.
      """
      return convert_x_to_bbox(self.state)

    def predict(self):
        """
        Advances the state of the particles and returns the predicted bounding box estimate.
        """
        self.particles = self.motion_model(self.particles)
        mena_position = self.mean_pos(self.particles)
        x_bbox = [mena_position[0], mena_position[1], self.state[2], self.state[3]]

        self.age += 1
        if(self.time_since_update>0):
          self.hit_streak = 0
        self.time_since_update += 1
        self.history.append(convert_x_to_bbox(x_bbox))
        return self.history[-1]

    def update(self, det):
        self.time_since_update = 0
        self.history = []
        self.hits += 1
        self.hit_streak += 1

        det = convert_bbox_to_z(det)
        particles = self.observation_model(self.particles, det)
        self.particles = self.resample(particles)
        pos = self.mean_pos(self.particles)
        self.state[0] = pos[0]
        self.state[1] = pos[1]
        self.state[2] = det[2]
        self.state[3] = det[3]

def iou(det,trk):
  """
  Computes IOU between two bboxes in the form [x1,y1,x2,y2]
  """
  xx1 = np.maximum(det[0], trk[0])
  yy1 = np.maximum(det[1], trk[1])
  xx2 = np.minimum(det[2], trk[2])
  yy2 = np.minimum(det[3], trk[3])
  w = np.maximum(0., xx2 - xx1)
  h = np.maximum(0., yy2 - yy1)
  wh = w * h
  o = wh / ((det[2]-det[0])*(det[3]-det[1]) + (trk[2]-trk[0])*(trk[3]-trk[1]) - wh)
  return(o)

def convert_bbox_to_z(bbox):
  """
  Takes a bounding box in the form [x1,y1,x2,y2] and returns z in the form
    [x,y,s,r] where x,y is the centre of the box and s is the scale/area and r is
    the aspect ratio
  """
  w = bbox[2]-bbox[0]
  h = bbox[3]-bbox[1]
  x = bbox[0]+w/2.
  y = bbox[1]+h/2.
  s = w*h    #scale is just area
  r = w/float(h)
  return np.array([x,y,s,r]).reshape((4,1))

def convert_x_to_bbox(x,score=None):
  """
  Takes a bounding box in the centre form [x,y,s,r] and returns it in the form
    [x1,y1,x2,y2] where x1,y1 is the top left and x2,y2 is the bottom right
  """
  w = np.sqrt(x[2]*x[3])
  h = x[2]/w
  if(score==None):
    return np.array([x[0]-w/2.,x[1]-h/2.,x[0]+w/2.,x[1]+h/2.]).reshape((1,4))
  else:
    return np.array([x[0]-w/2.,x[1]-h/2.,x[0]+w/2.,x[1]+h/2.,score]).reshape((1,5))

def associate_detections_to_trackers(detections,trackers,iou_threshold = 0.3):
  """
  Assigns detections to tracked object (both represented as bounding boxes)
  Returns 3 lists of matches, unmatched_detections and unmatched_trackers
  """
  if(len(trackers)==0):
    return np.empty((0,2),dtype=int), np.arange(len(detections)), np.empty((0,5),dtype=int)
  iou_matrix = np.zeros((len(detections),len(trackers)),dtype=np.float32)

  for d,det in enumerate(detections):
    for t,trk in enumerate(trackers):
      iou_matrix[d,t] = iou(det,trk)
  matched_indices = linear_sum_assignment(-iou_matrix) # Hungariaan algorithm
  matched_indices = np.concatenate((matched_indices[0].reshape(-1,1), matched_indices[1].reshape(-1,1)),axis=1)

  unmatched_detections = []
  for d,det in enumerate(detections):
    if(d not in matched_indices[:,0]):
      unmatched_detections.append(d)
  unmatched_trackers = []
  for t,trk in enumerate(trackers):
    if(t not in matched_indices[:,1]):
      unmatched_trackers.append(t)

  #filter out matched with low IOU
  matches = []
  for m in matched_indices:
    if(iou_matrix[m[0],m[1]]<iou_threshold):
      unmatched_detections.append(m[0])
      unmatched_trackers.append(m[1])
    else:
      matches.append(m.reshape(1,2))
  if(len(matches)==0):
    matches = np.empty((0,2),dtype=int)
  else:
    matches = np.concatenate(matches,axis=0)

  return matches, np.array(unmatched_detections), np.array(unmatched_trackers)

class Sort(object):
  def __init__(self,max_age=1,min_hits=3):
    """
    Sets key parameters for SORT
    """
    self.max_age = max_age
    self.min_hits = min_hits
    self.trackers = []
    self.frame_count = 0

  def update(self,dets):
    """
    Params:
      dets - a numpy array of detections in the format [[x1,y1,x2,y2,score],[x1,y1,x2,y2,score],...]
    Requires: this method must be called once for each frame even with empty detections.
    Returns the a similar array, where the last column is the object ID.
    NOTE: The number of objects returned may differ from the number of detections provided.
    """
    self.frame_count += 1
    #get predicted locations from existing trackers.
    trks = np.zeros((len(self.trackers),5))
    to_del = []
    ret = []
    for t,trk in enumerate(trks):
      pos = self.trackers[t].predict()[0] # Advances the state vector and returns the predicted bounding box estimate.
      trk[:] = [pos[0], pos[1], pos[2], pos[3], 0]
      if(np.any(np.isnan(pos))):
        to_del.append(t)
    trks = np.ma.compress_rows(np.ma.masked_invalid(trks))
    for t in reversed(to_del):
      self.trackers.pop(t)
    matched, unmatched_dets, unmatched_trks = associate_detections_to_trackers(dets,trks)

    #update matched trackers with assigned detections
    for t,trk in enumerate(self.trackers):
      if(t not in unmatched_trks):
        d = matched[np.where(matched[:,1]==t)[0],0]
        trk.update(dets[d,:][0])

    #create and initialise new trackers for unmatched detections
    for i in unmatched_dets:
        trk = ParticleBoxTracker(dets[i,:])
        self.trackers.append(trk)
    i = len(self.trackers)
    for trk in reversed(self.trackers):
        d = trk.get_state()[0]
        if((trk.time_since_update < 1) and (trk.hit_streak >= self.min_hits or self.frame_count <= self.min_hits)):
          #ret.append(np.concatenate((d,[trk.id+1], [trk.objclass])).reshape(1,-1)) # +1 as MOT benchmark requires positive
          ret.append(np.concatenate((d,[trk.id+1])).reshape(1,-1)) # +1 as MOT benchmark requires positive
        i -= 1
        #remove dead tracklet
        if(trk.time_since_update > self.max_age):
          self.trackers.pop(i)
    if(len(ret)>0):
      return np.concatenate(ret)
    return np.empty((0,5))

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='SORT demo')
    parser.add_argument('--display', dest='display', help='Display online tracker output (slow) [False]',action='store_true')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    # all train
    sequences = ['PETS09-S2L1','TUD-Campus','TUD-Stadtmitte','ETH-Bahnhof','ETH-Sunnyday','ETH-Pedcross2','KITTI-13','KITTI-17','ADL-Rundle-6','ADL-Rundle-8','Venice-2']
    args = parse_args()
    display = args.display
    phase = 'train'
    total_time = 0.0
    total_frames = 0
    colours = np.random.rand(32,3) #used only for display
    if(display):
        if not os.path.exists('mot_benchmark'):
            print('\n\tERROR: mot_benchmark link not found!\n\n    Create a symbolic link to the MOT benchmark\n    (https://motchallenge.net/data/2D_MOT_2015/#download). E.g.:\n\n    $ ln -s /path/to/MOT2015_challenge/2DMOT2015 mot_benchmark\n\n')
            exit()
        plt.ion()
        fig = plt.figure()

    if not os.path.exists('output'):
        os.makedirs('output')

    for seq in sequences:
        mot_tracker = Sort() #create instance of the SORT tracker
        seq_dets = np.loadtxt('data/%s/det.txt'%(seq),delimiter=',') #load detections
        with open('output/%s.txt'%(seq),'w') as out_file:
            print("Processing %s."%(seq))
            for frame in range(int(seq_dets[:,0].max())):
                frame += 1 #detection and frame numbers begin at 1
                dets = seq_dets[seq_dets[:,0]==frame,2:7]
                dets[:,2:4] += dets[:,0:2] #convert to [x1,y1,w,h] to [x1,y1,x2,y2]
                total_frames += 1

                if(display):
                    ax1 = fig.add_subplot(111, aspect='equal')
                    fn = 'mot_benchmark/%s/%s/img1/%06d.jpg'%(phase,seq,frame)
                    im =io.imread(fn)
                    ax1.imshow(im)
                    plt.title(seq+' Tracked Targets')

                start_time = time.time()
                print(dets)
                trackers = mot_tracker.update(dets)
                cycle_time = time.time() - start_time
                total_time += cycle_time

                for d in trackers:
                    print('%d,%d,%.2f,%.2f,%.2f,%.2f,1,-1,-1,-1'%(frame,d[4],d[0],d[1],d[2]-d[0],d[3]-d[1]),file=out_file)
                    if(display):
                        d = d.astype(np.int32)
                        ax1.add_patch(patches.Rectangle((d[0],d[1]),d[2]-d[0],d[3]-d[1],fill=False,lw=3,ec=colours[d[4]%32,:]))
                        ax1.set_adjustable('box')

                if(display):
                    fig.canvas.flush_events()
                    plt.draw()
                    ax1.cla()

    print("Total Tracking took: %.3f for %d frames or %.1f FPS"%(total_time,total_frames,total_frames/total_time))
    if(display):
        print("Note: to get real runtime results run without the option: --display")
