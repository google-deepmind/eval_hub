```latex
\textbf{Solution:}

We wish to find all real polynomials \( P(x) \) that satisfy
\[
x\,P(x-2) = (x-2024)P(x) \quad \text{for all } x\in\mathbb{R}.
\]

\textbf{Step 1.} First, set \( x=0 \) in the equation:
\[
0\cdot P(-2) = (-2024)P(0),
\]
which immediately gives
\[
P(0)=0.
\]
Thus, \( x \) is a factor of \( P(x) \). Write
\[
P(x)=x\,Q(x)
\]
for some real polynomial \( Q(x) \).

\textbf{Step 2.} Substitute \( P(x)=x\,Q(x) \) into the original equation:
\[
x\,P(x-2) = x\,(x-2)Q(x-2)
\]
and
\[
(x-2024)P(x) = (x-2024)x\,Q(x).
\]
Cancelling the common factor \( x \) (noting that the identity holds for all \( x \), and the case \( x=0 \) has already been handled) we obtain
\[
(x-2)Q(x-2) = (x-2024)Q(x).
\]

Now, set \( x=2 \) in the above:
\[
(2-2)Q(0) = (2-2024)Q(2) \quad \Longrightarrow \quad 0 = (-2022)Q(2),
\]
so that
\[
Q(2)=0.
\]
Hence, \((x-2)\) divides \(Q(x)\); we write
\[
Q(x) = (x-2)R(x)
\]
with \( R(x) \) a polynomial.

\textbf{Step 3.} Then,
\[
P(x) = x(x-2)R(x),
\]
and substituting back (following the same cancellation procedure) yields an equation for \( R(x) \) of the form
\[
(x-4)R(x-2) = (x-2024)R(x).
\]
Setting \( x=4 \) gives
\[
0 = (4-2024)R(4) \quad \Longrightarrow \quad R(4)=0.
\]
Thus, \((x-4)\) is a factor of \( R(x) \).

\textbf{Step 4.} Continuing in this manner, we see a pattern: at each step we obtain an extra factor. Namely, after \( k \) steps we deduce that
\[
P(x) = x\,(x-2)(x-4)\cdots (x-2k) \,S(x),
\]
with \( S(x) \) a polynomial satisfying
\[
(x-2k-2)S(x-2) = (x-2024)S(x).
\]
When we set \( x=2k+2 \) we find that
\[
S(2k+2)=0,
\]
provided that \( 2k+2 \neq 2024 \).

This process continues until we can no longer extract a factor in the same way. Notice that when
\[
2k+2 = 2024 \quad \Longrightarrow \quad k = 1011,
\]
the process stops. Thus, any nonzero polynomial \( P(x) \) satisfying the equation must be divisible by
\[
x(x-2)(x-4)\cdots (x-2022).
\]
That is, we can write
\[
P(x)=x(x-2)(x-4)\cdots (x-2022)\,S(x).
\]

\textbf{Step 5.} Substitute this form back into the original equation. Define
\[
A(x)= \prod_{j=0}^{1011}\bigl(x-2j\bigr).
\]
Then \( P(x) = A(x) \,S(x) \) and a careful computation shows that the functional equation simplifies to
\[
(x-2024)S(x-2) = (x-2024)S(x).
\]
For \( x\neq2024 \) we can cancel the factor \( (x-2024) \) to get
\[
S(x-2)=S(x) \quad \text{for all } x.
\]
This tells us that \( S(x) \) is a \( 2 \)-periodic polynomial. However, the only polynomials that are periodic are constant polynomials. Hence,
\[
S(x)= c \quad \text{for some constant } c\in\mathbb{R}.
\]

\textbf{Conclusion.} All solutions to the equation are of the form
\[
\boxed{P(x)= c\prod_{j=0}^{1011}(x-2j),\quad c\in\mathbb{R}.}
\]
This expression, with \( c=0 \) or any real number, represents all real polynomial solutions of the given functional equation.
```