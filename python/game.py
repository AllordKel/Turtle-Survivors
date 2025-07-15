import pygame
import os
import json
from sys import exit
from random import randint, choice

os.chdir(os.path.dirname(__file__))

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()  # launches pygame
clock = pygame.time.Clock()
screen = pygame.Surface((800, 400))  # game screen
full_screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)


# event timers
spawn_interval = 1000
enemy_timer = pygame.USEREVENT + 1  # enemy spawn timer
pygame.time.set_timer(enemy_timer, spawn_interval)

# font
text_font = pygame.font.SysFont(None, 30)

# utilities upload
pygame.display.set_caption("Turtle Survivors")

menu_music = pygame.mixer.Sound("sound//menu.ogg")
game_music = pygame.mixer.Sound("sound//game.ogg")
game_music_channel = game_music.play(-1)
game_music_channel.pause()

background1 = pygame.image.load("images\\Back.png").convert_alpha()  # background image
background1 = pygame.transform.scale(background1, (800, 400))  # scaling background image to 800x400

heart1 = pygame.image.load("images\\heart.png").convert_alpha()  # health img
heart1 = pygame.transform.scale(heart1, (heart1.get_width() // 8, heart1.get_height() // 8))

leaderboard = pygame.image.load("images\\leaderboard.png").convert_alpha()  # leaderboard image
leaderboard = pygame.transform.scale(leaderboard, (leaderboard.get_width() // 1.5, 400))  # leaderboard.get_height() // 1.5

enter_name_box = pygame.image.load("images\\enter_name.png").convert_alpha()  # enter name box image
enter_name_box = pygame.transform.scale(enter_name_box, (enter_name_box.get_width() // 1.5, enter_name_box.get_height() // 1.5))  # leaderboard.get_height() // 1.5

healthbar_text_surface = text_font.render("Health: ", False, "purple")  # healthbar text surface
exit_text_helper = text_font.render("Press Enter to continue", False, "black")

turtle1 = pygame.image.load("images\\turtle1.png").convert_alpha()
turtle1 = pygame.transform.scale(turtle1, (turtle1.get_width() // 7, turtle1.get_height() // 7))
turtle2 = pygame.image.load("images\\turtle2.png").convert_alpha()
turtle2 = pygame.transform.scale(turtle2, (turtle2.get_width() // 7, turtle2.get_height() // 7))
turtle3 = pygame.image.load("images\\turtle3.png").convert_alpha()
turtle3 = pygame.transform.scale(turtle3, (turtle3.get_width() // 7, turtle3.get_height() // 7))
turtle4 = pygame.image.load("images\\turtle4.png").convert_alpha()
turtle4 = pygame.transform.scale(turtle4, (turtle4.get_width() // 7, turtle4.get_height() // 7))
turtle_hide1 = pygame.image.load("images\\turtle_hide1.png").convert_alpha()
turtle_hide1 = pygame.transform.scale(turtle_hide1, (turtle_hide1.get_width() // 8, turtle_hide1.get_height() // 8))
turtle_hide2 = pygame.image.load("images\\turtle_hide2.png").convert_alpha()
turtle_hide2 = pygame.transform.scale(turtle_hide2, (turtle_hide2.get_width() // 8, turtle_hide2.get_height() // 8))
turtle_hide3 = pygame.image.load("images\\turtle_hide3.png").convert_alpha()
turtle_hide3 = pygame.transform.scale(turtle_hide3, (turtle_hide3.get_width() // 8, turtle_hide3.get_height() // 8))
green_turtle_animation_set = (turtle1, turtle2, turtle3, turtle4)
green_turtle_hide_animation_set = (turtle_hide1, turtle_hide2, turtle_hide3, turtle_hide2)

golden_turtle1 = pygame.image.load("images\\golden_turtle1.png").convert_alpha()
golden_turtle1 = pygame.transform.scale(golden_turtle1, (golden_turtle1.get_width() // 3, golden_turtle1.get_height() // 3))
golden_turtle2 = pygame.image.load("images\\golden_turtle2.png").convert_alpha()
golden_turtle2 = pygame.transform.scale(golden_turtle2, (golden_turtle2.get_width() // 3, golden_turtle2.get_height() // 3))
golden_turtle3 = pygame.image.load("images\\golden_turtle3.png").convert_alpha()
golden_turtle3 = pygame.transform.scale(golden_turtle3, (golden_turtle3.get_width() // 3, golden_turtle3.get_height() // 3))
golden_turtle4 = pygame.image.load("images\\golden_turtle4.png").convert_alpha()
golden_turtle4 = pygame.transform.scale(golden_turtle4, (golden_turtle4.get_width() // 3, golden_turtle4.get_height() // 3))
golden_turtle_hide1 = pygame.image.load("images\\golden_turtle_hide1.png").convert_alpha()
golden_turtle_hide1 = pygame.transform.scale(golden_turtle_hide1, (golden_turtle_hide1.get_width() * 3.4, golden_turtle_hide1.get_height() * 3.4))
golden_turtle_hide2 = pygame.image.load("images\\golden_turtle_hide2.png").convert_alpha()
golden_turtle_hide2 = pygame.transform.scale(golden_turtle_hide2, (golden_turtle_hide2.get_width() * 3.4, golden_turtle_hide2.get_height() * 3.4))
golden_turtle_hide3 = pygame.image.load("images\\golden_turtle_hide3.png").convert_alpha()
golden_turtle_hide3 = pygame.transform.scale(golden_turtle_hide3, (golden_turtle_hide3.get_width() * 3.4, golden_turtle_hide3.get_height() * 3.4))
golden_turtle_animation_set = (golden_turtle1, golden_turtle2, golden_turtle3, golden_turtle4)
golden_turtle_hide_animation_set = (golden_turtle_hide1, golden_turtle_hide2, golden_turtle_hide3, golden_turtle_hide2)

carrier_turtle1 = pygame.image.load("images\\carrier_turtle1.png").convert_alpha()
carrier_turtle1 = pygame.transform.scale(carrier_turtle1, (carrier_turtle1.get_width() * 3.8, carrier_turtle1.get_height() * 3.8))
carrier_turtle2 = pygame.image.load("images\\carrier_turtle2.png").convert_alpha()
carrier_turtle2 = pygame.transform.scale(carrier_turtle2, (carrier_turtle2.get_width() * 3.8, carrier_turtle2.get_height() * 3.8))
carrier_turtle3 = pygame.image.load("images\\carrier_turtle3.png").convert_alpha()
carrier_turtle3 = pygame.transform.scale(carrier_turtle3, (carrier_turtle3.get_width() * 3.8, carrier_turtle3.get_height() * 3.8))
carrier_turtle4 = pygame.image.load("images\\carrier_turtle4.png").convert_alpha()
carrier_turtle4 = pygame.transform.scale(carrier_turtle4, (carrier_turtle4.get_width() * 3.8, carrier_turtle4.get_height() * 3.8))
carrier_turtle_hide1 = pygame.image.load("images\\carrier_turtle_hide1.png").convert_alpha()
carrier_turtle_hide1 = pygame.transform.scale(carrier_turtle_hide1, (carrier_turtle_hide1.get_width() * 3.4, carrier_turtle_hide1.get_height() * 3.4))
carrier_turtle_hide2 = pygame.image.load("images\\carrier_turtle_hide2.png").convert_alpha()
carrier_turtle_hide2 = pygame.transform.scale(carrier_turtle_hide2, (carrier_turtle_hide2.get_width() * 3.4, carrier_turtle_hide2.get_height() * 3.4))
carrier_turtle_hide3 = pygame.image.load("images\\carrier_turtle_hide3.png").convert_alpha()
carrier_turtle_hide3 = pygame.transform.scale(carrier_turtle_hide3, (carrier_turtle_hide3.get_width() * 3.4, carrier_turtle_hide3.get_height() * 3.4))
carrier_turtle_animation_set = (carrier_turtle1, carrier_turtle2, carrier_turtle3, carrier_turtle4)
carrier_turtle_hide_animation_set = (carrier_turtle_hide1, carrier_turtle_hide2, carrier_turtle_hide3, carrier_turtle_hide2)

girl_turtle1 = pygame.image.load("images\\girl_turtle1.png").convert_alpha()
girl_turtle1 = pygame.transform.scale(girl_turtle1, (girl_turtle1.get_width() * 3, girl_turtle1.get_height() * 3))
girl_turtle2 = pygame.image.load("images\\girl_turtle2.png").convert_alpha()
girl_turtle2 = pygame.transform.scale(girl_turtle2, (girl_turtle2.get_width() * 3, girl_turtle2.get_height() * 3))
girl_turtle3 = pygame.image.load("images\\girl_turtle3.png").convert_alpha()
girl_turtle3 = pygame.transform.scale(girl_turtle3, (girl_turtle3.get_width() * 3, girl_turtle3.get_height() * 3))
girl_turtle4 = pygame.image.load("images\\girl_turtle4.png").convert_alpha()
girl_turtle4 = pygame.transform.scale(girl_turtle4, (girl_turtle4.get_width() * 3, girl_turtle4.get_height() * 3))
girl_turtle_hide1 = pygame.image.load("images\\girl_turtle_hide1.png").convert_alpha()
girl_turtle_hide1 = pygame.transform.scale(girl_turtle_hide1, (girl_turtle_hide1.get_width() * 3.4, girl_turtle_hide1.get_height() * 3.4))
girl_turtle_hide2 = pygame.image.load("images\\girl_turtle_hide2.png").convert_alpha()
girl_turtle_hide2 = pygame.transform.scale(girl_turtle_hide2, (girl_turtle_hide2.get_width() * 3.4, girl_turtle_hide2.get_height() * 3.4))
girl_turtle_hide3 = pygame.image.load("images\\girl_turtle_hide3.png").convert_alpha()
girl_turtle_hide3 = pygame.transform.scale(girl_turtle_hide3, (girl_turtle_hide3.get_width() * 3.4, girl_turtle_hide3.get_height() * 3.4))
girl_turtle_animation_set = (girl_turtle1, girl_turtle2, girl_turtle3, girl_turtle4)
girl_turtle_hide_animation_set = (girl_turtle_hide1, girl_turtle_hide2, girl_turtle_hide3, girl_turtle_hide2)

rat1 = pygame.image.load("images\\rat1.png").convert_alpha()
rat1 = pygame.transform.scale(rat1, (rat1.get_width() // 2, rat1.get_height() // 2))
rat2 = pygame.image.load("images\\rat2.png").convert_alpha()
rat2 = pygame.transform.scale(rat2, (rat2.get_width() // 2, rat2.get_height() // 2))

eagle1 = pygame.image.load("images\\eagle1.png").convert_alpha()
eagle1 = pygame.transform.scale(eagle1, (eagle1.get_width() // 6, eagle1.get_height() // 6))
eagle2 = pygame.image.load("images\\eagle2.png").convert_alpha()
eagle2 = pygame.transform.scale(eagle2, (eagle2.get_width() // 6, eagle2.get_height() // 6))
eagle3 = pygame.image.load("images\\eagle3.png").convert_alpha()
eagle3 = pygame.transform.scale(eagle3, (eagle3.get_width() // 6, eagle3.get_height() // 6))

endgame_box = pygame.Rect(150, 75, 500, 250)  # menu black box

turtle1_skin_box = turtle1.get_rect(center=(endgame_box.centerx - 125, endgame_box.centery - 60))
golden_turtle1_skin_box = golden_turtle1.get_rect(center=(endgame_box.centerx + 125, endgame_box.centery - 60))
carrier_turtle1_skin_box = carrier_turtle1.get_rect(center=(endgame_box.centerx - 125, endgame_box.centery + 60))
girl_turtle1_skin_box = girl_turtle1.get_rect(center=(endgame_box.centerx + 125, endgame_box.centery + 60))

leaderboard_text_rect = pygame.Rect(300, 165, 200, 180)


class turtle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.selected_skin = load_selected_skin()
        if self.selected_skin == "green_turtle":
            self.turtle_animation_set = green_turtle_animation_set
            self.turtle_jump_animation_set = turtle1
            self.turtle_hide_animation_set = green_turtle_hide_animation_set
        elif self.selected_skin == "golden_turtle":
            self.turtle_animation_set = golden_turtle_animation_set
            self.turtle_jump_animation_set = golden_turtle1
            self.turtle_hide_animation_set = golden_turtle_hide_animation_set
        elif self.selected_skin == "carrier_turtle":
            self.turtle_animation_set = carrier_turtle_animation_set
            self.turtle_jump_animation_set = carrier_turtle1
            self.turtle_hide_animation_set = carrier_turtle_hide_animation_set
        elif self.selected_skin == "girl_turtle":
            self.turtle_animation_set = girl_turtle_animation_set
            self.turtle_jump_animation_set = girl_turtle1
            self.turtle_hide_animation_set = girl_turtle_hide_animation_set

        self.turtle_gravity = 0
        self.max_health = 3
        self.health = 0
        self.damage_time = 0

        self.image = self.turtle_animation_set[int(pygame.time.get_ticks() // 100 % len(self.turtle_animation_set))]
        self.rect = self.image.get_rect(midbottom=(80, 380))

    def inputs(self):
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.bottom == 380:  # turtle jumping
            self.turtle_gravity = -20

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.rect.bottom == 380:  # turtle hiding
            self.defense_state = True
        else:
            self.defense_state = False

    def gravity(self):
        if self.rect.bottom != 380:
            self.turtle_gravity += 1
        self.rect.y += self.turtle_gravity
        if self.rect.bottom >= 380:
            self.rect.bottom = 380

    def animation(self):
        old_midbottom = self.rect.midbottom
        if self.defense_state:
            self.image = self.turtle_hide_animation_set[int(pygame.time.get_ticks() // 100 % len(self.turtle_hide_animation_set))]
        elif self.rect.bottom != 380:
            self.image = self.turtle_jump_animation_set
        else:
            self.image = self.turtle_animation_set[int(pygame.time.get_ticks() // 100 % len(self.turtle_animation_set))]
        self.rect = self.image.get_rect(midbottom=old_midbottom)

    def draw(self, screen):
        if self.damage_cooldown:
            if pygame.time.get_ticks() // 200 % 2 == 0:
                screen.blit(self.image, self.rect)
        else:
            screen.blit(self.image, self.rect)

    def update_damage_cooldown(self):
        if self.damage_cooldown and pygame.time.get_ticks() - self.damage_time > 2500:  # restoring from damage in 2.5 seconds
            self.damage_cooldown = False

    def update(self):
        self.inputs()
        self.gravity()
        self.animation()
        self.update_damage_cooldown()


class mobs(pygame.sprite.Sprite):
    def __init__(self, enemy_type):
        super().__init__()
        if enemy_type == "rat":
            self.enemy_animation_set = (rat1, rat2)
            self.height_spawn = 380
        elif enemy_type == "eagle":
            self.enemy_animation_set = (eagle1, eagle2, eagle3, eagle2)
            self.height_spawn = 150

        self.enemy_type = enemy_type
        self.image = self.enemy_animation_set[int(pygame.time.get_ticks() // 100 % len(self.enemy_animation_set))]
        self.rect = self.image.get_rect(midbottom=(randint(950, 1050), self.height_spawn))

    def animation(self):
        self.image = self.enemy_animation_set[int(pygame.time.get_ticks() // 100 % len(self.enemy_animation_set))]

    def moving(self):
        self.rect.x -= 6 * speeding_rate
        if self.enemy_type == "eagle" and self.rect.x <= 220 and self.rect.bottom < player.sprite.rect.top + 1:
            self.rect.y += 6 * speeding_rate
        self.destruction()

    def destruction(self):
        if self.rect.x <= -200:
            self.kill()

    def attack(self):
        self.attack_area = pygame.Rect(self.rect.left + 30, self.rect.top, 3, self.rect.height)
        if not player.sprite.damage_cooldown and (self.enemy_type == "eagle" and not player.sprite.defense_state or self.enemy_type != "eagle") and self.attack_area.colliderect(player.sprite.rect):
            player.sprite.health -= 1
            player.sprite.damage_time = pygame.time.get_ticks()
            player.sprite.damage_cooldown = True

    def update(self):
        self.animation()
        self.moving()
        self.attack()


def new_game():  # starting new game state
    player.sprite.health = player.sprite.max_health
    global score
    score = 0
    enemies.empty()
    player.sprite.damage_cooldown = False
    player.sprite.defense_state = False
    global game_state
    game_state = "game"  # game
    global background_animation_x
    background_animation_x = 0
    global spawn_interval
    spawn_interval = 1500
    pygame.time.set_timer(enemy_timer, spawn_interval)
    global player_name
    player_name = ""
    game_music_channel.play(game_music, loops=-1)
    global old_score_display
    old_score_display = -1


def scale_mouse(pos):
    rx, ry = full_screen.get_size()
    vx, vy = screen.get_size()
    return (pos[0] * vx / rx, pos[1] * vy / ry)


def load_leaderboard():
    try:
        with open("saves\\leaderboard.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def add_new_score(name, score):
    leaderboard_data = load_leaderboard()
    leaderboard_data.append({"name": name, "score": score})
    leaderboard_data.sort(key=lambda x: x["score"], reverse=True)  # descent sorting
    leaderboard_data = leaderboard_data[:6]  # leaving only top 6
    with open("saves\\leaderboard.json", "w") as f:
        json.dump(leaderboard_data, f, indent=4)


def save_selected_skin(skin):
    with open("saves\\skins.json", "w") as f:
        json.dump({"selected_skin": skin}, f)


def load_selected_skin():
    try:
        with open("saves\\skins.json", "r") as f:
            data = json.load(f)
            return data.get("selected_skin", "green_turtle")
    except FileNotFoundError:
        return "green_turtle"


def play_music():
    if game_state == "menu" and player.sprite.health == 0:
        game_music_channel.pause()
        menu_music.set_volume(0.1)
        menu_music.play(loops=-1)
    if game_state == "game":
        menu_music.stop()
        game_music.set_volume(0.15)
        game_music_channel.unpause()


# groups
player = pygame.sprite.GroupSingle()
player.add(turtle())
enemies = pygame.sprite.Group()

game_state = "menu"
play_music()

while True:
    events = pygame.event.get()  # saving all events
    keys = pygame.key.get_pressed()  # saving all keyboard inputs

    for event in events:  # for global events regardlesss of game state
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_state == "game":

        # speeding
        if score <= 100:
            speeding_rate = 1 + score / 100
        else:
            speeding_rate = 2

        # background animation
        background_animation_x -= 3 * speeding_rate  # background animation speed
        if background_animation_x <= -background1.get_width():
            background_animation_x += background1.get_width()

        # enemies spawn interval
        new_spawn_interval = round(1000 - 50 * (score // 10))
        if new_spawn_interval != spawn_interval and spawn_interval > 650:
            spawn_interval = new_spawn_interval
            pygame.time.set_timer(enemy_timer, spawn_interval)

        # buttons
        for event in events:
            if event.type == enemy_timer:  # adding enemies to the enemy list
                enemies.add(mobs(choice(["rat", "eagle"])))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # pause
                    game_state = "menu"

        # drowing
        screen.blit(background1, (background_animation_x, 0))
        screen.blit(background1, (background1.get_width() + background_animation_x, 0))

        # score
        if round(score) != old_score_display:
            score_text = text_font.render(f"Score: {round(score)}", False, "purple")
            score_box = score_text.get_rect(topright=(790, 15))
            old_score_display = round(score)
        screen.blit(score_text, score_box)
        score += 1 / 60

        screen.blit(healthbar_text_surface, (10, 15))
        for i in range(player.sprite.health):
            screen.blit(heart1, (90 + i * 40, 10))  # drowing health hearts

        player.sprite.draw(screen)
        player.update()
        enemies.draw(screen)
        enemies.update()

        # gameover condition
        if player.sprite.health == 0:
            score_saved = False
            game_state = "gameover"

    elif game_state == "menu":
        # music
        play_music()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and menu_continue_box.inflate(10, 10).collidepoint(scale_mouse(event.pos)) and player.sprite.health != 0:  # continue
                    game_state = "game"

                if pygame.mouse.get_pressed()[0] and newgame_box.inflate(10, 10).collidepoint(scale_mouse(event.pos)):  # start new game
                    new_game()
                    play_music()

                if pygame.mouse.get_pressed()[0] and menu_skins_box.inflate(10, 10).collidepoint(scale_mouse(event.pos)):  # skins button
                    game_state = "skin_selection"

                if pygame.mouse.get_pressed()[0] and leaderboard_menu_text_box.inflate(10, 10).collidepoint(scale_mouse(event.pos)):  # leaderboard button
                    score_saved = True
                    game_state = "leaderboard"

                if pygame.mouse.get_pressed()[0] and exit_button_box.inflate(10, 10).collidepoint(scale_mouse(event.pos)):  # exit game
                    pygame.quit()
                    exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and player.sprite.health != 0:
                    game_state = "game"

        try:  # background
            screen.blit(background1, (background_animation_x, 0))
            screen.blit(background1, (background1.get_width() + background_animation_x, 0))
        except NameError:
            screen.blit(background1, (0, 0))

        pygame.draw.rect(screen, "#303030", endgame_box)
        pygame.draw.rect(screen, "#aaeebb", endgame_box, 2)

        game_name = text_font.render("Turtle Survivors", False, "#aaeebb")  # game name in menu text
        game_name_box = game_name.get_rect(center=(endgame_box.centerx, endgame_box.top + 25))
        screen.blit(game_name, game_name_box)

        if player.sprite.health == 0:
            menu_continue = text_font.render("Continue", False, "#969696")  # continue text
        else:
            menu_continue = text_font.render("Continue", False, "#FFFFFF")
        menu_continue_box = menu_continue.get_rect(center=(endgame_box.centerx, game_name_box.centery + 35))
        if player.sprite.health == 0:
            pygame.draw.rect(screen, "#3C3C3C", menu_continue_box.inflate(10, 10), 15, 10)  # drowing continue button
        else:
            pygame.draw.rect(screen, "#4682B4", menu_continue_box.inflate(10, 10), 15, 10)
        screen.blit(menu_continue, menu_continue_box)

        newgame = text_font.render("Start Game", False, "#FFFFFF")  # start new game text
        newgame_box = newgame.get_rect(center=(endgame_box.centerx, menu_continue_box.centery + 40))
        pygame.draw.rect(screen, "#4682B4", newgame_box.inflate(10, 10), 15, 10)  # drowing start game button
        screen.blit(newgame, newgame_box)

        menu_skins = text_font.render("Skins", False, "#FFFFFF")  # menu skins button
        menu_skins_box = menu_skins.get_rect(center=(endgame_box.centerx, newgame_box.centery + 40))
        pygame.draw.rect(screen, "#4682B4", menu_skins_box.inflate(10, 10), 15, 10)
        screen.blit(menu_skins, menu_skins_box)

        leaderboard_menu_text = text_font.render("Leaderboard", False, "#FFFFFF")  # menu leaderboard button
        leaderboard_menu_text_box = leaderboard_menu_text.get_rect(center=(endgame_box.centerx, menu_skins_box.centery + 40))
        pygame.draw.rect(screen, "#4682B4", leaderboard_menu_text_box.inflate(10, 10), 15, 10)
        screen.blit(leaderboard_menu_text, leaderboard_menu_text_box)

        exit_button = text_font.render("Exit Game", False, "#FFFFFF")  # exit game text
        exit_button_box = exit_button.get_rect(center=(endgame_box.centerx, leaderboard_menu_text_box.centery + 40))
        pygame.draw.rect(screen, "#B22222", exit_button_box.inflate(10, 10), 15, 10)  # drowing exit game button
        screen.blit(exit_button, exit_button_box)

    elif game_state == "gameover":
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_state = "leaderboard"
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    if len(player_name) < 10:
                        player_name += event.unicode

        try:
            screen.blit(background1, (background_animation_x, 0))
            screen.blit(background1, (background1.get_width() + background_animation_x, 0))
        except NameError:
            screen.blit(background1, (0, 0))

        screen.blit(enter_name_box, ((screen.get_width() - enter_name_box.get_width()) // 2, (screen.get_height() - enter_name_box.get_height()) // 2))

        end_game_score_text = text_font.render(f"Game Over with Score: {round(score)}", False, "#db9b3a")
        end_game_score_text_box = end_game_score_text.get_rect(center=(400, 175))
        screen.blit(end_game_score_text, end_game_score_text_box)

        title_surface = text_font.render("Enter your name", False, "#db9b3a")
        title_rect = title_surface.get_rect(center=(400, 200))
        screen.blit(title_surface, title_rect)

        input_box = pygame.Rect(0, 0, 100, 50)
        input_box.center = (400, 230)
        text_surface = text_font.render(player_name, False, "#db9b3a")
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

    elif game_state == "leaderboard":
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    game_state = "menu"
                    play_music()

        try:  # background
            screen.blit(background1, (background_animation_x, 0))
            screen.blit(background1, (background1.get_width() + background_animation_x, 0))
        except NameError:
            screen.blit(background1, (0, 0))
        screen.blit(exit_text_helper, exit_text_helper.get_rect(topright=(800, 0)))

        screen.blit(leaderboard, ((screen.get_width() - leaderboard.get_width()) // 2, 0))  # leadderboard background

        leaderboard_data = load_leaderboard()

        if not score_saved and len(player_name) > 0:  # saving score in leaderboard
            add_new_score(player_name, round(score))
            score_saved = True

        for i, entry in enumerate(leaderboard_data):  # drowing leaderboard
            line_surface = text_font.render(f"{i+1}. {entry['name']}: {entry['score']}", False, "#db9b3a")
            screen.blit(line_surface, (leaderboard_text_rect.x, leaderboard_text_rect.y + i * 30))

    elif game_state == "skin_selection":
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                    game_state = "menu"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and turtle1_skin_box.collidepoint(scale_mouse(event.pos)):
                    player.sprite.selected_skin = "green_turtle"
                    save_selected_skin(player.sprite.selected_skin)
                    player.sprite.turtle_animation_set = green_turtle_animation_set
                    player.sprite.turtle_jump_animation_set = turtle1
                    player.sprite.turtle_hide_animation_set = green_turtle_hide_animation_set

                if pygame.mouse.get_pressed()[0] and golden_turtle1_skin_box.collidepoint(scale_mouse(event.pos)):
                    player.sprite.selected_skin = "golden_turtle"
                    save_selected_skin(player.sprite.selected_skin)
                    player.sprite.turtle_animation_set = golden_turtle_animation_set
                    player.sprite.turtle_jump_animation_set = golden_turtle1
                    player.sprite.turtle_hide_animation_set = golden_turtle_hide_animation_set

                if pygame.mouse.get_pressed()[0] and carrier_turtle1_skin_box.collidepoint(scale_mouse(event.pos)):
                    player.sprite.selected_skin = "carrier_turtle"
                    save_selected_skin(player.sprite.selected_skin)
                    player.sprite.turtle_animation_set = carrier_turtle_animation_set
                    player.sprite.turtle_jump_animation_set = carrier_turtle1
                    player.sprite.turtle_hide_animation_set = carrier_turtle_hide_animation_set

                if pygame.mouse.get_pressed()[0] and girl_turtle1_skin_box.collidepoint(scale_mouse(event.pos)):
                    player.sprite.selected_skin = "girl_turtle"
                    save_selected_skin(player.sprite.selected_skin)
                    player.sprite.turtle_animation_set = girl_turtle_animation_set
                    player.sprite.turtle_jump_animation_set = girl_turtle1
                    player.sprite.turtle_hide_animation_set = girl_turtle_hide_animation_set

        try:
            screen.blit(background1, (background_animation_x, 0))
            screen.blit(background1, (background1.get_width() + background_animation_x, 0))
        except NameError:
            screen.blit(background1, (0, 0))

        pygame.draw.rect(screen, "#303030", endgame_box)
        pygame.draw.rect(screen, "#aaeebb", endgame_box, 2)
        screen.blit(exit_text_helper, exit_text_helper.get_rect(topright=(800, 0)))

        screen.blit(turtle1, turtle1_skin_box)
        pygame.draw.rect(screen, "#aaeebb" if player.sprite.selected_skin == "green_turtle" else "#303030", turtle1_skin_box, 2)
        screen.blit(golden_turtle1, golden_turtle1_skin_box)
        pygame.draw.rect(screen, "#aaeebb" if player.sprite.selected_skin == "golden_turtle" else "#303030", golden_turtle1_skin_box, 2)
        screen.blit(carrier_turtle1, carrier_turtle1_skin_box)
        pygame.draw.rect(screen, "#aaeebb" if player.sprite.selected_skin == "carrier_turtle" else "#303030", carrier_turtle1_skin_box, 2)
        screen.blit(girl_turtle1, girl_turtle1_skin_box)
        pygame.draw.rect(screen, "#aaeebb" if player.sprite.selected_skin == "girl_turtle" else "#303030", girl_turtle1_skin_box, 2)

    scaled_screen = pygame.transform.scale(screen, full_screen.get_size())
    full_screen.blit(scaled_screen, (0, 0))
    pygame.display.flip()  # updating screen

    clock.tick(60)  # max frame rate
