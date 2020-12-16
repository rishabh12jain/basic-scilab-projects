 //FITTING A CURVE IN PARABOLA

num=input("no. of points=")

x=[]
y=[]
for i=1:num
   x(i)=input("x:")
   y(i)=input("y:") 
end
x_sum=0
y_sum=0
x_sq_sum=0
x_y_sum=0
x_cu_sum=0
x_sq_y_sum=0
x_qua_sum=0


for j=1:num
    x_sum=x_sum+x(j)
    y_sum=y_sum+y(j)
    x_sq_sum=x_sq_sum+x(j)*x(j)
    x_y_sum=x_y_sum+x(j)*y(j)
    x_cu_sum=x_cu_sum+x(j)*x(j)*x(j)
    x_sq_y_sum=x_sq_y_sum+x(j)*x(j)*y(j)
    x_qua_sum=x_qua_sum+x(j)*x(j)*x(j)*x(j)
end


a=[num x_sum x_sq_sum;x_sum x_sq_sum x_cu_sum;x_sq_sum x_cu_sum x_qua_sum]
b=[y_sum;x_y_sum;x_sq_y_sum]

c=linsolve(a,-b)
disp(c)

plot(x,y,'ro')

x_line=[]
y_line=[]
t=1
for m=-5:10
    x_line(t)=m
    y_line(t)=c(1)+c(2)*m+c(3)*(m^2)
    t=t+1
end
plot(x_line,y_line)
