Let the given limit be $L$. The sum is $S_n = \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right)$.
The argument of the sine function is $x_{n,k} = \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)}$.
We are considering the limit as $n \to \infty$. For the sum to be defined, we must have $n(n-1) \neq 0$, so $n \neq 0, 1$. Thus, we consider $n \ge 2$.

For $n \ge 2$ and $1 \le k \le n$, we have $n+2(1)-1 \le n+2k-1 \le n+2n-1$, which simplifies to $n+1 \le n+2k-1 \le 3n-1$.
The denominator is $n(n-1)$. For $n \ge 2$, $n(n-1) > 0$.
So, the argument $x_{n,k}$ is bounded as follows:
$\frac{\pi}{2} \cdot \frac{n+1}{n(n-1)} \le x_{n,k} \le \frac{\pi}{2} \cdot \frac{3n-1}{n(n-1)}$.
As $n \to \infty$, $\frac{n+1}{n(n-1)} \sim \frac{n}{n^2} = \frac{1}{n}$ and $\frac{3n-1}{n(n-1)} \sim \frac{3n}{n^2} = \frac{3}{n}$.
Thus, $x_{n,k} \to 0$ as $n \to \infty$ for all $k \in \{1, \dots, n\}$.
More formally, for $n \ge 2$, $n-1 \ge n/2$. So $n(n-1) \ge n^2/2$.
Thus $\frac{1}{n(n-1)} \le \frac{2}{n^2}$ for $n \ge 2$.
$x_{n,k} \le \frac{\pi}{2} \cdot \frac{3n-1}{n(n-1)} \le \frac{\pi}{2} \cdot \frac{3n}{n(n-1)} = \frac{\pi}{2} \frac{3}{n-1}$.
As $n \to \infty$, $\frac{3\pi}{2(n-1)} \to 0$. So $x_{n,k} \to 0$ uniformly for $k \in \{1, \dots, n\}$.

Since $x_{n,k} \to 0$, we can use the Taylor expansion of $\sin(x)$ around $x=0$, which is $\sin(x) = x - \frac{x^3}{6} + O(x^5)$.
So, $\sin(x_{n,k}) = x_{n,k} - \frac{x_{n,k}^3}{6} + O(x_{n,k}^5)$.
The sum becomes $S_n = \sum_{k=1}^n \left( x_{n,k} - \frac{x_{n,k}^3}{6} + O(x_{n,k}^5) \right) = \sum_{k=1}^n x_{n,k} - \frac{1}{6}\sum_{k=1}^n x_{n,k}^3 + \sum_{k=1}^n O(x_{n,k}^5)$.

Let's evaluate the first part, $\sum_{k=1}^n x_{n,k}$:
$$ \sum_{k=1}^n x_{n,k} = \sum_{k=1}^n \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} = \frac{\pi}{2n(n-1)} \sum_{k=1}^n (n+2k-1) $$
The sum $\sum_{k=1}^n (n+2k-1)$ can be split into two parts:
$$ \sum_{k=1}^n (n+2k-1) = \sum_{k=1}^n (n-1) + \sum_{k=1}^n 2k $$
The first part is a sum of $n$ terms, each equal to $n-1$: $\sum_{k=1}^n (n-1) = n(n-1)$.
The second part is $2$ times the sum of the first $n$ integers: $\sum_{k=1}^n 2k = 2 \sum_{k=1}^n k = 2 \frac{n(n+1)}{2} = n(n+1)$.
So, $\sum_{k=1}^n (n+2k-1) = n(n-1) + n(n+1) = n^2 - n + n^2 + n = 2n^2$.

Substituting this back into the sum of $x_{n,k}$:
$$ \sum_{k=1}^n x_{n,k} = \frac{\pi}{2n(n-1)} (2n^2) = \frac{\pi n^2}{n(n-1)} = \frac{\pi n}{n-1} $$
As $n \to \infty$, $\lim_{n\to\infty} \frac{\pi n}{n-1} = \lim_{n\to\infty} \frac{\pi}{1-1/n} = \pi$.

Now consider the error terms. We need to evaluate $\lim_{n\to\infty} \left( -\frac{1}{6}\sum_{k=1}^n x_{n,k}^3 + \sum_{k=1}^n O(x_{n,k}^5) \right)$.
We established that $x_{n,k} \le \frac{\pi}{2} \frac{3n-1}{n(n-1)}$. For $n \ge 2$, $n(n-1) \ge n^2/2$.
So $x_{n,k} \le \frac{\pi}{2} \frac{3n}{n^2/2} = \frac{3\pi n}{n^2} = \frac{3\pi}{n}$ for $n \ge 2$.
Thus, $x_{n,k} = O(1/n)$ uniformly for $k \in \{1, \dots, n\}$.

The second term is $-\frac{1}{6}\sum_{k=1}^n x_{n,k}^3$. Since $x_{n,k} = O(1/n)$, $x_{n,k}^3 = O(1/n^3)$.
The sum has $n$ terms, each of order $1/n^3$. So the sum is of order $n \cdot O(1/n^3) = O(1/n^2)$.
$$ \left| \sum_{k=1}^n x_{n,k}^3 \right| \le \sum_{k=1}^n |x_{n,k}|^3 \le \sum_{k=1}^n \left(\frac{3\pi}{n}\right)^3 = \sum_{k=1}^n \frac{27\pi^3}{n^3} = n \cdot \frac{27\pi^3}{n^3} = \frac{27\pi^3}{n^2} $$
As $n \to \infty$, $\frac{27\pi^3}{n^2} \to 0$. So $\lim_{n\to\infty} \sum_{k=1}^n x_{n,k}^3 = 0$.
The term $-\frac{1}{6}\sum_{k=1}^n x_{n,k}^3$ goes to 0.

The third term is $\sum_{k=1}^n O(x_{n,k}^5)$.
$x_{n,k}^5 = O(1/n^5)$.
The sum has $n$ terms, each of order $1/n^5$. So the sum is of order $n \cdot O(1/n^5) = O(1/n^4)$.
This term also goes to 0 as $n \to \infty$.

So, the limit of $S_n$ is the limit of the first part:
$$ \lim_{n\to\infty} S_n = \lim_{n\to\infty} \sum_{k=1}^n x_{n,k} = \pi $$

Alternatively, we could use the approximation $\sin x = x + (\sin x - x)$.
$S_n = \sum_{k=1}^n x_{n,k} + \sum_{k=1}^n (\sin(x_{n,k}) - x_{n,k})$.
We know $\sum x_{n,k} \to \pi$.
The error term is $E_n = \sum_{k=1}^n (\sin(x_{n,k}) - x_{n,k})$.
Using the inequality $|\sin x - x| \le \frac{|x|^3}{6}$ for all real $x$:
$|E_n| \le \sum_{k=1}^n |\sin(x_{n,k}) - x_{n,k}| \le \sum_{k=1}^n \frac{|x_{n,k}|^3}{6}$.
Using the bound $|x_{n,k}| \le \frac{3\pi}{n}$ for $n \ge 2$:
$|E_n| \le \sum_{k=1}^n \frac{1}{6} \left(\frac{3\pi}{n}\right)^3 = \sum_{k=1}^n \frac{27\pi^3}{6n^3} = n \cdot \frac{27\pi^3}{6n^3} = \frac{27\pi^3}{6n^2}$.
As $n \to \infty$, $\frac{27\pi^3}{6n^2} \to 0$. Thus, $\lim_{n\to\infty} E_n = 0$.
Therefore, $\lim_{n\to\infty} S_n = \lim_{n\to\infty} \sum_{k=1}^n x_{n,k} + \lim_{n\to\infty} E_n = \pi + 0 = \pi$.

The final answer is $\boxed{\pi}$.