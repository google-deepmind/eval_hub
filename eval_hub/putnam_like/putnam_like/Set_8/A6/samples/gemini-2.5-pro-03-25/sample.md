Let $I$ denote the integral in question:
\[
I = \int_\alpha^\infty \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx.
\]
We are given that $f:[0,\infty)\to\mathbb{R}$ is a strictly decreasing continuous function, $\alpha>0$, and $\lim_{x\to\infty} f(x)=0$.
Since $f$ is strictly decreasing and $\lim_{x\to\infty} f(x)=0$, it must be that $f(x)>0$ for all $x\ge 0$.
Indeed, if $f(x_0)\le 0$ for some $x_0$, then for any $x>x_0$, $f(x)<f(x_0)\le 0$. This contradicts the limit being 0.
Since $f$ is strictly decreasing, for $x>\alpha$, we have $x-\alpha < x < x+\alpha$, which implies $f(x-\alpha)>f(x)>f(x+\alpha)$.
Therefore, the numerator $f(x-\alpha)-f(x+\alpha)$ is positive for all $x>\alpha$.
Since $f(x)>0$, the integrand $\frac{f(x-\alpha)-f(x+\alpha)}{f(x)}$ is positive for all $x>\alpha$.
Thus, the integral $I$ is either a positive real number or diverges to $\infty$. We want to show it diverges to $\infty$.

We can split the integrand into two parts:
\[
\frac{f(x-\alpha)-f(x+\alpha)}{f(x)} = \frac{f(x-\alpha)-f(x)}{f(x)} + \frac{f(x)-f(x+\alpha)}{f(x)}.
\]
Let $I_1 = \int_\alpha^\infty \frac{f(x-\alpha)-f(x)}{f(x)} dx$ and $I_2 = \int_\alpha^\infty \frac{f(x)-f(x+\alpha)}{f(x)} dx$.
Then $I = I_1 + I_2$. Since both integrands are positive, $I_1 \ge 0$ and $I_2 \ge 0$.

Let's analyze $I_1$. We perform a change of variables $y = x-\alpha$. Then $x=y+\alpha$ and $dx=dy$. The lower limit $x=\alpha$ corresponds to $y=0$. The upper limit $x=\infty$ corresponds to $y=\infty$.
\[
I_1 = \int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy.
\]
Now let's rewrite $I$ using this substitution:
\begin{align*} I &= \int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy + \int_\alpha^\infty \frac{f(x)-f(x+\alpha)}{f(x)} dx \\ &= \int_0^\alpha \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy + \int_\alpha^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy + \int_\alpha^\infty \frac{f(x)-f(x+\alpha)}{f(x)} dx \end{align*}
Let $C = \int_0^\alpha \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy$. Since the integrand is positive, $C>0$.
Let $h(x) = f(x)-f(x+\alpha)$. $h(x)>0$ for $x \ge 0$.
\[
I = C + \int_\alpha^\infty \left( \frac{h(x)}{f(x+\alpha)} + \frac{h(x)}{f(x)} \right) dx = C + \int_\alpha^\infty h(x) \left( \frac{1}{f(x+\alpha)} + \frac{1}{f(x)} \right) dx.
\]
Since $f$ is strictly decreasing, $f(x) > f(x+\alpha) > 0$ for $x\ge 0$. This implies $\frac{1}{f(x+\alpha)} > \frac{1}{f(x)}$.
Therefore, $\frac{1}{f(x+\alpha)} + \frac{1}{f(x)} > \frac{2}{f(x+\alpha)}$.
\[
I > C + \int_\alpha^\infty h(x) \frac{2}{f(x+\alpha)} dx = C + 2 \int_\alpha^\infty \frac{f(x)-f(x+\alpha)}{f(x+\alpha)} dx.
\]
Let $I_1' = \int_\alpha^\infty \frac{f(x)-f(x+\alpha)}{f(x+\alpha)} dx$. Then $I > C + 2I_1'$.
Note that $I_1 = \int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy = \int_0^\alpha \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy + I_1' = C + I_1'$.
So $I > C + 2(I_1 - C) = 2I_1 - C$.
If we can show that $I_1$ diverges to $\infty$, then $I$ must also diverge to $\infty$.

Let's analyze the convergence of $I_1 = \int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy$.
We can write $I_1$ as a series of integrals over intervals of length $\alpha$:
\[
I_1 = \sum_{k=0}^\infty \int_{k\alpha}^{(k+1)\alpha} \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy.
\]
Let $a_k = \int_{k\alpha}^{(k+1)\alpha} \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy$. Since the integrand is positive, $a_k > 0$.
For $y \in [k\alpha, (k+1)\alpha]$, we have $y+\alpha \in [(k+1)\alpha, (k+2)\alpha]$.
Since $f$ is decreasing, $f(y+\alpha) \le f((k+1)\alpha)$. Let $x_k = f(k\alpha)$ for $k \ge 0$. Then $f((k+1)\alpha) = x_{k+1}$.
So $f(y+\alpha) \le x_{k+1}$.
\[
a_k = \int_{k\alpha}^{(k+1)\alpha} \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy \ge \frac{1}{x_{k+1}} \int_{k\alpha}^{(k+1)\alpha} (f(y)-f(y+\alpha)) dy.
\]
Let $J_k = \int_{k\alpha}^{(k+1)\alpha} f(y) dy$. Then
\[
\int_{k\alpha}^{(k+1)\alpha} (f(y)-f(y+\alpha)) dy = \int_{k\alpha}^{(k+1)\alpha} f(y) dy - \int_{k\alpha}^{(k+1)\alpha} f(y+\alpha) dy.
\]
In the second integral, let $u=y+\alpha$. Then $du=dy$. The limits are $(k+1)\alpha$ and $(k+2)\alpha$.
\[
\int_{k\alpha}^{(k+1)\alpha} f(y+\alpha) dy = \int_{(k+1)\alpha}^{(k+2)\alpha} f(u) du = J_{k+1}.
\]
So, $\int_{k\alpha}^{(k+1)\alpha} (f(y)-f(y+\alpha)) dy = J_k - J_{k+1}$.
Thus, $a_k \ge \frac{J_k - J_{k+1}}{x_{k+1}}$.
Let $S_N = \sum_{k=0}^N a_k$. Then $S_N \ge \sum_{k=0}^N \frac{J_k - J_{k+1}}{x_{k+1}}$.
Let's analyze the sum $T_N = \sum_{k=0}^N \frac{J_k - J_{k+1}}{x_{k+1}}$. We use summation by parts. The formula is $\sum_{k=m}^n u_k (v_{k+1}-v_k) = [u_k v_k]_m^{n+1} - \sum_{k=m}^n v_{k+1}(u_{k+1}-u_k)$.
Let $u_k = 1/x_{k+1}$ and $v_k = -J_k$. Then $v_{k+1}-v_k = -J_{k+1} - (-J_k) = J_k - J_{k+1}$.
\[
T_N = \sum_{k=0}^N u_k (v_{k+1}-v_k) = u_{N+1} v_{N+1} - u_0 v_0 - \sum_{k=0}^N v_{k+1} (u_{k+1}-u_k)
\]
\[
T_N = \frac{1}{x_{N+2}} (-J_{N+1}) - \frac{1}{x_1} (-J_0) - \sum_{k=0}^N (-J_{k+1}) \left( \frac{1}{x_{k+2}} - \frac{1}{x_{k+1}} \right)
\]
\[
T_N = \frac{J_0}{x_1} - \frac{J_{N+1}}{x_{N+2}} + \sum_{k=0}^N J_{k+1} \left( \frac{1}{x_{k+2}} - \frac{1}{x_{k+1}} \right) = \frac{J_0}{x_1} - \frac{J_{N+1}}{x_{N+2}} + \sum_{k=1}^{N+1} J_k \left( \frac{1}{x_{k+1}} - \frac{1}{x_k} \right).
\]
This summation by parts is correct, but let's use the simpler version derived in thought:
$T_N = \frac{J_0-J_1}{x_1} + \frac{J_1-J_2}{x_2} + \dots + \frac{J_N-J_{N+1}}{x_{N+1}}$
$T_N = \frac{J_0}{x_1} + J_1(\frac{1}{x_2}-\frac{1}{x_1}) + \dots + J_N(\frac{1}{x_{N+1}}-\frac{1}{x_N}) - \frac{J_{N+1}}{x_{N+1}}$
$T_N = \frac{J_0}{x_1} + \sum_{k=1}^N J_k \left( \frac{1}{x_{k+1}} - \frac{1}{x_k} \right) - \frac{J_{N+1}}{x_{N+1}}$.
Since $f$ is decreasing, $J_k = \int_{k\alpha}^{(k+1)\alpha} f(y) dy \ge \alpha f((k+1)\alpha) = \alpha x_{k+1}$.
Also, $x_k > x_{k+1} > 0$, so $\frac{1}{x_{k+1}} - \frac{1}{x_k} = \frac{x_k-x_{k+1}}{x_k x_{k+1}} > 0$.
\[
T_N \ge \frac{J_0}{x_1} + \sum_{k=1}^N \alpha x_{k+1} \left( \frac{x_k-x_{k+1}}{x_k x_{k+1}} \right) - \frac{J_{N+1}}{x_{N+1}}
\]
\[
T_N \ge \frac{J_0}{x_1} + \alpha \sum_{k=1}^N \frac{x_k-x_{k+1}}{x_k} - \frac{J_{N+1}}{x_{N+1}} = \frac{J_0}{x_1} + \alpha \sum_{k=1}^N \left( 1 - \frac{x_{k+1}}{x_k} \right) - \frac{J_{N+1}}{x_{N+1}}.
\]
Now we need bounds for the last term. $J_{N+1} = \int_{(N+1)\alpha}^{(N+2)\alpha} f(y) dy \le \alpha f((N+1)\alpha) = \alpha x_{N+1}$.
So $\frac{J_{N+1}}{x_{N+1}} \le \alpha$.
\[
T_N \ge \frac{J_0}{x_1} - \alpha + \alpha \sum_{k=1}^N \left( 1 - \frac{x_{k+1}}{x_k} \right).
\]
We need to show that the sum $\sum_{k=1}^\infty (1 - \frac{x_{k+1}}{x_k})$ diverges.
Let $y_k = x_k/x_{k-1}$ for $k\ge 1$. Since $f$ is strictly decreasing, $0 < x_k < x_{k-1}$, so $0 < y_k < 1$.
We have $x_N = x_0 y_1 y_2 \dots y_N$.
Since $\lim_{N\to\infty} f(N\alpha) = 0$, we have $\lim_{N\to\infty} x_N = 0$.
This means the product $\prod_{k=1}^\infty y_k = \lim_{N\to\infty} \frac{x_N}{x_0} = 0$.
A known result states that for a sequence $(y_k)$ with $0 < y_k < 1$, the product $\prod_{k=1}^\infty y_k$ converges to a non-zero limit if and only if the sum $\sum_{k=1}^\infty (1-y_k)$ converges.
Since $\prod y_k = 0$, the sum $\sum_{k=1}^\infty (1-y_k)$ must diverge.
The sum in the lower bound for $T_N$ is $\sum_{k=1}^N (1 - x_{k+1}/x_k) = \sum_{k=1}^N (1-y_{k+1})$. Let $j=k+1$. This is $\sum_{j=2}^{N+1} (1-y_j)$.
Since $\sum_{j=1}^\infty (1-y_j)$ diverges, and the terms are positive, the tail sum $\sum_{j=2}^\infty (1-y_j)$ also diverges.
Therefore, $\lim_{N\to\infty} \sum_{k=1}^N (1 - x_{k+1}/x_k) = \infty$.
This implies $\lim_{N\to\infty} T_N = \infty$.
Since $S_N \ge T_N$, we must have $\lim_{N\to\infty} S_N = \infty$.
So the series $\sum a_k$ diverges, which means the integral $I_1 = \int_0^\infty \frac{f(y)-f(y+\alpha)}{f(y+\alpha)} dy$ diverges to $\infty$.
Since $I > 2I_1 - C$ (or rather $I \ge C+2I_1'$ and $I_1 = C+I_1'$, so $I_1'=\infty$), we conclude that $I$ diverges to $\infty$.

Final check: The argument relies on $f$ being strictly decreasing and $\lim_{x\to\infty} f(x)=0$. Continuity is used to define the integrals $J_k$. $f(x)>0$ is derived from these conditions. The argument about the divergence of $\sum(1-y_k)$ is standard. All steps seem correct.

\[
\boxed{\int_\alpha^\infty \frac{f(x-\alpha)-f(x+\alpha)}{f(x)}dx= \infty}
\]