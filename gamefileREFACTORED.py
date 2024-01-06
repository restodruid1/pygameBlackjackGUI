import pygame
import random



def renderText(user_text, location, color_text):
    font = pygame.font.Font(None, 50)
    text = font.render(user_text, True, color_text)
    screen.blit(text, location)


def moneyEntryBox(new_color, new_text=' '):
    textbox = pygame.draw.rect(screen, new_color, [525,300,200,50], 2)
    color = 'black'
    text = f"${new_text}"
    font = pygame.font.Font(None, 50)
    surface = font.render(text, True, color)
    screen.blit(surface, (textbox.x+5, textbox.y+5))   
    
    return textbox


def drawRectCard(screen1, colorCard, location, text):
    card = pygame.draw.rect(screen1, colorCard, location)
    card_text = text
    card_color = 'black'
    font = pygame.font.Font(None, 36)
    surface = font.render(card_text,True,card_color)
    rect = surface.get_rect(center=card.center)
    screen.blit(surface,rect)
    
    return card


def drawCircle(screen1, colorCircle, location, size, type=''):
    circle = pygame.draw.circle(screen1,colorCircle,location,size)
    pygame.draw.circle(screen1,'black',location,size+3,3) # Draw black border for the button
    font = pygame.font.Font(None, 36)
    text = type
    color = "black"
    surface = font.render(text,True,color)
    circle = surface.get_rect(center=circle.center)
    screen.blit(surface,circle)
    
    return circle


def createDeck():
    card_values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    card_types = ['Club','Spades','Hearts','Diamonds']
    deck = []
    for ele in card_types:
        for value in card_values:
            deck.append((value, ele))
            
    return deck


def player_cards():
    for i in range(2):
        user_card = random.choice(deck)
        #print(user_card)
        user_hand.append(user_card)
        deck.remove(user_card)

    
def dealer_cards():
    for i in range(2):
        dealer_card = random.choice(deck)
        #print(user_card)
        dealer_hand.append(dealer_card)
        deck.remove(dealer_card)


if __name__ == "__main__":
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    new_game = True
    deck = createDeck() * 2         # Create two decks of cards(can scale if more decks wanted)
    color = pygame.Color('red')     # For money input box
    active = False                  # Check if money input box is clicked on
    pressed_enter = False           # Checks if user entered money
    text = ""                       # Dollar amount user entered, gets converted to integer
    user_money = 0                  # Integer amount of user entered text
    user_bet = 0                    # Keep track of players bet $
    value_error = False             # Error for user money input
    cards_dealt = False             # Tracks when cards are dealt
    user_hand = []                  # Stores the players current hand
    dealer_hand = []                # Stores the dealers current hand


    while running:
        # poll for events
        
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Logic that occurs when user input is recieved
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if new_game == True:
                    if money_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = "blue" if active else "red"
                    
                    # Prevents user from playing game without inputting money
                    if deal_button.collidepoint(event.pos) and user_money < 1:
                            print("Need money")
                    elif deal_button.collidepoint(event.pos):
                        print('works')
                        new_game = False
                else:
                    if chip1.collidepoint(event.pos):
                        if user_money >= 1:
                            user_money -= 1
                            user_bet += 1
                        print("yo9")
                    elif chip5.collidepoint(event.pos):
                        if user_money >= 5:
                            user_money -= 5
                            user_bet += 5
                        print("yo")
                    elif chip25.collidepoint(event.pos):
                        if user_money >= 25:
                            user_money -= 25
                            user_bet += 25
                        print("yooo")
                    elif chip50.collidepoint(event.pos):
                        if user_money >= 50:
                            user_money -= 25
                            user_bet += 50
                        print("yooo3")
                    elif deal.collidepoint(event.pos):
                        if user_bet > 0:
                            print("deal cards")
                            cards_dealt = True
                            player_cards()
                            dealer_cards()
            
            # Handling the keyboard input for the money input box
            elif event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        temp_text = text
                        # Ensures user enters correct money to play
                        try:
                            user_money = int(temp_text)
                            pressed_enter = True
                        except ValueError:
                            # Renders warning message to screen
                            value_error = True  
                        print(temp_text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        # Resets value error when user starts entering money again
                        value_error = False
                        text += event.unicode

                    
            
                    
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("dark green")
        
        # RENDER YOUR GAME HERE
        # New game menu buttons and money
        if new_game:
            renderText("BLACKJACK!!!", (475, 50), "white" )
            renderText("Input your money and press 'Play'", (325, 100), "white" )
            deal_button = drawCircle(screen, "white", [615,500], 75, "Play")
            money_box = moneyEntryBox(color, text)
            
            # When user presses enter on their keyboard
            if value_error:
                renderText("Invalid, must enter a number", (425, 200), "red")
            
            elif pressed_enter:
                renderText(f"You entered: ${temp_text}", (500, 350), "white")
        
        # Render game after the main menu phase is over        
        elif not cards_dealt:
            # Player betting phase, before cards are dealt
            renderText(f"Player money ${user_money}",[10,10],"white")
            chip1 = drawCircle(screen, "white", [1000,275], 50, "$1")
            chip5 = drawCircle(screen, "red", [1000,400], 50, "$5")
            chip25 = drawCircle(screen, "blue", [1000,525], 50, "$25")
            chip50 = drawCircle(screen, "grey", [1000,650], 50, "$50")
            drawCircle(screen, "white", [615,500], 75)
            drawCircle(screen, "green", [615,500], 50, f'${user_bet}')
            deal = drawCircle(screen, "white", [415,500], 75, "DEAL")

        elif cards_dealt:
            # Displays each player card 
            for i in range(len(user_hand)):
                drawRectCard(screen, "white",[400+(i * 100), 400,100,100], f"{user_hand[i][0]}")

            for i in range(len(dealer_hand)-1):
                drawRectCard(screen, "white",[400+(i * 100), 100,100,100], f"{dealer_hand[i][0]}")
            
            hit = drawCircle(screen, "white", [400,600], 50, "Hit")
            stand = drawCircle(screen, "white", [515,600], 50, "Stand")
            double_down = drawCircle(screen, "white", [630,600], 50, "DD")
            split = drawCircle(screen, "white", [745,600], 50, "Split")

        # flip() the display to put your work on screen
        pygame.display.flip()
        
        clock.tick(60)  # limits FPS to 60

    pygame.quit()