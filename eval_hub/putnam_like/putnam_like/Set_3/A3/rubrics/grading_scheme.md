This step is worth 2 points.
Let $a_{k,n}$ denotes the probability of drawing red ball $k$-times in $n$-moves. Of course $a_{k,n}=0$ if $k>n$ or $k<0$. Moreover,
$$
\begin{array}{lll}
a_{0,1}=\frac 23,& a_{1,1}=\frac 13, \\
a_{0,2}=\frac 23\cdot \frac 34=\frac 36,& a_{1,2}=\frac 23\cdot \frac 14 +\frac 13\cdot\frac 24 = \frac 26,& a_{2,2}=\frac 13\cdot\frac 24=\frac 16.
\end{array}
$$

This step is worth 7 points.
Since the probability of drawing a red ball depends of the number of red hits in the previous steps, we can observe the following recurrence relation
$$
\begin{split}
a_{k,n}&=a_{k-1,n-1}P((\text{R in the n-th move})|(\text{R was drawn (k-1) times so far}))\\
&+a_{k,n-1}P((\text{G or B in the n-th move})|(\text{R was drawn k times so far}))=\\
&=a_{k-1,n-1}\cdot\frac{k}{n+2}+a_{k,n-1}\cdot\frac{n+2-(k+1)}{n+2}\\
&=a_{k-1,n-1}\cdot\frac{k}{n+2}+a_{k,n-1}\cdot\frac{n-k+1}{n+2}
\end{split}
$$
Using this relation we compute
$$
\begin{array}{ll}
a_{0,3}=a_{0,2}\cdot\frac 45=\frac{4}{10}, & 
a_{1,3}=a_{0,2}\cdot\frac 15 +a_{1,2}\cdot\frac 35=\frac{3}{10}, \\
a_{2,3}=a_{1,2}\cdot\frac{2}{5}+a_{2,2}\cdot\frac 25=\frac{2}{10}, & 
a_{3,3}=a_{2,2}\cdot \frac 35 = \frac{1}{10}.
\end{array}
$$
Observing the computed values we formulate the following proposition 
$$
a_{k,n}=\frac{(n+1-k)}{\frac 12(n+1)(n+2)},\quad\text{for } k=0,\ldots,n.
$$
We prove it by the induction on $n$. The verification for $n=1$ is straightforward. Assume that the formula is valid for $n-1$ and $k=0,\ldots,n-1$. Then
$$
\begin{split}
a_{0,n}&=a_{0,n-1}\cdot\frac{n+1}{n+2}=\frac{2n}{n(n+1)}\cdot\frac{n+1}{n+2}=\frac{2(n+1)}{(n+1)(n+2)} \\
a_{n,n}&=a_{n-1,n-1}\frac{n}{n+2}=\frac{2}{(n+1)(n+2)}\\
a_{k,n}&=a_{k-1,n-1}\frac{k}{n+2}+a_{k,n-1}\frac{n-k+1}{n+2}=\\
&=\frac{2(n+1-k)k}{n(n+1)(n+2)}+\frac{2(n-k)(n-k+1)}{n(n+1)(n+2)}=\frac{2(n+1-k)}{(n+1)(n+2)},\quad k=1,\ldots,n-1,
\end{split}
$$
and the prove of the formula for $n$ is completed.

This step is worth 1 point.
To finish the solution we compute $a_{45,90}=\frac{2\cdot 46}{91\cdot 92}=\frac{1}{91}$.