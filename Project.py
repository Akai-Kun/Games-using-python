import os, pygame

WIDTH , HEIGHT = 1280 , 720                                                     #Window Size
COLOR = (255 , 255 , 255)                                                       #Window Color
WIN = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("Ping-Pong")
FPS = 60                                                                        #Frames Per Second
VEL = 2                                                                         #Velocity       
ELE_HEIGHT = 100                                                                #Element Height
ELE_WIDTH = 100                                                                 #Element Width

BG_IMAGE = pygame.image.load(                                                   #Background Image
    os.path.join("Game/Ping-Pong/Assets", "bg.png"))
BG = pygame.transform.scale(BG_IMAGE , (WIDTH , HEIGHT))                                   
RED_BAR_IMAGE = pygame.image.load(
    os.path.join("Game/Ping-Pong/Assets" , "red_bar.png"))                                #Red Bar Image
RED_BAR = pygame.transform.scale(RED_BAR_IMAGE , (ELE_WIDTH , ELE_HEIGHT))
BLUE_BAR_IMAGE = pygame.image.load(
    os.path.join("Game/Ping-Pong/Assets" , "blue_bar.png"))                               #Blue Bar Image
BLUE_BAR = pygame.transform.scale(BLUE_BAR_IMAGE , (ELE_WIDTH , ELE_HEIGHT))
BALL_IMAGE = pygame.image.load(
    os.path.join("Game/Ping-Pong/Assets" , "ball.png"))                                   #Ball Image
BALL = pygame.transform.scale(BALL_IMAGE , (75 , 75))



def window_color(red, blue):
    WIN.fill(COLOR)                                                             #Window Color                                                                     
    WIN.blit(BG , (0 , 0))                                                      #Background Image
    WIN.blit(RED_BAR , (red.x , red.y))                                         #Red Bar
    WIN.blit(BLUE_BAR , (blue.x , blue.y))                                      #Blue Bar
    WIN.blit(BALL , (300 , 50))                                                 #Ball
    pygame.display.update()                                                     #Update Window

def red_bar_movement(keys_pressed_red, red):
        keys_pressed_red = pygame.key.get_pressed()                             #Red Bar Movement
        if keys_pressed_red[pygame.K_w]:                                        #Red Bar Up
            red.y -= VEL
        elif keys_pressed_red[pygame.K_s]:                                      #Red Bar Down
            red.y += VEL  

def blue_bar_movement(keys_pressed_blue, blue):
        keys_pressed_blue = pygame.key.get_pressed()                            #Blue Bar Movement
        if keys_pressed_blue[pygame.K_UP]:                                      #Blue Bar Up
            blue.y -= VEL
        elif keys_pressed_blue[pygame.K_DOWN]:                                  #Blue Bar Down
            blue.y += VEL

def ball_movement(ball):
    ball.x += VEL
    ball.y += VEL                                               

def main():
    red = pygame.Rect(50 , 300 , ELE_WIDTH , ELE_HEIGHT)                            
    blue = pygame.Rect(1150 , 300 , ELE_WIDTH , ELE_HEIGHT)
    clock = pygame.time.Clock()                                                 #Clock
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed_red = pygame.key.get_pressed()
        red_bar_movement(keys_pressed_red, red)
        keys_pressed_blue = pygame.key.get_pressed()
        blue_bar_movement(keys_pressed_blue, blue)

        window_color(red, blue)

if __name__ == "__main__":                                                      #Main
    main()

pygame.quit()                                                                   #Quit