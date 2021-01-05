from turtle import *

screen=Screen()
screen.bgcolor('black')
screensize(400,400)
#=======================================================
rectan=Turtle()
#rectan.shape('square')
rectan.color('white')
rectan.penup()
rectan.speed(1000)
rectan.sety(240)
#rectan.shapesize(2,8)




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
    y=y+20
    block1.sety(y)
    key='w'
    return key

def s():
    block1.penup()
    s=block1.ycor()
    s=s-20
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
     
      if (ball.xcor()>290 and ball.xcor()<315) and (ball.ycor()<block2.ycor()+60 and ball.ycor()>block2.ycor()-60):
         ball.dx=ball.dx*(-1)
         
         
      if (ball.xcor()<(-290) and ball.xcor()>(-315) and (ball.ycor()<block1.ycor()+60 and ball.ycor()>block1.ycor()-60)):
         ball.dx=ball.dx*(-1)





def new_ball():
    num=0
    if ball.xcor()>300 or ball.xcor()<-300:
        ball.speed(100)
        ball.setx(0)
        ball.sety(0)
        ball.speed(10)
        num=1    
    return num
    
    
    
    
    
    
game_lose=0  
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
    num=new_ball()
    game_lose=game_lose+num
    if game_lose==3:
        print('game finished')
        break
    rectan.write("SCORE = ",game_lose,align="center",font=("courier",24,"normal"))
    screen.listen()
    screen.update()
    
    #print(block2.xcor(),block1.xcor(),block2.ycor()+30,block2.ycor()-30,block1.ycor()+30,block1.ycor()-30)
   
done()