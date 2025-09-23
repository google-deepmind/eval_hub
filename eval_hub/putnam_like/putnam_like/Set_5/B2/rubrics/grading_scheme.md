Solution step (1 point):
Matrices $A,B$ commute. Indeed, $AB=A(I-A)=A-A^2=(I-A)A=BA$.

Solution step (2 points):
Therefore
$$
I=(A+B)^4=A^4+B^4-4AB(A+B)^2+2A^2B^2=I-4C+2C^2,
$$
where $C=AB$.

Solution step (5 points):
It implies $0=2C^2-4C=2C(C-2I)$. Since the polynomial $p(x)=x(x-2)$ annihilates the matrix $C$, the only possible eigenvalues of $C$ are $0$ and $2$.

Solution step (2 points):
However, $A$ and $B$ are invertible, so $C$ is invertible and the only possible eigenvalue is $2$. The determinant, as a product of all eigenvalues, equals $2^n$.