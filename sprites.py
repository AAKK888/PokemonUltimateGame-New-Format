import pygame
import var
import random
import time
from os import path

pygame.init()
pygame.mixer.init()
listtodeside = [True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
directionlist = ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW']
img_dir = path.join(path.dirname(__file__), 'img')
# pichu_img = pygame.image.load(path.join(img_dir, "Pichu.png")).convert()
# pikachu_img = pygame.image.load(path.join(img_dir, "Pikachu.png")).convert()
movegroup = pygame.sprite.Group()


class RoamPichu(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.transform.scale(pichu_img, (20, 20))
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.YELLOW)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)

        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel

    def update(self,):
        if self.rect.x - MyCharac.rect.x == var.FLEE_DISTANCE:
            self.kill()
 












class PichuEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.transform.scale(pichu_img, (20, 20))
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.YELLOW)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)

        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        if 5 <= self.level < 10:
            self.name = 'pichu'
            # self.image = pygame.transform.scale(pichu_img, (20, 20))
        if 5 <= self.level < 15:
            self.name = 'pikachu'
            # self.image = pygame.transform.scale(pikachu_img, (20, 20))
        if self.level >= 15:
            self.name = 'raichu'
            # self.image = pygame.image.load("raichu.png").convert_alpha()
        if self.name == 'pichu':
            self.health = 20
        if self.name == 'pikachu':
            self.health = 35
        if self.name == 'raichu':
            self.health = 60
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 393:
            self.rect.top = 393
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1

    def domove(self):
        amove = Moves(self.rect.centerx, self.rect.top)
        movegroup.add(amove)


class BulbasaurEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.GREEN)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        if 5 <= self.level < 16:
            self.name = 'bulbasaur'
        if 16 <= self.level < 32:
            self.name = 'ivysaur'
        if self.level >= 32:
            self.name = 'venusaur'
        if self.name == 'bulbasaur':
            self.health = 45
        if self.name == 'ivysaur':
            self.health = 60
        if self.name == 'venusaur':
            self.health = 80
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1


class CharmanderEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.RED)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        if 5 <= self.level < 16:
            self.name = 'charmander'
        if 16 <= self.level < 32:
            self.name = 'charmeleon'
        if self.level >= 32:
            self.name = 'charzard'
        if self.name == 'charmamder':
            self.health = 39
        if self.name == 'charmeleon':
            self.health = 58
        if self.name == 'charzard':
            self.health = 78
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1


class SquirtleEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.BLUE)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        if 5 <= self.level < 16:
            self.name = 'squirtle'
        if 16 <= self.level < 32:
            self.name = 'wartortle'
        if self.level >= 32:
            self.name = 'blastoise'
        if self.name == 'squirtle':
            self.health = 39
        if self.name == 'wartortle':
            self.health = 58
        if self.name == 'blastoise':
            self.health = 78
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1


class OnixEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.GRAY)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        if 5 <= self.level < 15:
            self.name = 'onix'
        if self.level >= 15:
            self.name = 'steelix'
        if self.name == 'onix':
            self.health = 35
        if self.name == 'steelix':
            self.health = 75
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1


class FletchlingEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.WHITE)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        if 5 <= self.level < 17:
            self.name = 'fletchling'
        if 17 <= self.level < 35:
            self.name = 'fletchinder'
        if self.level >= 35:
            self.name = 'talonflame'
        if self.name == 'fletchling':
            self.health = 45
        if self.name == 'fletchinder':
            self.health = 62
        if self.name == 'talonflame':
            self.health = 78

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
            if self.yspeed != 0 and self.xspeed != 0:
                self.yspeed /= 1.414
                self.xspeed /= 1.414


class MagikarpEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.RED)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        if 5 <= self.level < 20:
            self.name = 'magikarp'
        if self.level >= 20:
            self.name = 'gyarados'
        if self.name == 'magikarp':
            self.health = 20
        if self.name == 'gyarados':
            self.health = 95
            self.image.fill(var.BLUE)
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1


class Farfetch_dEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.BROWN)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0
        self.health = 35
        self.level_add = 0
        self.level = startlevel
        self.xspeed = 0
        self.yspeed = 0
        self.name = 'Farfetch\' d'

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1


class ElekidEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.YELLOW)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        if 5 <= self.level < 10:
            self.name = 'elekid'
        if 10 <= self.level < 15:
            self.name = 'electabuzz'
        if self.level >= 15:
            self.name = 'electrive'
        if self.name == 'elekid':
            self.health = 20
        if self.name == 'electabuzz':
            self.health = 35
        if self.name == 'electrive':
            self.health = 60
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1


class GastlyEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.BLACK)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        if 5 <= self.level < 25:
            self.name = 'gastly'
        if 25 <= self.level < 40:
            self.name = 'haunter'
        if self.level >= 40:
            self.name = 'gengar'
        if self.name == 'gastly':
            self.health = 30
        if self.name == 'haunter':
            self.health = 45
        if self.name == 'gengar':
            self.health = 60
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1


class GrowlitleEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.RED)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        if self.level < 16:
            self.name = 'growlithe'
        if self.level >= 32:
            self.name = 'arcanine'
        if self.name == 'growlithe':
            self.health = 55
        if self.name == 'arcanine':
            self.health = 90
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1


class RioluEvo(pygame.sprite.Sprite):
    def __init__(self, startlevel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.RED)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0
        self.health = 0
        self.level_add = 0
        self.level = startlevel
        if self.level < 16:
            self.name = 'riolu'
        if self.level >= 32:
            self.name = 'lucario'
        if self.name == 'riolu':
            self.health = 40
        if self.name == 'lucario':
            self.health = 70
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.xspeed = -8
        if keystate[pygame.K_RIGHT]:
            self.xspeed = 8
        if keystate[pygame.K_UP]:
            self.yspeed = -8
        if keystate[pygame.K_DOWN]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
           
class BushesAndStuff(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bushimg, (var.BUSH_SIZE_WIDTH, var.BUSH_SIZE_HEIGHT))
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, var.WIDTH), (random.randint(385, var.HEIGHT)))

    def update(self):
        pass
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
class Guy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(var.BROWN)
        self.image.set_colorkey(var.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (var.WIDTH / 2, var.HEIGHT / 2)
        self.xspeed = 0
        self.yspeed = 0

    def update(self):
        self.xspeed = 0
        self.yspeed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.xspeed = -8
        if keystate[pygame.K_d]:
            self.xspeed = 8
        if keystate[pygame.K_w]:
            self.yspeed = -8
        if keystate[pygame.K_s]:
            self.yspeed = 8
        if self.yspeed != 0 and self.xspeed != 0:
            self.yspeed /= 1.414
            self.xspeed /= 1.414

        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.right > var.WIDTH:
            self.rect.right = var.WIDTH - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.top < 393:
            self.rect.top = 393
        if self.rect.bottom > var.HEIGHT:
            self.rect.bottom = var.HEIGHT - 1
            
            

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
class Moves(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(var.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()
