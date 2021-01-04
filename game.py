from turtle import *

screen=Screen()
screen.bgcolor('black')
screensize(400,400)
#=======================================================
block1=Turtle()
block1.shape('square')
block1.color('white')
block1.speed(100)
block1.penup()
block1.setx(-300)
block1.shapesize(5,1)
#======================================================
block2=Turtle()
block2.shape('square')
block2.speed(100)
block2.color('white')
block2.penup()
block2.setx(300)
block2.shapesize(5, 1)
#=======================================================
ball=Turtle()
ball.penup()
ball.shape('circle')
ball.color('white')
x=ball.xcor()
y=ball.ycor()
x_block2=block2.xcor()
y_block2=block2.ycor()
ball.dx=3
ball.dy=3
#========================================================
#func
key=0

left_flange=0
right_flange=0    

def w():
    block1.penup()
    y=block1.ycor()
    y=y+24
    block1.sety(y)
    key='w'
    return key

def s():
    block1.penup()
    s=block1.ycor()
    s=s-24
    block1.sety(s)
    key='s'
    return key

def u():
    block2.penup() 
    y=block2.ycor()
    y=y+20
    block2.sety(y)
    key='u'
    return key

def j():
    block2.penup()
    s=block2.ycor()
    s=s-20
    block2.sety(s)
    key='j'
    return key
    

def border_checking():
      if ball.ycor()>260:
          ball.dy=ball.dy*(-1)
      if ball.ycor()<-260:
          ball.dy=ball.dy*(-1)
     
      if (ball.xcor()>250 and ball.xcor()<265) and (ball.ycor()<block2.ycor()+50 and ball.ycor()>block2.ycor()-50):
         ball.dx=ball.dx*(-1)
         
         
      if (ball.xcor()<-248 and (ball.ycor()<block1.ycor()+30 and ball.ycor()>block1.ycor()-30)):
         ball.dx=ball.dx*(-1)





def new_ball():
    if ball.xcor()>300 or ball.xcor()<-300:
        ball.speed(100)
        ball.setx(0)
        ball.sety(0)
        ball.speed(3)
        
    
    
    
    
    
    
    
    
y=0
#game loop
while True:
    screen.onkey(w,"w")
    screen.onkey(s,"s")
    screen.onkey(u,"u")
    screen.onkey(j,"j")
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    border_checking()
    new_ball()
    
    screen.listen()
    screen.update()
    print(ball.xcor(),ball.ycor(),block2.ycor()+30,block2.ycor()-30,block1.ycor()+30,block1.ycor()-30)
   
done()