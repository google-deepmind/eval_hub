An expert mathematician's step-by-step solution:

We are asked if there exists a function $f:\mathbb{Z}\to\mathbb{Z}$ satisfying the two equations:
1. $9f(x)-10f(f(x))=2x$ for all $x\in\mathbb{Z}$ (let's call this (E1))
2. $f(2x)=2f(x)$ for all $x\in\mathbb{Z}$ (let's call this (E2))

We will assume such a function exists and derive a contradiction.

### Step 1: Initial deductions about the function $f$

First, let's determine the value of $f(0)$.
Using (E2) with $x=0$, we have $f(2 \cdot 0) = 2f(0)$, which simplifies to $f(0) = 2f(0)$. This implies $f(0)=0$.
Let's check this with (E1). For $x=0$, (E1) gives $9f(0) - 10f(f(0)) = 2(0) = 0$.
If $f(0)=0$, this becomes $9(0) - 10f(0) = 0$, which is $0=0$. So, $f(0)=0$ is consistent with both equations.

Next, we use (E2) to understand the structure of $f$. Any non-zero integer $x$ can be uniquely written as $x = 2^k \cdot m$, where $m$ is an odd integer and $k \ge 0$ is an integer.
By repeated application of (E2), we get:
$f(x) = f(2^k m) = 2f(2^{k-1} m) = 2^2 f(2^{k-2} m) = \dots = 2^k f(m)$.
This crucial property tells us that the entire function $f$ is determined by its values on the set of odd integers.

### Step 2: Analyze the behavior of $f$ on odd integers

Let $m$ be an arbitrary odd integer. Let's apply (E1) with $x=m$:
$9f(m) - 10f(f(m)) = 2m$.
The right-hand side, $2m$, is an even integer. The term $10f(f(m))$ is also an even integer, since it's a multiple of 10. Therefore, for the equation to hold, $9f(m)$ must be even.
$9f(m) = 2m + 10f(f(m)) = 2(m + 5f(f(m)))$.
Since 9 is odd, for $9f(m)$ to be even, $f(m)$ must be an even integer.
So, for any odd integer $m$, $f(m)$ is an even integer.

Since $f(m)$ is even, we can write $f(m) = 2^j \cdot n$ for some integer $j \ge 1$ and some odd integer $n$.
Now we analyze the term $f(f(m))$:
$f(f(m)) = f(2^j n) = 2^j f(n)$ using the property from Step 1.
Substituting this back into the equation for odd $m$:
$9f(m) - 10(2^j f(n)) = 2m$
$9(2^j n) - 10(2^j f(n)) = 2m$
Since $j \ge 1$, we can divide the entire equation by 2:
$9(2^{j-1} n) - 10(2^{j-1} f(n)) = m$
$2^{j-1} (9n - 10f(n)) = m$.

Recall that $m$ is an odd integer. The left-hand side of the equation is a power of 2 multiplied by an integer. For the product to be odd, the power of 2 must be $2^0=1$.
This implies that $j-1=0$, so $j=1$.

This is a powerful conclusion: for any odd integer $m$, the prime factorization of $f(m)$ contains exactly one factor of 2. In other words, $f(m)/2$ is an odd integer.

### Step 3: Define an auxiliary function and derive a new functional equation

Based on the conclusion of Step 2, we can define a new function $g$ whose domain and codomain are the set of odd integers, $\mathbb{Z}_{odd}$.
Let $g: \mathbb{Z}_{odd} \to \mathbb{Z}_{odd}$ be defined by $g(m) = \frac{f(m)}{2}$.

From $f(m)=2g(m)$ and $j=1$, the equation $m = 2^{j-1} (9n - 10f(n))$ becomes:
$m = 9n - 10f(n)$.
We also need to identify $n$. Recall that $f(m) = 2^j n$ with $j=1$, so $f(m) = 2n$. This means $n = f(m)/2 = g(m)$.
Since $m$ is odd, $n=g(m)$ is also an odd integer. So we can apply our findings to $n$ as well: $f(n) = 2g(n)$.
Substituting $n=g(m)$ and $f(n)=2g(n)$ into the equation $m = 9n - 10f(n)$:
$m = 9g(m) - 10(2g(n)) = 9g(m) - 20g(g(m))$.

So, if a function $f$ exists, it must induce a function $g: \mathbb{Z}_{odd} \to \mathbb{Z}_{odd}$ satisfying:
$m = 9g(m) - 20g(g(m))$ for all $m \in \mathbb{Z}_{odd}$. (Let's call this (E3))

### Step 4: The contradiction from the dynamics of $g$

Let us fix an arbitrary odd integer $m_0$. Define a sequence $(m_k)_{k\ge 0}$ by:
$m_0$ is our chosen odd integer.
$m_{k+1} = g(m_k)$ for $k \ge 0$.
Since the codomain of $g$ is $\mathbb{Z}_{odd}$, every term $m_k$ in this sequence must be an odd integer.

Now, let's apply the functional equation (E3) to each term $m_k$ of the sequence. For any $k \ge 0$:
$m_k = 9g(m_k) - 20g(g(m_k))$
Substituting the definition of the sequence, $g(m_k) = m_{k+1}$ and $g(g(m_k))=g(m_{k+1})=m_{k+2}$:
$m_k = 9m_{k+1} - 20m_{k+2}$.
This gives us a linear homogeneous recurrence relation for the sequence $(m_k)$:
$20m_{k+2} - 9m_{k+1} + m_k = 0$.

The characteristic equation of this recurrence is $20r^2 - 9r + 1 = 0$.
We solve for the roots using the quadratic formula:
$r = \frac{9 \pm \sqrt{(-9)^2 - 4(20)(1)}}{2(20)} = \frac{9 \pm \sqrt{81 - 80}}{40} = \frac{9 \pm 1}{40}$.
The roots are $r_1 = \frac{10}{40} = \frac{1}{4}$ and $r_2 = \frac{8}{40} = \frac{1}{5}$.

The general solution for the sequence $(m_k)$ is given by:
$m_k = C_1 \left(\frac{1}{4}\right)^k + C_2 \left(\frac{1}{5}\right)^k$
for some constants $C_1$ and $C_2$. These constants depend on the initial values $m_0$ and $m_1 = g(m_0)$.

We have a sequence $(m_k)$ that must consist entirely of odd integers.
However, for large $k$, the terms $(1/4)^k$ and $(1/5)^k$ both approach 0.
So, $\lim_{k \to \infty} m_k = \lim_{k \to \infty} \left(C_1 \left(\frac{1}{4}\right)^k + C_2 \left(\frac{1}{5}\right)^k\right) = 0$.
For a sequence of integers to converge to 0, it must be eventually equal to 0 for all sufficiently large $k$.
So, there must exist an integer $K$ such that for all $k \ge K$, $m_k = 0$.
But this contradicts the fact that every term $m_k$ must be an odd integer. Odd integers are never zero.

The only way the sequence of integers $m_k$ does not converge to 0 is if the formula is not actually a sum of two decaying exponentials. This could happen if one of the constants $C_1$ or $C_2$ is zero. Let's check these special cases. The constants $C_1, C_2$ are found by solving:
$m_0 = C_1 + C_2$
$m_1 = C_1/4 + C_2/5$
Solving this system gives $C_1 = 20m_1 - 4m_0$ and $C_2 = 5m_0 - 20m_1$.

Case 1: $C_1 = 0$.
$20m_1 - 4m_0 = 0 \implies m_1 = \frac{4m_0}{20} = \frac{m_0}{5}$.
Since $m_1 = g(m_0)$, this means $g(m_0) = m_0/5$.
This relation must hold for any odd integer $m_0$ we might have chosen. But if we choose $m_0=1$ (which is odd), then $g(1) = 1/5$, which is not an integer. This contradicts the definition of $g$. Thus $C_1$ cannot be zero for all odd $m_0$.

Case 2: $C_2 = 0$.
$5m_0 - 20m_1 = 0 \implies m_1 = \frac{5m_0}{20} = \frac{m_0}{4}$.
So, $g(m_0) = m_0/4$. If we choose $m_0=1$, $g(1) = 1/4$, which is not an integer. This is also a contradiction.

So for any odd integer $m_0$, both $C_1$ and $C_2$ must be non-zero.
Therefore, the sequence $m_k = g^k(m_0)$ must converge to 0. As argued before, this requires $m_k=0$ for large $k$, which contradicts that $m_k$ must be an odd integer.

### Conclusion

Our initial assumption that a function $f: \mathbb{Z} \to \mathbb{Z}$ satisfying the given properties exists leads to the necessary existence of a function $g: \mathbb{Z}_{odd} \to \mathbb{Z}_{odd}$ satisfying $m = 9g(m) - 20g(g(m))$. We have shown that such a function $g$ cannot exist because it implies that for any odd $m_0$, the sequence $m_{k+1}=g(m_k)$ must consist of odd integers, but the recurrence relation it satisfies forces the sequence to converge to 0. This is a fundamental contradiction.

Therefore, no such function $f$ exists.