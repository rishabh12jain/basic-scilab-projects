//FITTING A CURVE IN LINE
num=input('no. of points=')

x=[]
y=[]
for i=1:num
   x(i)=input('x:')
   y(i)=input('y:') 
end
x_sum=0
y_sum=0
x_sq_sum=0
x_y_sum=0


for j=1:num
    x_sum=x_sum+x(j)
    y_sum=y_sum+y(j)
    x_sq_sum=x_sq_sum+x(j)*x(j)
    x_y_sum=x_y_sum+x(j)*y(j)
end
a=((x_sum*x_y_sum)-(x_sq_sum*y_sum))/((x_sum*x_sum)-(num*x_sq_sum))
b=(y_sum-num*a)/x_sum


plot(x,y,'ro')


x_line=[]
y_line=[]
t=1
for m=-10:10
    x_line(t)=m
    y_line(t)=a+b*m
    t=t+1
end
plot(x_line,y_line)
