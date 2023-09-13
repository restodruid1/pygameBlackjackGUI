import random
import pygame


def display_player_cards(who,card,location):

    if who == "player":
        card1 = pygame.draw.rect(screen, "white",location,0,5) #x,y coordinates and size of button
        pygame.draw.rect(screen, "black",location, 3,5)
        card_text = f'{card[0]}'
        card_color = 'black'
        font = pygame.font.Font(None, 36)
        surface = font.render(card_text,True,card_color)
        rect = surface.get_rect(center=card1.center)
        screen.blit(surface,rect)

    else :
        card1 = pygame.draw.rect(screen, "white",location,0,5) #x,y coordinates and size of button
        pygame.draw.rect(screen, "black",location, 3,5)
        card_text = f'{card[0]}'
        card_color = 'black'
        font = pygame.font.Font(None, 36)
        surface = font.render(card_text,True,card_color)
        rect = surface.get_rect(center=card1.center)
        screen.blit(surface,rect)



def play_again_button():
    play = pygame.draw.rect(screen, "white",[100,175,200,100],0,5) #x,y coordinates and size of button
    pygame.draw.rect(screen, "black",[100,175,200,100], 3,5)
    card_text = 'Play Again'
    card_color = 'black'
    font = pygame.font.Font(None, 36)
    surface = font.render(card_text,True,card_color)
    rect = surface.get_rect(center=play.center)
    screen.blit(surface,rect)
    return play

def play_button():
    play = pygame.draw.rect(screen, "white",[500,300,300,200],0,5) #x,y coordinates and size of button
    pygame.draw.rect(screen, "black",[500,300,300,200], 3,5)
    card_text = 'Deal Cards'
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

def draw_dd_button():
    dd = pygame.draw.circle(screen,'white',[800,650],50)
    pygame.draw.circle(screen,'black',[800,650],53,3)
    text = "Double"
    color = "black"
    font = pygame.font.Font(None, 36)
    surface = font.render(text,True,color)
    circle = surface.get_rect(center=dd.center)
    screen.blit(surface,circle)
    return dd


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


def game_interface():
    buttons_list = []
    if new_cards == True:
        buttons_list.append(play_button())
    elif new_cards == False:
        #display_player_cards(user_hand[0],user_hand[1])
        buttons_list.append(draw_hit_button())
        buttons_list.append(draw_stand_button())


    return buttons_list

def game_interface2():
    buttons_list = []
    if new_cards == True:
        buttons_list.append(play_button())
    elif new_cards == False:
        #display_player_cards(user_hand[0],user_hand[1])
        buttons_list.append(draw_hit_button())
        buttons_list.append(draw_stand_button())
        buttons_list.append(draw_dd_button())
        

    return buttons_list


def end_game_interface():
    buttons_list = []
    buttons_list.append(play_again_button())

    return buttons_list

def player_cards():
    for i in range(2):
        user_card = random.choice(game_double_deck)
        #print(user_card)
        user_hand.append(user_card)
        game_double_deck.remove(user_card)

def add_one_card(player):
    if player == True:
        user_card = random.choice(game_double_deck)
        user_hand.append(user_card)
        game_double_deck.remove(user_card)
    else:
        dealer_card = random.choice(game_double_deck)
        dealer_hand.append(dealer_card)
        game_double_deck.remove(dealer_card)

def dealer_cards():
    for i in range(2):
        dealer_card = random.choice(game_double_deck)
        #print(user_card)
        dealer_hand.append(dealer_card)
        game_double_deck.remove(dealer_card)


def get_values(player_value1, dealer_value1):
    player_value = 0
    dealer_value = 0
    player_aces = 0
    dealer_aces = 0
    for value in player_value1:    
        if value[0] in ['J','Q','K']:
            player_value += 10
        elif value[0] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            player_value += int(value[0])
        elif value[0] in ['A']:
            player_value += 11
            player_aces += 1
        if player_value > 21 and player_aces > 0:
            player_aces -= 1
            player_value -= 10
               
    for value in dealer_value1:
        if value[0] in ['J','Q','K']:
            dealer_value += 10
        elif value[0] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            dealer_value += int(value[0])
        elif value[0] in ['A']:    
            dealer_value += 11
            dealer_aces += 1
        if dealer_value > 21 and dealer_aces > 0:
            dealer_aces -= 1
            dealer_value -= 10

    return player_value, dealer_value

def display_cards_ext():
    if deal == True:
        for i in range(len(user_hand)):
            display_player_cards("player",user_hand[i] ,[(550+((i-1)*100)),300,150,150])
        for i in range(len(dealer_hand)):    
            display_player_cards("dealer",dealer_hand[i] ,[(550+((i-1)*50)),100,150,150])

    else:
        for i in range(len(user_hand)):
            display_player_cards("player",user_hand[i] ,[(550+((i-1)*100)),300,150,150])
        for i in range(len(dealer_hand)):    
            display_player_cards("dealer",dealer_hand[i] ,[(550+((i-1)*100)),100,150,150])

def display_dealer_score(total):
    card_text = f'[{total[1]}]'
    card_color = 'white'
    font = pygame.font.Font(None, 36)
    surface = font.render(card_text,True,card_color)
    rect = surface.get_rect(x=325, y=100)
    screen.blit(surface,rect)
    
    
def display_player_score(total):    
    card_text = f'[{total[0]}]'
    card_color = 'white'
    font = pygame.font.Font(None, 36)
    surface = font.render(card_text,True,card_color)
    rect = surface.get_rect(x=325, y=300)
    screen.blit(surface,rect)

def display_winner(total):
    if (total[0] == 21 and uH == 2):
        card_text = "Blackjack"
    elif ((total[0] > total[1]) and (total[0]) < 22):
        card_text = "Player Wins"
    elif ((total[0] < total[1]) and (total[1]) < 22):
        card_text = "Dealer Wins"
    elif (total[0] == total[1]):
          card_text = "Tie"
    elif total[0] > 21:
        card_text = "Player Busts"
    elif total[1] > 21:
        card_text = "Dealer Busts"
    else:
        card_text = "bug"
    
    card_color = 'white'
    font = pygame.font.Font(None, 56)
    surface = font.render(card_text,True,card_color)
    rect = surface.get_rect(x=450, y=25)
    screen.blit(surface,rect)


#THE SPLIT FEATURE FUNCTIONS
def draw_split_button():
    split = pygame.draw.circle(screen,'white',[950,650],50)
    pygame.draw.circle(screen,'black',[950,650],53,3)
    text = "Split"
    color = "black"
    font = pygame.font.Font(None, 36)
    surface = font.render(text,True,color)
    circle = surface.get_rect(center=split.center)
    screen.blit(surface,circle)
    return split

def game_interface3():
    buttons_list = []
    if new_cards == True:
        buttons_list.append(play_button())
    elif new_cards == False:
        #display_player_cards(user_hand[0],user_hand[1])
        buttons_list.append(draw_hit_button())
        buttons_list.append(draw_stand_button())
        buttons_list.append(draw_dd_button())
        buttons_list.append(draw_split_button())
        

    return buttons_list

def add_one_card_split(main):
    if main:
        user_card = random.choice(game_double_deck)
        user_hand.append(user_card)
        game_double_deck.remove(user_card)
    else:
        user_card = random.choice(game_double_deck)
        split_hand.append(user_card)
        game_double_deck.remove(user_card)

def display_cards_split():
    if deal == True:
        for i in range(len(user_hand)):
            display_player_cards("player",user_hand[i] ,[(350+((i-1)*100)),300,150,150])
        for i in range(len(split_hand)):
            display_player_cards("player",split_hand[i] ,[(850+((i-1)*100)),300,150,150])
        for i in range(len(dealer_hand)):    
            display_player_cards("dealer",dealer_hand[i] ,[(550+((i-1)*50)),100,150,150])

    else:
        for i in range(len(user_hand)):
            display_player_cards("player",user_hand[i] ,[(350+((i-1)*100)),300,150,150])
        for i in range(len(split_hand)):
            display_player_cards("player",split_hand[i] ,[(850+((i-1)*100)),300,150,150])
        for i in range(len(dealer_hand)):    
            display_player_cards("dealer",dealer_hand[i] ,[(550+((i-1)*100)),100,150,150])

def display_player_split(total1, total2):    
    card_text = f'[{total1}]'
    card_color = 'white'
    font = pygame.font.Font(None, 36)
    surface = font.render(card_text,True,card_color)
    rect = surface.get_rect(x=125, y=300)
    screen.blit(surface,rect)

    card_text = f'[{total2}]'
    card_color = 'white'
    font = pygame.font.Font(None, 36)
    surface = font.render(card_text,True,card_color)
    rect = surface.get_rect(x=900, y=250)
    screen.blit(surface,rect)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
deal = True
new_cards = True
game_double_deck = deck()*2
user_hand = []
split_hand = []
uH = len(user_hand)
dealer_hand = []
counter = 0
hit = False
stand = False
game_over = 1
pairs = False
split = False
first_hand = True

while running:   
    screen.fill("dark green")
    clock = pygame.time.Clock()
    clock.tick(60)  # limits FPS to 60
    
    if (new_cards == True and counter > 0):
        if game_over == 2:
            test_game = end_game_interface()
            display_cards_split()
            display_dealer_score(get_values(user_hand, dealer_hand))
            display_player_split(firstValue[0],secondValue[0])
        else:
            test_game = end_game_interface()
            display_cards_ext()
            display_dealer_score(get_values(user_hand, dealer_hand))
            display_player_score(get_values(user_hand, dealer_hand))
            display_winner(get_values(user_hand, dealer_hand))

    if new_cards == True and counter == 0:
        test_game = game_interface()  
    elif new_cards == False:
        if game_over == 0:
            test_game = end_game_interface()
            display_cards_ext()
            display_player_score(get_values(user_hand, dealer_hand))
            display_dealer_score(get_values(user_hand, dealer_hand))
            display_winner(get_values(user_hand, dealer_hand))
            
        elif game_over == 1:
            if hit == False:  
                if pairs == True:
                    test_game = game_interface3()
                    display_cards_ext()
                    display_player_score(get_values(user_hand, dealer_hand))
                else:
                    test_game = game_interface2()
                    display_cards_ext()
                    display_player_score(get_values(user_hand, dealer_hand))
            else:
                test_game = game_interface()
                display_cards_ext()
                display_player_score(get_values(user_hand, dealer_hand))
        elif game_over == 2:
            test_game = game_interface()
            display_cards_split()
            display_player_split(firstValue[0],secondValue[0])
        
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if new_cards == True:
                if test_game[0].collidepoint(event.pos): #If the play button was pressed
                    user_hand = []
                    dealer_hand = []
                    split_hand = []
                    game_over = 1
                    deal = True
                    pairs = False
                    hit = False
                    first_hand = True
                    
                    print("Play button works")
                    player_cards()
                    print(f'user hand:{user_hand}')
                    dealer_cards()
                    print(f'dealers hand{dealer_hand}')
                    cards = get_values(user_hand, dealer_hand)                                        
                    new_cards = False
                    if cards[0] == 21:
                        game_over = 0 
                        new_cards = True
                    if user_hand[0][0] == user_hand[1][0]:
                        pairs = True
                    uH = len(user_hand)

            elif new_cards == False: 
                if test_game[0].collidepoint(event.pos):
                    hit = True
                    pairs = False
                    if game_over == 2:
                        if first_hand == True:
                            add_one_card_split(True)
                            compare = get_values(user_hand, dealer_hand)
                            if compare[0] > 21:
                                first_hand = False
                                add_one_card_split(False)
                        else:
                            add_one_card_split(False)
                            compare = get_values(split_hand, dealer_hand)
                            if compare[0] > 21:
                                new_cards = True
                                deal = False
                                #game_over = 1
                                print(dealer_hand)
                                while compare[1] < 17:
                                    add_one_card(False)
                                    compare = get_values(user_hand, dealer_hand)
                                print(dealer_hand)
                    else:
                        print("user pressed hit")
                        add_one_card(True)
                        print(f'user hand:{user_hand}, dealers hand{dealer_hand}')
                        compare = get_values(user_hand, dealer_hand)
                        if compare[0] > 21:
                            game_over = 0
                            new_cards = True
                            deal = False
                            hit = False
                    

                elif test_game[1].collidepoint(event.pos):
                    if game_over == 2:
                        if first_hand == True:
                            first_hand = False
                            add_one_card_split(False)
                        else:
                            new_cards = True
                            compare = get_values(user_hand, dealer_hand)
                            print(dealer_hand)
                            while compare[1] < 17:
                                add_one_card(False)
                                compare = get_values(user_hand, dealer_hand)
                            print(dealer_hand)
                            deal = False
                            #game_over = 1

                    else:
                        print("user pressed stand")
                        compare = get_values(user_hand, dealer_hand)
                        while compare[1] < 17:
                            add_one_card(False) #Dealer hits here
                            compare = get_values(user_hand, dealer_hand)
                            if compare[1] > 21:
                                print("dealer loses")
                                game_over = 0
                                new_cards = True
                                
                        if (compare[0] < compare[1]) and (compare[1] < 22):
                            print("dealer wins")
                            game_over = 0
                            new_cards = True
                            
                        if (compare[0] > compare[1]) and (compare[1] < 22):
                            print("Player wins")
                            game_over = 0
                            new_cards = True
                        if compare[0] == compare[1]:
                            print("Players Tie")
                            game_over = 0
                            new_cards = True
                        #stand = True
                        deal = False
                        hit = False
                        uH = len(user_hand)
                elif test_game[2].collidepoint(event.pos):
                    print("player doubles down")
                    add_one_card(True)
                    compare = get_values(user_hand, dealer_hand)
                    if compare[0] > 21:
                        print("player loses")
                        game_over = 0
                        new_cards = True
                    else:
                        while compare[1] < 17:
                            add_one_card(False) #Dealer hits here
                            compare = get_values(user_hand, dealer_hand)
                            if compare[1] > 21:
                                print("dealer loses")
                                game_over = 0
                                new_cards = True
                        if (compare[0] < compare[1]) and (compare[1] < 22):
                            print("dealer wins")
                            game_over = 0
                            new_cards = True
                            
                        if (compare[0] > compare[1]) and (compare[1] < 22):
                            print("Player wins")
                            game_over = 0
                            new_cards = True
                        if compare[0] == compare[1]:
                            print("Players Tie")
                            game_over = 0
                            new_cards = True
                    uH = len(user_hand)
                    deal = False
                    hit = False

                elif test_game[3].collidepoint(event.pos):
                    game_over = 2
                    split = True
                    split_hand.append(user_hand.pop(1))
                    print(user_hand)
                    print(split_hand)
                    print(dealer_hand)
                    add_one_card_split(True)
                              
            counter += 1
            firstValue = get_values(user_hand, dealer_hand)
            secondValue = get_values(split_hand,dealer_hand)
            if len(game_double_deck) < 10:
                print("New deck")
                game_double_deck = deck() * 2

        
                    
          
                


    # flip() the display to put your work on screen
        
    pygame.display.flip()        
pygame.quit()


"""
Add ability to use chips?
Show text on screen for who won
give aces the ability to be 1 or 11
add card graphics
add split feature
"""