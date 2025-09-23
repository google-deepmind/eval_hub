Solution step (2 points)
We can simplify the formula for $a_n$ as follows
$$
\begin{split}
a_n&=\frac{\left(1+\frac 1n\right)^{3n+2}}{\left(1+\frac 1n\right)^n+\left(1+\frac 1n\right)^{n+1}+\left(1+\frac 1n\right)^{n+2}}=
\frac{(n+1)^{3n+2}\cdot n^{-(3n+2)}}{n^{-n}(n+1)^n+n^{-(n+1)}(n+1)^{n+1}+n^{-(n+2)}(n+1)^{n+2}}=\\
&=\frac{(n+1)^{2n+2}n^{-2n}}{n^2+n(n+1)+(n+1)^2}=\frac{(n+1)^{2n+2}}{n^{2n}(3n^2+3n+1)}.
\end{split}
$$

Solution step (7 points)
We study the behavior of the sequence $b_n=\ln(a_n)=(2n+2)\ln(n+1)-2n\ln(n)-\ln(3n^2+3n+1)$. Consider a function $f:(0,\infty)\to\mathbb{R}$ given by $f(x)=(2x+2)\ln(x+1)-2x\ln(x)-\ln(3x^2+3x+1)$. Then
$$
\begin{split}
f'(x)&=2\ln(x+1)+\frac{2x+2}{x+1}-2\ln x-x-\frac{6x+3}{3x^2+3x+1}=2\ln\left(\frac{x+1}x\right)-\frac{6x+3}{3x^2+3x+1}\\
f''(x)&=\frac{2}{x+1}-\frac{2}{x}-\frac{6(3x^2+3x+1)-(6x+3)(6x+3)}{(3x^2+3x+1)^2}=\frac{-2}{x(x+1)} +\frac{18x^2+18x+8}{(3x^2+3x+1)^2}=\\
&=\frac{-2(9x^4+9x^1+1+12x^3+6x^2+6x)+(x^2+x)(18x^2+18x+8}{x(x+1)(3x^2+3x+1)^2}=\\
&=\frac{-4x^2-4x-2}{x(x+1)(3x^2+3x+1)^2}<0.
\end{split}
$$
Since the function $f'(x)$ is decreasing and $\lim_{x\to\infty} f'(x)=0$, the derivative $f'(x)$ is positive, so $f(x)$ is an increasing function.

Solution step (1 point)
Therefore $b_n$ is the strictly increasing sequence and therefore $a_n=e^{b_n}$ is strictly increasing.