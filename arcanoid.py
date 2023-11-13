#arcanoid

import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블록깨기 게임")

# 색깔 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# 패들 설정
paddle_width, paddle_height = 100, 10
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 20

# 공 설정
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# 블록 설정
block_width, block_height = 50, 20
block_rows = 5
block_cols = WIDTH // block_width
blocks = []
for row in range(block_rows):
    for col in range(block_cols):
        block = pygame.Rect(col * block_width, row * block_height, block_width, block_height)
        blocks.append(block)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += 5

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # 벽과 충돌 검사
    if ball_x <= 0 or ball_x >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y <= 0:
        ball_speed_y = -ball_speed_y

    # 패들과 충돌 검사
    if paddle_y <= ball_y <= paddle_y + paddle_height and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_speed_y = -ball_speed_y

    # 블록과 충돌 검사
    for block in blocks:
        if block.colliderect(pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, 2 * ball_radius, 2 * ball_radius)):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    for block in blocks:
        pygame.draw.rect(screen, BLUE, block)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
