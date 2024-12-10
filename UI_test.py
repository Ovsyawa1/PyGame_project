import pygame

pygame.init()

# стартовые параметры
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode([WIDTH, HEIGHT])
fps = 60
timer = pygame.time.Clock()

def game_font(size):
    return pygame.font.Font("include\Oswald-Regular.ttf", size)

# main game loops
def main_menu():
    pygame.display.set_caption("Menu")
    
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = game_font(100).render("MAIN MENU", True, "#E5E4E2")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

def players_settings():
    pass

def gameplay():
    pass


pygame.quit()
    