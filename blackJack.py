import random

def setCard(x):
    getCards = {
    1: {"cardValue": 1, "cardSymbol": 'Spade', "cardDescription": 'Ace'},
    2: {"cardValue": 2, "cardSymbol": 'Spade', "cardDescription": '2' },
    3: {"cardValue": 3, "cardSymbol": 'Spade', "cardDescription": '3'},
    4: {"cardValue": 4, "cardSymbol": 'Spade', "cardDescription": '4'},
    5: {"cardValue": 5, "cardSymbol": 'Spade', "cardDescription": '5'},
    6: {"cardValue": 6, "cardSymbol": 'Spade', "cardDescription": '6'},
    7: {"cardValue": 7, "cardSymbol": 'Spade', "cardDescription": '7'},
    8: {"cardValue": 8, "cardSymbol": 'Spade', "cardDescription": '8'},
    9: {"cardValue": 9, "cardSymbol": 'Spade', "cardDescription": '9'},
    10: {"cardValue": 10, "cardSymbol": 'Spade', "cardDescription": '10'},
    11: {"cardValue": 10, "cardSymbol": 'Spade', "cardDescription": 'Jack'},
    12: {"cardValue": 10, "cardSymbol": 'Spade', "cardDescription": 'Queen'},
    13: {"cardValue": 10, "cardSymbol": 'Spade', "cardDescription": 'King'},
    14: {"cardValue": 1, "cardSymbol": 'Heart', "cardDescription": 'Ace' },
    15: {"cardValue": 2, "cardSymbol": 'Heart', "cardDescription": '2'},
    16: {"cardValue": 3, "cardSymbol": 'Heart', "cardDescription": '3'},
    17: {"cardValue": 4, "cardSymbol": 'Heart', "cardDescription": '4'},
    18: {"cardValue": 5, "cardSymbol": 'Heart', "cardDescription": '5'},
    19: {"cardValue": 6, "cardSymbol": 'Heart', "cardDescription": '6'},
    20: {"cardValue": 7, "cardSymbol": 'Heart', "cardDescription": '7'},
    21: {"cardValue": 8, "cardSymbol": 'Heart', "cardDescription": '8'},
    22: {"cardValue": 9, "cardSymbol": 'Heart', "cardDescription": '9'},
    23: {"cardValue": 10, "cardSymbol": 'Heart', "cardDescription": '10'},
    24: {"cardValue": 10, "cardSymbol": 'Heart', "cardDescription": 'Jack'},
    25: {"cardValue": 10, "cardSymbol": 'Heart', "cardDescription": 'Queen'},
    26: {"cardValue": 10, "cardSymbol": 'Heart', "cardDescription": 'King'},
    27: {"cardValue": 1, "cardSymbol": 'Club', "cardDescription": 'Ace'},
    28: {"cardValue": 2, "cardSymbol": 'Club', "cardDescription": '2'},
    29: {"cardValue": 3, "cardSymbol": 'Club', "cardDescription": '3'},
    30: {"cardValue": 4, "cardSymbol": 'Club', "cardDescription": '4'},
    31: {"cardValue": 5, "cardSymbol": 'Club', "cardDescription": '5'},
    32: {"cardValue": 6, "cardSymbol": 'Club', "cardDescription": '6'},
    33: {"cardValue": 7, "cardSymbol": 'Club', "cardDescription": '7'},
    34: {"cardValue": 8, "cardSymbol": 'Club', "cardDescription": '8'},
    35: {"cardValue": 9, "cardSymbol": 'Club', "cardDescription": '9'},
    36: {"cardValue": 10, "cardSymbol": 'Club', "cardDescription": '10'},
    37: {"cardValue": 10, "cardSymbol": 'Club', "cardDescription": 'Jack'},
    38: {"cardValue": 10, "cardSymbol": 'Club', "cardDescription": 'Queen'},
    39: {"cardValue": 10, "cardSymbol": 'Club', "cardDescription": 'King'},
    40: {"cardValue": 1, "cardSymbol": 'Diamond', "cardDescription": 'Ace'},
    41: {"cardValue": 2, "cardSymbol": 'Diamond', "cardDescription": '2'},
    42: {"cardValue": 3, "cardSymbol": 'Diamond', "cardDescription": '3'},
    43: {"cardValue": 4, "cardSymbol": 'Diamond', "cardDescription": '4'},
    44: {"cardValue": 5, "cardSymbol": 'Diamond', "cardDescription": '5'},
    45: {"cardValue": 6, "cardSymbol": 'Diamond', "cardDescription": '6'},
    46: {"cardValue": 7, "cardSymbol": 'Diamond', "cardDescription": '7'},
    47: {"cardValue": 8, "cardSymbol": 'Diamond', "cardDescription": '8'},
    48: {"cardValue": 9, "cardSymbol": 'Diamond', "cardDescription": '9'},
    49: {"cardValue": 10, "cardSymbol": 'Diamond', "cardDescription": '10'},
    50: {"cardValue": 10, "cardSymbol": 'Diamond', "cardDescription": 'Jack'},
    51: {"cardValue": 10, "cardSymbol": 'Diamond', "cardDescription": 'Queen'},
    52: {"cardValue": 10, "cardSymbol": 'Diamond', "cardDescription": 'King'}
    }
    return getCards[x]

def displayCards(playerHand,playerScore):
    print('========================== Displaying Cards ==========================')
    print('Current Score:',playerScore)
    a = 1
    for x in playerHand: 
        print('Card ',a,':',playerHand[x]['cardDescription'],' ',playerHand[x]['cardValue'])
        a += 1

def drawCard():
    getNum = random.randrange(1,53)
    rand = {}
    rand[getNum] = setCard(getNum)
    return rand
        
def playAgainPrompt():
    replyPlayer = input('Play again? Yes or No\n').lower()
    if replyPlayer == 'yes':
        main()
    else:
        exit()

def nonAcedScore(allHands):
    score = 0
    for x in allHands:
        score += allHands[x]['cardValue']
    return score

def getAcedScore(allHands):
    checkOnce = True
    score = 0
    
    for x in allHands:
        if checkOnce == True:
            if (x == 1) or (x == 14) or (x == 27) or (x == 40):
                score += 11
                checkOnce = False
            else:
                score += allHands[x]['cardValue']
        else:
            score += allHands[x]['cardValue']
    return score

def dealAcedScoreChecks(playerScore,dealerScore):
    X = 21
    if (playerScore == X and dealerScore == X):
        print('Draw! Player got ',playerScore,' while the Dealer got ',dealerScore)
        playAgainPrompt()
    elif playerScore == X:
        print('Player Win with ', playerScore,' Blackjack!')
        playAgainPrompt()
    elif dealerScore == X:
        print('Dealer Win with ', dealerScore,' Blackjack!')
        playAgainPrompt()

def drawingPhaseLimiter(currentScore,idCounter,otherScore): #1 is dealer over 21 #2 is player over 21
    X = 21
    if currentScore > X and idCounter == 1:
        print('Player Win with ', otherScore,' against Dealer\'s card of ',currentScore,': over 21')
        playAgainPrompt()
    if currentScore > X and idCounter == 2:
        print('Dealer Win with ', otherScore,' against Player\'s card of ',currentScore,': over 21')
        playAgainPrompt()

def finalScoreCheck(playerScore, dealerScore):
    if playerScore == dealerScore:
        print('Draw! Both players got the same score of Player\'s ', playerScore,' and Dealer\'s ', dealerScore)
        playAgainPrompt()
    elif playerScore > dealerScore:
        print('Player Win with ', playerScore,' against Dealer\'s ',dealerScore)
        playAgainPrompt()
    elif playerScore < dealerScore:
        print('Dealer Win with ', dealerScore,' against Player\'s ',playerScore)
        playAgainPrompt()

def main():
    keepDrawing = True
    dealerHand = {}
    playerHand = {}
    count_startDraw = 0
    
    while count_startDraw != 2:
        playerHand.update(drawCard())
        dealerHand.update(drawCard())
        count_startDraw += 1
    if len(playerHand.keys()) == 1:
        playerHand.update(drawCard())
    if len(dealerHand.keys()) == 1:
        dealerHand.update(drawCard())
        
    playerAcedScore = getAcedScore(playerHand)
    dealerAcedScore = getAcedScore(dealerHand)

    dealAcedScoreChecks(playerAcedScore , dealerAcedScore)
    displayCards(playerHand,playerAcedScore)
    
    playerNonAcedScore = 0
    
    print('========================== DRAW PHASE ==========================')
    
    while keepDrawing:
        keepDrawing = input('Draw a Card? Yes or No\n').lower()
        if keepDrawing == 'yes':
            keepDrawing = True
            playerHand.update(drawCard())
            playerAcedScore = getAcedScore(playerHand)
            dealAcedScoreChecks(playerAcedScore,dealerAcedScore)
            if playerAcedScore > 21:
                playerNonAcedScore = nonAcedScore(playerHand)
                displayCards(playerHand,playerNonAcedScore)
                print(playerNonAcedScore,' ', playerAcedScore,' non aced')
                drawingPhaseLimiter(playerNonAcedScore,2,dealerAcedScore)
                dealAcedScoreChecks(playerNonAcedScore,dealerAcedScore) ### if player got 21 stop
            else:
                displayCards(playerHand,playerAcedScore)
                drawingPhaseLimiter(playerAcedScore,2,dealerAcedScore)
            if playerAcedScore == 21:
                break
        elif keepDrawing == '' or keepDrawing == 'no':
            keepDrawing = False
            break
    
    if playerNonAcedScore > 0:
        print('Current card value is: ', playerNonAcedScore)
        displayCards(playerHand,playerNonAcedScore)
    elif playerAcedScore < 21:
        print('Current card value is: ', playerAcedScore)
        displayCards(playerHand,playerAcedScore)
    
    dealerNonAced = 0
    keepDrawing = True
    
    while keepDrawing:
        if dealerAcedScore < 16:
            dealerHand.update(drawCard())
            dealerAcedScore = nonAcedScore(dealerHand)
            print(dealerAcedScore,' drawn')
            if dealerAcedScore > 21:
                dealerNonAced = nonAcedScore(dealerHand)
                drawingPhaseLimiter(dealerNonAced,1,playerAcedScore if playerAcedScore < 21 else playerNonAcedScore)
                dealAcedScoreChecks(playerAcedScore if playerAcedScore < 21 else playerNonAcedScore,dealerNonAced)
                print(dealerNonAced,' drawn')
                if dealerNonAced > 16:
                    break
                elif dealerNonAced < 16:
                    dealerHand.update(drawCard())
                    dealerNonAced = nonAcedScore(dealerHand)
                else:
                    break
        else:
            break
            
    print('========================== END PHASE ==========================')
    
    dealAcedScoreChecks(playerAcedScore if playerAcedScore < 21 else playerNonAcedScore,
                        dealerAcedScore if dealerAcedScore < 21 else dealerNonAced)
    
    finalScoreCheck(playerAcedScore if playerAcedScore < 21 else playerNonAcedScore,
                    dealerAcedScore if dealerAcedScore < 21 else dealerNonAced)


main()
