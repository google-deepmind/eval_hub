Let the limit be $L$. We want to compute
\[
L = \lim\limits_{n\to\infty} \frac{1}{n^2}\sum\limits_{k=1}^n\sum\limits_{l=1}^k e^{l/k}.
\]
Let $A_k = \sum\limits_{l=1}^k e^{l/k}$. The expression can be written as $L = \lim\limits_{n\to\infty} \frac{1}{n^2}\sum\limits_{k=1}^n A_k$.

The inner sum $A_k$ is a finite geometric series:
\[
A_k = e^{1/k} + e^{2/k} + \dots + e^{k/k}.
\]
This series has the first term $a = e^{1/k}$, the common ratio $r = e^{1/k}$, and $k$ terms.
The sum of a geometric series is given by $a \frac{r^k - 1}{r - 1}$.
So,
\[
A_k = e^{1/k} \frac{(e^{1/k})^k - 1}{e^{1/k} - 1} = e^{1/k} \frac{e^{k/k} - 1}{e^{1/k} - 1} = e^{1/k} \frac{e^1 - 1}{e^{1/k} - 1} = (e-1) \frac{e^{1/k}}{e^{1/k} - 1}.
\]
Now we need to compute the limit
\[
L = \lim_{n\to\infty} \frac{1}{n^2}\sum_{k=1}^n (e-1) \frac{e^{1/k}}{e^{1/k} - 1}.
\]
Let $S_n = \sum_{k=1}^n A_k = \sum_{k=1}^n (e-1) \frac{e^{1/k}}{e^{1/k} - 1}$. We want to compute $L = \lim_{n\to\infty} \frac{S_n}{n^2}$.
We can use the Cesaro-Stolz theorem. Let $x_n = S_n$ and $y_n = n^2$. Since $y_n = n^2$ is strictly increasing and $y_n \to \infty$ as $n \to \infty$, the theorem states that if the limit $\lim_{n\to\infty} \frac{x_n - x_{n-1}}{y_n - y_{n-1}}$ exists, then $\lim_{n\to\infty} \frac{x_n}{y_n}$ exists and is equal to it.

We compute the difference $x_n - x_{n-1}$:
\[
x_n - x_{n-1} = S_n - S_{n-1} = A_n = (e-1) \frac{e^{1/n}}{e^{1/n} - 1}.
\]
We compute the difference $y_n - y_{n-1}$:
\[
y_n - y_{n-1} = n^2 - (n-1)^2 = n^2 - (n^2 - 2n + 1) = 2n - 1.
\]
Now we compute the limit of the ratio:
\[
L = \lim_{n\to\infty} \frac{A_n}{2n - 1} = \lim_{n\to\infty} \frac{(e-1) \frac{e^{1/n}}{e^{1/n} - 1}}{2n - 1} = (e-1) \lim_{n\to\infty} \frac{e^{1/n}}{(e^{1/n} - 1)(2n - 1)}.
\]
To evaluate this limit, let $t = 1/n$. As $n \to \infty$, $t \to 0$. Also $n = 1/t$, so $2n - 1 = 2/t - 1 = (2-t)/t$.
Substituting $t$ into the expression:
\[
L = (e-1) \lim_{t\to 0} \frac{e^t}{(e^t - 1) \frac{2-t}{t}} = (e-1) \lim_{t\to 0} \frac{t e^t}{(e^t - 1)(2-t)}.
\]
We can separate the limit into factors whose limits are known:
\[
L = (e-1) \left( \lim_{t\to 0} \frac{t}{e^t - 1} \right) \left( \lim_{t\to 0} \frac{e^t}{2-t} \right).
\]
Using the fundamental limit $\lim_{t\to 0} \frac{e^t - 1}{t} = 1$, we have $\lim_{t\to 0} \frac{t}{e^t - 1} = 1$.
For the second factor, we substitute $t=0$:
\[
\lim_{t\to 0} \frac{e^t}{2-t} = \frac{e^0}{2-0} = \frac{1}{2}.
\]
Substituting these values back into the expression for $L$:
\[
L = (e-1) \cdot 1 \cdot \frac{1}{2} = \frac{e-1}{2}.
\]

Thus, the limit is $\frac{e-1}{2}$.

Final Answer: The final answer is $\boxed{\frac{e-1}{2}}$