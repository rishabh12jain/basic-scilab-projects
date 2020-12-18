//BISECTION METHOD

max_itera=input('give max iteration')

function y=myfunction (x)
    y=x^3-2*x-5
endfunction

for i=1:10
    if myfunction(i)*myfunction(i+1)<0 then
       a=i
       b=i+1
       break
    end,
end;
if myfunction(a)<0 then
    negative=a
    positive=b
else
    positive=a
    negative=b
end

n=0
while positive-negative>0.001 & n~=max_itera
    
     new_value=(negative+positive)/2
        if myfunction(new_value)<0 then
            negative=new_value
        else
            positive=new_value
        end,
        n=n+1

end
