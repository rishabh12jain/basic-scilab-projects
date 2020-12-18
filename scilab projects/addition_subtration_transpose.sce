//code for transpose ,addition , multiplication
//matrix input-
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
//if row_a<row_b | row_a==row_b then
//    result_row=row_b
//    count_row=row_a
//else
//    result_row=row_a
//    count_row=row_b
//end
//
//if column_a<column_b | column_a==column_b then
//    result_column=column_b
//    count_column=column_a
//else
//    result_column=column_a
//    count_column=column_b    
//    
//end
//MATRIX ADDITION
RESULT_ADDITION=zeros(ROW_A,COLUMN_A)
for i=1:ROW_A 
    for j=1:COLUMN_A 
    RESULT_ADDITION(i,j)=B(i,j)+A(i,j);
    end
end
//for i=1:count_row
//    for j=1:count_column 
//    RESULT_ADDITION(i,j)=RESULT_ADDITION(i,j)+B(i,j);
//    end
//end
disp(RESULT_ADDITION)

RESULT_SUBTRACTION=zeros(ROW_A,COLUMN_A)
for i=1:ROW_A
    for j=1:COLUMN_A 
    RESULT_SUBTRACTION(i,j)=A(i,j)-B(i,j);
    end
end
TRANSPOSE_A=zeros(COLUMN_A,ROW_A)
TRANSPOSE_B=zeros(COLUMN_B,ROW_B)
for i=1:ROW_A 
    for j=1:COLUMN_A 
    TRANSPOSE_A(j,i)=A(i,j)
    
    end
end

for i=1:ROW_A 
    for j=1:COLUMN_A 
    TRANSPOSE_B(j,i)=B(i,j)
    
    end
end
clc()
disp('ADDITION')
disp(RESULT_ADDITION)
disp('SUBTRACTION')
disp(RESULT_SUBTRACTION)
disp('TRANSPOSE_A')
disp(TRANSPOSE_A)
disp('TRANSPOSE_B')
disp(TRANSPOSE_B)
