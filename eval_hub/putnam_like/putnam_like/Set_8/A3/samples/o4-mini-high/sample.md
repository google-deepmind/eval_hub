```markdown
**Solution.**  
Let 
\[
X=\Bigl\{(x_n)_{n\ge0}\subset(0,\infty)\:\Big|\:\sum_{n=0}^\infty x_n=c\Bigr\}, 
\qquad
Y=\Bigl\{\sum_{n=0}^\infty x_n^3\;:\;(x_n)\in X\Bigr\}.
\]
We claim 
\[
Y=(0,\;c^3).
\]

1.  **Upper bound.**  
By the power–mean (or simply by Hölder), for any \((x_n)\in X\)
\[
\sum_{n=0}^\infty x_n^3
\;\le\;
\Bigl(\sum_{n=0}^\infty x_n\Bigr)^3
\;=\;c^3.
\]
Moreover, by “concentrating’’ most of the mass in one term, e.g.  
\[
x_1 = c-\varepsilon,\quad x_2=\varepsilon,\quad x_n=0\;(n\ge3),
\]
one gets
\[
\sum_{n=0}^\infty x_n^3
=(c-\varepsilon)^3+\varepsilon^3
\;\xrightarrow[\varepsilon\to 0]{}\;c^3,
\]
so \(\sup Y=c^3\), but \(c^3\) is not attained when all \(x_n>0\).

2.  **Lower bound.**  
If one “spreads’’ \(c\) equally over \(N\) terms,
\[
x_1=\cdots=x_N=\frac cN,\quad x_{N+1}=x_{N+2}=\cdots=0,
\]
then
\[
\sum_{n=0}^\infty x_n^3
=N\Bigl(\frac cN\Bigr)^3
=\frac{c^3}{N^2}
\;\xrightarrow[N\to\infty]{}\;0.
\]
Thus \(\inf Y=0\), and again \(0\) is not attained among strictly positive \(x_n\).

Putting these together shows
\[
Y=(0,\;c^3).
\]
```

**Answer.**  
\[
Y = \bigl\{\,t\in\Bbb R:0<t<c^3\bigr\}=(0,c^3).
\]