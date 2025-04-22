import pygame
import random
import os

# Configuración inicial
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sketch Aquarium")

# Cargar fondo
if os.path.exists("background.jpg"):
    background = pygame.image.load("background.jpg")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
else:
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((0, 100, 200))

# Cargar todos los peces del directorio
fish_images = []
fish_dir = 'fish_sprites'
for file in os.listdir(fish_dir):
    if file.endswith('.png'):
        img = pygame.image.load(os.path.join(fish_dir, file)).convert_alpha()
        img = pygame.transform.scale(img, (80, 60))
        fish_images.append(img)

# Clase Pez
class Fish:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(100, HEIGHT - 100)
        self.speed = random.uniform(1, 3)
        self.image = random.choice(fish_images).copy()
        self.direction = random.choice(["left", "right"])
        if self.direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
            self.speed *= -1

    def move(self):
        self.x += self.speed
        if self.x > WIDTH + 80 or self.x < -80:
            self.__init__()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Crear peces (uno por imagen al menos)
fishes = [Fish() for _ in range(len(fish_images) * 2)]

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for fish in fishes:
        fish.move()
        fish.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
