//MULTIPLICATION OF MATRICES
A=input('MATRIX A =')
B=input('MATRIX B =')
//matrix row and column input
row_a=input('NO.OF row A =')
column_a=input('NO OF column A =')
row_b=input('NO OF row B =')
column_b=input('NO OF COLUMN B=')
ROW_A=row_a
COLUMN_A=column_a
ROW_B=row_b
COLUMN_B=column_b

c=zeros(3,3)





for i=1:3
    for j=1:3 
        k=0
        for k=1:3 
           c(i,j)=c(i,j)+A(i,k)*B(k,j)
        end;
    end;
end;


disp(c)         
  
