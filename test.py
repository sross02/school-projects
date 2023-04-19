import pygame
import random

pygame.init()

screen_width = 800
screen_height = 700
game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('BRAIN GAME')

light_pink = (255, 182, 193)
black = (0, 0, 0)

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

# maybe change these to be less annoying. maybe simpler sound.
correct_sound = pygame.mixer.Sound('correct.wav')
incorrect_sound = pygame.mixer.Sound('incorrect.wav')

score = 0
time_remaining = 30
running = True
game_over = False
#i want to add some level system seperate
def generate_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])
    problem = f'{num1} {operator} {num2}'
    answer = eval(problem)
    return problem, answer

def show_problem():
    problem_text = font.render(problem, True, black)
    game_display.blit(problem_text, (screen_width/2 - problem_text.get_width()/2, 50))

def show_score():
    score_text = font.render(f'Score: {score}', True, black)
    game_display.blit(score_text, (10, 10))

def show_time():
    time_text = font.render(f'Time: {int(round(time_remaining))}', True, black)
    game_display.blit(time_text, (screen_width - time_text.get_width() - 10, 10))

def show_game_over():
    #have to add function that allows "r to restart", might put 
    game_over_text = font.render('Game Over', True, black)
    score_text = font.render(f'Your score: {score}', True, black)
    restart_text = font.render('Press R to restart', True, black)
    game_display.blit(game_over_text, (screen_width/2 - game_over_text.get_width()/2, 150))
    game_display.blit(score_text, (screen_width/2 - score_text.get_width()/2, 200))
    game_display.blit(restart_text, (screen_width/2 - restart_text.get_width()/2, 250))


# the main game loop needs to be changed so that it doesn't rely on the game over because i think that is the problem
#while not game_over:
while True:
    if game_over:
        game_display.fill(light_pink)
        show_game_over()
        pygame.display.update()
        if event.type == pygame.K_r:
              game_over = False 
    else:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_RETURN and not game_over:
                    # checking the answer (good)
                    if answer_input == str(answer):
                        score += 1
                        correct_sound.play()
                    else:
                        incorrect_sound.play()
                    problem, answer = generate_problem()
                    answer_input = ''
                elif event.unicode.isnumeric() or event.unicode == '-':
                    if event.unicode == '-' and answer_input != '' and answer_input[-1] not in ['+', '-']:
                        continue
                    answer_input += event.unicode
                elif event.key == pygame.K_r and game_over:
                    # restarting the game i have to change the game can't restart
                    score = 0
                    time_remaining = 30
                    game_over = False
                    problem, answer = generate_problem()
                    answer_input = ''
        
        # generating a new problem (good)
        if 'answer_input' not in locals() and not game_over:
            problem, answer = generate_problem()
            answer_input = ''
        
        # update the screen (fix)
        game_display.fill(light_pink)
        if not game_over:
            show_problem()
            show_score()
            show_time()
            answer_input_text = font.render(answer_input, True, black)
            game_display.blit(answer_input_text, (screen_width/2 - answer_input_text.get_width()/2, 100))
        else:
            show_game_over()
        pygame.display.update()
    #^^^ berry important
        # updating game date and such (somewhat fix, the time is slightly faster but still functional)
        if not game_over:
            time_remaining -= .004

        # checking if the time ran out (fix along with the rest of the )
        if time_remaining <= 0:
            game_over = True

    # supposed to display game-over with an option to start over but will be fixed
    
