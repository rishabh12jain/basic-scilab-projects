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
block1.setx(-285)
block1.shapesize(10,1)
#======================================================
block2=Turtle()
block2.shape('square')
block2.speed(100)
block2.color('white')
block2.penup()
block2.setx(285)
block2.shapesize(10,1)
#=======================================================
ball=Turtle()
ball.penup()
ball.shape('circle')
ball.color('white')
x=ball.xcor()
y=ball.ycor()
x_block2=block2.xcor()
y_block2=block2.ycor()
    
#========================================================
#func
key=0

left_flange=0
right_flange=0    

def w():
    block1.penup()
    y=block1.ycor()
    block1.sety(y+25)
    key='w'
    return key

def s():
    block1.penup()
    s=block1.ycor()
    block1.sety(s-25)
    key='s'
    return key

def u():
    block2.penup() 
    y=block2.ycor()
    block2.sety(y+25)
    key='u'
    return key

def j():
    block2.penup()
    s=block2.ycor()
    block2.sety(s-25)
    key='j'
    return key
    




    
def ball_func(x):
    if x==0:
        i=ball.xcor()
        ball.setx(i+2)
        
        
def start():
    
      x=ball.xcor()
      y=ball.ycor()
      x_block2=block2.xcor()
      y_block2=block2.ycor()
        
      if x+19!=x_block2:
          x=0
          y=0
          
      elif x+19==x_block2 and y==y_block2:
        x=1  
        y=1
    
      return x,y
  

#global  x=ball.xcor(),      y=ball.ycor(), x_block2=block2.xcor(), y_block2=block2.ycor(), x_block1=block1.xcor(), y_block1=block1.ycor()
      
     
left_flange=0
right_flange=0


def turn_condition():
      x=int(ball.xcor())
      y=ball.ycor()
      x_block2=block2.xcor()
      y_block2=block2.ycor()
      
      x_block1=block1.xcor()
      y_block1=block1.ycor()
      left_flange=0
      right_flange=0
    
      if (ball.xcor()+19==x_block2): #and y==y_block2):
          turn=1
          left_flange=1
          right_flange=2
      elif (x-20==x_block1): #and y==y_block1):
          turn=1
          
          left_flange=1
          right_flange=2
      else:    
          turn=0
      arr=[turn,left_flange,right_flange]
      return arr


y=0
#game loop
while True:
    screen.onkey(w,"w")
    screen.onkey(s,"s")
    screen.onkey(u,"u")
    screen.onkey(j,"j")
    
    turn_condition()
    arr=turn_condition()
    #ball_continue(arr)
    if arr[0]==1:
        if arr[1]==1:
            ball.left(175)
        if arr[2]==1:
            ball.right(175)
        x=1
        y=1
    
    if y==0:
        x,y=start()
        ball_func(x) 
    
    if arr[1]!=0 and arr[2]!=0:
        brr=[]
        brr=arr[:]
        print('brr:',brr)
    try: 
        if (brr[1]==1 and brr[2]==2) or (brr[1]==2 and brr[2]==1):
            ball.forward(2)
            print('done')
    except:
        print('ok')
        
    
   
    
    screen.listen()
    screen.update()
    print(block1.xcor(),ball.xcor(),ball.ycor(),block2.xcor(),left_flange,right_flange)
    print(arr[0],arr[1],arr[2])
done()