import time
import pygame
import random

class Gene(pygame.sprite.Sprite):
    
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.radius = 7  # Radius of the gene circle
        self.color = (0, 102, 204)  # Blue color for the gene
        self.fitness = 0
        #
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        # 
        self.rect = self.image.get_rect()
        base_x = (800 - self.radius) // 2
        base_y = (600 - self.radius) // 2
        self.rect.center = (
            random.randint(base_x - random.randint(45, 55), base_x + random.randint(45, 55)),
            random.randint(base_y + 250, base_y + 300)
        )
        

    def move(self):
        self.rect.x += random.randint(-5, 5)
        self.rect.y += random.randint(-5, 5)

        # Keep the gene within the screen boundaries
        self.rect.x = max(min(self.rect.x, 600 - self.radius * 2), 0)
        self.rect.y = max(min(self.rect.y, 800 - self.radius * 2), 0)


    def calculate_fitness(self):
        pass


def move_towards_goal()->None:
    global POPULATION, screen
    start = time.time()
    duration = random.randint(5, 7)
    while time.time() - start <= duration:
        screen.fill((255, 255, 153))
        create_goal_for_generation()

        for gene in POPULATION:
            gene.move()
            gene.calculate_fitness()
            screen.blit(gene.image, gene.rect)

        pygame.display.flip()
        time.sleep(0.125)
        

def select_offspring()->None:
    global POPULATION
    pass


def create_initial_population(num_population: int)->None:
    global POPULATION
    
    for g_id in range(num_population): 
        gene = Gene(g_id)
        POPULATION.append(gene)


def create_goal_for_generation()->None:
    global screen
    # Create Goal
    box_width = 100
    box_height = 50
    box_x = (800 - box_width) // 2
    box_y = 1 
    pygame.draw.rect(screen, (255, 254, 255), (box_x, box_y, box_width, box_height))


def run_simulation(generation: int)->None:
    global MAX_GENERATIONS

    if generation == MAX_GENERATIONS:
        # pygame.quit()
        print(f"All generation exhausted")
        return
    
    print(f"Generation {generation}, moving towards the goal..")
    # Moving towards a goal (i.e. more knowledge, multiplanetary life etc..)
    move_towards_goal()
    
    # Evaluate fitter individual in a generation

    # Select the next generation
    select_offspring()
    run_simulation(generation + 1)


if __name__ == '__main__':
    MAX_GENERATIONS = 20
    POPULATION = []
    # Initialize pygame
    pygame.init()
    # Set up the screen
    screen = pygame.display.set_mode((800, 600)) # height, width
    screen.fill((255, 255, 153)) # bg
    pygame.display.set_caption("Natural Selection")
    create_goal_for_generation()
    create_initial_population(num_population=30)
    run_simulation(1)