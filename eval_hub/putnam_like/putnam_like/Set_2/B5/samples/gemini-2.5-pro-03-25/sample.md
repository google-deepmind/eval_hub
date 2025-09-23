Let $L_n$ be the left hand side and $R_n$ be the right hand side of the equation.
We have
$$L_n = \sum_{k=0}^n \binom{n}{k}\frac{(-1)^k}{(k+1)^3}$$
$$R_n = \frac{1}{n+1}\sum_{k=0}^n\sum_{j=0}^k\frac{1}{k+1}\cdot \frac{1}{j+1}$$

First, let's simplify $L_n$. We use the identity $\frac{1}{k+1}\binom{n}{k} = \frac{1}{n+1}\binom{n+1}{k+1}$.
\begin{align*} L_n &= \sum_{k=0}^n \frac{1}{k+1}\binom{n}{k}\frac{(-1)^k}{(k+1)^2} \\ &= \sum_{k=0}^n \frac{1}{n+1}\binom{n+1}{k+1}\frac{(-1)^k}{(k+1)^2} \\ &= \frac{1}{n+1} \sum_{k=0}^n \binom{n+1}{k+1}\frac{(-1)^k}{(k+1)^2}\end{align*}
Let $j=k+1$. When $k=0$, $j=1$. When $k=n$, $j=n+1$. $(-1)^k = (-1)^{j-1}$.
$$L_n = \frac{1}{n+1} \sum_{j=1}^{n+1} \binom{n+1}{j}\frac{(-1)^{j-1}}{j^2}$$

Next, let's simplify $R_n$. Let $H_m = \sum_{i=1}^m \frac{1}{i}$ denote the $m$-th harmonic number.
The inner sum is $\sum_{j=0}^k \frac{1}{j+1} = \sum_{i=1}^{k+1} \frac{1}{i} = H_{k+1}$.
$$R_n = \frac{1}{n+1}\sum_{k=0}^n \frac{H_{k+1}}{k+1}$$
Let $j=k+1$. When $k=0$, $j=1$. When $k=n$, $j=n+1$.
$$R_n = \frac{1}{n+1}\sum_{j=1}^{n+1} \frac{H_j}{j}$$

Let $m=n+1$. The identity we need to prove is equivalent to
$$ \sum_{j=1}^{m} \binom{m}{j}\frac{(-1)^{j-1}}{j^2} = \sum_{j=1}^{m} \frac{H_j}{j} $$
for all integers $m \geq 1$.
Let $f(m) = \sum_{j=1}^{m} \binom{m}{j}\frac{(-1)^{j-1}}{j^2}$ and $g(m) = \sum_{j=1}^{m} \frac{H_j}{j}$. We want to prove $f(m)=g(m)$.

We can prove the identity $f(m)=g(m)$ using generating functions or finite differences (induction). Let's try another approach using integral representations.
We use the identity $\frac{1}{k^2} = \int_0^1 (-\ln x) x^{k-1} dx$.
\begin{align*} f(m) &= \sum_{k=1}^m \binom{m}{k} (-1)^{k-1} \int_0^1 (-\ln x) x^{k-1} dx \\ &= \int_0^1 (-\ln x) \sum_{k=1}^m \binom{m}{k} (-1)^{k-1} x^{k-1} dx \\ &= \int_0^1 (-\ln x) \frac{1}{x} \sum_{k=1}^m \binom{m}{k} (-x)^k dx \end{align*}
Using the binomial theorem, $\sum_{k=0}^m \binom{m}{k} (-x)^k = (1-x)^m$. So $\sum_{k=1}^m \binom{m}{k} (-x)^k = (1-x)^m - \binom{m}{0}(-x)^0 = (1-x)^m - 1$.
\begin{align*} f(m) &= \int_0^1 (-\ln x) \frac{(1-x)^m - 1}{x} dx \\ &= \int_0^1 \frac{1-(1-x)^m}{x} (-\ln x) dx \end{align*}
Now make the substitution $u=1-x$. Then $x=1-u$ and $dx=-du$.
\begin{align*} f(m) &= \int_1^0 \frac{1-u^m}{1-u} (-\ln(1-u)) (-du) \\ &= \int_0^1 \frac{1-u^m}{1-u} (-\ln(1-u)) du \end{align*}
Since $\frac{1-u^m}{1-u} = \sum_{k=0}^{m-1} u^k$, we have
$$ f(m) = \int_0^1 \left(\sum_{k=0}^{m-1} u^k\right) (-\ln(1-u)) du = \sum_{k=0}^{m-1} \int_0^1 u^k (-\ln(1-u)) du $$
Now we need to evaluate the integral $I_k = \int_0^1 u^k (-\ln(1-u)) du$.
We use the Taylor series expansion $-\ln(1-u) = \sum_{j=1}^\infty \frac{u^j}{j}$ for $|u|<1$.
\begin{align*} I_k &= \int_0^1 u^k \left(\sum_{j=1}^\infty \frac{u^j}{j}\right) du \\ &= \sum_{j=1}^\infty \frac{1}{j} \int_0^1 u^{k+j} du \\ &= \sum_{j=1}^\infty \frac{1}{j(k+j+1)} \end{align*}
Using partial fraction decomposition $\frac{1}{j(k+j+1)} = \frac{1}{k+1} \left(\frac{1}{j} - \frac{1}{j+k+1}\right)$.
$$ I_k = \frac{1}{k+1} \sum_{j=1}^\infty \left(\frac{1}{j} - \frac{1}{j+k+1}\right) $$
This is a telescoping series sum. Let $S_N = \sum_{j=1}^N \left(\frac{1}{j} - \frac{1}{j+k+1}\right)$.
\begin{align*} S_N &= \sum_{j=1}^N \frac{1}{j} - \sum_{j=1}^N \frac{1}{j+k+1} \\ &= \sum_{j=1}^N \frac{1}{j} - \sum_{l=k+2}^{N+k+1} \frac{1}{l} \\ &= \left( \sum_{j=1}^{k+1} \frac{1}{j} + \sum_{j=k+2}^N \frac{1}{j} \right) - \left( \sum_{l=k+2}^N \frac{1}{l} + \sum_{l=N+1}^{N+k+1} \frac{1}{l} \right) \\ &= H_{k+1} - \sum_{l=N+1}^{N+k+1} \frac{1}{l} \end{align*}
As $N \to \infty$, $\sum_{l=N+1}^{N+k+1} \frac{1}{l} \to 0$. Thus, the sum is $H_{k+1}$.
$$ I_k = \frac{H_{k+1}}{k+1} $$
Substituting this back into the expression for $f(m)$:
$$ f(m) = \sum_{k=0}^{m-1} I_k = \sum_{k=0}^{m-1} \frac{H_{k+1}}{k+1} $$
Let $j=k+1$. When $k=0$, $j=1$. When $k=m-1$, $j=m$.
$$ f(m) = \sum_{j=1}^m \frac{H_j}{j} = g(m) $$
We have shown that $f(m)=g(m)$ for all $m \geq 1$.
Since $L_n = \frac{1}{n+1} f(n+1)$ and $R_n = \frac{1}{n+1} g(n+1)$, we have $L_n=R_n$ for all $n \geq 0$.

Final Answer: The final answer is $\boxed{\sum_{k=0}^n \binom{n}{k}\frac{(-1)^k}{(k+1)^3}=\frac{1}{n+1}\sum_{k=0}^n\sum_{j=0}^k\frac{1}{k+1}\cdot \frac{1}{j+1}}$