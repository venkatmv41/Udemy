#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
#this project is to solve a maze puzzle with defined or built in functions
#this is to test the programming and logical skills, a programmer shuould have
# while loop, if/else statements
#functions are related to puzzle mentioned in this website

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def path():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
            
 
while not at_goal():
    path()
    
