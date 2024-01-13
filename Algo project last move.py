def playerStoneInput(playerNo):
    player = input(f'Enter a capital letter to represent player {playerNo} (except O):')
    notValid = True
    if player != 'O' and isinstance(player,str):
        notValid = False
    while notValid:
        print('Error occured')
        player = input(f'Enter a capital letter to represent player {playerNo} (except O):')
        if player != 'O' and isinstance(player,str):
            notValid = False
    player = player.upper()
    return player

def listGenerator(rowcolNumber,player1,player2):
    match rowcolNumber:
        case 3:
            playingList = []
            for i in range(3):
                playingList.append([' ']*3)

            playingList[0][1] = player2
            playingList[2][1] = player1
            
        case 5:
            playingList = []
            for i in range(5):
                playingList.append([' ']*5)

            playingList[0][2] = player2
            playingList[4][2] = player1

        case 7:
            playingList = []
            for i in range(7):
                playingList.append([' ']*7)

            playingList[0][3] = player2
            playingList[6][3] = player1
    return playingList

def visualMatrixGen(baseList):
    rowcolNumber = len(baseList)
    match rowcolNumber:
        case 3:
            print(f'{'   A':3} {'   B':3} {'   C':3}')
            print(f'{'  -------------':3}')
            print('1', f'|',baseList[0][0],'|',baseList[0][1],'|',baseList[0][2],'|','1')
            print(f'{'  -------------':3}')
            print('2', f'|',baseList[1][0],'|',baseList[1][1],'|',baseList[1][2],'|','2')
            print(f'{'  -------------':3}')
            print('3', f'|',baseList[2][0],'|',baseList[2][1],'|',baseList[2][2],'|','3')
            print(f'{'  -------------':3}')
            print(f'{'   A':3} {'   B':3} {'   C':3}')
        case 5:
            print(f'{'    A':4} {'  B':4} {' C':4} {'D':3} {'E':3}')
            print(f'{'  ---------------------':3}')
            print('1', f'|',baseList[0][0],'|',baseList[0][1],'|',baseList[0][2],'|',baseList[0][3],'|',baseList[0][4],'|','1')
            print(f'{'  ---------------------':3}')
            print('2', f'|',baseList[1][0],'|',baseList[1][1],'|',baseList[1][2],'|',baseList[1][3],'|',baseList[1][4],'|','2')
            print(f'{'  ---------------------':3}')
            print('3', f'|',baseList[2][0],'|',baseList[2][1],'|',baseList[2][2],'|',baseList[2][3],'|',baseList[2][4],'|','3')
            print(f'{'  ---------------------':3}')
            print('4', f'|',baseList[3][0],'|',baseList[3][1],'|',baseList[3][2],'|',baseList[3][3],'|',baseList[3][4],'|','4')
            print(f'{'  ---------------------':3}')
            print('5', f'|',baseList[4][0],'|',baseList[4][1],'|',baseList[4][2],'|',baseList[4][3],'|',baseList[4][4],'|','5')
            print(f'{'  ---------------------':3}')
            print(f'{'    A':4} {'  B':4} {' C':4} {'D':3} {'E':3}')
        case _:
            print(f'{'    A':3} {'  B':4} {' C':4} {'D':3} {'E':3} {'F':3} {'G'}')
            print(f'{'  ----------------------------':3}')
            print('1', f'|',baseList[0][0],'|',baseList[0][1],'|',baseList[0][2],'|',baseList[0][3],'|',baseList[0][4],'|',baseList[0][5],'|',baseList[0][6],'|','1')
            print(f'{'  ----------------------------':3}')
            print('2', f'|',baseList[1][0],'|',baseList[1][1],'|',baseList[1][2],'|',baseList[1][3],'|',baseList[1][4],'|',baseList[1][5],'|',baseList[1][6],'|','2')
            print(f'{'  ----------------------------':3}')
            print('3', f'|',baseList[2][0],'|',baseList[2][1],'|',baseList[2][2],'|',baseList[2][3],'|',baseList[2][4],'|',baseList[2][5],'|',baseList[2][6],'|','3')
            print(f'{'  ----------------------------':3}')
            print('4', f'|',baseList[3][0],'|',baseList[3][1],'|',baseList[3][2],'|',baseList[3][3],'|',baseList[3][4],'|',baseList[3][5],'|',baseList[3][6],'|','4')
            print(f'{'  ----------------------------':3}')
            print('5', f'|',baseList[4][0],'|',baseList[4][1],'|',baseList[4][2],'|',baseList[4][3],'|',baseList[4][4],'|',baseList[4][5],'|',baseList[4][6],'|','5')
            print(f'{'  ----------------------------':3}')
            print('6', f'|',baseList[5][0],'|',baseList[5][1],'|',baseList[5][2],'|',baseList[5][3],'|',baseList[5][4],'|',baseList[5][5],'|',baseList[5][6],'|','6')
            print(f'{'  ----------------------------':3}')
            print('7', f'|',baseList[6][0],'|',baseList[6][1],'|',baseList[6][2],'|',baseList[6][3],'|',baseList[6][4],'|',baseList[6][5],'|',baseList[6][6],'|','7')
            print(f'{'  ----------------------------':3}')
            print(f'{'    A':3} {'  B':4} {' C':4} {'D':3} {'E':3} {'F':3} {'G'}')

def bigStoneMove(player,playingList):  #Input is not being validated again in try except blocks update needed

    
    rowcolNumber = len(playingList)
    playerRowIndex = 0
    letterFound = False
    for innerList in playingList:
        playerColumnIndex = -1
        for n in innerList:
            playerColumnIndex += 1
            if n == player:
                letterFound = True
                break
        if letterFound:
            break
                
        playerRowIndex +=1

    moveDirection = input(f'Player {player}, please enter the direction you want to move your own big stone\
        (N, S, E, W, NE, NW, SE, SW):')
    while moveDirection not in ['N','S','E','W','NE','NW','SE','SW']:
        print('error')
        moveDirection = input('Please enter a valid value (N, S, E, W, NE, NW, SE, SW)')
        
    match moveDirection:
        case 'N':
            incorrect_entry = True

            if (playerRowIndex-1 > rowcolNumber-1 or playerColumnIndex > rowcolNumber-1 or
                playerRowIndex-1 < 0 or playerColumnIndex < 0 ): #Getting out of the table
                incorrect_entry = True
                print('Out of boundary error')
            elif playingList[playerRowIndex-1][playerColumnIndex] != ' ': #Checks if empty or not
                print('There is another entity on that position')
                incorrect_entry = True

            else:
                incorrect_entry = False
                
            if incorrect_entry == True:
                bigStoneMove(player,playingList)
            else:
                playingList[playerRowIndex][playerColumnIndex] = ' '
                playerRowIndex -= 1
                playingList[playerRowIndex][playerColumnIndex] = f'{player}'
                #incorrect_entry = False
                    
        case 'S':
            incorrect_entry = True
            if playingList[playerRowIndex+1][playerColumnIndex] != ' ':
                print('There is another entity on that position')
                incorrect_entry = True
                
            elif (playerRowIndex+1 > rowcolNumber-1 or playerColumnIndex > rowcolNumber-1 or
                playerRowIndex+1 < 0 or playerColumnIndex < 0 ):
                incorrect_entry = True
                print('Out of boundary error')
                
            else:
                incorrect_entry = False
                
            if incorrect_entry == True:
                bigStoneMove(player,playingList)
            else:
                playingList[playerRowIndex][playerColumnIndex] = ' '
                playerRowIndex += 1
                playingList[playerRowIndex][playerColumnIndex] = f'{player}'
                incorrect_entry = False
        
        case 'E':
            incorrect_entry = True
            if playingList[playerRowIndex][playerColumnIndex+1] != ' ':
                print('There is another entity on that position')
                incorrect_entry = True
                
            elif (playerRowIndex > rowcolNumber-1 or playerColumnIndex+1 > rowcolNumber-1 or
                playerRowIndex < 0 or playerColumnIndex+1 < 0 ):
                incorrect_entry = True
                print('Out of boundary error')
                
            else:
                incorrect_entry = False
                
            if incorrect_entry == True:
                bigStoneMove(player,playingList)
            else:
                playingList[playerRowIndex][playerColumnIndex] = ' '
                playerColumnIndex += 1
                playingList[playerRowIndex][playerColumnIndex] = f'{player}'
                incorrect_entry = False

        case 'W':
            incorrect_entry = True
            if playingList[playerRowIndex][playerColumnIndex-1] != ' ':
                print('There is another entity on that position')
                incorrect_entry = True
                
            elif (playerRowIndex > rowcolNumber-1 or playerColumnIndex-1 > rowcolNumber-1 or
                playerRowIndex < 0 or playerColumnIndex-1 < 0 ):
                incorrect_entry = True
                print('Out of boundary error')
                
            else:
                incorrect_entry = False
                
            if incorrect_entry == True:
                bigStoneMove(player,playingList)
            else:
                playingList[playerRowIndex][playerColumnIndex] = ' '
                playerColumnIndex -= 1
                playingList[playerRowIndex][playerColumnIndex] = f'{player}'
                incorrect_entry = False

        case 'NE':
            incorrect_entry = True

            if (playerRowIndex-1 > rowcolNumber-1 or playerColumnIndex+1 > rowcolNumber-1 or
                playerRowIndex-1 < 0 or playerColumnIndex+1 < 0 ):
                incorrect_entry = True
                print('Out of boundary error')
            elif playingList[playerRowIndex-1][playerColumnIndex+1] != ' ':
                print('There is another entity on that position')
                incorrect_entry = True

            else:
                incorrect_entry = False
                
            if incorrect_entry == True:
                bigStoneMove(player,playingList)
            else:
                playingList[playerRowIndex][playerColumnIndex] = ' '
                playerRowIndex -= 1
                playerColumnIndex += 1
                playingList[playerRowIndex][playerColumnIndex] = f'{player}'
                incorrect_entry = False
            
        case 'NW':
            incorrect_entry = True

            if (playerRowIndex-1 > rowcolNumber-1 or playerColumnIndex-1 > rowcolNumber-1 or
                playerRowIndex-1 < 0 or playerColumnIndex-1 < 0 ):
                incorrect_entry = True
                print('Out of boundary error')
            elif playingList[playerRowIndex-1][playerColumnIndex-1] != ' ':
                print('There is another entity on that position')
                incorrect_entry = True
                
                
            else:
                incorrect_entry = False
                
            if incorrect_entry == True:
                bigStoneMove(player,playingList)
            else:
                playingList[playerRowIndex][playerColumnIndex] = ' '
                playerRowIndex -= 1
                playerColumnIndex -= 1
                playingList[playerRowIndex][playerColumnIndex] = f'{player}'
                incorrect_entry = False
        case 'SE':
            incorrect_entry = True

            if (playerRowIndex+1 > rowcolNumber-1 or playerColumnIndex+1 > rowcolNumber-1 or
                playerRowIndex+1 < 0 or playerColumnIndex+1 < 0 ):
                incorrect_entry = True
                print('Out of boundary error')
            elif playingList[playerRowIndex+1][playerColumnIndex+1] != ' ':
                print('There is another entity on that position')
                incorrect_entry = True
                
            else:
                incorrect_entry = False
                
            if incorrect_entry == True:
                bigStoneMove(player,playingList)
            else:
                playingList[playerRowIndex][playerColumnIndex] = ' '
                playerRowIndex += 1
                playerColumnIndex += 1
                playingList[playerRowIndex][playerColumnIndex] = f'{player}'
                incorrect_entry = False
        case 'SW':
            incorrect_entry = True

            if (playerRowIndex+1 > rowcolNumber-1 or playerColumnIndex-1 > rowcolNumber-1 or
                playerRowIndex+1 < 0 or playerColumnIndex-1 < 0 ):
                incorrect_entry = True
                print('Out of boundary error')
            elif playingList[playerRowIndex+1][playerColumnIndex-1] != ' ':
                print('There is another entity on that position')
                incorrect_entry = True
                
            else:
                incorrect_entry = False
                
            if incorrect_entry == True:
                bigStoneMove(player,playingList)
            else:
                playingList[playerRowIndex][playerColumnIndex] = ' '
                playerRowIndex += 1
                playerColumnIndex -= 1
                playingList[playerRowIndex][playerColumnIndex] = f'{player}'
                incorrect_entry = False
        

        #Return
     
    return playingList

def smallStonePositioner(playingList): #Not efficient due to using the same validation code block multiple times
    rowcolNumber = len(playingList)
    validatorList = []
    for i in range(rowcolNumber): #Making a list which consist of number of rows in table to check if valid.
        validatorList.append(i+1)

    match rowcolNumber: #Used for checking letter of the location input value and get the column index
        case 3:
            validatorLetterList = ['A','B','C']
        case 5:
            validatorLetterList = ['A','B','C','D','E']
        case 7:
            validatorLetterList = ['A','B','C','D','E','F','G']
   
    impossibleMove = True
    while impossibleMove:

        stoneLocation = input('enter small stone location')
        if not stoneLocation[0].isdigit():
            print('Invalid Value')
            smallStonePositioner(playingList)
            break

        stoneRowIndex = int(stoneLocation[0]) - 1
        for letter in validatorLetterList:
            if letter == stoneLocation[1]:
                stoneColumnIndex = validatorLetterList.index(letter)
                break

        if len(stoneLocation) != 2 or (int(stoneLocation[0]) not in validatorList) or (stoneLocation[1] not in validatorLetterList):
            print('Incorrect value has entered')
            impossibleMove = True

        elif playingList[stoneRowIndex][stoneColumnIndex] != ' ':
            print('There is another entity in the area')
            impossibleMove = True
        
        elif (stoneRowIndex > rowcolNumber-1 or stoneColumnIndex > rowcolNumber-1 or
              stoneRowIndex < 0 or stoneColumnIndex < 0 ):
            print('Out of boundary')
            impossibleMove = True
        
        else:
            impossibleMove = False
        
    
    playingList[stoneRowIndex][stoneColumnIndex] = 'O'
    
    #Return

    return playingList   
    
def gameFinishedChecker(player,playingList):

    playerWin = True
    rowcolNumber = len(playingList)

    playerRowIndex = 0
    letterFound = False
    for innerList in playingList:
        playerColumnIndex = -1
        for n in innerList:
            playerColumnIndex += 1
            if n == player:
                letterFound = True
                break
        if letterFound:
            break
            
        playerRowIndex +=1

    if playerRowIndex == 0:
        if playerColumnIndex == 0:
            if (playingList[playerRowIndex][playerColumnIndex+1] == ' ' or 
                playingList[playerRowIndex+1][playerColumnIndex] == ' ' or 
                playingList[playerRowIndex+1][playerColumnIndex+1] == ' '):
                playerWin = False
        elif playerColumnIndex == rowcolNumber-1:
            if (playingList[playerRowIndex][playerColumnIndex-1] == ' ' or 
                playingList[playerRowIndex+1][playerColumnIndex] == ' ' or 
                playingList[playerRowIndex+1][playerColumnIndex-1] == ' '):
                playerWin = False
        else:
            if (playingList[playerRowIndex][playerColumnIndex+1] == ' ' or 
                playingList[playerRowIndex][playerColumnIndex-1] == ' ' or 
                playingList[playerRowIndex+1][playerColumnIndex] == ' ' or
                playingList[playerRowIndex+1][playerColumnIndex+1] == ' 'or
                playingList[playerRowIndex+1][playerColumnIndex-1] == ' '):
                playerWin = False

    elif playerRowIndex == rowcolNumber-1:
        if playerColumnIndex == 0:
            if (playingList[playerRowIndex][playerColumnIndex+1] == ' ' or 
                playingList[playerRowIndex-1][playerColumnIndex] == ' ' or 
                playingList[playerRowIndex-1][playerColumnIndex+1] == ' '):
                playerWin = False 
        elif playerColumnIndex == rowcolNumber -1:
            if (playingList[playerRowIndex][playerColumnIndex-1] == ' ' or 
                playingList[playerRowIndex-1][playerColumnIndex] == ' ' or 
                playingList[playerRowIndex-1][playerColumnIndex-1] == ' '):
                playerWin = False
        else:
            if (playingList[playerRowIndex][playerColumnIndex+1] == ' ' or 
                playingList[playerRowIndex][playerColumnIndex-1] == ' ' or 
                playingList[playerRowIndex-1][playerColumnIndex] == ' ' or
                playingList[playerRowIndex-1][playerColumnIndex+1] == ' 'or
                playingList[playerRowIndex-1][playerColumnIndex-1] == ' '):
                playerWin = False

    elif playerColumnIndex == rowcolNumber - 1:
        if (playingList[playerRowIndex][playerColumnIndex-1] == ' ' or 
            playingList[playerRowIndex-1][playerColumnIndex] == ' ' or 
            playingList[playerRowIndex-1][playerColumnIndex-1] == ' ' or
            playingList[playerRowIndex+1][playerColumnIndex] == ' ' or
            playingList[playerRowIndex+1][playerColumnIndex-1] == ' ') :
            playerWin = False
    
    elif playerColumnIndex == 0:
        if (playingList[playerRowIndex][playerColumnIndex+1] == ' ' or 
                playingList[playerRowIndex-1][playerColumnIndex] == ' ' or
                playingList[playerRowIndex-1][playerColumnIndex+1] == ' 'or
                playingList[playerRowIndex+1][playerColumnIndex] == ' ' or
                playingList[playerRowIndex+1][playerColumnIndex+1] == ' ') :
                playerWin = False

    else:
        if (playingList[playerRowIndex][playerColumnIndex+1] == ' ' or 
                playingList[playerRowIndex][playerColumnIndex-1] == ' ' or 
                playingList[playerRowIndex-1][playerColumnIndex] == ' ' or
                playingList[playerRowIndex-1][playerColumnIndex+1] == ' 'or
                playingList[playerRowIndex-1][playerColumnIndex-1] == ' ' or
                playingList[playerRowIndex+1][playerColumnIndex] == ' ' or
                playingList[playerRowIndex+1][playerColumnIndex+1] == ' 'or
                playingList[playerRowIndex+1][playerColumnIndex-1] == ' ') :
                playerWin = False
    
    return playerWin

def main():
    another = 'Y'
    player1 = playerStoneInput(1)
    player2 = playerStoneInput(2)
    while another == 'Y':
        rowcolNumber = int(input('Enter the row/column number of the playing field (3, 5, 7):'))
        while rowcolNumber not in [3,5,7]:
            print('Please enter valid')
            rowcolNumber = int(input('Enter the row/column number of the playing field (3, 5, 7):'))

        playingList = listGenerator(rowcolNumber,player1,player2)
        visualMatrixGen(playingList)

        gameFinished = False
        playerIndexer = 0
        while not gameFinished: 
       
            if playerIndexer % 2 == 0: #Chooses which player has their turn
                playerInTurn = player1
                otherPlayer = player2
            else:
                playerInTurn = player2
                otherPlayer = player1
            playerIndexer += 1

            playingList = bigStoneMove(playerInTurn,playingList)
            visualMatrixGen(playingList)
            playingList = smallStonePositioner(playingList)
            visualMatrixGen(playingList)
    
            gameFinished = gameFinishedChecker(otherPlayer,playingList) #Checks if opponent has lost or not

        print(f'Player {playerInTurn} won the game.')
        another = input('Would you like to play again(Y/N)?:')
        while another not in ['Y','N']:
            print('Please enter correctly')
            another = input('Would you like to play again(Y/N)?:')


main()
    

    








               
     


    
    

        
        
        