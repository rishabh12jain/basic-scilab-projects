function y=unit_function (x)
    if  x<2 then
        y=0
    else
        y=1
    end
endfunction

x_mat=[]
y_mat=[]
num=1
for i=-100:100
    x_mat(num)=i
    
    y_mat(num)=3*unit_function(i)
    num=num+1
end
xlabel='X'
title='UNIT STEP FUNCTION'
plot(x_mat,y_mat,'bo','markersize',20)
