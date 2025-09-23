# Solution

We need to prove that for any continuous decreasing function $f: [0,1] \to \mathbb{R}$ and for all $n \in \mathbb{N}$:

$$\int_{1-\frac{1}{n}}^1 f(x)dx \leq \int_0^1 x^{n-1}f(x)dx \leq \int_0^{\frac{1}{n}}f(x)dx$$

I'll approach this problem using the concept of stochastic dominance.

## Step 1: Define three random variables

Let's define three random variables:

- $Z_n \sim \text{Uniform}(1-\frac{1}{n}, 1)$: Uniformly distributed on $[1-\frac{1}{n}, 1]$
- $X_n$ with PDF $p_{X_n}(x) = nx^{n-1}$ on $[0,1]$
- $Y_n \sim \text{Uniform}(0, \frac{1}{n})$: Uniformly distributed on $[0, \frac{1}{n}]$

Their cumulative distribution functions (CDFs) are:

$$F_{Z_n}(t) = 
\begin{cases}
0, & \text{if } t < 1-\frac{1}{n} \\
n(t-(1-\frac{1}{n})), & \text{if } 1-\frac{1}{n} \leq t \leq 1 \\
1, & \text{if } t > 1
\end{cases}$$

$$F_{X_n}(t) = 
\begin{cases}
0, & \text{if } t < 0 \\
t^n, & \text{if } 0 \leq t \leq 1 \\
1, & \text{if } t > 1
\end{cases}$$

$$F_{Y_n}(t) = 
\begin{cases}
0, & \text{if } t < 0 \\
nt, & \text{if } 0 \leq t \leq \frac{1}{n} \\
1, & \text{if } t > \frac{1}{n}
\end{cases}$$

## Step 2: Establish stochastic dominance

We need to verify that $F_{Z_n}(t) \leq F_{X_n}(t) \leq F_{Y_n}(t)$ for all $t$ and all $n \in \mathbb{N}$.

### Case 1: $0 \leq t < \frac{1}{n}$
For this range, $F_{Z_n}(t) = 0$, $F_{X_n}(t) = t^n$, and $F_{Y_n}(t) = nt$.

To show $t^n \leq nt$ for $t \in (0, \frac{1}{n})$, consider $r(t) = nt - t^n$. We have $r(0) = 0$ and $r'(t) = n - nt^{n-1}$. For $t \in (0, \frac{1}{n})$ and $n > 1$, we have $t^{n-1} < (\frac{1}{n})^{n-1} = \frac{1}{n^{n-1}}$. Therefore, $nt^{n-1} < n \cdot \frac{1}{n^{n-1}} = \frac{n}{n^{n-1}} = n$, which means $r'(t) > 0$. This implies $r(t) > 0$ for $t \in (0, \frac{1}{n})$, so $t^n < nt$.

For $n = 1$, we have $t^n = t = nt$, so the inequality holds with equality.

### Case 2: $\frac{1}{n} \leq t < 1-\frac{1}{n}$
For this range, $F_{Z_n}(t) = 0$, $F_{X_n}(t) = t^n$, and $F_{Y_n}(t) = 1$.

Since $t < 1$ implies $t^n < 1$ for all $n \in \mathbb{N}$, we have $F_{Z_n}(t) < F_{X_n}(t) < F_{Y_n}(t)$.

### Case 3: $1-\frac{1}{n} \leq t \leq 1$
For this range, $F_{Z_n}(t) = n(t-(1-\frac{1}{n}))$, $F_{X_n}(t) = t^n$, and $F_{Y_n}(t) = 1$.

First, since $t \leq 1$ implies $t^n \leq 1$ for all $n \in \mathbb{N}$, we have $F_{X_n}(t) \leq F_{Y_n}(t)$.

To show $F_{Z_n}(t) \leq F_{X_n}(t)$, we need to verify that $n(t-(1-\frac{1}{n})) \leq t^n$ for $t \in [1-\frac{1}{n}, 1]$. Let $p(t) = t^n - n(t-(1-\frac{1}{n}))$.

At $t = 1-\frac{1}{n}$, we have $p(1-\frac{1}{n}) = (1-\frac{1}{n})^n - 0 = (1-\frac{1}{n})^n > 0$.

At $t = 1$, we have $p(1) = 1 - n \cdot \frac{1}{n} = 0$.

For $t \in [1-\frac{1}{n}, 1)$ and $n > 1$, the derivative $p'(t) = nt^{n-1} - n < 0$ (since $t < 1$ implies $t^{n-1} < 1$). So $p(t)$ is decreasing on this interval. Given that $p(1) = 0$, this means $p(t) > 0$ for all $t \in [1-\frac{1}{n}, 1)$.

For $n = 1$, we have $p(t) = t - 1 \cdot (t - 0) = 0$ for all $t$, so the inequality holds with equality.

## Step 3: Apply stochastic dominance to our integrals

Since $F_{Z_n}(t) \leq F_{X_n}(t) \leq F_{Y_n}(t)$ for all $t$, we know that $Z_n$ stochastically dominates $X_n$, and $X_n$ stochastically dominates $Y_n$.

For a decreasing function $f$, stochastic dominance implies:
$$E[f(Z_n)] \leq E[f(X_n)] \leq E[f(Y_n)]$$

These expected values translate to:
$$n\int_{1-\frac{1}{n}}^1 f(x)dx \leq n\int_0^1 x^{n-1}f(x)dx \leq n\int_0^{\frac{1}{n}}f(x)dx$$

Dividing by $n$, we get the desired result:
$$\int_{1-\frac{1}{n}}^1 f(x)dx \leq \int_0^1 x^{n-1}f(x)dx \leq \int_0^{\frac{1}{n}}f(x)dx$$

Therefore, the inequality holds for all continuous decreasing functions $f: [0,1] \to \mathbb{R}$ and for all $n \in \mathbb{N}$.