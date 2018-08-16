i mport turtle
import random
import time



turtle.bgpic("env.gif")

score = 0
scoreTurtle=turtle.clone()
scoreTurtle.hideturtle()
scoreTurtle.penup()
scoreTurtle.goto(480,450)
scoreTurtle.write(score,align="center",font=("times",33,"bold"))

game_over=turtle.clone()
game_over.hideturtle()
game_over.penup()
game_over.goto(0,0)





SQUARE_SIZE = 20

man=turtle.clone()
turtle.hideturtle()
turtle.register_shape("man.gif")
man.shape("man.gif")
turtle.setup(1000,1000)
man.penup()
man.goto(0,-150)

turtle.tracer(1,0)

LEFT_ARROW = "Left" 
RIGHT_ARROW = "Right" 
LEFT=1
RIGHT=3
UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300
direction = LEFT 

fire=turtle.clone()
turtle.register_shape("fire.gif")
fire.shape("fire.gif")
fire.penup()
fire.showturtle()
fire.goto(0,-490)

turtle.register_shape("bottle.gif")

gun1 = turtle.clone()


gun1.hideturtle()
gun1.penup()



SPACE = "space"
#a function that creates a "gun"
def up():
    
    print('You shoot the gun!')
    
    turtle.register_shape("recycle.gif")
    gun1.shape("recycle.gif")
    gun1.hideturtle()
    gun1.penup()
    gun1.setheading(90)
    gun1.goto(man.pos())
    gun1.showturtle()
    gun1.forward(1000)

z=0
difficulty=0.1
num_bottle=0
max_bottle=8
bottle_list=[]
#a function that creates bottles
def make_bottle(): 
    for num_bottle in range(max_bottle):
        random_x=random.randint(-470,470)
        bottle=turtle.clone()
        bottle.speed(0)
        bottle.hideturtle()
        bottle.penup()
        bottle.shape("bottle.gif")
        bottle.goto(random_x,480)
        bottle_list.append(bottle)
        bottle.showturtle()
        bottle.speed(0)
    
 #a function that chooses a random bottle and moves it by a little bit   
def move_bottle():
    random_bottle=random.randint(0,max_bottle-1)
    bottle=bottle_list[random_bottle]
    bottle.goto(bottle.pos()[0],bottle.pos()[1]- SQUARE_SIZE)  
    time.sleep(difficulty)        
 
old_stamp="not set"

#a function that enables the movement of the main character
def move_man():
    my_pos = man.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        man.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        man.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    
        
#defining movement to the left
def left():
    global direction 
    direction=LEFT 
    print("You pressed the left key!")
    move_man()
#defining movement to the right
def right():
    global direction 
    direction=RIGHT 
    print("You pressed the right key!")    
    move_man()
    

turtle.onkeypress(right,RIGHT_ARROW) # Create listener for up key
turtle.onkeypress(left,LEFT_ARROW) # Create listener for up key
turtle.listen()
make_bottle()
#this is our main loop which always runs
while True:
    
   
    turtle.onkeypress(up,SPACE)
    #each time we choose a bottle and check for it several things
    for bottle in bottle_list:
        #here we check if a bottle hits the bottom of the screen, if so you lose the game.
        if  bottle.pos()[1] < -410:
            game_over.write("Great Job ! You Recycle " + str(score) + " bottles",align="center",font=("times",45,"bold"))
            quit()
        #here we check if the bullet hits a bottle, if so the bottle disappears
        if  gun1.pos()[0] < bottle.pos()[0] + 30 and gun1.pos()[0] > bottle.pos()[0] - 30 and gun1.pos()[1] > bottle.pos()[1] - 30 :
            bottle_list.remove(bottle)
            bottle.hideturtle()
            score+=1
            scoreTurtle.clear()
            scoreTurtle.write(int(score),align="center",font=("times",33,"bold"))
        #here we check if there are less than 8 bottles, if so we create another one
        if len(bottle_list) < max_bottle:
            random_x=random.randint(-470,470)
            bottle=turtle.clone()
            bottle.speed(0)
            bottle.hideturtle()
            bottle.penup()
            bottle.shape("bottle.gif")
            bottle.goto(random_x,480)
            bottle_list.append(bottle)
            bottle.showturtle()
            bottle.speed(8)    
        #here we make the bottles move faster every 10 points you get
        if score - z >= 10:
            difficulty-=0.025
            z=z+10
        move_bottle()

turtle.mainloop()
