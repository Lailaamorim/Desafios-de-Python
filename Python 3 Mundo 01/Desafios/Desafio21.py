# ============================================
# DESAFIO 21
# ============================================
# Crie um programa que:
# - Abra um arquivo de áudio MP3
# - Toque esse áudio
#
# DICA:
# - Você vai precisar instalar uma biblioteca externa
# - Exemplo: pygame

import pygame 

pygame.init()
pygame.mixer.music.load("audio.mpeg")
pygame.mixer.music.play()
pygame.event.wait()
