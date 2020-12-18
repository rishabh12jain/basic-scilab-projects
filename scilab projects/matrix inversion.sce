//INVERSE OF A MATRIX
row=input('enter the row of matrix=')
col=input('enter the colummn of matrix=')
for i=1:row
 for j=1:col
 A(i,j)=input('enter element=')
end
end
B=eye(col,col)
Augmented=[A,B]
if(row~=col)
 disp("inverse of matrix not found!")
else if (det(A)==0)
 disp("inverse of matrix not found!")
else
 for(i=1:row)
 Augmented(i,i:row+row)=Augmented(i,i:row+row)/Augmented(i,i)
 disp(Augmented)
 for(k=1:row)
 if(k~=i)
 Augmented(k,i:row+row)=Augmented(k,i:row+row)-Augmented(k,i)*Augmented(i,i:row+row)
 end
 end
 disp(Augmented)
end
disp("Inverse of the matrix :")
disp(Augmented)
end
end
