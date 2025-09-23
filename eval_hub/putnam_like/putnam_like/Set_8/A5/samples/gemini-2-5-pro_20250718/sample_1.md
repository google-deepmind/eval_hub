Here is a detailed, step-by-step solution to the problem.

Let $I_n = \int_0^{2\pi}f_n(x)dx$, where $f_n(x) =\prod_{i=1}^{n}\cos((2i-1)x)$.
Our goal is to find $\liminf_{n\to\infty} I_n$.

### Step 1: Express the integral in terms of the constant term of a Fourier series

The function $f_n(x)$ is a product of cosine functions. The product of any number of cosine functions can be expressed as a sum of cosine functions using product-to-sum identities repeatedly.
For example, $\cos(A)\cos(B) = \frac{1}{2}(\cos(A-B)+\cos(A+B))$.
Thus, $f_n(x)$ can be written as a finite sum of the form:
$$f_n(x) = a_0 + \sum_{k=1}^M a_k \cos(k x)$$
for some integer $M$ and coefficients $a_k$.

When we integrate $f_n(x)$ from $0$ to $2\pi$, the terms involving $\cos(kx)$ for $k \ge 1$ will integrate to zero:
$$ \int_0^{2\pi} \cos(kx) dx = \left[\frac{\sin(kx)}{k}\right]_0^{2\pi} = 0 \quad \text{for } k \in \mathbb{Z}, k\neq 0 $$
The integral of the constant term is:
$$ \int_0^{2\pi} a_0 dx = 2\pi a_0 $$
So, $I_n = 2\pi a_0$, where $a_0$ is the constant term in the Fourier cosine series expansion of $f_n(x)$.

### Step 2: Determine the constant term $a_0$

To find the constant term $a_0$, we can use the complex exponential form of the cosine function: $\cos(\theta) = \frac{e^{i\theta} + e^{-i\theta}}{2}$.
$$ f_n(x) = \prod_{i=1}^{n} \frac{e^{i(2i-1)x} + e^{-i(2i-1)x}}{2} $$
$$ f_n(x) = \frac{1}{2^n} \prod_{i=1}^{n} (e^{i(2i-1)x} + e^{-i(2i-1)x}) $$
When we expand this product, we get a sum of $2^n$ terms, each of the form:
$$ \frac{1}{2^n} e^{i \epsilon_1(1)x} e^{i \epsilon_2(3)x} \cdots e^{i \epsilon_n(2n-1)x} = \frac{1}{2^n} \exp\left(i x \sum_{j=1}^n \epsilon_j (2j-1)\right) $$
where each $\epsilon_j$ is either $+1$ or $-1$.
The sum is:
$$ f_n(x) = \frac{1}{2^n} \sum_{\epsilon \in \{-1,1\}^n} \exp\left(i x \sum_{j=1}^n \epsilon_j (2j-1)\right) $$
The constant term $a_0$ corresponds to the terms where the exponent of $e$ is zero. This occurs when the coefficient of $ix$ is zero, i.e.,
$$ \sum_{j=1}^n \epsilon_j (2j-1) = 0 $$
Let $N_n$ be the number of choices for $(\epsilon_1, \dots, \epsilon_n)$ that satisfy this equation. The constant term $a_0$ is then $N_n/2^n$.
Therefore, the integral is $I_n = 2\pi a_0 = \frac{2\pi N_n}{2^n}$.

Since $N_n$ is a count of the number of ways, it is a non-negative integer ($N_n \ge 0$).
This implies that $I_n \ge 0$ for all $n \in \mathbb{N}$.

### Step 3: Analyze the case where $n$ is odd

We will show that $I_n=0$ for all odd $n$. We present two different proofs for this fact.

**Method 1: Integer Partition Argument**

For the sum $\sum_{j=1}^n \epsilon_j (2j-1)$ to be zero, we can partition the set of numbers $S = \{1, 3, 5, \dots, 2n-1\}$ into two subsets, $P$ (for which $\epsilon_j = +1$) and $M$ (for which $\epsilon_j = -1$), such that the sum of elements in $P$ is equal to the sum of elements in $M$.
Let $S_P = \sum_{j \in P} j$ and $S_M = \sum_{j \in M} j$. We need $S_P - S_M = 0$, so $S_P = S_M$.
The total sum of all elements in $S$ is the sum of the first $n$ odd numbers, which is $n^2$.
$$ \sum_{j=1}^n (2j-1) = n^2 $$
So, $S_P + S_M = n^2$. Since we need $S_P=S_M$, this implies $2S_P = n^2$, or $S_P = n^2/2$.

Now, let $n$ be an odd number. Then $n^2$ is also odd. In this case, $n^2/2$ is not an integer.
However, the set $S$ consists of only integers. The sum of any subset of $S$, such as $S_P$, must be an integer.
Since $S_P$ must be an integer and $n^2/2$ is not, it is impossible to find a subset $P$ whose elements sum to $n^2/2$.
Therefore, there are no solutions to $\sum_{j=1}^n \epsilon_j (2j-1) = 0$ when $n$ is odd.
This means $N_n=0$ for odd $n$.
Consequently, $I_n = \frac{2\pi N_n}{2^n} = 0$ for all odd $n$.

**Method 2: Symmetry Argument**

The function $f_n(x)$ is a product of even functions, so it is an even function: $f_n(-x)=f_n(x)$.
The integral over $[0, 2\pi]$ can be written as:
$$ I_n = \int_0^{2\pi} f_n(x) dx = 2 \int_0^\pi f_n(x) dx $$
Let's analyze the behavior of $f_n(x)$ around $x=\pi/2$. Consider the substitution $x = \pi - y$:
$$ \cos((2i-1)(\pi-y)) = \cos((2i-1)\pi - (2i-1)y) $$
Since $2i-1$ is always odd, $(2i-1)\pi$ is an odd multiple of $\pi$. Using the identity $\cos(\text{odd} \cdot \pi - \theta) = -\cos(\theta)$, we have:
$$ \cos((2i-1)(\pi-y)) = -\cos((2i-1)y) $$
Therefore,
$$ f_n(\pi-y) = \prod_{i=1}^n \cos((2i-1)(\pi-y)) = \prod_{i=1}^n [-\cos((2i-1)y)] = (-1)^n \prod_{i=1}^n \cos((2i-1)y) = (-1)^n f_n(y) $$
Now, let's split the integral $\int_0^\pi f_n(x) dx$:
$$ \int_0^\pi f_n(x) dx = \int_0^{\pi/2} f_n(x) dx + \int_{\pi/2}^\pi f_n(x) dx $$
In the second integral, let $x = \pi-y$, so $dx=-dy$. When $x=\pi/2$, $y=\pi/2$. When $x=\pi$, $y=0$.
$$ \int_{\pi/2}^\pi f_n(x) dx = \int_{\pi/2}^0 f_n(\pi-y) (-dy) = \int_0^{\pi/2} f_n(\pi-y) dy = \int_0^{\pi/2} (-1)^n f_n(y) dy = (-1)^n \int_0^{\pi/2} f_n(x) dx $$
So,
$$ \int_0^\pi f_n(x) dx = \int_0^{\pi/2} f_n(x) dx + (-1)^n \int_0^{\pi/2} f_n(x) dx = (1+(-1)^n) \int_0^{\pi/2} f_n(x) dx $$
If $n$ is odd, $1+(-1)^n = 1-1=0$. Thus, $\int_0^\pi f_n(x) dx = 0$.
This implies $I_n = 2 \times 0 = 0$ for all odd $n$.

### Step 4: Finding the Limit Inferior

We have established two key facts:
1. $I_n \ge 0$ for all $n \in \mathbb{N}$.
2. $I_n = 0$ for all odd $n \in \mathbb{N}$.

The limit inferior of a sequence $(a_n)$ is defined as $\liminf_{n\to\infty} a_n = \lim_{n\to\infty} \left( \inf_{k\ge n} a_k \right)$.
Let's consider the sequence $(I_n)$.
From point 1, we know that $I_k \ge 0$ for all $k$. This means for any $n$, the infimum of the set $\{I_k : k \ge n\}$ must be non-negative:
$$ \inf_{k\ge n} I_k \ge 0 $$
Taking the limit as $n\to\infty$, we get:
$$ \liminf_{n\to\infty} I_n \ge 0 $$

From point 2, we have a subsequence of $(I_n)$ that is identically zero. Specifically, the subsequence of odd-indexed terms $(I_{2m+1})_{m\in\mathbb{N}}$ is $(0, 0, 0, \dots)$.
The existence of a subsequence that converges to a value $L$ implies that the limit inferior of the original sequence is less than or equal to $L$.
$$ \liminf_{n\to\infty} I_n \le \lim_{m\to\infty} I_{2m+1} = \lim_{m\to\infty} 0 = 0 $$

Combining our two findings:
$$ \liminf_{n\to\infty} I_n \ge 0 \quad \text{and} \quad \liminf_{n\to\infty} I_n \le 0 $$
The only value satisfying both inequalities is 0.

Therefore, $\liminf_{n\to\infty} I_n = 0$.

For completeness, let's look at a few terms for even $n$:
$I_2 = 0$ (since partitioning $\{1,3\}$ into sets of sum 2 is impossible, $N_2=0$).
$I_4 = \frac{2\pi N_4}{2^4}$. Partitions of $\{1,3,5,7\}$ into sets of sum 8: $\{1,7\}$ and $\{3,5\}$. This is one partition. Each partition corresponds to 2 ways of choosing signs (e.g., $+1,-1,-1,+1$ and $-1,+1,+1,-1$). So $N_4=2$. $I_4 = \frac{2\pi(2)}{16} = \frac{\pi}{4}$.
The sequence $I_n$ begins $(0, 0, 0, \pi/4, 0, \pi/16, 0, \dots)$. While the even terms are not all zero, the presence of the zero-valued odd terms forces the limit inferior to be zero.