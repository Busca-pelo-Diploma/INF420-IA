import sys
import math

# Grab Snaffles and try to throw them through the opponent's goal!
# Move towards a Snaffle and use your team id to determine where you need to throw it.

# Entities classES used to save values outside of for loop, WIZARD for Wizards and close Snaffles and Snaffle for every Snaffle in the game
class Wizard:
    def __init__(self, id, x, y, state, closeX, closeY, closerSanffleID):
        self.id = id
        self.x = x
        self.y = y
        self.state = state
        self.closeX = closeX
        self.closeY = closeY
        self.closerSanffleID = closerSanffleID

class Snaffle:
    def __init__(self, id, x, y, state):
        self.id = id
        self.x = x
        self.y = y
        self.state = state

my_team_id = int(input())  # if 0 you need to score on the right of the map, if 1 you need to score on the left

# Setting where i need to score based on team ID
if(my_team_id==0):
    goalX = 16000
    goalY = 3750
else:
    goalX = 0
    goalY = 3750

# game loop
while True:

    my_score, my_magic = [int(i) for i in input().split()]
    opponent_score, opponent_magic = [int(i) for i in input().split()]
    entities = int(input())  # number of entities still in game
    
    # Lists of wizards and Snaffles in game being initialized
    wizards = [Wizard(0,0,0,0,0,0,0), Wizard(0,0,0,0,0,0,0)]
    snaffles = []

    for i in range(entities-4):
        snaffles.append(Snaffle(0,0,0,0))

    for i in range(entities):
        inputs = input().split()
        entity_id = int(inputs[0])  # entity identifier
        entity_type = inputs[1]  # "WIZARD", "OPPONENT_WIZARD" or "SNAFFLE" (or "BLUDGER" after first league)
        x = int(inputs[2])  # position
        y = int(inputs[3])  # position
        vx = int(inputs[4])  # velocity
        vy = int(inputs[5])  # velocity
        state = int(inputs[6])  # 1 if the wizard is holding a Snaffle, 0 otherwise

        # Save Wizards in wizards list
        if(i<2):
            wizards[i].id = entity_id
            wizards[i].x = x
            wizards[i].y = y
            wizards[i].state = state
        
        # Save Snaffles in snaffles list
        elif(i>3):
            snaffles[i-4].id = entity_id
            snaffles[i-4].x = x
            snaffles[i-4].y = y
            snaffles[i-4].state = state

        # Set default value for closer snaffle auxs
        closerSnaffle = 100000
        closerSnaffleX = 0
        closerSnaffleY = 0

        # For each Wizard it does the calculation to find which snaffle is closer
        for i in range(2):
            for j in range(entities-4):
                if(snaffles[i].state): continue

                distance = math.dist([wizards[i].x, wizards[i].y],[snaffles[j].x, snaffles[j].y])

                if(distance < closerSnaffle):
                    closerSnaffle = distance
                    closerSnaffleX = snaffles[j].x
                    closerSnaffleY = snaffles[j].y
            
            wizards[i].closeX = closerSnaffleX
            wizards[i].closeY = closerSnaffleY
            
            closerSnaffle = 100000
            closerSnaffleX = 0
            closerSnaffleY = 0

    for i in range(2):

        # Move if wizard is not holding snaffle, throw the ball if so
        if(i==0):
            if(wizards[0].state==0):
                print("MOVE " + str(wizards[0].closeX) + " " + str(wizards[0].closeY) + " 100")
            else:
                print("THROW " + str(goalX) + " " + str(goalY) + " 500")
        
        else:
            if(wizards[1].state==0):
                print("MOVE " + str(wizards[1].closeX) + " " + str(wizards[0].closeY) + " 100")
            else:
                print("THROW " + str(goalX) + " " + str(goalY) + " 500")