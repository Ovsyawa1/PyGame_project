import pygame
import random

pygame.init()

class Button():
    def __init__(self, x, y, image, hover_image):
        self.image = image
        self.hover_image = hover_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        if self.rect.collidepoint(MENU_MOUSE_POS):
            surface.blit(self.hover_image, (self.rect.x, self.rect.y))
            if (pygame.mouse.get_pressed()[0]) and (self.clicked == False):
                print("Clicked")
                action = True
                self.clicked = True
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

# стартовые параметры
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode([WIDTH, HEIGHT])
fps = 60
timer = pygame.time.Clock()
text_font = pygame.font.SysFont('Arial Bold', 280)
background = "#18224D"

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, [x,y])

def main_menu():
    start_img = pygame.image.load("include\start_img.png").convert_alpha()
    start_img_hover = pygame.image.load("include\start_img_cursor.png").convert_alpha()
    exit_img = pygame.image.load("include\exit_img.png").convert_alpha()
    exit_img_hover = pygame.image.load("include\exit_img_cursor.png").convert_alpha()

    start_button = Button(440, 100, start_img, start_img_hover)
    exit_button = Button(425, 400, exit_img, exit_img_hover)
    run = True

    while run:
        timer.tick(fps)
        screen.fill(background)

        if start_button.draw(screen):
            players_count()
        if exit_button.draw(screen):
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.flip()

    pygame.quit()

def players_count():
    start_img = pygame.image.load("include\start.png").convert_alpha()
    right_arrow = pygame.image.load("include\\not_left_arrow.png").convert_alpha()
    left_arrow = pygame.image.load("include\left_arrow.png").convert_alpha()
    number_of_players = '2'
    temp = 2

    start_button = Button(440, 500, start_img, start_img)
    right_button = Button(680-50, 260, right_arrow, right_arrow)
    left_button = Button(300-50, 260, left_arrow, left_arrow)
    run = True

    while run:
        timer.tick(fps)
        screen.fill(background)

        draw_text(number_of_players, text_font, 'white', 640-50, 260)

        if start_button.draw(screen):
            game_screen(temp)

        if right_button.draw(screen):
            temp = int(number_of_players)
            temp += 1
            if temp == 5:
                temp = 2
            number_of_players = str(temp)

        if left_button.draw(screen):
            temp = int(number_of_players)
            temp -= 1
            if temp == 1:
                temp = 4
            number_of_players = str(temp)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()

    pygame.quit()
    
def game_screen(number_of_players):
    # some variables
    text_font = pygame.font.SysFont('Arial Bold', 40)
    first_turn = True
    turn = True
    players_score = [0 for _ in range(0, number_of_players)] # число очков каждого игрока хранится в массиве
    turns_numb = [0 for _ in range(0, number_of_players)] # число ходов до нажатия кнопки пас

    # score measurement
    fps_timer = 0
    alpha = 0
    text = ""
    copy_text = text_font.render(text, True, 'white')

    # images initialisation
    roll_img = pygame.image.load("include\dice_img.png").convert_alpha()
    roll_img = pygame.transform.scale(roll_img, [200, 200])
    pass_img = pygame.image.load("include\pass_img.png").convert_alpha()
    pass_img = pygame.transform.scale(pass_img, [300, 150])
    pass_hover_img = pygame.image.load("include\pass_hover.png").convert_alpha()
    pass_hover_img = pygame.transform.scale(pass_hover_img, [300, 150])

    # sounds initialistation
    dice_sound = pygame.mixer.Sound('include\dice_sound.mp3')

    # buttons initialisation 
    roll_button = Button(50, 500, roll_img, roll_img)
    pass_button = Button(900, 550, pass_img, pass_hover_img)
    run = True

    while run:
        timer.tick(fps)
        screen.fill(background)

        # players scores UI
        player_score_text1 = f"Player 1: {players_score[0]}"
        player_turn_count1 = f"Player 1: {turns_numb[0]}"

        player_score_text2 = f"Player 2: {players_score[1]}"
        player_turn_count2 = f"Player 2: {turns_numb[1]}"

        draw_text("Players score", text_font, 'white', 10, 10)
        draw_text("Turn count: ", text_font, 'white', 1000, 10)
        
        draw_text(player_score_text1, text_font, '#FA7764', 10, 50)
        draw_text(player_turn_count1, text_font, '#FA7764', 1000, 50)

        draw_text(player_score_text2, text_font, '#898DFA', 10, 90)
        draw_text(player_turn_count2, text_font, '#898DFA', 1000, 90)
        
        if number_of_players == 3:
            player_score_text3 = f"Player 3: {players_score[2]}"
            player_turn_count3 = f"Player 3: {turns_numb[2]}"
            draw_text(player_score_text3, text_font, '#83FC8B', 10, 130)
            draw_text(player_turn_count3, text_font, '#83FC8B', 1000, 130)

        elif number_of_players == 4:
            player_score_text3 = f"Player 3: {players_score[2]}"
            player_turn_count3 = f"Player 3: {turns_numb[2]}"
            player_score_text4 = f"Player 4: {players_score[3]}"
            player_turn_count4 = f"Player 4: {turns_numb[3]}"

            draw_text(player_score_text3, text_font, '#83FC8B', 10, 130)
            draw_text(player_turn_count3, text_font, '#83FC8B', 1000, 130)
            draw_text(player_score_text4, text_font, '#FFF5A7', 10, 170)
            draw_text(player_turn_count4, text_font, '#FFF5A7', 1000, 170)
        

        # game logic
        if first_turn: # for first turn we will decide who's turn will be first
            which_turn = random.randrange(1, number_of_players + 1)
            first_turn = False

        elif turn:
            which_turn += 1
            if which_turn > number_of_players:
                which_turn = 1
            turn = False

        draw_text(f"It's Player {which_turn} turn!", text_font, 'white', 500, 10)

        if roll_button.draw(screen):
            score_count = random.randrange(1, 7)
            if score_count == 1:
                text = pygame.font.SysFont('Arial Bold', 60).render(f"Unclucky!", True, 'white')
            else:
                text = pygame.font.SysFont('Arial Bold', 60).render(f"You've got {score_count} points", True, 'white')
                players_score[which_turn - 1] += score_count
                turns_numb[which_turn - 1] += 1
            copy_text = text.copy()
            alpha = 255
            fps_timer = 20
            turn = True
            pygame.mixer.Sound.play(dice_sound)

        if fps_timer > 0:
            fps_timer -= 1
        else:
            if alpha > 0:
                alpha = max(0, alpha - 4)
                copy_text = text.copy()
                copy_text.fill((255, 255, 255, alpha), special_flags = pygame.BLEND_RGBA_MULT)

        screen.blit(copy_text, (450, 350))

        if pass_button.draw(screen):
            players_score[which_turn - 1] += turns_numb[which_turn - 1]
            turns_numb[which_turn - 1] = 0
            turn = True

        if players_score[which_turn - 1] >= 50:
            win_screen(which_turn)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.flip()

    pygame.quit()

def win_screen(which_turn):
    run = True
    text_font = pygame.font.SysFont('Arial Bold', 100)
    while run:
        timer.tick(fps)
        screen.fill(background)

        draw_text(f"Player {which_turn} won!", text_font, 'white', 430, 250)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONUP:
                run = False

        pygame.display.flip()

    pygame.quit()

main_menu()
