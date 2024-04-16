import pygame

pygame.init()

width=800
height=600

dispaly_surface= pygame.display.set_mode((width,height))
pygame.display.set_caption("Monster Wrangler")

FPS=60
clock= pygame.time.Clock()

class Game():
    # Clase para controlar el juego
    def __init__(self):
        #Inicializar el objeto Game
        pass

    def update(self):
        #Actualizar nuestro objeto Game
        pass
    
    def draw(self):
        #Dibuja el HUD del juego
        pass

    def check_collisions(self):
        #check for collision between players and monsters
        pass

    def start_new_round(self):
        #repobla la pantalla con nuevos monstruos
        pass

    def choose_new_target(self):
        #Elige un nuevo mosntruo para el player
        pass

    def pause_game(self):
        #pausar el juego
        pass

    def reset_game(self):
        #Reiniciar el juego
        pass

class Player(pygame.sprite.Sprite):
     #Player class that the user can control
    def __init__(self):
        #Inicializamos al player
        pass

    def update(self):
        #Actualizar a nuestro Player
        pass

    def warp(self):
        pass
    
    def reset_position(self):
        #Reset player psoition
        pass
    
class Monster(pygame.sprite.Sprite):

    def __init__(self):
        pass

    def update(self):
        #Actualizar al mosntruo
        pass


running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.update()

pygame.quit()