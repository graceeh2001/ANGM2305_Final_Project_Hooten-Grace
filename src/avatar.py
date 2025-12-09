import pygame
import random


pygame.init()

#window size 
WINDOW_WIDTH = 920
WINDOW_HEIGHT = 1000
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Avatar Randomizer <3")

#bg
WHITE = (255, 255, 255)

#avatar feature images
hairbottom_images = [pygame.image.load("bottom_shorthair.png").convert_alpha(), pygame.image.load("bottom_curls.png").convert_alpha(), pygame.image.load("bottom_straight.png").convert_alpha()]
clothes_images = [pygame.image.load("yellow_shirt.png").convert_alpha(), pygame.image.load("pink_shirt.png").convert_alpha(), pygame.image.load("blue_shirt.png").convert_alpha()]
head_images = [pygame.image.load("head_lightskin.png").convert_alpha(), pygame.image.load("head_tanskin.png").convert_alpha(), pygame.image.load("head_darkskin.png").convert_alpha()]
acc_images = [pygame.image.load("glasses.png").convert_alpha(), pygame.image.load("earrings.png").convert_alpha(), pygame.image.load("neckglass.png").convert_alpha()]
hairtop_images = [pygame.image.load("black_hijab.png").convert_alpha(), pygame.image.load("straight_bang.png").convert_alpha(), pygame.image.load("shaggy_bangs.png").convert_alpha(), pygame.image.load("middlepart_bang.png").convert_alpha()]
eye_images = [pygame.image.load("nolashes_eye.png").convert_alpha(), pygame.image.load("lashes_eye.png").convert_alpha(), pygame.image.load("sideeyes_eye.png").convert_alpha(), pygame.image.load("wink_eye.png").convert_alpha()]
mouth_images = [pygame.image.load("bored_lips.png").convert_alpha(), pygame.image.load("smirk_lips.png").convert_alpha(), pygame.image.load("happy_lips.png").convert_alpha(), pygame.image.load("lipstick_lips.png").convert_alpha()]
nose_images = [pygame.image.load("line_nose.png").convert_alpha(), pygame.image.load("button_nose.png").convert_alpha(), pygame.image.load("manga_nose.png").convert_alpha(), pygame.image.load("round_nose.png").convert_alpha()]



#function draws the avatar
def draw_avatar(hairbottom_image, clothes_image, head_image, acc_image, hairtop_image, eye_image, mouth_image, nose_image):
    scaled_hairbottom = pygame.transform.scale(hairbottom_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_hairbottom, (0, 0))

    scaled_clothes = pygame.transform.scale(clothes_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_clothes, (0, 0))
    
    scaled_head = pygame.transform.scale(head_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_head, (0, 0))

    scaled_acc = pygame.transform.scale(acc_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_acc, (0, 0))

    scaled_hairtop = pygame.transform.scale(hairtop_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_hairtop, (0, 0))
    
    scaled_eye = pygame.transform.scale(eye_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_eye, (0, 0))

    scaled_mouth = pygame.transform.scale(mouth_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_mouth, (0, 0))

    scaled_nose = pygame.transform.scale(nose_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit(scaled_nose, (0, 0))
    

#initializes the avatar images
hairbottom_image = random.choice(hairbottom_images)
clothes_image = random.choice(clothes_images)
head_image = random.choice(head_images)
acc_image = random.choice(acc_images)
hairtop_image = random.choice(hairtop_images)
eye_image = random.choice(eye_images)
mouth_image = random.choice(mouth_images)
nose_image = random.choice(nose_images)

#main game loop
running = True
clock = pygame.time.Clock()
while running:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # randomize avatar features on mouse click
            hairbottom_image = random.choice(hairbottom_images)
            clothes_image = random.choice(clothes_images)
            head_image = random.choice(head_images)
            acc_image = random.choice(acc_images)
            hairtop_image = random.choice(hairtop_images)
            eye_image = random.choice(eye_images)
            mouth_image = random.choice(mouth_images)
            nose_image = random.choice(nose_images)
            #randomize bg color on mose click
            WHITE = (pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        #save jpg on right mouse click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            pygame.image.save(window, "avatar.jpg")
            

    
    window.fill(WHITE)

    # draws avatar
    draw_avatar(hairbottom_image, clothes_image, head_image, acc_image, hairtop_image, eye_image, mouth_image, nose_image)

    # update display
    pygame.display.flip()

# quit pygame
pygame.quit()