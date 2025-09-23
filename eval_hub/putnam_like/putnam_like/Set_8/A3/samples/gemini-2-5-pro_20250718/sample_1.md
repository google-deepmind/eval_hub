An expert solution to the mathematical problem is provided below.

### **Problem Statement**

Let $c$ be a positive constant. Consider a set $X$ of all sequences $(x_n)_{n=0}^\infty$ of positive reals such that $\sum_{n=0}^{\infty}x_n=c$. Describe the set
$$
Y = \left\{\sum_{n=0}^{\infty}x_n^3\;:\; (x_n)\in X\right\}.
$$

### **Solution**

The problem asks for the range of the function $S((x_n)) = \sum_{n=0}^{\infty}x_n^3$ where the domain is the set $X$ of all sequences of positive real numbers whose terms sum to $c$. We need to find the infimum and supremum of the set $Y$ and determine if these bounds are attained.

Let $S = \sum_{n=0}^{\infty}x_n^3$.

#### **Step 1: Finding the Supremum of Y**

We will show that the supremum of $Y$ is $c^3$ and that this value is not attained.

**1a. Establishing an Upper Bound**

Let $(x_n)$ be any sequence in $X$. By definition, $x_n > 0$ for all $n \ge 0$ and $\sum_{n=0}^{\infty}x_n=c$.
Since the series converges and all terms are positive, it must be that $x_n \to 0$ as $n \to \infty$. Also, for any given $n$, the sum of the other terms is positive, so $x_n = c - \sum_{k \ne n} x_k < c$.
Thus, for every $n \ge 0$, we have $0 < x_n < c$.

This implies $x_n^2 < c^2$. We can write $x_n^3$ as $x_n \cdot x_n^2$.
So, for each term, we have:
$x_n^3 = x_n \cdot x_n^2 < x_n \cdot c^2$.

Summing over all $n$:
$$S = \sum_{n=0}^{\infty}x_n^3 < \sum_{n=0}^{\infty} (c^2 x_n)$$
The inequality is strict because $x_n > 0$ for all $n$.
Factoring out the constant $c^2$:
$$S < c^2 \sum_{n=0}^{\infty}x_n$$
Since $(x_n) \in X$, we know $\sum_{n=0}^{\infty}x_n = c$. Substituting this in:
$$S < c^2 \cdot c = c^3$$
This shows that $c^3$ is a strict upper bound for the set $Y$. This also implies that the supremum cannot be attained; there is no sequence in $X$ for which the sum of cubes is equal to $c^3$.

**1b. Showing the Supremum is $c^3$**

To show that $c^3$ is the least upper bound (supremum), we must demonstrate that we can find sequences in $X$ for which the sum of cubes is arbitrarily close to $c^3$. We can do this by constructing a family of sequences where one term dominates the sum.

Consider the following family of sequences $(x_n^{(\delta)})$ parameterized by a small positive number $\delta \in (0, c)$:
Let
$$
x_0^{(\delta)} = c - \delta \\
x_n^{(\delta)} = \frac{\delta}{2^n} \quad \text{for } n \ge 1
$$
First, let's verify that this sequence is in $X$.
All terms are positive since $c > \delta > 0$.
The sum of the terms is:
$$ \sum_{n=0}^{\infty} x_n^{(\delta)} = (c-\delta) + \sum_{n=1}^{\infty} \frac{\delta}{2^n} = (c-\delta) + \delta \sum_{n=1}^{\infty} \left(\frac{1}{2}\right)^n $$
The geometric series $\sum_{n=1}^{\infty} (1/2)^n = \frac{1/2}{1-1/2} = 1$.
So, the sum is $(c-\delta) + \delta \cdot 1 = c$. Thus, $(x_n^{(\delta)}) \in X$ for any $\delta \in (0,c)$.

Now, let's compute the sum of the cubes, $S(\delta)$:
$$ S(\delta) = \sum_{n=0}^{\infty} (x_n^{(\delta)})^3 = (c-\delta)^3 + \sum_{n=1}^{\infty} \left(\frac{\delta}{2^n}\right)^3 = (c-\delta)^3 + \delta^3 \sum_{n=1}^{\infty} \left(\frac{1}{8}\right)^n $$
The geometric series $\sum_{n=1}^{\infty} (1/8)^n = \frac{1/8}{1-1/8} = \frac{1/8}{7/8} = \frac{1}{7}$.
So, the sum of cubes is:
$$ S(\delta) = (c-\delta)^3 + \frac{\delta^3}{7} $$
To see what values $S(\delta)$ can approach, we take the limit as $\delta \to 0^+$:
$$ \lim_{\delta \to 0^+} S(\delta) = \lim_{\delta \to 0^+} \left( (c-\delta)^3 + \frac{\delta^3}{7} \right) = (c-0)^3 + 0 = c^3 $$
Since we can choose $\delta$ to be arbitrarily small and positive, we can make $S(\delta)$ arbitrarily close to $c^3$. This proves that the supremum of $Y$ is $c^3$.

#### **Step 2: Finding the Infimum of Y**

We will now show that the infimum of $Y$ is $0$ and that this value is not attained.

**2a. Establishing a Lower Bound**

For any sequence $(x_n) \in X$, we have $x_n > 0$ for all $n$. Therefore, $x_n^3 > 0$ for all $n$.
The sum of a sequence of strictly positive terms must be strictly positive.
$$ S = \sum_{n=0}^{\infty} x_n^3 > 0 $$
This shows that $0$ is a lower bound for the set $Y$. Since the sum must be strictly greater than 0, the infimum is not attained; there is no sequence in $X$ for which the sum of cubes is 0.

**2b. Showing the Infimum is 0**

To show that $0$ is the greatest lower bound (infimum), we must find sequences in $X$ for which the sum of cubes is arbitrarily close to 0. We can achieve this by "spreading out" the sum $c$ over a very large number of terms.

Consider the family of geometric sequences $(x_n^{(r)})$ parameterized by $r \in (0, 1)$:
$$ x_n^{(r)} = c(1-r)r^n, \quad n \ge 0 $$
Let's verify this sequence is in $X$.
Since $c>0$ and $r \in (0,1)$, we have $c(1-r)>0$ and $r^n > 0$, so $x_n^{(r)} > 0$ for all $n$.
The sum is a geometric series:
$$ \sum_{n=0}^{\infty} x_n^{(r)} = \sum_{n=0}^{\infty} c(1-r)r^n = c(1-r) \sum_{n=0}^{\infty} r^n = c(1-r) \cdot \frac{1}{1-r} = c $$
So, $(x_n^{(r)}) \in X$ for any $r \in (0,1)$.

Now, let's compute the sum of the cubes, $S(r)$:
$$ S(r) = \sum_{n=0}^{\infty} (x_n^{(r)})^3 = \sum_{n=0}^{\infty} (c(1-r)r^n)^3 = c^3(1-r)^3 \sum_{n=0}^{\infty} (r^3)^n $$
This is another geometric series with ratio $r^3$. Since $0<r<1$, we have $0<r^3<1$.
$$ S(r) = c^3(1-r)^3 \cdot \frac{1}{1-r^3} = c^3(1-r)^3 \frac{1}{(1-r)(1+r+r^2)} = c^3 \frac{(1-r)^2}{1+r+r^2} $$
To see what values $S(r)$ can approach, we take the limit as $r \to 1^-$:
$$ \lim_{r \to 1^-} S(r) = \lim_{r \to 1^-} c^3 \frac{(1-r)^2}{1+r+r^2} = c^3 \frac{(1-1)^2}{1+1+1^2} = c^3 \cdot \frac{0}{3} = 0 $$
Since we can choose $r$ arbitrarily close to 1, we can make $S(r)$ arbitrarily close to 0. This proves that the infimum of $Y$ is 0.

#### **Step 3: Describing the Set Y**

We have established that $\inf(Y) = 0$ and $\sup(Y) = c^3$. Neither bound is attained. This means $Y \subseteq (0, c^3)$.
To show that $Y$ is exactly the interval $(0, c^3)$, we need to show that any value $v \in (0, c^3)$ can be realized as the sum of cubes of some sequence in $X$.

Let's re-examine the function $S(r) = c^3 \frac{(1-r)^2}{1+r+r^2}$ derived from the geometric sequences, for $r \in (0,1)$.
This function $S(r)$ is continuous on the interval $(0,1)$.
We calculated the limits at the endpoints of the interval:
- $\lim_{r \to 0^+} S(r) = c^3 \frac{(1-0)^2}{1+0+0} = c^3$
- $\lim_{r \to 1^-} S(r) = 0$

Let's check if $S(r)$ is monotonic. The derivative of $f(r) = \frac{(1-r)^2}{1+r+r^2}$ is
$$ f'(r) = \frac{-2(1-r)(1+r+r^2) - (1-r)^2(1+2r)}{(1+r+r^2)^2} = \frac{-3(1-r^2)}{(1+r+r^2)^2} $$
For $r \in (0,1)$, $1-r^2 > 0$, so $f'(r) < 0$. This means $S(r)$ is a strictly decreasing function of $r$ on $(0,1)$.

By the Intermediate Value Theorem, a continuous, strictly monotonic function on an interval takes on all values between its limiting values at the endpoints of the interval.
The range of $S(r)$ for $r \in (0,1)$ is therefore the open interval $(\lim_{r\to 1^-}S(r), \lim_{r\to 0^+}S(r)) = (0, c^3)$.
This shows that for any value $v \in (0, c^3)$, there exists an $r \in (0,1)$ such that the corresponding geometric sequence $(x_n^{(r)})$ gives a sum of cubes equal to $v$.
Therefore, $(0, c^3) \subseteq Y$.

Since we already showed $Y \subseteq (0, c^3)$, we can conclude that $Y = (0, c^3)$.

### **Conclusion**

The set $Y$ is the set of all possible values for the sum of the cubes of sequences of positive reals that sum to $c$.

- The supremum of this set is $c^3$. This value is approached by sequences where one term is close to $c$ and all other terms are very small. The supremum is not attained.
- The infimum of this set is $0$. This value is approached by sequences where the sum $c$ is distributed among many terms of small magnitude. The infimum is not attained.
- By constructing a suitable family of sequences (e.g., geometric sequences), we have shown that every value between $0$ and $c^3$ can be achieved.

Thus, the set $Y$ is the open interval $(0, c^3)$.
$$ Y = (0, c^3) $$