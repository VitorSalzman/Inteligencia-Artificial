import random
import numpy as np
import math

W = 0.5
c1 = 0.15
c2 = 0.15

n_iterations = int(input("Inform the number of iterations: "))
target_error = float(input("Inform the target error: "))
n_particles = int(input("Inform the number of particles: "))


class Particle():
    def __init__(self):
        self.position = np.array([(-1) ** (bool(random.getrandbits(1))) * random.random() * 512,
                                  (-1) ** (bool(random.getrandbits(1))) * random.random() * 512])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0, 0])

    def move(self):
        self.position = self.position + self.velocity


class Space():

    def __init__(self, target, target_error, n_particles):
        self.target = target
        self.target_error = target_error
        self.n_particles = n_particles
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([random.random() * 50, random.random() * 50])

    def print_particles(self):
        for particle in self.particles:
            print("I am at {} my pbest is {} and my fitness is {}".format(particle.position,particle.pbest_position,self.fitness(particle)))

    def fitness(self, particle):
        x = particle.position[0]
        y = particle.position[1]

        a = -(y + 47)
        b = math.sin( (abs((x/2) + (y+47)))**(1/2) )
        c = x * math.sin( (abs(x - (y+47)))**(1/2))
        return a*b-c

    def set_pbest(self):
        for particle in self.particles:
            fitness_cadidate = self.fitness(particle)
            if (particle.pbest_value > fitness_cadidate):
                particle.pbest_value = fitness_cadidate
                particle.pbest_position = particle.position

    def set_gbest(self):
        for particle in self.particles:
            best_fitness_cadidate = self.fitness(particle)
            if (self.gbest_value > best_fitness_cadidate):
                self.gbest_value = best_fitness_cadidate
                self.gbest_position = particle.position

    def move_particles(self):
        for particle in self.particles:
            global W
            new_velocity = (W * particle.velocity) + (c1 * random.random()) * (
                        particle.pbest_position - particle.position) + \
                           (random.random() * c2) * (self.gbest_position - particle.position)
            particle.velocity = new_velocity
            particle.move()


search_space = Space(1, target_error, n_particles)
particles_vector = [Particle() for _ in range(search_space.n_particles)]
search_space.particles = particles_vector
search_space.print_particles()

iteration = 0
while (iteration < n_iterations):
    search_space.set_pbest()
    search_space.set_gbest()

    if (abs(search_space.gbest_value - search_space.target) <= search_space.target_error):
        #condição de parada
        break

    search_space.move_particles()
    iteration += 1

# f(512,404.2319) = -959.6407
print("The best solution is: {} in n_iterations: {}".format(search_space.gbest_position,iteration))