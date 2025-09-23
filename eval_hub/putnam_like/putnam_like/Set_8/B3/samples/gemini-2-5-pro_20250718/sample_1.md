Of course. Here is a detailed, step-by-step solution to the problem.

### The Problem
Let $f: [0,1]\to \mathbb{R}$ be a continuous and decreasing function. We want to show that for all $n\in \mathbb{N}$:
$$
\int_{1-\frac{1}{n}}^1 f(x)dx\leq \int_0^1 x^{n-1}f(x)dx\leq \int_0^{\frac{1}{n}}f(x)dx
$$

We will prove the two inequalities separately.

### Part 1: Proving the Right-Hand Inequality
We want to show that
$$
\int_0^1 x^{n-1}f(x)dx\leq \int_0^{\frac{1}{n}}f(x)dx
$$

**Step 1: Transform the integrals to have a common interval of integration.**
To compare the two integrals, it is helpful to have them over the same interval, for example, $[0, 1]$.

Let's start with the middle integral, $I_{mid} = \int_0^1 x^{n-1}f(x)dx$.
We perform a change of variables. Let $u = x^n$. Then $du = nx^{n-1}dx$, which gives $x^{n-1}dx = \frac{1}{n}du$.
The limits of integration remain the same: when $x=0$, $u=0$; when $x=1$, $u=1$.
Also, we have $x = u^{1/n}$. Substituting these into the integral gives:
$$
I_{mid} = \int_0^1 f(u^{1/n}) \frac{1}{n}du = \frac{1}{n}\int_0^1 f(u^{1/n})du
$$

Now let's transform the right-hand integral, $I_{right} = \int_0^{\frac{1}{n}}f(x)dx$.
We perform a change of variables. Let $x = t/n$. Then $dx = \frac{1}{n}dt$.
The new limits of integration are: when $x=0$, $t=0$; when $x=1/n$, $t=1$.
Substituting these gives:
$$
I_{right} = \int_0^1 f(t/n) \frac{1}{n}dt = \frac{1}{n}\int_0^1 f(t/n)dt
$$

**Step 2: Compare the integrands.**
The inequality we want to prove, $\int_0^1 x^{n-1}f(x)dx\leq \int_0^{\frac{1}{n}}f(x)dx$, is now equivalent to:
$$
\frac{1}{n}\int_0^1 f(u^{1/n})du \leq \frac{1}{n}\int_0^1 f(t/n)dt
$$
Multiplying by $n$ and using the same dummy variable of integration (say, $y$) for both, we need to show:
$$
\int_0^1 f(y^{1/n})dy \leq \int_0^1 f(y/n)dy
$$
This inequality holds if the integrand on the left is less than or equal to the integrand on the right for all $y \in [0,1]$. That is, if $f(y^{1/n}) \leq f(y/n)$ for all $y \in [0,1]$.

**Step 3: Use the decreasing property of f.**
Since $f$ is a decreasing function, $f(a) \leq f(b)$ if and only if $a \geq b$.
So, we need to show that $y^{1/n} \geq y/n$ for all $y \in [0,1]$.

Let's prove this auxiliary inequality.
For $y=0$, we have $0^{1/n} \geq 0/n$, which is $0 \geq 0$. This is true.
For $y \in (0,1]$, we can divide by $y$ (which is positive) to get:
$y^{1/n - 1} \geq 1/n \iff y^{\frac{1-n}{n}} \geq \frac{1}{n}$.
This is equivalent to $\frac{1}{y^{\frac{n-1}{n}}} \geq \frac{1}{n}$, or $n \geq y^{\frac{n-1}{n}}$.
Since $y \in (0,1]$ and $n \geq 1$, we have $y^{\frac{n-1}{n}} \leq 1^{\frac{n-1}{n}} = 1$.
Since $n \in \mathbb{N}$, we have $n \geq 1$.
Therefore, $n \geq 1 \geq y^{\frac{n-1}{n}}$ holds for all $y \in (0,1]$.
So, the inequality $y^{1/n} \geq y/n$ is true for all $y \in [0,1]$.

**Step 4: Conclude the proof of the right-hand inequality.**
Since $y^{1/n} \geq y/n$ for $y \in [0,1]$ and $f$ is decreasing, we have:
$$ f(y^{1/n}) \leq f(y/n) \quad \text{for all } y \in [0,1] $$
Integrating this inequality over the interval $[0,1]$:
$$ \int_0^1 f(y^{1/n})dy \leq \int_0^1 f(y/n)dy $$
Multiplying by $\frac{1}{n}$:
$$ \frac{1}{n}\int_0^1 f(y^{1/n})dy \leq \frac{1}{n}\int_0^1 f(y/n)dy $$
Substituting back the original integral forms:
$$ \int_0^1 x^{n-1}f(x)dx \leq \int_0^{\frac{1}{n}}f(x)dx $$
This completes the proof of the right-hand inequality.

---

### Part 2: Proving the Left-Hand Inequality
We want to show that
$$
\int_{1-\frac{1}{n}}^1 f(x)dx\leq \int_0^1 x^{n-1}f(x)dx
$$

**Step 1: Formulate the inequality in a suitable form.**
The inequality is equivalent to showing that the difference is non-negative:
$$ \int_0^1 x^{n-1}f(x)dx - \int_{1-\frac{1}{n}}^1 f(x)dx \geq 0 $$
We can write the second integral over the interval $[0,1]$ using an indicator function $\mathbb{I}_{[a,b]}(x)$, which is 1 if $x \in [a,b]$ and 0 otherwise.
$$ \int_0^1 \left(x^{n-1} - \mathbb{I}_{[1-\frac{1}{n}, 1]}(x)\right) f(x) dx \geq 0 $$
Let $g(x) = x^{n-1} - \mathbb{I}_{[1-\frac{1}{n}, 1]}(x)$. We want to show $\int_0^1 g(x)f(x)dx \geq 0$.

**Step 2: A key lemma.**
We will use the following lemma, which is a consequence of the Second Mean Value Theorem for Integrals (or can be proved by "summation by parts"):

**Lemma:** Let $f: [a,b] \to \mathbb{R}$ be a decreasing function and let $g: [a,b] \to \mathbb{R}$ be an integrable function. If $G(x) = \int_a^x g(t)dt \geq 0$ for all $x \in [a,b]$ and $G(b)=0$, then $\int_a^b f(x)g(x)dx \geq 0$.

*(A brief proof of the lemma for a continuously differentiable $f$: Using integration by parts, $\int_a^b f(x)g(x)dx = [f(x)G(x)]_a^b - \int_a^b f'(x)G(x)dx$. Since $G(a)=G(b)=0$, the first term is zero. So $\int_a^b f(x)g(x)dx = -\int_a^b f'(x)G(x)dx$. Since $f$ is decreasing, $f'(x) \leq 0$. Since $G(x) \geq 0$, the integrand $-f'(x)G(x)$ is non-negative. Thus, the integral is non-negative. The result holds for any continuous decreasing $f$ by an approximation argument.)*

**Step 3: Apply the lemma.**
Let's check if the conditions of the lemma apply to our function $g(x) = x^{n-1} - \mathbb{I}_{[1-\frac{1}{n}, 1]}(x)$ on the interval $[0,1]$.

First, let's calculate $G(1) = \int_0^1 g(x)dx$:
$$
\int_0^1 g(x)dx = \int_0^1 x^{n-1}dx - \int_0^1 \mathbb{I}_{[1-\frac{1}{n}, 1]}(x)dx = \left[\frac{x^n}{n}\right]_0^1 - \int_{1-\frac{1}{n}}^1 1 dx = \frac{1}{n} - \left(1 - (1-\frac{1}{n})\right) = \frac{1}{n} - \frac{1}{n} = 0.
$$
So, $G(1)=0$.

Next, let's check if $G(x) = \int_0^x g(t)dt \geq 0$ for all $x \in [0,1]$. We consider two cases for $x$.

Case 1: $x \in [0, 1-\frac{1}{n})$
In this interval, $\mathbb{I}_{[1-\frac{1}{n}, 1]}(t) = 0$ for $t \in [0,x]$.
$$
G(x) = \int_0^x t^{n-1}dt = \frac{x^n}{n}
$$
Since $x \geq 0$ and $n \in \mathbb{N}$, $G(x) = \frac{x^n}{n} \geq 0$.

Case 2: $x \in [1-\frac{1}{n}, 1]$
$$
\begin{aligned}
G(x) &= \int_0^x (t^{n-1} - \mathbb{I}_{[1-\frac{1}{n}, 1]}(t))dt \\
&= \int_0^{1-\frac{1}{n}} t^{n-1}dt + \int_{1-\frac{1}{n}}^x (t^{n-1}-1)dt \\
&= \left[\frac{t^n}{n}\right]_0^{1-\frac{1}{n}} + \left[\frac{t^n}{n} - t\right]_{1-\frac{1}{n}}^x \\
&= \frac{(1-1/n)^n}{n} + \left(\frac{x^n}{n} - x\right) - \left(\frac{(1-1/n)^n}{n} - (1-\frac{1}{n})\right) \\
&= \frac{x^n}{n} - x + 1 - \frac{1}{n}
\end{aligned}
$$
Let's analyze the function $h(x) = \frac{x^n}{n} - x + 1 - \frac{1}{n}$ on the interval $[1-\frac{1}{n}, 1]$.
Its derivative is $h'(x) = x^{n-1}-1$. For $x \in [1-\frac{1}{n}, 1]$, we have $x \leq 1$, so $x^{n-1} \leq 1$, which means $h'(x) \leq 0$.
Thus, $h(x)$ is a decreasing function on this interval. Its minimum value will be at $x=1$.
$h(1) = \frac{1^n}{n} - 1 + 1 - \frac{1}{n} = \frac{1}{n} - \frac{1}{n} = 0$.
Since $h(x)$ is decreasing on $[1-\frac{1}{n}, 1]$ and its minimum value is 0, we must have $h(x) \geq 0$ for all $x \in [1-\frac{1}{n}, 1]$.
So, $G(x) \geq 0$ in this case as well.

**Step 4: Conclude the proof of the left-hand inequality.**
We have shown that $G(x) = \int_0^x g(t)dt \geq 0$ for all $x\in[0,1]$ and $G(1)=0$. Since $f(x)$ is a decreasing function, we can apply the lemma:
$$
\int_0^1 f(x)g(x)dx \geq 0
$$
Substituting $g(x)$ back:
$$
\int_0^1 f(x) \left(x^{n-1} - \mathbb{I}_{[1-\frac{1}{n}, 1]}(x)\right)dx \geq 0
$$
$$
\int_0^1 x^{n-1}f(x)dx - \int_0^1 \mathbb{I}_{[1-\frac{1}{n}, 1]}(x)f(x)dx \geq 0
$$
$$
\int_0^1 x^{n-1}f(x)dx \geq \int_{1-\frac{1}{n}}^1 f(x)dx
$$
This completes the proof of the left-hand inequality.

### Conclusion
We have successfully proven both the left-hand and right-hand inequalities:
$$
\int_{1-\frac{1}{n}}^1 f(x)dx\leq \int_0^1 x^{n-1}f(x)dx \quad \text{and} \quad \int_0^1 x^{n-1}f(x)dx\leq \int_0^{\frac{1}{n}}f(x)dx
$$
Combining these gives the desired result for all $n \in \mathbb{N}$.