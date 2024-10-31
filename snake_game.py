from turtle import Turtle,Screen
import random
import  time
delay = 0.1
score = 0
high_score = 0



#setting the screen
scr = Screen()
scr.title('Snake Game')
scr.bgcolor('dark green')
scr.setup(600,600)
scr.tracer(0)

#creating head of the snake
head = Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.up()
head.goto(0,0)
head.direction = 'up'

#creating food
food = Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.up()
food.goto(0,100)

#display the score
pen = Turtle()
pen.speed(0)
pen.color('White')
pen.hideturtle()
pen.up()
pen.goto(0,250)
pen.write('Score:0 High score:0',False,'center',('arial',20,'bold'))


def move_up():
    if head.direction != 'down':
        head.direction = 'up'
def move_down():
    if head.direction != 'up':
        head.direction = 'down'
def move_left():
    if head.direction != 'right':
        head.direction = 'left'
def move_right():
    if head.direction != 'left':
        head.direction = 'right'
def move():
    if head.direction == 'up':
        y_pos = head.ycor()
        head.sety(y_pos+20)
    if head.direction == 'down':
        y_pos2 = head.ycor()
        head.sety(y_pos2-20)
    if head.direction == 'left':
        x_pos = head.xcor()
        head.setx(x_pos-20)
    if head.direction == 'right':
        x_pos2 = head.xcor()
        head.setx(x_pos2+20)

scr.listen()
scr.onkeypress(move_up, 'Up')
scr.onkeypress(move_down , 'Down')
scr.onkeypress(move_left , 'Left')
scr.onkeypress(move_right , 'Right')

segments = []
while True:
    scr.update()
    # if snake cross the boundaries
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'
        for i in segments:
            i.goto(1000,1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f'score: {score} High score: {high_score}',False,'center',('arial',20,'bold'))

    # Growing part of the snake
    if head.distance(food) < 20:
        food_x = random.randint(-270,270)
        food_y = random.randint(-270,270)
        food.goto(food_x,food_y)

        # Adding new piece/block at the last of the snake
        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('light green')
        new_segment.up()
        segments.append(new_segment)
        delay-=0.001
        score+=10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f'Score: {score} High score: {high_score}',False,'center',('arial',20,'bold'))


    #Check the snake is hits by itself or boundaries
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        #moving the segments/blocks
        segments[index].goto(x,y)
    if len(segments) > 0:
        x_head = head.xcor()
        y_head = head.ycor()
        #moving first new_segment at head position
        segments[0].goto(x_head,y_head)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'
            for segment2 in segments:
                segment2.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f'Score: {score} High score: {high_score}',False,'center',('arial',20,'bold'))
    time.sleep(delay)










