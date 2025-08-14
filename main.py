import pygame
from win10toast import ToastNotifier
# Initialize Pygame
pygame.init()
pygame.font.init()
Title = "Undertale Python"
# Set up the window
screen = pygame.display.set_mode((480, 360))
pygame.display.set_caption(Title)
icon = pygame.image.load("assets/icon2.ico")
pygame.display.set_icon(icon)
pygame.mixer.music.load("assets/BATTLE.mp3")
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
#Varibles
notify = ToastNotifier()
# Game Variables
PlayX = 230
PlayY = 250
Speed = 1
CoinsColleted = 0
Hp = 100
# Load Images
PlayerIMG = pygame.image.load("assets/Player2.png")
BgIMG = pygame.image.load("assets/BG.png")
# Get Rects from images
player_rect = PlayerIMG.get_rect(topleft=(PlayX, PlayY))
# Font setup
font = pygame.font.Font("assets/Pixel.ttf", 36)
buleorred = "bule"
# Main Game Loop
running = True
while running:
    screen.fill("Black")

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    def redmovement():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w or pygame.K_UP]:
            player_rect.y -= Speed
        if keys[pygame.K_s or pygame.K_DOWN]:
            player_rect.y += Speed
        if keys[pygame.K_a or pygame.K_LEFT]:
            player_rect.x -= Speed
        if keys[pygame.K_d or pygame.K_RIGHT]:
            player_rect.x += Speed

        if keys[pygame.K_UP]:
            player_rect.y -= Speed
        if keys[pygame.K_DOWN]:
            player_rect.y += Speed
        if keys[pygame.K_LEFT]:
            player_rect.x -= Speed
        if keys[pygame.K_RIGHT]:
            player_rect.x += Speed
    def bulemovement():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w or pygame.K_UP]:
            player_rect.y -= Speed
        if keys[pygame.K_a or pygame.K_LEFT]:
            player_rect.x -= Speed
        if keys[pygame.K_d or pygame.K_RIGHT]:
            player_rect.x += Speed

        if keys[pygame.K_UP]:
            player_rect.y -= Speed
        if keys[pygame.K_LEFT]:
            player_rect.x -= Speed
        if keys[pygame.K_RIGHT]:
            player_rect.x += Speed
        player_rect.y += Speed/2
    redmovement()
    #Check if player is out of bound
    if player_rect.x <165:
        player_rect.x = player_rect.x + Speed
    if player_rect.x >303:
        player_rect.x = player_rect.x - Speed
    if player_rect.y <194:
        player_rect.y = player_rect.y + Speed
    if player_rect.y > 308:
        player_rect.y = player_rect.y - Speed
    # Draw text
    HP_text = font.render(f"Health: {Hp}", True, (255, 255, 255))
    # Draw player and coin

    screen.blit(BgIMG, (0, 0))
    screen.blit(PlayerIMG, player_rect)
    screen.blit(HP_text, (0, 0))
    # Update screen
    pygame.display.flip()
    clock.tick(60)
pygame.quit()


notify = ToastNotifier()
notify.show_toast("BUBS Services", "Undertale Python has been closed", duration=5)