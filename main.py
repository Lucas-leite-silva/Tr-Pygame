import pygame

print("Setup Start")
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print("Setup End")

print("Loop Start")
while True:
    # Checagem de todos eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit() Fechar janela
              quit() # fechar o pygame


