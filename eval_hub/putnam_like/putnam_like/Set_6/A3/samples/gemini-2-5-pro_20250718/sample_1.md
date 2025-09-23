Here is a detailed, step-by-step solution to the problem.

### **1. Understanding the Problem and Devising a Strategy**

We are given a condition that links the sum of the first $n$ derivatives of a function $f$ at two points, $a_n$ and $b_n$. This condition is:
$$
\frac{f(b_n) + f'(b_n) + \cdots + f^{(n)}(b_n)}{f(a_n) + f'(a_n) + \cdots + f^{(n)}(a_n)} = \frac{e^{b_n}}{e^{a_n}}.
$$
The structure of this equation, especially the presence of $e^{a_n}$ and $e^{b_n}$ in the denominator, suggests defining an auxiliary function that involves $e^{-x}$.

Let's define a sequence of functions $S_n(x)$ for $n \in \mathbb{N}$ as the sum of the first $n$ derivatives of $f$:
$$
S_n(x) = \sum_{k=0}^n f^{(k)}(x) = f(x) + f'(x) + \cdots + f^{(n)}(x).
$$
With this notation, the given condition can be rewritten as:
$$
\frac{S_n(b_n)}{S_n(a_n)} = \frac{e^{b_n}}{e^{a_n}}.
$$
Rearranging this equation gives:
$$
e^{-b_n} S_n(b_n) = e^{-a_n} S_n(a_n).
$$
This form strongly suggests using Rolle's Theorem on a new function $H_n(x) = e^{-x}S_n(x)$. The condition $H_n(b_n) = H_n(a_n)$ implies the existence of a point $\xi_n \in (a_n, b_n)$ where the derivative $H_n'(\xi_n)$ is zero. We will then analyze the expression for $H_n'(x)$ to find a relationship between the derivatives of $f$. Finally, we will take the limit as $n \to \infty$ and use the given conditions on $a_n, b_n$ and the uniform boundedness of the derivatives of $f$ to reach the desired conclusion.

### **2. Step-by-step Solution**

**Step 1: Define an auxiliary function and apply Rolle's Theorem**

For each $n \in \mathbb{N}$, let us define the function $H_n: (-1,1) \to \mathbb{R}$ by
$$
H_n(x) = e^{-x} \sum_{k=0}^n f^{(k)}(x).
$$
Since $f \in C^\infty((-1,1), \mathbb{R})$, each derivative $f^{(k)}$ is continuous. Therefore, the sum $\sum_{k=0}^n f^{(k)}(x)$ is a continuous and differentiable function. As $e^{-x}$ is also continuous and differentiable, $H_n(x)$ is continuous on $[a_n, b_n]$ and differentiable on $(a_n, b_n)$ for every $n \in \mathbb{N}$.

The given condition in the problem is:
$$
\frac{\sum_{k=0}^n f^{(k)}(b_n)}{\sum_{k=0}^n f^{(k)}(a_n)} = \frac{e^{b_n}}{e^{a_n}}.
$$
This can be rewritten as:
$$
e^{-b_n} \sum_{k=0}^n f^{(k)}(b_n) = e^{-a_n} \sum_{k=0}^n f^{(k)}(a_n).
$$
In terms of our auxiliary function $H_n(x)$, this is precisely:
$$
H_n(b_n) = H_n(a_n).
$$
By Rolle's Theorem, since $H_n$ is continuous on $[a_n, b_n]$ and differentiable on $(a_n, b_n)$, and $H_n(a_n)=H_n(b_n)$, there must exist a point $\xi_n \in (a_n, b_n)$ such that $H_n'(\xi_n) = 0$.

**Step 2: Calculate the derivative of the auxiliary function**

Let's compute the derivative of $H_n(x)$ using the product rule:
\begin{align*}
H_n'(x) &= \frac{d}{dx} \left( e^{-x} \sum_{k=0}^n f^{(k)}(x) \right) \\
&= (-e^{-x}) \left( \sum_{k=0}^n f^{(k)}(x) \right) + e^{-x} \left( \frac{d}{dx} \sum_{k=0}^n f^{(k)}(x) \right) \\
&= -e^{-x} \sum_{k=0}^n f^{(k)}(x) + e^{-x} \sum_{k=0}^n f^{(k+1)}(x) \\
&= e^{-x} \left( \sum_{k=0}^n f^{(k+1)}(x) - \sum_{k=0}^n f^{(k)}(x) \right).
\end{align*}
Let's expand the sums to simplify the expression in the parenthesis:
\begin{align*}
\sum_{k=0}^n f^{(k+1)}(x) &= f^{(1)}(x) + f^{(2)}(x) + \cdots + f^{(n)}(x) + f^{(n+1)}(x) \\
\sum_{k=0}^n f^{(k)}(x)   &= f^{(0)}(x) + f^{(1)}(x) + \cdots + f^{(n)}(x).
\end{align*}
The difference is a telescoping sum:
$$
\left( \sum_{k=0}^n f^{(k+1)}(x) \right) - \left( \sum_{k=0}^n f^{(k)}(x) \right) = f^{(n+1)}(x) - f^{(0)}(x) = f^{(n+1)}(x) - f(x).
$$
Thus, the derivative of $H_n(x)$ is:
$$
H_n'(x) = e^{-x} \left( f^{(n+1)}(x) - f(x) \right).
$$

**Step 3: Use the result from Rolle's Theorem**

From Step 1, we know that for each $n \in \mathbb{N}$, there exists $\xi_n \in (a_n, b_n)$ such that $H_n'(\xi_n) = 0$. Using the expression for $H_n'(x)$ from Step 2, we have:
$$
e^{-\xi_n} \left( f^{(n+1)}(\xi_n) - f(\xi_n) \right) = 0.
$$
Since $e^{-\xi_n} > 0$ for any $\xi_n \in (-1,1)$, we must have:
$$
f^{(n+1)}(\xi_n) - f(\xi_n) = 0,
$$
which implies
$$
f^{(n+1)}(\xi_n) = f(\xi_n).
$$

**Step 4: Analyze the limit as $n \to \infty$**

We are given that $\lim_{n \to \infty} a_n = c$ and $\lim_{n \to \infty} b_n = c$. Since $\xi_n \in (a_n, b_n)$, we have $a_n < \xi_n < b_n$ for all $n$. By the Squeeze Theorem (or Sandwich Theorem), as $n \to \infty$:
$$
\lim_{n \to \infty} a_n \le \lim_{n \to \infty} \xi_n \le \lim_{n \to \infty} b_n,
$$
$$
c \le \lim_{n \to \infty} \xi_n \le c,
$$
which implies $\lim_{n \to \infty} \xi_n = c$.

Now, let's take the limit of the equation $f^{(n+1)}(\xi_n) = f(\xi_n)$ as $n \to \infty$.
The right-hand side is $\lim_{n \to \infty} f(\xi_n)$. Since $f$ is infinitely differentiable, it is continuous. As $\xi_n \to c$, by the continuity of $f$ at $c$, we have:
$$
\lim_{n \to \infty} f(\xi_n) = f(c).
$$
Therefore, we must have:
$$
\lim_{n \to \infty} f^{(n+1)}(\xi_n) = f(c).
$$
Our goal is to show that $\lim_{n \to \infty} f^{(n)}(c) = f(c)$. The result we have is very close. We need to show that $\lim_{n \to \infty} f^{(n+1)}(\xi_n)$ is the same as $\lim_{n \to \infty} f^{(n+1)}(c)$.

**Step 5: Use the uniform boundedness of derivatives**

We are given that all derivatives of $f$ are uniformly bounded. This means there exists a constant $M > 0$ such that $|f^{(k)}(x)| \le M$ for all $k \ge 0$ and for all $x \in (-1,1)$.

Let's consider the difference $|f^{(n+1)}(\xi_n) - f^{(n+1)}(c)|$. By the Mean Value Theorem, applied to the function $f^{(n+1)}(x)$, there exists a point $\eta_n$ between $\xi_n$ and $c$ such that:
$$
f^{(n+1)}(\xi_n) - f^{(n+1)}(c) = f^{(n+2)}(\eta_n) (\xi_n - c).
$$
Taking the absolute value:
$$
|f^{(n+1)}(\xi_n) - f^{(n+1)}(c)| = |f^{(n+2)}(\eta_n)| |\xi_n - c|.
$$
Using the uniform bound, $|f^{(n+2)}(\eta_n)| \le M$. So, we have the inequality:
$$
|f^{(n+1)}(\xi_n) - f^{(n+1)}(c)| \le M |\xi_n - c|.
$$
As $n \to \infty$, we know that $\xi_n \to c$, which means $|\xi_n - c| \to 0$. Therefore,
$$
\lim_{n \to \infty} |f^{(n+1)}(\xi_n) - f^{(n+1)}(c)| \le \lim_{n \to \infty} (M |\xi_n - c|) = 0.
$$
This implies $\lim_{n \to \infty} (f^{(n+1)}(\xi_n) - f^{(n+1)}(c)) = 0$, which means:
$$
\lim_{n \to \infty} f^{(n+1)}(\xi_n) = \lim_{n \to \infty} f^{(n+1)}(c).
$$

**Step 6: Combine the results to reach the conclusion**

From Step 4, we established:
$$
\lim_{n \to \infty} f^{(n+1)}(\xi_n) = f(c).
$$
From Step 5, we established:
$$
\lim_{n \to \infty} f^{(n+1)}(\xi_n) = \lim_{n \to \infty} f^{(n+1)}(c).
$$
Combining these two results, we get:
$$
\lim_{n \to \infty} f^{(n+1)}(c) = f(c).
$$
This is a limit statement about the sequence of values $(f^{(2)}(c), f^{(3)}(c), f^{(4)}(c), \dots)$. Let $m = n+1$. As $n \to \infty$, $m \to \infty$. The statement is equivalent to:
$$
\lim_{m \to \infty} f^{(m)}(c) = f(c).
$$
This is precisely what we were asked to show.

### **Conclusion**

By defining an auxiliary function $H_n(x) = e^{-x} \sum_{k=0}^n f^{(k)}(x)$, we used the given condition to apply Rolle's Theorem, which yielded the relation $f^{(n+1)}(\xi_n) = f(\xi_n)$ for some $\xi_n \in (a_n, b_n)$. The Squeeze Theorem on $\xi_n$ showed that $\xi_n \to c$. Using the continuity of $f$ and the uniform boundedness of its derivatives (via the Mean Value Theorem), we were able to take the limit as $n \to \infty$ and show that $\lim_{n \to \infty} f^{(n+1)}(c) = f(c)$, which is equivalent to the desired result $\lim_{n \to \infty} f^{(n)}(c) = f(c)$.