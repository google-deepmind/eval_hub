Solution step (1 point):
Since $a_{n+1}\leq\frac 12 a_n$ the radius of convergence of the power series $\sum a_nx^n$ is at least $2$.

Solution step (2 points):
Note that
$$
\begin{aligned}
\sum_{n=0}^{\infty} b_nx^{n+3}&=\sum_{n=0}^{\infty} a_n x^n\cdot x^3-\sum_{n=0}^{\infty} a_{n+1}x^{n+1}\cdot 3x^2+\sum_{n=0}^{\infty} a_{n+2}x^{n+2}\cdot 3x-\sum_{n=0}^{\infty} a_{n+3}x^{n+3}\\
&=x^3 \sum_{n=0}^{\infty} a_nx^n -3x^2\left(\sum_{n=0}^{\infty} a_nx^n - a_0\right)+3x \left(\sum_{n=0}^{\infty} a_nx^n - a_0 -a_1 x\right)\\
&- \left(\sum_{n=0}^{\infty} a_nx^n-a_0-a_1x-a_2x^2\right)\\
&= (x-1)^2 \sum_{n=0}^{\infty} a_nx^n + a_0(3x^2-3x+1)+a_1(-3x^2+x)+a_2x^2=: S(x)
\end{aligned}
$$
Since $S(x)$ is well defined for $|x|<2$, the series $\sum b_n x^n$ is convergent for $|x|<2$.

Solution step (7 points):
For $x\in(0,2)$ we have $\sum_{n=0}^{\infty} b_nx^n=\frac{S(x)}{x^3}$, hence, differentiating term by term, 
$$
\begin{aligned}
&\quad\sum_{n=1}^{\infty} nb_nx^{n-1}= \frac{S'(x)}{x^3}-\frac{3S(x)}{x^4}\\
&=\frac{2(x-1)\sum_{n=0}^{\infty} a_nx^n+(x-1)^2\frac{d}{dx}\left(\sum_{n=0}^{\infty} a_nx^n\right)+a_0(6x-3)+a_1(-6x+1)+2a_2x}{x^3}\\
&\quad-\frac{3S(x)}{x^4}.
\end{aligned}
$$
Evaluating at $x=1$ we finish at
$$
\sum_{n=1}^{\infty} nb_n=3a_0-5a_1+2a_2-3(a_0-2a_1+a_2)=a_1-a_2.
$$