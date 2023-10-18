import numpy as np
import os
import time
import data as data
import random

gameboard = [
        ["@","#","#","G"],
        ["#","#","#","G"],
        ["#","#","#","G"],
        ["#","#","#","G"]
        ]

actionboard = data.sectorMapping["area1"]

def refreshScreen(nX,nY):
    global gameboard
    gameboard[nY][nX] = "@"

def processEncounter(area):
    global team
    turn = 0
    battle = True
    possibleEncounters = data.encounterMapping[area]
    monster = data.encounterMapping[area][random.randint(0,len(possibleEncounters)-1)]
    os.system("clear")
    print(f'A wild {monster} has appeared')
    pause = input("... (press enter to continue)")
    
    monstersHp = data.allMonsters[monster]["maxHp"]
    possibleMoves = data.allMonsters[monster]["moves"]
    amountOfMoves = random.randint(1,4)
    monstersMoves = []
    monsterLevel = random.randint(0,15)

    conditions = [monsterLevel > 0 and monsterLevel <= 15, monsterLevel > 15 and monsterLevel <= 40, monsterLevel > 40 and monsterLevel <= 100]
    results = [True if cond else False for cond in conditions]
    
    for i, condition_result in enumerate(results):
        if results[i] == True:
            match i:
                case 0:
                    for i in range(0, amountOfMoves):
                        moveChoice = random.randint(0,len(possibleMoves["15"])-1)
                        while possibleMoves["15"][moveChoice] in monstersMoves and i != 0:
                            moveChoice = random.randint(0,len(possibleMoves["15"])-1)
                        else:
                            monstersMoves.append(possibleMoves["15"][moveChoice])
                    break
                case 1:
                    print("level is between 16 and 40")
                    break
                case 2:
                    print("level is over 40")
                    break
    
    activeMember = team["first"]
    while battle:
        os.system("clear")
        print(monstersMoves)
        print(f'{activeMember["name"]} {activeMember["hp"]}/{activeMember["maxHp"]}         {monster} {monstersHp}/{data.allMonsters[monster]["maxHp"]}')
        action = input("What will you do (battle, bag, team, run)")
        
        match action:
            case "battle":
                choice =  int(input(f'Choose your move: {np.matrix(activeMember["moves"])} (1,2,3,4)'))
                move = activeMember["moves"][choice-1]
                turn += 1
                
                #calculate damage
                monstersHp = monstersHp - ((data.moves[move][0]/10) * 2.5 + random.randint(0,3))
                
            case "run":
                if (random.randint(0,3) == 1):
                    battle = False
                else:
                    pass


x = 0
y = 0
newX = 0
newY = 0


play = True
team = {
        "first" : 
            {"name":"Hauntry",
             "maxHp":100,
             "hp":100,
             "moves" : ["haunting stare", "needle barrage", "scare", "tree bash"],
             "defense":15
            }
        }

while True:
    #refreshScreen
    os.system("clear")
    for row in gameboard:
        print(" ".join('"{0}"'.format(item) for item in row))
    moveDir = input("Which way would you like to move (left, right, up, down)")

    #check for special tiles
    if actionboard[newY][newX] == "G":
        gameboard[newY][newX] = "G"
        encounter = random.randint(0,10)
        if encounter == 5:
            print("A wild monster has appeared")
            processEncounter("area1")
        else:
            print("nuthin")
    else:
        gameboard[newY][newX] = "#"

    #calculateMovement
    match moveDir:
        case "left":
            if newX > 0:
                newX -= 1
        case "right":
            if newX < 3:
                newX += 1
        case "up":
            if newY > 0:
                newY -= 1
        case "down":
            if newY < 3:
                newY += 1



    refreshScreen(newX,newY)




