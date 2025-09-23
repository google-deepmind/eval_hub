# Solution

I'll solve this by carefully transforming the limit and analyzing the behavior of the transformed function as $x \to \infty$.

## Step 1: Make a substitution

Since $g(x) \to \infty$ as $x \to \infty$, let's make the substitution $t = g(x)$.

For each function $f(x)$, we'll define a corresponding function $F(t)$ such that:
$$F(t) = f(g^{-1}(t))$$

This means $f(x) = F(g(x))$. Now, applying the chain rule:
$$f'(x) = \frac{dF}{dt} \cdot g'(x)$$

Therefore:
$$\frac{f'(x)}{g'(x)} = \frac{dF}{dt}$$

## Step 2: Rewrite the given limit condition

The condition $\lim_{x\to\infty} \left( f(x) + \frac{f'(x)}{g'(x)} \right) = 0$ becomes:
$$\lim_{t\to\infty} \left( F(t) + \frac{dF}{dt} \right) = 0$$

## Step 3: Introduce an auxiliary function

Define $G(t) = F(t)e^t$. Computing its derivative:
$$\frac{dG}{dt} = \frac{dF}{dt}e^t + F(t)e^t = e^t\left(F(t) + \frac{dF}{dt}\right)$$

## Step 4: Bound the growth of G(t)

From our limit condition, for any $\epsilon > 0$, there exists $T_\epsilon > 0$ such that for all $t > T_\epsilon$:
$$\left|F(t) + \frac{dF}{dt}\right| < \epsilon$$

This means:
$$\left|\frac{dG}{dt}\right| = e^t\left|F(t) + \frac{dF}{dt}\right| < \epsilon e^t$$

For any $t_1, t_2 > T_\epsilon$ with $t_1 < t_2$:
$$|G(t_2) - G(t_1)| \leq \int_{t_1}^{t_2} \left|\frac{dG}{dt}\right| dt < \epsilon \int_{t_1}^{t_2} e^t dt = \epsilon(e^{t_2} - e^{t_1})$$

This gives us:
$$G(t_1) - \epsilon(e^{t_2} - e^{t_1}) < G(t_2) < G(t_1) + \epsilon(e^{t_2} - e^{t_1})$$

## Step 5: Recover information about F(t)

Since $F(t) = \frac{G(t)}{e^t}$, dividing by $e^{t_2}$:
$$\frac{G(t_1)}{e^{t_2}} - \epsilon\left(1 - \frac{e^{t_1}}{e^{t_2}}\right) < F(t_2) < \frac{G(t_1)}{e^{t_2}} + \epsilon\left(1 - \frac{e^{t_1}}{e^{t_2}}\right)$$

As $t_2 \to \infty$ (with $t_1$ fixed):
- $\frac{G(t_1)}{e^{t_2}} \to 0$ since $G(t_1)$ is constant and $e^{t_2} \to \infty$
- $\frac{e^{t_1}}{e^{t_2}} \to 0$ since $t_1 < t_2$

Therefore, for sufficiently large $t_2$:
$$-\epsilon < F(t_2) < \epsilon$$

Since this holds for any $\epsilon > 0$, we conclude $\lim_{t\to\infty} F(t) = 0$.

## Step 6: Translate back to the original problem

Since $F(t) = f(g^{-1}(t))$ and $t = g(x)$, we have $f(x) = F(g(x))$. 

Therefore, $\lim_{x\to\infty} f(x) = \lim_{t\to\infty} F(t) = 0$, which is what we wanted to prove.