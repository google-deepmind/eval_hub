This step is worth 2 points.
Note that
$$
\frac{2x^2+1}{(x^2-1)^2}= \frac{1}{4}\cdot
\frac{1}{x-1}-\frac{1}{4}\cdot\frac{1}{x+1}+\frac{3}{4}\cdot
\frac{1}{(x-1)^2}+\frac{3}{4}\cdot \frac{1}{(x+1)^2}.
$$

This step is worth 5 points.
Let $P(x)=(x-x_1)(x-x_2)(x-x_3)(x-x_4)=x^4-2x-1$. Then, taking the derivatives,
$$
\begin{aligned}
P'(x)&=(x-x_2)(x-x_3)(x-x_4)+\cdots+(x-x_1)(x-x_2)(x-x_3),\\
\frac{P'(x)}{P(x)}&=\sum_{i=1}^4\frac{1}{x-x_i}, \\
\frac{P''(x)P(x)-P'(x)P'(x)}{P(x)^2}&=-\sum_{i=1}^4\frac{1}{(x-x_i)^2}.
\end{aligned}
$$
On the other hand $P'(x)=4x^3-2$, $P''(x)=12x^2$.

This step is worth 3 points.
Hence
$$
\begin{aligned}
\sum_{i=1}^4 \frac{1}{x_i-1}&=-\frac{P'(1)}{P(1)}=-\frac{2}{-2}=1,\\
\sum_{i=1}^4 \frac{1}{x_i+1}&=-\frac{P'(-1)}{P(-1)}=-\frac{-6}{2}=3,\\
\sum_{i=1}^4\frac{1}{(x_i-1)^2}&=-\frac{P''(1)P(1)-P'(1)P'(1)}{P(1)^2}=-\frac{12\cdot (-2)-2^2}{(-2)^2}=7,\\
\sum_{i=1}^4\frac{1}{(x_i+1)^2}&=-\frac{P''(-1)P(-1)-P'(-1)P'(-1)}{P(-1)^2}=-\frac{12\cdot 2-(-6)^2}{2^2}=3.
\end{aligned}
$$

Finally, the sum we are computing is $\frac 14 \cdot 1-\frac 14 \cdot 3+\frac 34\cdot 7+\frac 34\cdot 3=\frac{28}4=7$.