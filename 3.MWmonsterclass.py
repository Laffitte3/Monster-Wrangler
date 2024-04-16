import pygame, random

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
        super().__init__()
        self.image = pygame.image.load("knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = width/2
        self.rect.centery =height

        #Variables especificas para el jugador
        self.lives=5
        self.warps=2
        self.velocity = 5

        #player sounds

        self.catch_sound=pygame.mixer.Sound("catch.wav")
        self.die_sound=pygame.mixer.Sound("die.wav")
        self.warp_sound= pygame.mixer.Sound("warp.wav")

    def update(self):
        #Actualizar a nuestro Player(movimiento)
        keys = pygame.key.get_pressed()

        #Move the player
        if keys[pygame.K_LEFT] and self.rect.left >0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < width:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top >0:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom<height:
            self.rect.y += self.velocity

    def warp(self):
        #Esconder personaje fuera de la linea
        if self.warps >0 :
            self.warps -=1
            self.warp_sound.play()
            self.rect.bottom= height
    
    def reset_position(self):
        #Reset the position of the player
        self.rect.centerx = width/2
        self.rect.centery = height
    
class Monster(pygame.sprite.Sprite):

    def __init__(self,x,y,image,monster_type):
        super().__init__()
        #Crear objeto monstruo
        #Aqui no creamos la imagen directamente, sino que se la pasamos como parametro
        self.image = image
        self.rect = self.image.get_rect()
        #La posicion donde apareceran los enemigos tambien se la pasamos como parametro
        self.rect.topleft = (x,y)

        #Atributos del monstruo
        #Monster_type is an int
        #example 0 is Blue, 1 is green....

        self.type = monster_type

        #set random motion
        self.dx = random.choice([-1,1])  
        self.dy = random.choice([-1,1])     
        self.velocity = random.randint(1,5)






    def update(self):
        #Actualizar al mosntruo
        #Aqui estaremos oendiente del movimiento dle monstruo
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity

        #Bounce the monster off the edges
        if self.rect.left <=0 or self.rect.right >= width:
            self.dx = -1 * self.dx

        if self.rect.top <=0 or self.rect.bottom >=height:
            self.dy = -1 * self.dy

#Creamos grupo
my_player_group = pygame.sprite.Group()
#Creamos un objeto
my_player = Player()
#Añadimos el ovjeto al grupo
my_player_group.add(my_player)

#Crear el grupo monstro
my_monster_group = pygame.sprite.Group()

#Test monster, vamos a crear un objeto monstruo para prueba solamente, ya que no crearemos los monstruos aqui sino en game class
monster = Monster(500,500,pygame.image.load("green_monster.png"),1)
my_monster_group.add(monster)



#Crear un game object
my_game = Game()

running=True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    #FILL THE DISPLAY
    dispaly_surface.fill((0,0,0))

    #Update and draw sprites
    my_player_group.update()
    my_player_group.draw(dispaly_surface)

    my_monster_group.update()
    my_monster_group.draw(dispaly_surface)

    #Update and draw the Game
    my_game.update()
    my_game.draw()

    pygame.display.update()

pygame.quit()