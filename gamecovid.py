import pygame


pygame.init()


display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("The best game for my Invoker!")


class Cactus:
    def __init__(self, x, y, width, image ,speed):
         self.x = x
         self.y = y
         self.width = width
         self.speed = speed
         self.image = image

    def move(self):
         if self.x >= -self.width:
            display.blit(self.image, (self.x , self.y))
            self.x -= self.speed
            return True
         else:
            return False
          
    
    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x , self.y))



usr_width = 140
usr_height = 150
usr_x = 10
usr_y = 380

cactus_width = 40
cactus_height = 100
cactus_x = display_height - 50
cactus_y = display_height - cactus_height - 100

covid_img = pygame.image.load(r'C:\\Users\\Тетяна\\Desktop\\python_work\\gitTest\\images\\p.png')
health_img = pygame.image.load(r"C:\\Users\Тетяна\\Desktop\\python_work\\gitTest\\images\\heart.png")
health_img = pygame.transform.scale(health_img, (40,40))
stars_img = pygame.image.load(r"C:\\Users\\Тетяна\\Desktop\\python_work\\gitTest\\images\\star.png"), pygame.image.load(r"C:\\Users\\Тетяна\\Desktop\\python_work\\gitTest\\images\\star.png")

img_counter = 0

health = 3

clock = pygame.time.Clock()
make_jump = False
jump_conter = 30

pygame.mixer.music.load(r"C:\Users\Тетяна\Desktop\python_work\gitTest\images\music.mp3")
pygame.mixer.music.set_volume(0.4)

def run_game():
    global make_jump

    game = True
    
    land = pygame.image.load(r'C:\Users\Тетяна\Desktop\python_work\gitTest\images\land.jpg')
    pygame.mixer.music.play(-1)
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

        if keys[pygame.K_ESCAPE]:
            pause()

        if make_jump:
            jump()

        display.blit(land, (0,0))
        
        show_health()
        draw_cactus()

        #pygame.draw.rect(display, (147, 40, 0), (usr_x, usr_y, usr_height, usr_width))
        draw_covid()
        pygame.display.update()

        clock.tick(50)

def jump():
    global usr_y, make_jump, jump_conter
    if jump_conter >= -30:
        usr_y -= jump_conter / 2
        jump_conter -= 1

    else:
        jump_conter = 30
        make_jump = False


def draw_cactus():
    global cactus_height, cactus_width, cactus_x, cactus_y
    if cactus_x >= - cactus_width:
        pygame.draw.rect(display, (30, 50, 0), (cactus_x, cactus_y, cactus_width, cactus_height))
        cactus_x -= 4
    else:
        cactus_x = display_width - 50


def draw_covid():
    global img_counter

    if img_counter == 1:
        img_counter = 0
    
    display.blit(covid_img, (usr_x, usr_y))
    img_counter += 1

def pause():
    paused = True

    pygame.mixer.music.pause()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.mixer.music.unpause()



        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(15)


def show_health():
    global health
    show = 0
    x = 20
    while show != health:
        display.blit(health_img, (x,20))
        x += 40
        show += 1

def check_health():
    global health
    health -= 1
    if health == 0:
        return False
    else:
        return True



run_game()
