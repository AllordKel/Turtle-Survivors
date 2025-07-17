import pygame
import os
import json
from sys import exit
from random import randint, choice

os.chdir(os.path.dirname(__file__))

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()  # launches pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 400), pygame.FULLSCREEN | pygame.SCALED) # game screen

try:
    with open("saves\\player_data.json", "r") as f:
        player_data = json.load(f)
except FileNotFoundError:
    player_data = {"leaderboard": [], "selected_skin": "green_turtle", "shells_currency": 0, "golden_turtle_purchased": False, "carrier_turtle_purchased": False, "girl_turtle_purchased": False}

# event timers
enemy_timer = pygame.USEREVENT + 1  # enemy spawn timer

# font
text_font = pygame.font.SysFont(None, 30)

# utilities upload
pygame.display.set_caption("Turtle Survivors")

menu_music = pygame.mixer.Sound("sound//menu.ogg")
game_music = pygame.mixer.Sound("sound//game.ogg")
game_music_channel = game_music.play(-1)
game_music_channel.pause()

background1 = pygame.image.load("images\\Back.png").convert_alpha()  # background image

heart1 = pygame.image.load("images\\heart.png").convert_alpha()  # health img
heart1 = pygame.transform.scale(heart1, (heart1.get_width() // 8, heart1.get_height() // 8))

leaderboard = pygame.image.load("images\\leaderboard.png").convert_alpha()  # leaderboard image
leaderboard = pygame.transform.scale(leaderboard, (leaderboard.get_width() // 1.5, 400))  # leaderboard.get_height() // 1.5

enter_name_frame = pygame.image.load("images\\enter_name.png").convert_alpha()  # enter name box image
enter_name_frame = pygame.transform.scale(enter_name_frame, (enter_name_frame.get_width() // 1.5, enter_name_frame.get_height() // 1.5))  # leaderboard.get_height() // 1.5
enter_name_frame_box = enter_name_frame.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

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

shell = pygame.image.load("images\\shell.png").convert_alpha()  # shell currency image
shell_box = shell.get_rect(topright=(endgame_box.centerx, endgame_box.top + 10))

ad_img = pygame.image.load("images\\ad.png").convert_alpha()
ad_img = pygame.transform.scale(ad_img, (800, 400))

game_hint_img = pygame.image.load("images\\hint.png").convert_alpha()
game_hint_img = pygame.transform.scale(game_hint_img, (800, 400))

# rendering text and setting boxes
healthbar_text_surface = text_font.render("Health: ", False, "purple")  # healthbar text surface

exit_text_helper = text_font.render("Press Space to continue", False, "black")

turtle1_skin_box = turtle1.get_rect(center=(endgame_box.centerx - 125, endgame_box.centery - 70))
golden_turtle1_skin_box = golden_turtle1.get_rect(center=(endgame_box.centerx + 125, endgame_box.centery - 70))
carrier_turtle1_skin_box = carrier_turtle1.get_rect(center=(endgame_box.centerx - 125, endgame_box.centery + 50))
girl_turtle1_skin_box = girl_turtle1.get_rect(center=(endgame_box.centerx + 125, endgame_box.centery + 50))

want_purchase = False
not_enough_shells = False
carrier_turtle_price = 25  # carrier turtle skin price
carrier_turtle_price_text = text_font.render(str(carrier_turtle_price), False, "#db9b3a")
carrier_turtle_price_text_box = carrier_turtle_price_text.get_rect(midtop=(carrier_turtle1_skin_box.centerx - (shell.get_width() + 5) // 2, girl_turtle1_skin_box.bottom + 10))
girl_turtle_price = 50  # girl turtle skin price
girl_turtle_price_text = text_font.render(str(girl_turtle_price), False, "#db9b3a")
girl_turtle_price_text_box = girl_turtle_price_text.get_rect(midtop=(girl_turtle1_skin_box.centerx - (shell.get_width() + 5) // 2, girl_turtle1_skin_box.bottom + 10))
golden_turtle_price = 10  # gold turtle skin price
gold_turtle_price_text = text_font.render(str(golden_turtle_price), False, "#db9b3a")
gold_turtle_price_text_box = gold_turtle_price_text.get_rect(midtop=(golden_turtle1_skin_box.centerx - (shell.get_width() + 5) // 2, golden_turtle1_skin_box.bottom + 10))

purchase_question_text1 = text_font.render("Do you want to", False, "#db9b3a")
purchase_question_text_box1 = purchase_question_text1.get_rect(center=(400, 175))

confirm_purchase_text = text_font.render("Yes", False, "#db9b3a")
confirm_purchase_text_box = confirm_purchase_text.get_rect(center=(350, 220))

reject_purchase_text = text_font.render("No", False, "#db9b3a")
reject_purchase_text_box = reject_purchase_text.get_rect(center=(450, 220))

not_enough_shells_text = text_font.render("Not enough shells", False, "#db9b3a")
not_enough_shells_text_box = not_enough_shells_text.get_rect(center=(400, 200))

ad_watch_text1 = text_font.render("You've been captured", False, "#db9b3a")
ad_watch_text1_box = ad_watch_text1.get_rect(center=(400, 175))

ad_watch_text2 = text_font.render("Watch the ad to get more     ?", False, "#db9b3a")
ad_watch_text2_box = ad_watch_text2.get_rect(center=(400, 195))

ad_finish_button_text = text_font.render("Get reward", False, "white")

reward_button_rect = pygame.Rect(300, 300, 200, 50)
leaderboard_text_rect = pygame.Rect(300, 165, 200, 180)


class turtle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.selected_skin = player_data["selected_skin"]
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
    global background_animation_x
    background_animation_x = 0
    global spawn_interval
    spawn_interval = 1000
    pygame.time.set_timer(enemy_timer, spawn_interval)
    global player_name
    player_name = ""
    game_music_channel.play(game_music, loops=-1)
    global old_score_display
    old_score_display = -1
    global ad_watched
    ad_watched = False
    global score_saved
    score_saved = False


def add_new_score(name, score):
    player_data["leaderboard"].append({"name": name, "score": score})
    player_data["leaderboard"].sort(key=lambda x: x["score"], reverse=True)  # descent sorting
    player_data["leaderboard"] = player_data["leaderboard"][:6]  # leaving only top 6
    with open("saves\\player_data.json", "w") as f:
        json.dump(player_data, f, indent=4)


def save_selected_skin(skin):
    player_data["selected_skin"] = skin
    with open("saves\\player_data.json", "w") as f:
        json.dump(player_data, f, indent=4)


def save_shells_currency(shells):
    player_data["shells_currency"] = shells
    with open("saves\\player_data.json", "w") as f:
        json.dump(player_data, f, indent=4)


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

hint_read = False
display_hint = False
game_state = "menu"
play_music()

while True:
    events = pygame.event.get()
    keys = pygame.key.get_pressed()  # saving all keyboard inputs

    for event in events:  # for inputss and events
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_state == "game":
            if event.type == enemy_timer:  # adding enemies to the enemy list
                enemies.add(mobs(choice(["rat", "eagle"])))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # pause
                    game_state = "menu"

        elif game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and menu_continue_box.inflate(10, 10).collidepoint(event.pos) and player.sprite.health != 0:  # continue
                    game_state = "game"

                elif not hint_read and pygame.mouse.get_pressed()[0] and newgame_box.inflate(10, 10).collidepoint(event.pos):  # start new game with hint
                    display_hint = True

                elif hint_read and pygame.mouse.get_pressed()[0] and newgame_box.inflate(10, 10).collidepoint(event.pos):  # start new game
                    new_game()
                    game_state = "game"
                    play_music()

                elif pygame.mouse.get_pressed()[0] and menu_skins_box.inflate(10, 10).collidepoint(event.pos):  # skins button
                    game_state = "skin_selection"

                elif pygame.mouse.get_pressed()[0] and leaderboard_menu_text_box.inflate(10, 10).collidepoint(event.pos):  # leaderboard button
                    score_saved = True
                    game_state = "leaderboard"

                elif pygame.mouse.get_pressed()[0] and exit_button_box.inflate(10, 10).collidepoint(event.pos):  # exit game
                    pygame.quit()
                    exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and player.sprite.health != 0:
                    game_state = "game"

                elif display_hint and (event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                    hint_read = True
                    display_hint = False
                    new_game()
                    game_state = "game"
                    play_music()

        elif game_state == "leaderboard":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    game_state = "menu"
                    play_music()

        elif game_state == "gameover":
            if event.type == pygame.KEYDOWN:
                if ad_watched and not ad_running and event.key == pygame.K_RETURN:
                    player_data["shells_currency"] += round(score)  # saving shells currency
                    save_shells_currency(player_data["shells_currency"])
                    game_state = "leaderboard"
                elif ad_watched and not ad_running and event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                elif ad_watched and not ad_running:
                    if len(player_name) < 10:
                        player_name += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ad_watched and pygame.mouse.get_pressed()[0] and reject_purchase_text_box.inflate(5, 5).collidepoint(event.pos):
                    ad_watched = True
                elif not ad_watched and pygame.mouse.get_pressed()[0] and confirm_purchase_text_box.inflate(5, 5).collidepoint(event.pos):
                    ad_start_time = pygame.time.get_ticks()
                    game_music_channel.pause()
                    ad_finished = False
                    ad_running = True
                elif ad_running and ad_finished and reward_button_rect.collidepoint(event.pos):
                    player.sprite.health = player.sprite.max_health
                    player.sprite.damage_time = pygame.time.get_ticks()
                    player.sprite.damage_cooldown = True
                    game_music_channel.unpause()
                    game_state = "game"
                    ad_watched = True
                    ad_running = False

        elif game_state == "skin_selection":
            if event.type == pygame.KEYDOWN:
                if not_enough_shells == True and (event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE):
                    not_enough_shells = False

                elif event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                    game_state = "menu"

            if event.type == pygame.MOUSEBUTTONDOWN:
                # selecting green turtle skin
                if not want_purchase and not not_enough_shells and pygame.mouse.get_pressed()[0] and turtle1_skin_box.collidepoint(event.pos):
                    player.sprite.selected_skin = "green_turtle"
                    save_selected_skin(player.sprite.selected_skin)
                    player.sprite.turtle_animation_set = green_turtle_animation_set
                    player.sprite.turtle_jump_animation_set = turtle1
                    player.sprite.turtle_hide_animation_set = green_turtle_hide_animation_set

                # wanting to purchase golden turtle skin
                elif not want_purchase and not not_enough_shells and pygame.mouse.get_pressed()[0] and golden_turtle1_skin_box.collidepoint(event.pos) and not player_data["golden_turtle_purchased"]:
                    want_purchase = True
                    purchase_skin = "Golden Turtle"

                # selecting golden turtle skin
                elif not want_purchase and not not_enough_shells and pygame.mouse.get_pressed()[0] and golden_turtle1_skin_box.collidepoint(event.pos) and player_data["golden_turtle_purchased"]:
                    player.sprite.selected_skin = "golden_turtle"
                    save_selected_skin(player.sprite.selected_skin)
                    player.sprite.turtle_animation_set = golden_turtle_animation_set
                    player.sprite.turtle_jump_animation_set = golden_turtle1
                    player.sprite.turtle_hide_animation_set = golden_turtle_hide_animation_set

                # wanting to purchase carrier turtle skin
                elif not want_purchase and not not_enough_shells and pygame.mouse.get_pressed()[0] and carrier_turtle1_skin_box.collidepoint(event.pos) and not player_data["carrier_turtle_purchased"]:
                    want_purchase = True
                    purchase_skin = "Carrier Turtle"

                # selecting carrier turtle skin
                elif not want_purchase and not not_enough_shells and pygame.mouse.get_pressed()[0] and carrier_turtle1_skin_box.collidepoint(event.pos) and player_data["carrier_turtle_purchased"]:
                    player.sprite.selected_skin = "carrier_turtle"
                    save_selected_skin(player.sprite.selected_skin)
                    player.sprite.turtle_animation_set = carrier_turtle_animation_set
                    player.sprite.turtle_jump_animation_set = carrier_turtle1
                    player.sprite.turtle_hide_animation_set = carrier_turtle_hide_animation_set

                # wanting to purchase girl turtle skin
                elif not want_purchase and not not_enough_shells and pygame.mouse.get_pressed()[0] and girl_turtle1_skin_box.collidepoint(event.pos) and not player_data["girl_turtle_purchased"]:
                    want_purchase = True
                    purchase_skin = "Girl Turtle"

                # selecting girl turtle skin
                elif not want_purchase and not not_enough_shells and pygame.mouse.get_pressed()[0] and girl_turtle1_skin_box.collidepoint(event.pos) and player_data["girl_turtle_purchased"]:
                    player.sprite.selected_skin = "girl_turtle"
                    save_selected_skin(player.sprite.selected_skin)
                    player.sprite.turtle_animation_set = girl_turtle_animation_set
                    player.sprite.turtle_jump_animation_set = girl_turtle1
                    player.sprite.turtle_hide_animation_set = girl_turtle_hide_animation_set

                # rejecting purchase
                elif want_purchase and pygame.mouse.get_pressed()[0] and reject_purchase_text_box.inflate(5, 5).collidepoint(event.pos):
                    want_purchase = False

                # confirming purchase
                elif want_purchase and pygame.mouse.get_pressed()[0] and confirm_purchase_text_box.inflate(5, 5).collidepoint(event.pos):
                    if purchase_skin == "Golden Turtle" and player_data["shells_currency"] >= golden_turtle_price:
                        player_data["golden_turtle_purchased"] = True
                        player_data["selected_skin"] = "golden_turtle"
                        player.sprite.selected_skin = "golden_turtle"
                        player.sprite.turtle_animation_set = golden_turtle_animation_set
                        player.sprite.turtle_jump_animation_set = golden_turtle1
                        player.sprite.turtle_hide_animation_set = golden_turtle_hide_animation_set
                        player_data["shells_currency"] -= carrier_turtle_price
                        save_shells_currency(player_data["shells_currency"])
                        shell_text_surface = text_font.render(f": {player_data["shells_currency"]}", False, "#db9b3a")
                        want_purchase = False
                    elif purchase_skin == "Golden Turtle" and player_data["shells_currency"] < golden_turtle_price:
                        not_enough_shells = True
                        want_purchase = False
                    elif purchase_skin == "Carrier Turtle" and player_data["shells_currency"] >= carrier_turtle_price:
                        player_data["carrier_turtle_purchased"] = True
                        player_data["selected_skin"] = "carrier_turtle"
                        player.sprite.selected_skin = "carrier_turtle"
                        player.sprite.turtle_animation_set = carrier_turtle_animation_set
                        player.sprite.turtle_jump_animation_set = carrier_turtle1
                        player.sprite.turtle_hide_animation_set = carrier_turtle_hide_animation_set
                        player_data["shells_currency"] -= carrier_turtle_price
                        save_shells_currency(player_data["shells_currency"])
                        shell_text_surface = text_font.render(f": {player_data["shells_currency"]}", False, "#db9b3a")
                        want_purchase = False
                    elif purchase_skin == "Carrier Turtle" and player_data["shells_currency"] < carrier_turtle_price:
                        not_enough_shells = True
                        want_purchase = False
                    elif purchase_skin == "Girl Turtle" and player_data["shells_currency"] >= girl_turtle_price:
                        player_data["girl_turtle_purchased"] = True
                        player_data["selected_skin"] = "girl_turtle"
                        player.sprite.selected_skin = "girl_turtle"
                        player.sprite.turtle_animation_set = girl_turtle_animation_set
                        player.sprite.turtle_jump_animation_set = girl_turtle1
                        player.sprite.turtle_hide_animation_set = girl_turtle_hide_animation_set
                        player_data["shells_currency"] -= carrier_turtle_price
                        save_shells_currency(player_data["shells_currency"])
                        shell_text_surface = text_font.render(f": {player_data["shells_currency"]}", False, "#db9b3a")
                        want_purchase = False
                    elif purchase_skin == "Girl Turtle" and player_data["shells_currency"] < girl_turtle_price:
                        not_enough_shells = True
                        want_purchase = False

                # closing not enough shells message
                elif not_enough_shells and pygame.mouse.get_pressed()[0] and enter_name_frame_box.collidepoint(event.pos):
                    not_enough_shells = False

    if game_state == "game":
        # speeding
        if score <= 100:
            speeding_rate = 1 + score / 100

        # background animation
        background_animation_x = (background_animation_x - 3 * speeding_rate) % background1.get_width()
        screen.blit(background1, (background_animation_x, 0))
        screen.blit(background1, (background_animation_x - background1.get_width(), 0))

        # enemies spawn interval
        new_spawn_interval = round(1000 - 50 * (score // 10))
        if new_spawn_interval != spawn_interval and spawn_interval > 650:
            spawn_interval = new_spawn_interval
            pygame.time.set_timer(enemy_timer, spawn_interval)

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
            ad_running = False
            game_state = "gameover"

    elif game_state == "menu":
        # music
        play_music()

        if display_hint:
            screen.blit(game_hint_img, (0, 0))
            screen.blit(exit_text_helper, exit_text_helper.get_rect(topright=(800, 0)))

        else:
            try:  # background
                screen.blit(background1, (-background_animation_x, 0))
                screen.blit(background1, (-background_animation_x + background1.get_width(), 0))
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
        try:
            screen.blit(background1, (-background_animation_x, 0))
            screen.blit(background1, (-background_animation_x + background1.get_width(), 0))
        except NameError:
            screen.blit(background1, (0, 0))

        screen.blit(enter_name_frame, enter_name_frame_box)

        if not ad_watched:
            screen.blit(ad_watch_text1, ad_watch_text1_box)
            screen.blit(ad_watch_text2, ad_watch_text2_box)
            screen.blit(heart1, (502, 180))
            pygame.draw.rect(screen, "#55aa55", confirm_purchase_text_box.inflate(5, 5), 15, 10)
            screen.blit(confirm_purchase_text, confirm_purchase_text_box)
            pygame.draw.rect(screen, "#aa5555", reject_purchase_text_box.inflate(5, 5), 15, 10)
            screen.blit(reject_purchase_text, reject_purchase_text_box)

        if ad_running:

            # showing ad screen
            screen.blit(ad_img, (0, 0))

            # after 5 seconds
            if pygame.time.get_ticks() - ad_start_time > 5000:
                ad_finished = True
                pygame.draw.rect(screen, "#88cc88", reward_button_rect)
                screen.blit(ad_finish_button_text, (reward_button_rect.centerx - ad_finish_button_text.get_width() // 2, reward_button_rect.centery - ad_finish_button_text.get_height() // 2))

        elif ad_watched:
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
        try:  # background
            screen.blit(background1, (-background_animation_x, 0))
            screen.blit(background1, (-background_animation_x + background1.get_width(), 0))
        except NameError:
            screen.blit(background1, (0, 0))
        screen.blit(exit_text_helper, exit_text_helper.get_rect(topright=(800, 0)))

        screen.blit(leaderboard, ((screen.get_width() - leaderboard.get_width()) // 2, 0))  # leadderboard background

        leaderboard_data = player_data["leaderboard"]

        if not score_saved and len(player_name) > 0:  # saving score in leaderboard
            add_new_score(player_name, round(score))
            score_saved = True

        for i, entry in enumerate(leaderboard_data):  # drowing leaderboard
            line_surface = text_font.render(f"{i+1}. {entry['name']}: {entry['score']}", False, "#db9b3a")
            screen.blit(line_surface, (leaderboard_text_rect.x, leaderboard_text_rect.y + i * 30))

    elif game_state == "skin_selection":
        try:
            screen.blit(background1, (-background_animation_x, 0))
            screen.blit(background1, (-background_animation_x + background1.get_width(), 0))
        except NameError:
            screen.blit(background1, (0, 0))

        pygame.draw.rect(screen, "#303030", endgame_box)
        pygame.draw.rect(screen, "#aaeebb", endgame_box, 2)
        screen.blit(exit_text_helper, exit_text_helper.get_rect(topright=(800, 0)))

        screen.blit(player.sprite.turtle_animation_set[int(pygame.time.get_ticks() // 100 % len(player.sprite.turtle_animation_set))] if player.sprite.selected_skin == "green_turtle" else turtle1, turtle1_skin_box)
        pygame.draw.rect(screen, "#aaeebb" if player.sprite.selected_skin == "green_turtle" else "#303030", turtle1_skin_box.inflate(15, 15), 2)
        screen.blit(player.sprite.turtle_animation_set[int(pygame.time.get_ticks() // 100 % len(player.sprite.turtle_animation_set))] if player.sprite.selected_skin == "golden_turtle" else golden_turtle1, golden_turtle1_skin_box)
        pygame.draw.rect(screen, "#aaeebb" if player.sprite.selected_skin == "golden_turtle" else "#303030", golden_turtle1_skin_box.inflate(15, 15), 2)
        screen.blit(player.sprite.turtle_animation_set[int(pygame.time.get_ticks() // 100 % len(player.sprite.turtle_animation_set))] if player.sprite.selected_skin == "carrier_turtle" else carrier_turtle1, carrier_turtle1_skin_box)
        pygame.draw.rect(screen, "#aaeebb" if player.sprite.selected_skin == "carrier_turtle" else "#303030", carrier_turtle1_skin_box.inflate(15, 15), 2)
        screen.blit(player.sprite.turtle_animation_set[int(pygame.time.get_ticks() // 100 % len(player.sprite.turtle_animation_set))] if player.sprite.selected_skin == "girl_turtle" else girl_turtle1, girl_turtle1_skin_box)
        pygame.draw.rect(screen, "#aaeebb" if player.sprite.selected_skin == "girl_turtle" else "#303030", girl_turtle1_skin_box.inflate(15, 15), 2)

        shell_text_surface = text_font.render(f": {player_data["shells_currency"]}", False, "#db9b3a")
        shell_text_surface_box = shell_text_surface.get_rect(midleft=(shell_box.right + 5, shell_box.centery))
        screen.blit(shell, shell_box)
        screen.blit(shell_text_surface, shell_text_surface_box)

        if not player_data["carrier_turtle_purchased"]:
            screen.blit(carrier_turtle_price_text, carrier_turtle_price_text_box)
            screen.blit(shell, (carrier_turtle_price_text_box.right + 5, carrier_turtle_price_text_box.top + 2))
        if not player_data["girl_turtle_purchased"]:
            screen.blit(girl_turtle_price_text, girl_turtle_price_text_box)
            screen.blit(shell, (girl_turtle_price_text_box.right + 5, girl_turtle_price_text_box.top + 2))
        if not player_data["golden_turtle_purchased"]:
            screen.blit(gold_turtle_price_text, gold_turtle_price_text_box)
            screen.blit(shell, (gold_turtle_price_text_box.right + 5, gold_turtle_price_text_box.top + 2))

        if want_purchase:
            screen.blit(enter_name_frame, enter_name_frame_box)

            purchase_question_text2 = text_font.render(f"Purchase {purchase_skin}?", False, "#db9b3a")
            purchase_question_text_box2 = purchase_question_text2.get_rect(center=(400, 195))
            screen.blit(purchase_question_text1, purchase_question_text_box1)
            screen.blit(purchase_question_text2, purchase_question_text_box2)

            pygame.draw.rect(screen, "#55aa55", confirm_purchase_text_box.inflate(5, 5), 15, 10)
            screen.blit(confirm_purchase_text, confirm_purchase_text_box)

            pygame.draw.rect(screen, "#aa5555", reject_purchase_text_box.inflate(5, 5), 15, 10)
            screen.blit(reject_purchase_text, reject_purchase_text_box)

        if not_enough_shells:
            screen.blit(enter_name_frame, enter_name_frame_box)
            screen.blit(not_enough_shells_text, not_enough_shells_text_box)

    pygame.display.flip()  # updating screen
    clock.tick(60)  # max frame rate
