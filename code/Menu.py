#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect, KSCAN_UP
from pygame.font import Font

from code.Const import WIN_WIDHT, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/bg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/fase1.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # Desenho das imagens (titulo)
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDHT / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDHT / 2), 120))

            # Iteração do menu, onde estiver sobreposto ficará marcado na cor Amarela.
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDHT / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDHT / 2), 200 +25 * i))

            # GO GAME, Coloca todas imagens e textos
            pygame.display.flip()

            #Checagem de todos eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechar janela
                    quit()  # fechar o pygame
                if event.type == pygame.KEYDOWN: # Mover para baixo
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option +=1
                        else: menu_option = 0
                    if event.key ==  pygame.K_UP: # Mover para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION ) - 1
                    if event.key == pygame.K_RETURN: #PRESSIONAR ENTER
                        return MENU_OPTION[menu_option]


    # Transforma todos os textos em imagens (Define, Textos, Centralização, Conversão para Imagem e fonte)
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
