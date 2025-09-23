Let $I$ be the integral we want to evaluate:
\begin{equation*}
I = \int_0^{\pi/2} e^{\sin x}\ dx.
\end{equation*}
We start by expanding the integrand $e^{\sin x}$ using the Taylor series for the exponential function $e^u = \sum_{n=0}^\infty \frac{u^n}{n!}$. Setting $u = \sin x$, we have:
\begin{equation*}
e^{\sin x} = \sum_{n=0}^\infty \frac{(\sin x)^n}{n!}.
\end{equation*}
Since $|\sin x| \le 1$ for $x \in [0, \pi/2]$, the series converges absolutely and uniformly on this interval. Therefore, we can interchange integration and summation:
\begin{equation*}
I = \int_0^{\pi/2} \sum_{n=0}^\infty \frac{(\sin x)^n}{n!} dx = \sum_{n=0}^\infty \frac{1}{n!} \int_0^{\pi/2} (\sin x)^n dx.
\end{equation*}
The integral $\int_0^{\pi/2} (\sin x)^n dx$ is known as the Wallis integral, let's denote it by $W_n$.
The Wallis integrals satisfy the recurrence relation $W_n = \frac{n-1}{n} W_{n-2}$ for $n \ge 2$. The base cases are $W_0 = \int_0^{\pi/2} 1 dx = \frac{\pi}{2}$ and $W_1 = \int_0^{\pi/2} \sin x dx = [-\cos x]_0^{\pi/2} = 1$.

Using the recurrence relation, we can derive closed-form expressions for $W_n$.
For even indices $n=2k$ where $k \ge 1$:
\begin{equation*}
W_{2k} = \frac{2k-1}{2k} W_{2k-2} = \frac{2k-1}{2k} \frac{2k-3}{2k-2} W_{2k-4} = \dots = \frac{(2k-1)(2k-3)\dots 1}{(2k)(2k-2)\dots 2} W_0.
\end{equation*}
Using the double factorial notation, $(2k-1)!! = (2k-1)(2k-3)\dots 1$ and $(2k)!! = (2k)(2k-2)\dots 2$.
So, for $k \ge 1$:
\begin{equation*}
W_{2k} = \frac{(2k-1)!!}{(2k)!!} W_0 = \frac{(2k-1)!!}{(2k)!!} \frac{\pi}{2}.
\end{equation*}
For $k=0$, we have $W_0 = \pi/2$. The formula $\frac{(-1)!!}{0!!} \frac{\pi}{2}$ would match if we define $(-1)!!=1$, given $0!!=1$. However, it's clearer to handle the $k=0$ term separately.

For odd indices $n=2k+1$ where $k \ge 0$:
\begin{equation*}
W_{2k+1} = \frac{2k}{2k+1} W_{2k-1} = \frac{2k}{2k+1} \frac{2k-2}{2k-1} W_{2k-3} = \dots = \frac{(2k)(2k-2)\dots 2}{(2k+1)(2k-1)\dots 3} W_1.
\end{equation*}
Using the double factorial notation, $(2k)!! = (2k)(2k-2)\dots 2$ and $(2k+1)!! = (2k+1)(2k-1)\dots 3 \times 1$.
Since $W_1 = 1$, we have for $k \ge 0$:
\begin{equation*}
W_{2k+1} = \frac{(2k)!!}{(2k+1)!!}.
\end{equation*}
This formula also holds for $k=0$, since $W_1 = \frac{0!!}{1!!} = \frac{1}{1} = 1$.

Now we can substitute these expressions back into the series for $I$. We split the sum into even and odd terms:
\begin{equation*}
I = \sum_{n=0}^\infty \frac{W_n}{n!} = \sum_{k=0}^\infty \frac{W_{2k}}{(2k)!} + \sum_{k=0}^\infty \frac{W_{2k+1}}{(2k+1)!}.
\end{equation*}

Let's analyze the first sum (even terms):
\begin{equation*}
\sum_{k=0}^\infty \frac{W_{2k}}{(2k)!} = \frac{W_0}{0!} + \sum_{k=1}^\infty \frac{W_{2k}}{(2k)!}.
\end{equation*}
Using $W_0 = \pi/2$ and the formula for $W_{2k}$ for $k \ge 1$:
\begin{equation*}
\sum_{k=0}^\infty \frac{W_{2k}}{(2k)!} = \frac{\pi/2}{1} + \sum_{k=1}^\infty \frac{1}{(2k)!} \left( \frac{(2k-1)!!}{(2k)!!} \frac{\pi}{2} \right).
\end{equation*}
Factoring out $\pi/2$:
\begin{equation*}
\sum_{k=0}^\infty \frac{W_{2k}}{(2k)!} = \frac{\pi}{2} \left( 1 + \sum_{k=1}^\infty \frac{(2k-1)!!}{(2k)!(2k)!!} \right).
\end{equation*}
This matches the first part of the expression we want to show.

Now let's analyze the second sum (odd terms):
\begin{equation*}
\sum_{k=0}^\infty \frac{W_{2k+1}}{(2k+1)!}.
\end{equation*}
Using the formula for $W_{2k+1}$ for $k \ge 0$:
\begin{equation*}
\sum_{k=0}^\infty \frac{W_{2k+1}}{(2k+1)!} = \sum_{k=0}^\infty \frac{1}{(2k+1)!} \frac{(2k)!!}{(2k+1)!!}.
\end{equation*}
This can be written as:
\begin{equation*}
\sum_{k=0}^\infty \frac{(2k)!!}{(2k+1)!(2k+1)!!}.
\end{equation*}
This matches the second part of the expression we want to show.

Combining the results for the even and odd parts, we get:
\begin{equation*}
I = \sum_{k=0}^\infty \frac{W_{2k}}{(2k)!} + \sum_{k=0}^\infty \frac{W_{2k+1}}{(2k+1)!} = \frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{(2k-1)!!}{(2k)!(2k)!!}\right)+\sum_{k=0}^{\infty}\frac{(2k)!!}{(2k+1)!(2k+1)!!}.
\end{equation*}
This is exactly the identity we were asked to show.

Final Answer: The final answer is $\boxed{\int_0^{\pi/2} e^{\sin x}\ dx=\frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{(2k-1)!!}{(2k)!(2k)!!}\right)+\sum_{k=0}^{\infty}\frac{(2k)!!}{(2k+1)!(2k+1)!!}}$