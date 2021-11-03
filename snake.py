import random
import pygame
import sys
import time

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}


class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False
    started = False

    apple_location = [0,0]

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        # TODO: See section 3, "Turning the snake".
        self.direction = dir
        pass

    def collision(self, x, y):
        # TODO: See section 2, "Collisions", and section 4, "Self Collisions"
        # check self-collision
        for i in range(1, len(self.body)):
            if x == self.body[i][0] and y == self.body[i][1]:
                return True
        # check collision
        if not 0 <= x <= 23:
            return True
        elif not 0 <= y <= 23:
            return True
        else:
            return False
        pass
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):

        if not self.started:
            return
        # add to list if ate an apple
        if self.l >= len(self.body):
            growth = self.body[-1]
            self.body.append(growth)

        # check for collision
        if self.collision(self.body[0][0], self.body[0][1]):
            self.kill()

        # TODO: See section 1, "Move the snake!". You will be revisiting this section a few times.
        new_location = [self.body[0][0] + DIR[self.direction][0], self.body[0][1] + DIR[self.direction][1]]
        
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i-1]
        self.body[0] = new_location
        pass

    def kill(self):
        # TODO: See section 11, "Try again!"
        
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')
        if k == pygame.K_SPACE:
            self.started = True
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.init()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            else:
                self.handle_keypress(event.key)
                self.wait_for_key()
    
    def wait_for_key(self):
        # TODO: see section 10, "wait for user input".
        # Implemented within handle_key_press. If Space pressed, game starts
        pass


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        # TODO: see section 6, "moving the apple".
        while True:
            location_x = rand_int(23)
            location_y = rand_int(23)
            unique = True
            for i in (snake):
                if location_x != i[0] or location_y != i[1]:
                    continue
                else:
                    unique = False
            if unique:
                break
        self.position = [location_x, location_y]              
        pass

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def show_score(x, y, font, score_val):
    score = font.render("Score :" + str(score_val), True, (255, 255, 255))


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    start_time = time.time()

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    apple = Apple()

    # score
    score = 0
    font = pygame.font.Font('freesansbold.ttf',28)

    while True:

        # TODO: see section 10, "incremental difficulty".
        # Implements feature #9
        time_passed = time.time() - start_time
        if time_passed <= 10:
            clock.tick(5)
        elif time_passed <= 20:
            clock.tick(7)
        elif time_passed <= 30:
            clock.tick(9)
        elif time_passed <= 40:
            clock.tick(15)
        else:
            clock.tick(25)
        snake.check_events()
        draw_grid(surface)        
        snake.move()

        snake.draw(surface)
        apple.draw(surface)

        # TODO: see section 5, "Eating the Apple".
        if snake.body[0] == apple.position:
            apple.place(snake.body)
            score += 1
            snake.l += 1
            print("the snake ate an apple!")

        screen.blit(surface, (0,0))
        # TODO: see section 8, "Display the Score"
        score_display = font.render("Score :" + str(score), True, (255, 255, 255))
        screen.blit(score_display, (10, 10))

        # Implements feature #10
        # add a text for space bar press
        if not snake.started:
            start_text = font.render("Press Space to Start", True, (255, 255, 255))
            screen.blit(start_text, (100, 100))

        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            snake.dead = False
            pygame.quit()
            sys.exit(0)

if __name__ == "__main__":
    main()