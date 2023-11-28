import turtle
import time
import random

delay = 0.3
#set up screen object 
wn=turtle.Screen()
wn.title('Snake-game by GHITA')
wn.setup(width=600 , height=300)
wn.bgcolor('black')
wn.tracer(0)

#Code goes here (game logic)->

#Snake head
head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()
head.goto(0,0)
head.direction = 'up'

# food logic
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

#list of segements
segments=[]


#Functions 
#change direction
def go_up():
    head.direction = 'up'
def go_down():
    head.direction ='down'
def go_right():
    head.direction = 'right'
def go_left():
    head.direction = 'left'

#move 
def move():
    #moving up 
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)
    #moving down
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)
    #moving right
    if head.direction == 'right':
        x = head.ycor()
        head.setx(x+20)
    #moving left    
    if head.direction == 'left':
        x = head.ycor()
        head.setx(x-20)

# keyboard bindings(keys-move)t
#event : open window to listeng
wn.listen()
wn.onkeypress(go_up,'t')
wn.onkeypress(go_down,'g')
wn.onkeypress(go_right,'h')
wn.onkeypress(go_left,'f')

#loop to update screen
# loop to update screen
while True:
    wn.update()
    if head.distance(food) < 20:
        # move the food to somewhere random
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)
    move()
    time.sleep(delay)

    # move the segments backwards starting from end
    for index in range(len(segments)-1, 0, -1):
        # move coordinates of the segments from tail to head
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        print(x,y)
        segments[index].goto(x, y)
     
    #head moving : special case
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

wn.mainloop()
