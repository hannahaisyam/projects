import turtle as t  
import random
import time


delay = 0.1

score = 0
highscore = 0

#screen
screen = t.Screen()
screen.title("My snack game")
screen.bgcolor("orange")
screen.setup(width = 600,height = 600)
screen.tracer(0)


#Caterpillar's head 
head = t.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"


#food
food = t.Turtle()
food.speed(0)
food.shape("circle")
food.color("brown")
food.penup()
food.goto(25,100)

segment = [] 

# Turtle's body
pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,240)
pen.write("Score :0 Highscore :0" , align = "center" , font = ("Arial" , 16))


#Movement of the turtle
direction = {
    "w" : "up",
    "s" : "down",
    "a" : "left",
    "d" : "right"
}

def handle_keypress(key):
    new_direction = direction.get(key)
    if new_direction != opposite_direction(head.direction):
        head.direction = new_direction

def opposite_direction(current_direction):
    opposite = {
    "w" : "down",
    "s" : "up",
    "a" : "right",
    "d" : "left"
    }
    return opposite.get(current_direction)

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


#Keyboard setting
screen.listen()
for key in direction:
    screen.onkeypress(lambda key=key : handle_keypress(key), key)


#THE MAIN GAME
while True:
    screen.update()

    #check if the snake collides with border 
    if head.xcor()> 290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for single in segment:
            single.goto(1000, 1000)
        
        # Clear the segments list
        segment.clear()

        #reset score
        score = 0

        #reset delay
        delay = 0.1

        pen.clear()
        pen.write(f"Score : {score} Highscore :{highscore}" , align = "center" , font = ("Arial" , 16))

    # Check with the food 
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        #add segments 
        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segment.append(new_segment)

        #shorten delay 
        delay -= 0.001

        # increase score 
        score +=10


        if score > highscore:
            highscore = score
    
        pen.clear()
        pen.write(f"Score : {score} Highscore :{highscore}" , align = "center" , font = ("Arial" , 16))

    #Adding the body to the segment of the snake  
    for index in range(len(segment)-1,0,-1):
        x = segment[index-1].xcor()
        y = segment[index-1].ycor()
        segment[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)

    move()

    #Check for head collision with body segment
    for single in segment:
        if single.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for single in segment:
                single.goto(1000, 1000)
        
            # Clear the segments list
            segment.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, highscore), align="center", font=("Courier", 16 ))

    time.sleep(delay)


screen.mainloop()