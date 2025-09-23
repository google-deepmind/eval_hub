Let $S_n$ be the sum we want to evaluate the limit of:
$$ S_n = \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right). $$
Let $x_{n,k} = \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)}$. We can rewrite this as:
$$ x_{n,k} = \frac{\pi}{2n(n-1)} (n+2k-1). $$
Let's analyze the structure of these terms for $k=1, 2, \dots, n$.
$$ x_{n,k} = \frac{\pi}{2n(n-1)} ((n-1) + 2k). $$
Let $C = \frac{\pi}{2n(n-1)}$. Then $x_{n,k} = C(n-1+2k)$.
Let's write $x_{n,k}$ in the form $a + (k-1)d$ to see if it's an arithmetic progression.
$x_{n,1} = C(n-1+2) = C(n+1)$.
$x_{n,2} = C(n-1+4) = C(n+3)$.
$x_{n,3} = C(n-1+6) = C(n+5)$.
The difference between consecutive terms is $x_{n,k+1} - x_{n,k} = C(n-1+2(k+1)) - C(n-1+2k) = C(n-1+2k+2) - C(n-1+2k) = 2C$.
So the terms $x_{n,k}$ form an arithmetic progression with first term $a = x_{n,1} = \frac{\pi(n+1)}{2n(n-1)}$ and common difference $d = 2C = \frac{2\pi}{2n(n-1)} = \frac{\pi}{n(n-1)}$.

We use the formula for the sum of sines in an arithmetic progression:
$$ \sum_{k=1}^n \sin(a + (k-1)d) = \frac{\sin(nd/2)}{\sin(d/2)} \sin(a + (n-1)d/2). $$
Let's calculate the terms needed for the formula:
$a = \frac{\pi(n+1)}{2n(n-1)}$.
$d = \frac{\pi}{n(n-1)}$.
$nd/2 = \frac{n}{2} \cdot \frac{\pi}{n(n-1)} = \frac{\pi}{2(n-1)}$.
$d/2 = \frac{\pi}{2n(n-1)}$.
$(n-1)d/2 = \frac{n-1}{2} \cdot \frac{\pi}{n(n-1)} = \frac{\pi}{2n}$.
$a + (n-1)d/2 = \frac{\pi(n+1)}{2n(n-1)} + \frac{\pi}{2n} = \frac{\pi}{2n} \left( \frac{n+1}{n-1} + 1 \right) = \frac{\pi}{2n} \left( \frac{n+1 + n-1}{n-1} \right) = \frac{\pi}{2n} \frac{2n}{n-1} = \frac{\pi}{n-1}$.

Substituting these into the sum formula:
$$ S_n = \frac{\sin\left(\frac{\pi}{2(n-1)}\right)}{\sin\left(\frac{\pi}{2n(n-1)}\right)} \sin\left(\frac{\pi}{n-1}\right). $$
Now we need to find the limit of $S_n$ as $n\to\infty$.
Let $x = \frac{\pi}{2(n-1)}$, $y = \frac{\pi}{2n(n-1)}$, and $z = \frac{\pi}{n-1}$. As $n\to\infty$, we have $x\to 0$, $y\to 0$, and $z\to 0$.
We can rewrite $S_n$ in terms of $x, y, z$:
$$ S_n = \frac{\sin x}{\sin y} \sin z. $$
To evaluate the limit, we use the standard limit $\lim_{\theta\to 0} \frac{\sin \theta}{\theta} = 1$.
$$ S_n = \frac{\sin x}{x} \cdot \frac{y}{\sin y} \cdot \frac{\sin z}{z} \cdot \frac{x \cdot z}{y}. $$
As $n\to\infty$:
$\lim_{n\to\infty} \frac{\sin x}{x} = 1$.
$\lim_{n\to\infty} \frac{y}{\sin y} = 1$.
$\lim_{n\to\infty} \frac{\sin z}{z} = 1$.
The remaining term is $\frac{x \cdot z}{y}$. Let's calculate this:
$$ \frac{x \cdot z}{y} = \frac{\frac{\pi}{2(n-1)} \cdot \frac{\pi}{n-1}}{\frac{\pi}{2n(n-1)}} = \frac{\frac{\pi^2}{2(n-1)^2}}{\frac{\pi}{2n(n-1)}} = \frac{\pi^2}{2(n-1)^2} \cdot \frac{2n(n-1)}{\pi} = \frac{\pi n}{n-1}. $$
The limit of this term is:
$$ \lim_{n\to\infty} \frac{\pi n}{n-1} = \lim_{n\to\infty} \frac{\pi}{1 - 1/n} = \pi. $$
Putting it all together:
$$ \lim_{n\to\infty} S_n = \left(\lim_{n\to\infty} \frac{\sin x}{x}\right) \left(\lim_{n\to\infty} \frac{y}{\sin y}\right) \left(\lim_{n\to\infty} \frac{\sin z}{z}\right) \left(\lim_{n\to\infty} \frac{x z}{y}\right). $$
$$ \lim_{n\to\infty} S_n = 1 \cdot 1 \cdot 1 \cdot \pi = \pi. $$

Alternative Method using Taylor Approximation:
For large $n$, the argument of the sine function $x_{n,k} = \frac{\pi}{2} \frac{n+2k-1}{n(n-1)}$ is small. The maximum value occurs at $k=n$, $x_{n,n} = \frac{\pi}{2} \frac{3n-1}{n(n-1)} \approx \frac{3\pi}{2n}$, which tends to 0 as $n\to\infty$.
Using the approximation $\sin x \approx x$ for small $x$.
$$ S_n \approx \sum_{k=1}^n x_{n,k} = \sum_{k=1}^n \frac{\pi}{2} \frac{n+2k-1}{n(n-1)}. $$
$$ \sum_{k=1}^n x_{n,k} = \frac{\pi}{2n(n-1)} \sum_{k=1}^n (n-1+2k). $$
The sum is $\sum_{k=1}^n (n-1) + \sum_{k=1}^n 2k = n(n-1) + 2 \frac{n(n+1)}{2} = n(n-1) + n(n+1) = n^2-n+n^2+n = 2n^2$.
$$ \sum_{k=1}^n x_{n,k} = \frac{\pi}{2n(n-1)} (2n^2) = \frac{\pi n^2}{n(n-1)} = \frac{\pi n}{n-1}. $$
The limit is $\lim_{n\to\infty} \frac{\pi n}{n-1} = \pi$.
This approximation can be justified using Taylor's theorem with remainder, $\sin x = x - \frac{x^3}{6} \cos(\xi)$ for some $\xi$ between 0 and $x$, or using bounds $x - x^3/6 < \sin x < x$ for $x>0$. The sum of the error terms $\sum \frac{x_{n,k}^3}{6}$ can be shown to tend to 0 as $n\to\infty$.

Final Result:
The limit is
$$ \lim_{n\to\infty} \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right) = \pi. $$

```markdown
Let the sum be denoted by $S_n$:
$$ S_n = \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right). $$
Let the argument of the sine function be $x_{n,k} = \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)}$. We can rewrite this as
$$ x_{n,k} = \frac{\pi}{2n(n-1)} (n-1+2k). $$
The terms $x_{n,k}$ for $k=1, 2, \dots, n$ form an arithmetic progression. Let's find the first term $a$ and the common difference $d$.
The first term is $a = x_{n,1} = \frac{\pi}{2n(n-1)} (n-1+2) = \frac{\pi(n+1)}{2n(n-1)}$.
The common difference is $d = x_{n,k+1} - x_{n,k} = \frac{\pi}{2n(n-1)} (n-1+2(k+1)) - \frac{\pi}{2n(n-1)} (n-1+2k) = \frac{\pi}{2n(n-1)} (2) = \frac{\pi}{n(n-1)}$.
We use the formula for the sum of sines in an arithmetic progression:
$$ \sum_{k=1}^n \sin(a + (k-1)d) = \frac{\sin(nd/2)}{\sin(d/2)} \sin(a + (n-1)d/2). $$
We compute the necessary components:
$$ nd/2 = \frac{n}{2} \cdot \frac{\pi}{n(n-1)} = \frac{\pi}{2(n-1)}. $$
$$ d/2 = \frac{\pi}{2n(n-1)}. $$
$$ a + (n-1)d/2 = \frac{\pi(n+1)}{2n(n-1)} + \frac{(n-1)}{2} \frac{\pi}{n(n-1)} = \frac{\pi(n+1)}{2n(n-1)} + \frac{\pi}{2n} = \frac{\pi}{2n} \left( \frac{n+1}{n-1} + 1 \right) = \frac{\pi}{2n} \left( \frac{n+1+n-1}{n-1} \right) = \frac{\pi}{2n} \frac{2n}{n-1} = \frac{\pi}{n-1}. $$
Substituting these into the sum formula gives $S_n$:
$$ S_n = \frac{\sin\left(\frac{\pi}{2(n-1)}\right)}{\sin\left(\frac{\pi}{2n(n-1)}\right)} \sin\left(\frac{\pi}{n-1}\right). $$
To find the limit as $n\to\infty$, we use the property $\lim_{x\to 0} \frac{\sin x}{x} = 1$.
Let $x = \frac{\pi}{2(n-1)}$, $y = \frac{\pi}{2n(n-1)}$, and $z = \frac{\pi}{n-1}$. As $n\to\infty$, $x, y, z \to 0$.
$$ S_n = \frac{\sin x}{x} \cdot \frac{y}{\sin y} \cdot \frac{\sin z}{z} \cdot \frac{x \cdot z}{y}. $$
The limit is
$$ \lim_{n\to\infty} S_n = \left(\lim_{n\to\infty} \frac{\sin x}{x}\right) \left(\lim_{n\to\infty} \frac{y}{\sin y}\right) \left(\lim_{n\to\infty} \frac{\sin z}{z}\right) \left(\lim_{n\to\infty} \frac{x z}{y}\right). $$
The first three limits are equal to 1. We compute the limit of the last term:
$$ \lim_{n\to\infty} \frac{x z}{y} = \lim_{n\to\infty} \frac{\frac{\pi}{2(n-1)} \cdot \frac{\pi}{n-1}}{\frac{\pi}{2n(n-1)}} = \lim_{n\to\infty} \frac{\frac{\pi^2}{2(n-1)^2}}{\frac{\pi}{2n(n-1)}} = \lim_{n\to\infty} \frac{\pi^2}{2(n-1)^2} \cdot \frac{2n(n-1)}{\pi} = \lim_{n\to\infty} \frac{\pi n}{n-1}. $$
$$ \lim_{n\to\infty} \frac{\pi n}{n-1} = \lim_{n\to\infty} \frac{\pi}{1 - 1/n} = \pi. $$
Therefore,
$$ \lim_{n\to\infty} S_n = 1 \cdot 1 \cdot 1 \cdot \pi = \pi. $$

Final Answer: The final answer is $\boxed{\pi}$
```