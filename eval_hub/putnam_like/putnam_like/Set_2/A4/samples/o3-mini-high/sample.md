```latex
\textbf{Solution:}

Since the matrix \( M \) is \( 3 \times 3 \) and the only eigenvalue is \( 1 \) with algebraic multiplicity \( 3 \), the minimal polynomial of \( M \) divides
\[
(x-1)^3.
\]
That is,
\[
(M-I)^3=0.
\]
This fact implies that every power of \( M \) can be written as a polynomial in \( M \) of degree at most 2. In other words, for any natural number \( m\ge3 \) there exist scalars \( a_m, b_m, c_m \) such that
\[
M^m=a_mM^2+b_mM+c_m I_3.
\]

A convenient way to determine the coefficients is to work in the ring of polynomials modulo \((x-1)^3\). That is, we wish to find \( a_m, b_m, c_m \) such that
\[
x^m \equiv a_m x^2 + b_m x + c_m \quad (\text{mod } (x-1)^3).
\]
Since two polynomials are equivalent modulo \((x-1)^3\) if and only if they have the same value and the same first and second derivatives at \( x=1 \), we impose the following conditions on the polynomial
\[
P(x)=x^m - \bigl( a_m x^2 + b_m x + c_m \bigr):
\]

\[
\begin{array}{rcl}
\text{(i)} & P(1)=0 & \Longrightarrow 1^m - (a_m+b_m+c_m)=0, \\
\text{(ii)} & P'(1)=0 & \Longrightarrow m\cdot1^{m-1} - \bigl(2a_m\cdot1+b_m\bigr)=0, \\
\text{(iii)} & P''(1)=0 & \Longrightarrow m(m-1)\cdot1^{m-2} - 2a_m=0.
\end{array}
\]

Let us solve these equations one by one.

\medskip

\textbf{Step 1.} From (i):
\[
a_m+b_m+c_m=1.
\]

\textbf{Step 2.} From (ii):
\[
m - (2a_m+b_m)=0 \quad \Longrightarrow \quad 2a_m+b_m=m.
\]

\textbf{Step 3.} From (iii):
\[
m(m-1)-2a_m=0 \quad \Longrightarrow \quad a_m=\frac{m(m-1)}{2}.
\]

\medskip

Now substitute \( a_m=\frac{m(m-1)}{2} \) into the equation from Step 2 to find \( b_m \):
\[
2\cdot \frac{m(m-1)}{2} + b_m = m \quad \Longrightarrow \quad m(m-1)+b_m=m,
\]
so that
\[
b_m = m - m(m-1) = m - m^2 + m = 2m - m^2.
\]
Notice that this can also be written as:
\[
b_m = m(2-m).
\]

\medskip

Finally, use the equation from Step 1 to find \( c_m \):
\[
c_m=1-a_m-b_m = 1 - \frac{m(m-1)}{2} - m(2-m).
\]
Let us simplify \( c_m \). Write \( m(2-m) \) as:
\[
m(2-m)=2m-m^2.
\]
Thus,
\[
c_m=1 - \frac{m^2-m}{2} - (2m-m^2).
\]
To combine the terms, express \( 1 \) as \(\frac{2}{2}\):
\[
c_m = \frac{2}{2} - \frac{m^2-m}{2} - \frac{4m-2m^2}{2}
=\frac{2 - (m^2-m) - (4m-2m^2)}{2}.
\]
Combine like terms in the numerator:
\[
2 - m^2 + m - 4m + 2m^2 = 2 + m^2 - 3m.
\]
Thus,
\[
c_m = \frac{m^2-3m+2}{2}.
\]
The quadratic in the numerator factors nicely:
\[
m^2-3m+2 = (m-1)(m-2),
\]
so that
\[
c_m = \frac{(m-1)(m-2)}{2}.
\]

\medskip

\textbf{Summary of the coefficients:}
\[
a_m = \frac{m(m-1)}{2}, \quad b_m = m(2-m), \quad c_m = \frac{(m-1)(m-2)}{2}.
\]

Therefore, for any natural number \( m\ge3 \),
\[
\boxed{M^m=\frac{m(m-1)}{2}\,M^2+m(2-m)\,M+\frac{(m-1)(m-2)}{2}\,I_3.}
\]
```