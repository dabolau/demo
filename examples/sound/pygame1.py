import time
import pygame

filename = 'jinggao.mp3'
pygame.mixer.init()
print('play')
track = pygame.mixer.music.load(filename)
pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.music.stop()