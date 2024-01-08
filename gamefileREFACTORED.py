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


def drawRectCard(screen1, colorCard, location, text=''):
    card = pygame.draw.rect(screen1, colorCard, location)
    pygame.draw.rect(screen, "black",location, 3,5)
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


def createShuffledDeck():
    card_values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    card_types = ['Club','Spades','Hearts','Diamonds']
    deck = []
    for ele in card_types:
        for value in card_values:
            deck.append((value, ele))
    random.shuffle(deck)      
    
    return deck


def player_cards(numCards):
    for i in range(numCards):
        user_card = deck.pop()
        user_hand.append(user_card)

    
def dealer_cards(numCards):
    for i in range(numCards):
        dealer_card = deck.pop()
        dealer_hand.append(dealer_card)

def get_values(cards):
    value = 0
    aces = 0
    
    for card in cards:    
        if card[0] in ['J','Q','K']:
            value += 10
        elif card[0] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            value += int(card[0])
        elif card[0] in ['A']:
            value += 11
            aces += 1
        if value > 21 and aces > 0:
            aces -= 1
            value -= 10
    
    return value


def compare_values():
    player_value = get_values(user_hand)
    dealer_value = get_values(dealer_hand)
    if (player_value > dealer_value and player_value < 22) or dealer_value > 21:
        return 0
    elif player_value < dealer_value:
        return 1
    elif player_value == dealer_value:
        return 2


if __name__ == "__main__":
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    new_game = True
    deck = createShuffledDeck() * 2     # Create two decks of shuffled cards(can scale if more decks wanted)
    color = pygame.Color('red')         # For money input box
    active = False                      # Check if money input box is clicked on
    pressed_enter = False               # Checks if user entered money
    text = ""                           # Dollar amount user entered, gets converted to integer
    user_money = 0                      # Integer amount of user entered text
    user_bet = 0                        # Keep track of players bet $
    value_error = False                 # Error for user money input
    cards_dealt = False                 # Tracks when cards are dealt
    user_hand = []                      # Stores the players current hand
    dealer_hand = []                    # Stores the dealers current hand
    played = False                      # 
    dd = False                          # Checks if player doubled down 
    able_to_split = False               # Checks if player can split
    splitting = False                   # Checks if player split
    dealer_turn = False
    hand_over = False                   # Signifies the hand is over, place bets again
    

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
                elif hand_over:
                    # Reset game to placing bets menu
                    if new_bets.collidepoint(event.pos):
                        user_hand = []
                        dealer_hand = []
                        played = False
                        cards_dealt = False
                        hand_over = False
                        dd = False
                        splitting = False
                        able_to_split = False
                        user_bet = 0
                        if len(deck) <= 10:
                            deck = createShuffledDeck() * 2
                            print("shuffling new deck")
                elif not new_game and not cards_dealt:
                    # Logic for placing bets phase
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
                            user_money -= 50
                            user_bet += 50
                        print("yooo3")
                    elif deal.collidepoint(event.pos):
                        if user_bet > 0:
                            print("deal cards")
                            cards_dealt = True
                            player_cards(2)
                            dealer_cards(2)
                            if get_values(user_hand) == 21:
                                user_money += (user_bet * 3)
                                hand_over = True
                            elif get_values(dealer_hand) == 21:
                                hand_over = True
                            elif user_hand[0][0] == user_hand[1][0]:
                                print("able_to_split")
                                able_to_split = True
                elif cards_dealt:
                    """if able_to_split:
                        # If able to split, these 4 buttons will be functional
                        if hit.collidepoint(event.pos):
                            player_cards(1)
                            played = True
                        elif stand.collidepoint(event.pos):
                            print()
                            played = True
                        elif double_down.collidepoint(event.pos):
                            dd = True
                            played = True
                            player_cards(1)
                        elif split.collidepoint(event.pos):
                            print("works")
                            splitting = True
                            played = True"""
                    if not played:
                        # If not able to split, these 3 buttons will be functional
                        if hit.collidepoint(event.pos):
                            player_cards(1)
                            played = True
                            if get_values(user_hand) > 21:
                                print("player loses")
                                hand_over = True
                        elif stand.collidepoint(event.pos):
                            while get_values(dealer_hand) < 17:
                                dealer_cards(1)
                            played = True
                            compare_values()
                            if compare_values() == 0:
                                    user_money += (user_bet * 2)
                            elif compare_values() == 2:
                                user_money += user_bet
                            hand_over = True
                        elif double_down.collidepoint(event.pos):
                            # Can't dd without enough money
                            if user_money >= user_bet:
                                user_money -= user_bet
                                user_bet += user_bet
                                dd = True
                                played = True
                                player_cards(1)
                                while get_values(dealer_hand) < 17:
                                    dealer_cards(1)
                                if compare_values() == 0:
                                    user_money += (user_bet * 2)
                                elif compare_values() == 2:
                                    user_money += user_bet 
                                hand_over = True
                    elif played:
                        # General hit and stand buttons for when player has made a move already
                        if hit.collidepoint(event.pos):
                            player_cards(1)
                            if get_values(user_hand) > 21:
                                print("player loses")
                                hand_over = True
                        elif stand.collidepoint(event.pos):
                            while get_values(dealer_hand) < 17:
                                dealer_cards(1)
                            compare_values()
                            if compare_values() == 0:
                                    user_money += (user_bet * 2)
                            elif compare_values() == 2:
                                user_money += user_bet
                            hand_over = True
                            """if get_values(user_hand) > get_values(dealer_hand) or get_values(dealer_hand) > 21:
                                print("player wins")
                                hand_over = True
                            elif get_values(user_hand) < get_values(dealer_hand):
                                print("dealer wins")
                                hand_over = True
                            elif get_values(user_hand) == get_values(dealer_hand):
                                print("Tie")
                                hand_over = True"""
                    

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
            renderText(f"Total: ${user_money}",[10,545],"white")
            chip1 = drawCircle(screen, "white", [1000,275], 50, "$1")
            chip5 = drawCircle(screen, "red", [1000,400], 50, "$5")
            chip25 = drawCircle(screen, "blue", [1000,525], 50, "$25")
            chip50 = drawCircle(screen, "grey", [1000,650], 50, "$50")
            drawCircle(screen, "white", [615,545], 60)
            drawCircle(screen, "green", [615,545], 50, f'${user_bet}')
            deal = drawCircle(screen, "white", [415,545], 60, "DEAL")

        elif hand_over:
            renderText(f"Total: ${user_money}",[10,545],"white")
            
            # Displays each player card 
            for i in range(len(user_hand)):
                drawRectCard(screen, "white",[400+(i * 100), 300,150,150], f"{user_hand[i][0]}")

            for i in range(len(dealer_hand)):
                drawRectCard(screen, "white",[400+(i * 100), 100,150,150], f"{dealer_hand[i][0]}")
            
            drawCircle(screen, "white", [615,545], 60)
            drawCircle(screen, "green", [615,545], 50, f'${user_bet}')
            new_bets = drawCircle(screen, "white", [915,545], 60, "New Bets")
            if compare_values() == 0:
                renderText(f"Player Wins",[600,50],"white")
            elif compare_values() == 1:
                renderText(f"Dealer Wins",[600,50],"white")    
            else: 
                renderText(f"Tie",[600,50],"white")
        
        elif cards_dealt and played:
            # Cards have been dealt and player has made at least one move
            if dd:
                renderText(f"Total: ${user_money}",[10,545],"white")
                # Displays each player card 
                for i in range(len(user_hand)):
                    drawRectCard(screen, "white",[400+(i * 100), 300,150,150], f"{user_hand[i][0]}")

                for i in range(len(dealer_hand)):
                    drawRectCard(screen, "white",[400+(i * 100), 100,150,150], f"{dealer_hand[i][0]}")
                
                drawCircle(screen, "white", [615,545], 60)
                drawCircle(screen, "green", [615,545], 50, f'${user_bet}')
            elif splitting:
                print("")              
            else:
                renderText(f"Total: ${user_money}",[10,545],"white")
                # Displays each player card 
                for i in range(len(user_hand)):
                    drawRectCard(screen, "white",[400+(i * 100), 300,150,150], f"{user_hand[i][0]}")

                for i in range(len(dealer_hand)-1):
                    drawRectCard(screen, "white",[400+(i * 100), 100,150,150], f"{dealer_hand[i][0]}")
                    drawRectCard(screen, "white",[500,100,150,150])
                
                drawCircle(screen, "white", [615,545], 60)
                drawCircle(screen, "green", [615,545], 50, f'${user_bet}')
                hit = drawCircle(screen, "white", [400,665], 50, "Hit")
                stand = drawCircle(screen, "white", [515,665], 50, "Stand")
                
        elif cards_dealt:
            # First cards have been dealt but no player move has been made
            renderText(f"Total: ${user_money}",[10,545],"white")
            # Displays each player card 
            for i in range(len(user_hand)):
                drawRectCard(screen, "white",[400+(i * 100), 300,150,150], f"{user_hand[i][0]}")
            # Display dealer card with one hidden
            drawRectCard(screen, "white",[400,100,150,150], f"{dealer_hand[0][0]}")
            drawRectCard(screen, "white",[500,100,150,150])

            drawCircle(screen, "white", [615,545], 60)
            drawCircle(screen, "green", [615,545], 50, f'${user_bet}')
            hit = drawCircle(screen, "white", [400,665], 50, "Hit")
            stand = drawCircle(screen, "white", [515,665], 50, "Stand")
            double_down = drawCircle(screen, "white", [630,665], 50, "DD")
            # Split feature shows up when player has two cards of same value          
            if able_to_split:
                #print(user_hand[0][0], user_hand[1][0])
                split = drawCircle(screen, "white", [745,665], 50, "Split")
        
        # flip() the display to put your work on screen
        pygame.display.flip()
        
        clock.tick(60)  # limits FPS to 60

    pygame.quit()