//mean median mode of ungrouped data
A= [1 2 3 4 5 6]
B=gsort(A);
n=length (B);
MeanA=sum (B)/n;
if pmodulo(n, 2)==0
MedianA= ((B (n/2) +B (n+1/2)));
else MedianA=B ((n+1/2));
end
C=diff (B)
D=find(C)
E=diff (D)
[m k]=max (E)
modeA=B(D(k)+1)
printf('Mean of the given data is:%f\n\n',MeanA);
printf('Median of the given data is :%f\n\n', MedianA);
printf('mode of the given data is:%f\n\n\',modeA )
printf ('First moment about the mean(M1)=%f \n \n', 0);
for i=1:n
X (i) =A (i)-MeanA;
end
M2=sum (X.*X)/n;
M3=sum (X.*X.*X)/n;
M4=sum (X.*X.*X.*X)/n;
disp ("Second moment about the mean (M2)=" ,M2);
disp ("Third moment about the mean(M3)=", M3);
disp ("Fourth moment about the mean(M4)=",M4);
sd=sqrt(M2);
disp("Standard Deviation:",sd);
coeff_of_skewness=(MeanA-modeA)/sd;
disp('coeff of skewnesss')
disp(coeff_of_skewness)
