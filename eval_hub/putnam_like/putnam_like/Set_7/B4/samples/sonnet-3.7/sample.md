# Solution

I'll solve this step-by-step to find all polynomials $f$ with real coefficients such that $f(\mathbb{O}) \subset \mathbb{O}$.

First, let's understand what $\mathbb{O}$ represents. For a given $p \geq 2$, the set $\mathbb{O}$ consists of all positive integers whose digits in base $p$ are all ones. These numbers can be written as:
$$a_n = \underbrace{11...1}_{\text{$n$ ones in base $p$}} = \sum_{i=0}^{n-1} p^i = \frac{p^n-1}{p-1}$$

For example, $a_1 = 1$, $a_2 = 1+p$, $a_3 = 1+p+p^2$, and so on.

## Step 1: Consider polynomial degrees

Let $f(x) = c_d x^d + c_{d-1} x^{d-1} + \ldots + c_1 x + c_0$ be a polynomial with real coefficients. Since $f$ maps integers to integers, the coefficients must be rational.

## Step 2: Analyze constant polynomials (degree 0)

If $f(x) = c$ is a constant polynomial, then $f(\mathbb{O}) \subset \mathbb{O}$ if and only if $c \in \mathbb{O}$. So all constant polynomials of the form $f(x) = a_m$ for any $m \geq 1$ are valid solutions.

## Step 3: Analyze linear polynomials (degree 1)

Let $f(x) = ax + b$ with $a \neq 0$. For $f(a_1) \in \mathbb{O}$, we need $a+b = a_m$ for some $m \geq 1$. This gives us:
$$(a+b)(p-1) = p^m-1$$

For this to be true for all $p \geq 2$, we need $a+b = 1$ and $m = 1$.

Now, for $a_2 = 1+p$, we have:
$$f(a_2) = a(1+p) + b = (a+b) + ap-a = 1 + a(p-1)$$

For $f(a_2) \in \mathbb{O}$, we need:
$$(1 + a(p-1))(p-1) = p^k-1$$

For $k = 1$, this gives $a(p-1)^2 = 0$, which means $a = 0$ (contradiction).
For $k = 2$, we get $p(1-p) + a(p-1)^2 = 0$, which gives $a = \frac{p}{p-1}$.

But this means $a$ depends on $p$, which contradicts our need for fixed coefficients. The only possibility is $a = 1$ and $b = 0$, giving us $f(x) = x$.

## Step 4: Analyze higher degree polynomials (degree ≥ 2)

For a polynomial of degree $d \geq 2$ with leading coefficient $c_d$, we can analyze the asymptotic behavior. For large $n$:
$$f(a_n) \approx c_d a_n^d \approx c_d \cdot \frac{p^{nd}}{(p-1)^d}$$

Since $f(a_n) \in \mathbb{O}$, there must exist $m_n$ such that $f(a_n) = a_{m_n}$. This gives:
$$\frac{p^{m_n}}{p-1} \approx c_d \cdot \frac{p^{nd}}{(p-1)^d}$$

For large $n$, the exponential growth implies $m_n \approx nd$, which leads to:
$$c_d \approx (p-1)^{d-1}$$

Since this depends on $p$, but our polynomial must have fixed coefficients for all $p \geq 2$, no polynomial of degree $d \geq 2$ can satisfy our condition.

## Conclusion

The only polynomials $f$ with real coefficients such that $f(\mathbb{O}) \subset \mathbb{O}$ are:
1. The identity polynomial $f(x) = x$
2. The constant polynomials $f(x) = a_m$ for some $m \geq 1$, where $a_m = \frac{p^m-1}{p-1}$