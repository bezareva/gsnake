import random
import pygame
import time

if __name__ == '__main__':

    pygame.init()

    orange = (247, 135, 30)
    pink = (240, 58, 215)
    green = (174, 240, 127)
    snake = (20, 65, 6)
    black = (0, 0, 0)

    dis_width = 800
    dis_height = 600
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake')

    clock = pygame.time.Clock()

    snake_speed = 10
    snake_block = 20

    font_style = pygame.font.SysFont("bahnschrift", 40)
    score_font = pygame.font.SysFont("bahnschrift", 40)
    smallfont = pygame.font.SysFont('Corbel', 35)


    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, black)
        dis.blit(value, [dis_width /20, dis_height / 20])

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, snake, [x[0], x[1], snake_block, snake_block])


    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 2])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block)/20.0)*20.0
        foody = round(random.randrange(0, dis_height - snake_block)/20.0)*20.0
        while not game_over:

            while game_close == True:
                dis.fill(green)
                message("You Lost! Press Q-Quit or C-Play Again", orange)
                Your_score(Length_of_snake - 1)

                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if dis_width / 20 <= mouse[0] <= dis_width / 20 + 140 and dis_height / 10 <= mouse[1] <= dis_height / 10 + 40:
                            pygame.draw.rect(dis, pink, [dis_width / 20, dis_height / 10, 140, 40])
                mouse = pygame.mouse.get_pos()
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(green)
            pygame.draw.rect(dis, pink, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)

            pygame.display.update()

            #zmija jede i raste
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
                foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
                Length_of_snake += 1
            clock.tick(snake_speed)

        pygame.quit()
        quit()
    gameLoop()

