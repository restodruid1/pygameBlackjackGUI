import pygame


def money_Entry_Box(new_color, new_text=' '):
    textbox = pygame.draw.rect(screen, new_color, [100,100,140,50], 2)
    color = 'black'
    text = f"{new_text}"
    font = pygame.font.Font(None, 50)
    txt_surface = font.render(text, True, color)
    #box = txt_surface.get_rect(center=textbox.center)
    screen.blit(txt_surface, (textbox.x+5, textbox.y+5))   
    return textbox

def drawRectCard(screen1, colorCard, location):
    card = pygame.draw.rect(screen1, colorCard, location)
    card_text = 'Play Again'
    card_color = 'black'
    font = pygame.font.Font(None, 36)
    surface = font.render(card_text,True,card_color)
    rect = surface.get_rect(center=card.center)
    screen.blit(surface,rect)
    return card

def drawCircle(screen1, colorCircle, location, size):
    circle = pygame.draw.circle(screen1,colorCircle,location,size)
    font = pygame.font.Font(None, 36)
    text = "Deal"
    color = "black"
    surface = font.render(text,True,color)
    circle = surface.get_rect(center=circle.center)
    screen.blit(surface,circle)
    return circle

def createNewGameMenu():
    pass

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
buttons = []        #Stores game buttons for event handling
new_game_buttons = []  #Stores game buttons for event handling but only for new game
new_game = True
color = pygame.Color('red')
active = False
text = ''

while running:
    # poll for events
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if new_game == True:
                if money_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = 'dodgerblue2' if active else "red"
                #if new_game_buttons[0].collidepoint(event.pos):
                if deal_button.collidepoint(event.pos):
                        print("yobb")
                        print(buttons)
                        new_game = False
            else:
                #A button like "Hit" has been pressed. Implement dealing logic
                print(buttons)
                if buttons[0].collidepoint(event.pos):
                    print("yo")
                elif buttons[1].collidepoint(event.pos):
                    print("yooo")
        
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

                
        
                
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark green")
    
    # RENDER YOUR GAME HERE
  
    if new_game == True:
        #new_game_buttons.append(drawCircle(screen, "white", [500,500], 50))
        deal_button = drawCircle(screen, "white", [500,500], 50)
        money_box = money_Entry_Box(color, text)
    else:
        buttons.append(drawRectCard(screen, "white",[100,100,100,100]))
        buttons.append(drawRectCard(screen, "white",[500,100,100,300]))

    # flip() the display to put your work on screen
    pygame.display.flip()
    
    clock.tick(60)  # limits FPS to 60

pygame.quit()