import turtle
import time
import random

score = 300
start = time.time()

t = turtle.Turtle ()
t.hideturtle()
t.up()
t.color ('red')

t1 = turtle.Turtle()
t1.ht()
t1.up()
t1.color ('red')

t2 = turtle.Turtle()
t2.ht()
t2.width (4)
turtle.delay (0)
t2.up()
t2.goto (-250,250)
t2.down ()
t2.setx(250)
t2.sety(-250)
t2.setx(-250)
t2.sety(250)
t2.up()
t2.sety (260)
t2.write (score)


x = t.xcor ()
y = t.ycor ()

list1 =[(x-20,y),(x-10,y),(x,y)]

x1 = random.randrange(-100,100,10) 
y1 = random.randrange(-100,100,10)
t1.goto (x1,y1)
t1.write (chr(9899))


direction = 'x'
a = 0.5

def movement (direction) :
    global x,y
    
    if direction == 'x' :
        x += 10
    elif direction == 'y' :
        y += 10
    elif direction == '-x' :
        x -= 10
    elif direction  == '-y' :
        y -= 10

def move_up () :
    global direction
    if direction != '-y' :
        direction = 'y'

def move_down () :
    global direction
    if direction != 'y' :
        direction = '-y'
    
def move_left () :
    global direction
    if direction != 'x' :
        direction = '-x'
    
def move_right () :
    global direction
    if direction != '-x':
        direction  = 'x'

def inside () :
    global x, y
    if list1[-1][0] > 240 :
        x = -250
    if list1[-1][0] < -240 :
        x = 250
    if list1[-1][1] > 240 :
        y = -250
    if list1[-1][1] < -240 :
         y= 250
    
    
turtle.onkeypress(move_up, 'Up')
turtle.onkeypress(move_down, 'Down')
turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(move_right, 'Right')

turtle.listen()

turtle.tracer(False)

def game () : 
    global x1,y1,score,a
    inside ()
    movement (direction)
    list1.append((x,y))
    if list1[-1] == (x1,y1) :
        t1.clear()
        x1 = random.randrange(-250,250,10)
        y1 = random.randrange(-250,250,10)
        t1.goto (x1,y1)
        t1.write (chr(9899))
        t2.undo ()
        score += 100
        t2.write (score)
    else :
        list1.pop (0)
    for i in list1 :
        t.goto(i)
        t.write (chr(9608))
    for i in range (len(list1)-1) :
        if list1[i] == list1[-1]:
            t2.up()
            t2.home()
            t2.write ('Game over')
            turtle.done()
            turtle.mainloop()
    time.sleep(a)
    t.clear()
    turtle.ontimer(game())

game ()
turtle.done ()
turtle.mainloop()


    




    
        
        
        
    
    
