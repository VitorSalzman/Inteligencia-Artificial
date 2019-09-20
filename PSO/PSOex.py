import random
import numpy as np
import math

c1 = 2.5
c2 = 2.5

n_iterations = int(input("Inform the number of iterations: "))
n_particles = int(input("Inform the number of particles: "))


class Particle():
    def __init__(self):
        self.position = np.array([(-1) ** (bool(random.getrandbits(1))) * random.random() * 512,
                                  (-1) ** (bool(random.getrandbits(1))) * random.random() * 512])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([(-1) ** (bool(random.getrandbits(1))) * random.random() * 77,
                                  (-1) ** (bool(random.getrandbits(1))) * random.random() * 77])

    def move(self):
        caminha = self.position + self.velocity
        for i in range(len(caminha)):
            if caminha[i] > 512:
                caminha[i] = 512
                self.velocity = np.array([float(0.0),float(0.0)])
            elif caminha[i] < -512:
                caminha[i] = -512
                self.velocity = np.array([float(0.0),float(0.0)])

        self.position = caminha


class Space():

    def __init__(self, n_particles):
        self.n_particles = n_particles
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array([0,0])

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

    def move_particles(self,W):

        for particle in self.particles:
            # print("particle velocity: {}".format(particle.velocity))
            a = W * particle.velocity
            b = c1 * random.uniform(0, 1)
            c = (particle.pbest_position - particle.position)
            d = c2 * random.uniform(0, 1)
            e = (self.gbest_position - particle.position)

            new_velocity =  a + b * c + d * e
            for i in range(len(new_velocity)):
                if (new_velocity[i] > 77.0):
                    new_velocity[i] = 77.0
                elif (new_velocity[i] < -77.0):
                    new_velocity[i] = -77.0

            particle.velocity = new_velocity
            particle.move()


search_space = Space(n_particles)
particles_vector = [Particle() for _ in range(search_space.n_particles)] # criando uma particula para n particulas
search_space.particles = particles_vector
search_space.print_particles()

iteration = 0
while (iteration < n_iterations):
    search_space.set_pbest()
    search_space.set_gbest()
    W = 0.9 - (iteration * ((0.9 - 0.4) / n_iterations))
    search_space.move_particles(W)
    iteration += 1

# f(512,404.2319) = -959.6407
print("The best solution is: {} in n_iterations: {} | result: {}".format(search_space.gbest_position,iteration,search_space.gbest_value))