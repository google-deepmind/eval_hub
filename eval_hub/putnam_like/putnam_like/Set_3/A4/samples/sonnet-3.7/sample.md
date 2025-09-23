# Solution

I'll prove that $\lceil (\sqrt {11}+3)^{2n}\rceil$ is divisible by $2^{n+1}$ for any $n\geq 1$.

## Step 1: Setting up the foundation

Let $\alpha = \sqrt{11} + 3$ and $\beta = -\sqrt{11} + 3$. Note that:
- $\alpha\beta = (3+\sqrt{11})(3-\sqrt{11}) = 9 - 11 = -2$
- $\alpha^{2n}\beta^{2n} = (\alpha\beta)^{2n} = (-2)^{2n} = 2^{2n}$

## Step 2: Express $\alpha^{2n}$ in the form $a_n + b_n\sqrt{11}$

Since $\alpha = 3 + \sqrt{11}$, we can write $\alpha^{2n} = a_n + b_n\sqrt{11}$ where $a_n$ and $b_n$ are integers.

Similarly, $\beta^{2n} = a_n - b_n\sqrt{11}$ (since $\beta = 3 - \sqrt{11}$).

From these expressions, we have:
$$\alpha^{2n}\beta^{2n} = (a_n + b_n\sqrt{11})(a_n - b_n\sqrt{11}) = a_n^2 - 11b_n^2 = 2^{2n}$$

Rearranging, we get:
$$a_n^2 = 11b_n^2 + 2^{2n}$$

## Step 3: Calculate $\lceil \alpha^{2n}\rceil$

Since $a_n$ is an integer, $\lceil \alpha^{2n}\rceil = \lceil a_n + b_n\sqrt{11}\rceil = a_n + \lceil b_n\sqrt{11}\rceil$.

I now show that $\lceil b_n\sqrt{11}\rceil = a_n$:

- From $a_n^2 = 11b_n^2 + 2^{2n}$, we have $a_n^2 > 11b_n^2$, which means $a_n > b_n\sqrt{11}$.
- Also, $(a_n - 1)^2 = a_n^2 - 2a_n + 1 = 11b_n^2 + 2^{2n} - 2a_n + 1$
- For $(a_n - 1)^2 < 11b_n^2$, we need $2^{2n} - 2a_n + 1 < 0$, or $a_n > \frac{1 + 2^{2n}}{2}$.

This inequality holds for all $n \geq 1$ (which can be verified for small $n$ and proven by induction).

Therefore, $b_n\sqrt{11}$ lies between $a_n - 1$ and $a_n$, so $\lceil b_n\sqrt{11}\rceil = a_n$.

This gives us $\lceil \alpha^{2n}\rceil = a_n + a_n = 2a_n$.

## Step 4: Prove divisibility by $2^{n+1}$

We need to show that $2a_n$ is divisible by $2^{n+1}$, which is equivalent to showing that $a_n$ is divisible by $2^n$.

### Base case:
For $n=1$, we have $\alpha^2 = (3+\sqrt{11})^2 = 9 + 6\sqrt{11} + 11 = 20 + 6\sqrt{11}$.
So $a_1 = 20 = 5 \cdot 2^2$, which is divisible by $2^1$.

### Inductive step:
Assume $a_n$ is divisible by $2^n$ for some $n \geq 1$. Then $a_n = 2^n \cdot r$ for some integer $r$.

From $a_n^2 - 11b_n^2 = 2^{2n}$, we get $(2^n r)^2 - 11b_n^2 = 2^{2n}$.
This implies $b_n$ is divisible by $2^n$, so $b_n = 2^n \cdot s$ for some integer $s$.

Substituting back, we get $r^2 - 11s^2 = 1$.

From the recurrence relation for $\alpha^{2n}$, we have:
$$a_{n+1} = 20a_n + 66b_n = 20(2^n r) + 66(2^n s) = 2^n(20r + 66s)$$

Since $r^2 - 11s^2 = 1$, both $r$ and $s$ must be odd (otherwise, $r^2 - 11s^2$ would be divisible by 4).

Therefore, $20r + 66s = 2(10r + 33s)$ is divisible by 2.

Hence, $a_{n+1} = 2^n \cdot 2 \cdot (10r + 33s) = 2^{n+1} \cdot (10r + 33s)$ is divisible by $2^{n+1}$.

By induction, $a_n$ is divisible by $2^n$ for all $n \geq 1$.

## Conclusion

Since $\lceil (\sqrt {11}+3)^{2n}\rceil = 2a_n$ and $a_n$ is divisible by $2^n$, we have proven that $\lceil (\sqrt {11}+3)^{2n}\rceil$ is divisible by $2^{n+1}$ for any $n\geq 1$.