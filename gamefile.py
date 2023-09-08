import random
import pygame


def draw_card():
    card = pygame.draw.rect(screen, "white",[450,200,100,100],0,5) #x,y coordinates and size of button
    pygame.draw.rect(screen, "black",[450,200,100,100], 3,5)
    card_text = 'Card'
    card_color = 'black'
    font = pygame.font.Font(None, 36)
    surface = font.render(card_text,True,card_color)
    rect = surface.get_rect(center=card.center)
    screen.blit(surface,rect)

def play_button():
    play = pygame.draw.rect(screen, "white",[650,300,100,100],0,5) #x,y coordinates and size of button
    pygame.draw.rect(screen, "black",[650,300,100,100], 3,5)
    card_text = 'PLAY'
    card_color = 'black'
    font = pygame.font.Font(None, 36)
    surface = font.render(card_text,True,card_color)
    rect = surface.get_rect(center=play.center)
    screen.blit(surface,rect)
    return play
    

def draw_hit_button():
    hit = pygame.draw.circle(screen,'white',[500,650],50)
    pygame.draw.circle(screen,'black',[500,650],53,3)
    text = "Hit"
    color = "black"
    font = pygame.font.Font(None, 36)
    surface = font.render(text,True,color)
    circle = surface.get_rect(center=hit.center)
    screen.blit(surface,circle)
    return hit

def draw_stand_button():
    stand = pygame.draw.circle(screen,'white',[650,650],50)
    pygame.draw.circle(screen,'black',[650,650],53,3)
    text = "Stand"
    color = "black"
    font = pygame.font.Font(None, 36)
    surface = font.render(text,True,color)
    circle = surface.get_rect(center=stand.center)
    screen.blit(surface,circle)
    return stand

def deck():
    card_values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    card_types = ['Club','Spades','Hearts','Diamonds']
    deck_list = []
    for ele in card_types:
        for value in card_values:
            deck_list.append((value, ele))
            
    return deck_list


"""
Each button click, the necessary buttons will appear based on the current state of the game. The card values and money will differ"""

def game(first_game):
    buttons_list = []
    if first_game == True:
        buttons_list.append(play_button())
        #buttons_list.append(draw_card())
        
    elif first_game != True:
        buttons_list.append(draw_card())
        buttons_list.append(draw_hit_button())
        buttons_list.append(draw_stand_button())

    return buttons_list

"""screen = pygame.display.set_mode((1280, 720))
screen.fill("dark green")
clock = pygame.time.Clock()
clock.tick(60)  # limits FPS to 60"""
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
new_game = True
game_double_deck = deck()*2
user_hand = []
dealer_hand = []

while running:   
    screen.fill("dark green")
    clock = pygame.time.Clock()
    clock.tick(60)  # limits FPS to 60
    
    
    test_game = game(new_game)

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if new_game == True:
                if test_game[0].collidepoint(event.pos): #If the play button was pressed
                    new_game = False
                    
                    for i in range(2):
                        user_card = random.choice(game_double_deck)
                        print(user_card)
                        user_hand.append(user_card)
                        game_double_deck.remove(user_card)
                        dealer_card = random.choice(game_double_deck)
                        print(dealer_card)
                        dealer_hand.append(dealer_card)
                        game_double_deck.remove(dealer_card)
                    
            elif new_game == False:
                print("WIP")
                
                


    # flip() the display to put your work on screen
        
    pygame.display.flip()        
pygame.quit()