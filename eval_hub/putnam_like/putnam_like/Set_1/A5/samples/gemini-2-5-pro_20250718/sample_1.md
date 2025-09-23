Here is a detailed, step-by-step solution to the problem.

### **Problem Statement**
Find the limit
$$ L = \lim_{n\to\infty} \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right). $$

### **Method 1: Approximation using Taylor Series**

**Step 1: Analyze the argument of the sine function**

Let the argument of the sine function be denoted by $x_{n,k}$:
$$ x_{n,k} = \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} $$
The summation is over $k$ from $1$ to $n$. Let's determine the range of values for the term $n+2k-1$:
- For $k=1$, the term is $n+2(1)-1 = n+1$.
- For $k=n$, the term is $n+2(n)-1 = 3n-1$.

So, for $1 \le k \le n$, we have $n+1 \le n+2k-1 \le 3n-1$.
This allows us to bound the argument $x_{n,k}$:
$$ \frac{\pi}{2} \cdot \frac{n+1}{n(n-1)} \le x_{n,k} \le \frac{\pi}{2} \cdot \frac{3n-1}{n(n-1)} $$
As $n \to \infty$, the lower bound behaves like $\frac{\pi}{2} \cdot \frac{n}{n^2} = \frac{\pi}{2n}$, which goes to 0.
The upper bound behaves like $\frac{\pi}{2} \cdot \frac{3n}{n^2} = \frac{3\pi}{2n}$, which also goes to 0.
By the Squeeze Theorem, $\lim_{n\to\infty} x_{n,k} = 0$ for all $k \in \{1, 2, \dots, n\}$.

**Step 2: Use the small-angle approximation for sine**

Since the argument $x_{n,k}$ tends to zero, we can use the Taylor series expansion for $\sin(x)$ around $x=0$:
$$ \sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots $$
For small $x$, we have the approximation $\sin(x) \approx x$. We will first compute the limit of the sum by replacing $\sin(x_{n,k})$ with $x_{n,k}$, and then we will rigorously justify that the error term vanishes.

Let's define a new sum, $S_n$:
$$ S_n = \sum_{k=1}^n x_{n,k} = \sum_{k=1}^n \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} $$

**Step 3: Evaluate the limit of the approximated sum $S_n$**

We can factor out the terms that do not depend on $k$:
$$ S_n = \frac{\pi}{2n(n-1)} \sum_{k=1}^n (n+2k-1) $$
Now, let's evaluate the sum:
$$ \sum_{k=1}^n (n+2k-1) = \sum_{k=1}^n (n-1) + \sum_{k=1}^n 2k $$
The first part is the sum of a constant:
$$ \sum_{k=1}^n (n-1) = n(n-1) $$
The second part is the sum of an arithmetic progression:
$$ \sum_{k=1}^n 2k = 2 \sum_{k=1}^n k = 2 \cdot \frac{n(n+1)}{2} = n(n+1) $$
Combining these results:
$$ \sum_{k=1}^n (n+2k-1) = n(n-1) + n(n+1) = n^2 - n + n^2 + n = 2n^2 $$
Now substitute this back into the expression for $S_n$:
$$ S_n = \frac{\pi}{2n(n-1)} \cdot (2n^2) = \frac{2\pi n^2}{2n^2 - 2n} $$
Finally, we take the limit as $n \to \infty$:
$$ \lim_{n\to\infty} S_n = \lim_{n\to\infty} \frac{2\pi n^2}{2n^2 - 2n} = \lim_{n\to\infty} \frac{2\pi}{2 - \frac{2}{n}} = \frac{2\pi}{2-0} = \pi $$

**Step 4: Justify the approximation by analyzing the error term**

Let $L_n$ be the original sum. The error in our approximation is the difference between the original sum and $S_n$:
$$ E_n = \left| L_n - S_n \right| = \left| \sum_{k=1}^n \sin(x_{n,k}) - \sum_{k=1}^n x_{n,k} \right| = \left| \sum_{k=1}^n (\sin(x_{n,k}) - x_{n,k}) \right| $$
Using the triangle inequality:
$$ E_n \le \sum_{k=1}^n \left| \sin(x_{n,k}) - x_{n,k} \right| $$
From the Taylor expansion of $\sin(x)$, we know that for any $x$, there exists a $c$ between $0$ and $x$ such that $\sin(x) = x - \frac{\cos(c)}{6}x^3$. Therefore,
$$ |\sin(x) - x| = \left| -\frac{\cos(c)}{6}x^3 \right| \le \frac{1}{6}|x|^3 $$
Applying this to our sum:
$$ E_n \le \sum_{k=1}^n \frac{1}{6} |x_{n,k}|^3 $$
From Step 1, we have an upper bound for $|x_{n,k}|$:
$$ |x_{n,k}| \le \frac{\pi}{2} \cdot \frac{3n-1}{n(n-1)} $$
Let's call this upper bound $M_n$. As $n \to \infty$, $M_n \sim \frac{3\pi}{2n}$, so $M_n$ is of order $O(1/n)$.
The error sum is bounded by:
$$ E_n \le \sum_{k=1}^n \frac{1}{6} M_n^3 = n \cdot \frac{1}{6} M_n^3 = \frac{n}{6} \left( \frac{\pi}{2} \cdot \frac{3n-1}{n(n-1)} \right)^3 $$
$$ E_n \le \frac{n}{6} \cdot \frac{\pi^3}{8} \cdot \frac{(3n-1)^3}{n^3(n-1)^3} = \frac{\pi^3}{48} \cdot \frac{n(3n-1)^3}{n^3(n-1)^3} $$
Let's analyze the limit of this upper bound as $n \to \infty$:
$$ \lim_{n\to\infty} \frac{n(3n-1)^3}{n^3(n-1)^3} = \lim_{n\to\infty} \frac{n \cdot n^3(3-1/n)^3}{n^3 \cdot n^3(1-1/n)^3} = \lim_{n\to\infty} \frac{n^4(3-1/n)^3}{n^6(1-1/n)^3} = \lim_{n\to\infty} \frac{1}{n^2} \frac{(3-1/n)^3}{(1-1/n)^3} $$
This limit is $0 \cdot \frac{3^3}{1^3} = 0$.
Since the upper bound of the error $E_n$ goes to 0, we have $\lim_{n\to\infty} E_n = 0$.
This means $\lim_{n\to\infty} |L_n - S_n| = 0$, which implies $\lim_{n\to\infty} L_n = \lim_{n\to\infty} S_n$.
We have already calculated that $\lim_{n\to\infty} S_n = \pi$.

### **Method 2: Using the Formula for Sum of Sines in Arithmetic Progression**

**Step 1: Identify the arithmetic progression**

The arguments of the sine terms are $x_{n,k} = \frac{\pi}{2} \cdot \frac{n-1+2k}{n(n-1)}$.
Let's rewrite this as:
$$ x_{n,k} = \frac{\pi(n-1)}{2n(n-1)} + \frac{2\pi k}{2n(n-1)} = \frac{\pi}{2n} + k \cdot \frac{\pi}{n(n-1)} $$
This is an arithmetic progression in the variable $k$.
The sum is $\sum_{k=1}^n \sin(A+kd)$, where $A = \frac{\pi}{2n}$ and $d = \frac{\pi}{n(n-1)}$.

**Step 2: Apply the sum formula**

The formula for the sum of sines in an arithmetic progression is:
$$ \sum_{k=1}^n \sin(a+kd) = \frac{\sin(nd/2)}{\sin(d/2)} \sin\left(a + \frac{(n+1)d}{2}\right) $$
Let's calculate the components for our sum:
- $d = \frac{\pi}{n(n-1)}$
- $\frac{d}{2} = \frac{\pi}{2n(n-1)}$
- $\frac{nd}{2} = \frac{n\pi}{2n(n-1)} = \frac{\pi}{2(n-1)}$
- $a = \frac{\pi}{2n}$
- $a + \frac{(n+1)d}{2} = \frac{\pi}{2n} + \frac{(n+1)\pi}{2n(n-1)} = \frac{\pi}{2n} \left( 1 + \frac{n+1}{n-1} \right) = \frac{\pi}{2n} \left( \frac{n-1+n+1}{n-1} \right) = \frac{\pi}{2n} \frac{2n}{n-1} = \frac{\pi}{n-1}$

Substituting these into the formula, the sum $L_n$ is:
$$ L_n = \frac{\sin\left(\frac{\pi}{2(n-1)}\right)}{\sin\left(\frac{\pi}{2n(n-1)}\right)} \sin\left(\frac{\pi}{n-1}\right) $$

**Step 3: Evaluate the limit**

We need to find $\lim_{n\to\infty} L_n$. As $n\to\infty$, the arguments of all the sine functions tend to 0. We can use the limit $\lim_{u\to 0} \frac{\sin(u)}{u} = 1$.
$$ L = \lim_{n\to\infty} \left[ \frac{\sin\left(\frac{\pi}{2(n-1)}\right)}{\frac{\pi}{2(n-1)}} \cdot \frac{\frac{\pi}{2n(n-1)}}{\sin\left(\frac{\pi}{2n(n-1)}\right)} \cdot \frac{\frac{\pi}{2(n-1)}}{\frac{\pi}{2n(n-1)}} \cdot \sin\left(\frac{\pi}{n-1}\right) \right] $$
Let's group the terms:
$$ L = \lim_{n\to\infty} \underbrace{\left[ \frac{\sin\left(\frac{\pi}{2(n-1)}\right)}{\frac{\pi}{2(n-1)}} \right]}_{\to 1} \cdot \underbrace{\left[ \frac{\frac{\pi}{2n(n-1)}}{\sin\left(\frac{\pi}{2n(n-1)}\right)} \right]}_{\to 1} \cdot \left[ \frac{\frac{\pi}{2(n-1)}}{\frac{\pi}{2n(n-1)}} \cdot \sin\left(\frac{\pi}{n-1}\right) \right] $$
The limit simplifies to:
$$ L = \lim_{n\to\infty} \left[ \frac{\frac{\pi}{2(n-1)}}{\frac{\pi}{2n(n-1)}} \cdot \sin\left(\frac{\pi}{n-1}\right) \right] $$
Simplify the fraction:
$$ \frac{\frac{\pi}{2(n-1)}}{\frac{\pi}{2n(n-1)}} = \frac{\pi}{2(n-1)} \cdot \frac{2n(n-1)}{\pi} = n $$
So the expression becomes:
$$ L = \lim_{n\to\infty} n \cdot \sin\left(\frac{\pi}{n-1}\right) $$
Let $m = n-1$. As $n\to\infty$, $m\to\infty$ and $n=m+1$.
$$ L = \lim_{m\to\infty} (m+1) \sin\left(\frac{\pi}{m}\right) = \lim_{m\to\infty} \left( m\sin\left(\frac{\pi}{m}\right) + \sin\left(\frac{\pi}{m}\right) \right) $$
We evaluate the two parts of the limit:
$$ \lim_{m\to\infty} m\sin\left(\frac{\pi}{m}\right) = \lim_{m\to\infty} \pi \frac{\sin(\pi/m)}{\pi/m} $$
Let $u = \pi/m$. As $m \to \infty$, $u \to 0$.
$$ \lim_{u\to 0} \pi \frac{\sin(u)}{u} = \pi \cdot 1 = \pi $$
The second part is:
$$ \lim_{m\to\infty} \sin\left(\frac{\pi}{m}\right) = \sin(0) = 0 $$
Therefore,
$$ L = \pi + 0 = \pi $$

Both methods yield the same result.

### **Conclusion**

The limit of the given sum is $\pi$.

$$ \lim_{n\to\infty} \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right) = \pi $$