import pygame
import sys
import time
import random

pygame.init()

Width = 800
Height = 600
white = (255,255,255)
black = (0,0,0)
blue = (0,0,139)
player_width = 80
player_height = 100
player_speed = 5
ice_width = 40
ice_height = 60
ice_x = (Width - player_width)//2
ice_y = Height - player_height - 1
ice_speed = 20
font = pygame.font.Font(None,36)
start_time = pygame.time.get_ticks()

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Ice Fall")

start_image = pygame.image.load("start.png")
print("Loaded start screen")

background_image = pygame.image.load("background.png")
print("Loaded background image")

player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (player_width, player_height))

print("Loaded player")

ice_image = pygame.image.load("ice.png")
ice_image = pygame.transform.scale(ice_image, (ice_width, ice_height))
print("Loaded ice")

clock = pygame.time.Clock()

hit = False

pygame.mouse.set_visible(False)


def start_screen():
    while True:
        screen.blit(start_image, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return

def draw(player, ice, time_elapse):
    screen.blit(background_image, (0,0))
    screen.blit(player_image, (player.x, player.y))
    screen.blit(ice_image, (ice.x,ice.y))

    timer_surface = font.render(f"Time: {time_elapse // 1000}", True, "blue")
    text_rect = timer_surface.get_rect(center=(Width//2, Height//2))
    screen.blit(timer_surface, text_rect)

    pygame.display.update()

def get_random_x():
    return random.randint(0, Width - ice_width)

def main():
    global hit

    clock = pygame.time.Clock()

    running = True

    player = pygame.Rect(350, Height - player_height, player_width, player_height)
    ice = pygame.Rect(get_random_x(), 0, ice_width, ice_height)


    while running:

        clock.tick(60)

        time_elapse = pygame.time.get_ticks() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_speed >= 0:
            player.x -= player_speed

        if keys[pygame.K_RIGHT] and player.x + player_speed + player_width <= Width:
            player.x += player_speed

        ice.y += ice_speed
        if ice.y > Height:
            ice.x = get_random_x()
            ice.y = -ice_height

        if player.colliderect(ice):
            hit = True

        if hit:
            game_over_text = font.render(f"You Lost", True, "blue")
            game_over_text_rect = game_over_text.get_rect(center=(395, 150))
            screen.blit(game_over_text, game_over_text_rect)
            pygame.display.update()
            pygame.time.delay(2000)
            break

        draw(player, ice, time_elapse)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    start_screen()
    main()
