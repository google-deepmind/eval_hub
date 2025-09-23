```latex
\documentclass{article}
\usepackage{amsmath, amssymb}
\begin{document}

We wish to evaluate
\[
S=\sum_{i=1}^4 \frac{2x_i^2+1}{(x_i^2-1)^2},
\]
where the numbers \( x_1,x_2,x_3,x_4 \) are the roots of 
\[
x^4-2x-1=0.
\]

A key idea is to first rewrite the numerator as follows:
\[
\frac{2x^2+1}{(x^2-1)^2} = \frac{2x^2-2+3}{(x^2-1)^2}
=\frac{2(x^2-1)}{(x^2-1)^2} +\frac{3}{(x^2-1)^2}
=\frac{2}{x^2-1}+\frac{3}{(x^2-1)^2}.
\]
Thus,
\[
S=2\sum_{i=1}^4\frac{1}{x_i^2-1}+3\sum_{i=1}^4\frac{1}{(x_i^2-1)^2}.
\]
We will compute the two sums separately.

\medskip

\textbf{Step 1. Computation of } \(\displaystyle \sum_{i=1}^4\frac{1}{x_i^2-1}\).

First, note that
\[
\frac{1}{x^2-1}=\frac{1}{(x-1)(x+1)}
=\frac{1}{2}\left(\frac{1}{x-1}-\frac{1}{x+1}\right).
\]
Hence,
\[
\sum_{i=1}^4\frac{1}{x_i^2-1}
=\frac{1}{2}\left(\sum_{i=1}^4\frac{1}{x_i-1}
-\sum_{i=1}^4\frac{1}{x_i+1}\right).
\]
A standard fact about a monic polynomial 
\[
P(x)=\prod_{i=1}^4 (x-x_i)
\]
is that
\[
\frac{P'(x)}{P(x)}=\sum_{i=1}^4 \frac{1}{x-x_i}.
\]
Thus, setting \( x=c \) (where \( c \) is not a root) we have
\[
\sum_{i=1}^4\frac{1}{c-x_i}=\frac{P'(c)}{P(c)}.
\]
In our application, to obtain sums of the form \( \sum \frac{1}{x_i-1} \) and \( \sum \frac{1}{x_i+1} \) we work as follows.

For \( c=1 \):
\[
\frac{P'(1)}{P(1)}=\sum_{i=1}^4\frac{1}{1-x_i}.
\]
But since
\[
\frac{1}{x_i-1} = -\frac{1}{1-x_i},
\]
we deduce that
\[
\sum_{i=1}^4 \frac{1}{x_i-1}=-\frac{P'(1)}{P(1)}.
\]
Similarly, with \( c=-1 \) we have
\[
\frac{P'(-1)}{P(-1)}=\sum_{i=1}^4 \frac{1}{-1-x_i}
=-\sum_{i=1}^4 \frac{1}{x_i+1},
\]
so that
\[
\sum_{i=1}^4 \frac{1}{x_i+1}=-\frac{P'(-1)}{P(-1)}.
\]

Now, our polynomial is 
\[
P(x)=x^4-2x-1.
\]
We compute:
\[
P(1)=1^4-2\cdot1-1=-2,\quad P' (x)=4x^3-2,\quad P'(1)=4-2=2,
\]
and
\[
P(-1)=(-1)^4-2(-1)-1=1+2-1=2,\quad P'(-1)=4(-1)^3-2=-4-2=-6.
\]
Thus,
\[
\sum_{i=1}^4\frac{1}{x_i-1}=-\frac{2}{-2}=1,\quad
\sum_{i=1}^4\frac{1}{x_i+1}=-\frac{-6}{2}=3.
\]
It follows that
\[
\sum_{i=1}^4 \frac{1}{x_i^2-1}
=\frac{1}{2}(1-3)=-1.
\]
Therefore,
\[
2\sum_{i=1}^4\frac{1}{x_i^2-1} = 2(-1)=-2.
\]

\medskip

\textbf{Step 2. Computation of } \(\displaystyle \sum_{i=1}^4 \frac{1}{(x_i^2-1)^2}\).

Again, writing
\[
\frac{1}{(x^2-1)^2}=\frac{1}{(x-1)^2(x+1)^2},
\]
we use the partial fraction decomposition
\[
\frac{1}{(x^2-1)^2}=\frac{1}{4}\left(\frac{1}{(x-1)^2} 
- \frac{2}{(x-1)(x+1)}+\frac{1}{(x+1)^2}\right).
\]
Summing over all roots we obtain
\[
\sum_{i=1}^4 \frac{1}{(x_i^2-1)^2}=\frac{1}{4}
\left(\sum_{i=1}^4\frac{1}{(x_i-1)^2} -2\sum_{i=1}^4\frac{1}{(x_i-1)(x_i+1)}+
\sum_{i=1}^4 \frac{1}{(x_i+1)^2}\right).
\]

We now compute each of the three sums.

\medskip

\underline{\( \displaystyle A=\sum_{i=1}^4\frac{1}{(x_i-1)^2} \):} 

A known formula tells us that
\[
\sum_{i=1}^4 \frac{1}{(x-c)^2}=\frac{P''(c)}{P(c)}-\left(\frac{P'(c)}{P(c)}\right)^2.
\]
Taking \( c=1 \) and using
\[
P(1)=-2,\quad P'(1)=2,\quad P''(x)=12x^2,\quad P''(1)=12,
\]
we have
\[
A=\frac{12}{-2}-\left(\frac{2}{-2}\right)^2 = -6-(-1)^2=-6-1=-7.
\]

\medskip

\underline{\( \displaystyle B=\sum_{i=1}^4\frac{1}{(x_i+1)^2} \):}

For \( c=-1 \) we have
\[
P(-1)=2,\quad P'(-1)=-6,\quad P''(-1)=12,
\]
so that
\[
B=\frac{12}{2}-\left(\frac{-6}{2}\right)^2=6-(-3)^2=6-9=-3.
\]

\medskip

\underline{\( \displaystyle C=\sum_{i=1}^4\frac{1}{(x_i-1)(x_i+1)} \):}

Notice that
\[
\frac{1}{(x_i-1)(x_i+1)}
=\frac{1}{2}\left(\frac{1}{x_i-1}-\frac{1}{x_i+1}\right).
\]
Thus,
\[
C=\frac{1}{2}\left(\sum_{i=1}^4\frac{1}{x_i-1}-
\sum_{i=1}^4\frac{1}{x_i+1}\right)
=\frac{1}{2}(1-3)=-1.
\]

\medskip

Putting these together, we have
\[
\sum_{i=1}^4 \frac{1}{(x_i^2-1)^2}=\frac{1}{4}\Bigl(A - 2C+B\Bigr)
=\frac{1}{4}\Bigl((-7)-2(-1)+(-3)\Bigr)
=\frac{1}{4}(-7+2-3)
=\frac{-8}{4}=-2.
\]
Multiplying by 3 gives
\[
3\sum_{i=1}^4 \frac{1}{(x_i^2-1)^2}=3(-2)=-6.
\]

\medskip

\textbf{Conclusion.} Combining the two parts we found:
\[
S=2\left(\sum_{i=1}^4\frac{1}{x_i^2-1}\right)
+3\left(\sum_{i=1}^4\frac{1}{(x_i^2-1)^2}\right)
=-2+(-6)=-8.
\]

Thus, the value of the given sum is 
\[
\boxed{-8}.
\]

\end{document}
```