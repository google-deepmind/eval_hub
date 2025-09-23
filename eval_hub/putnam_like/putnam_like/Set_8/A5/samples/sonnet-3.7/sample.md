# Solution

I'll analyze the function $f_n(x) =\prod_{i=1}^{n}\cos((2i-1)x)$ and find the $\liminf_{n\to\infty}\int_0^{2\pi}f_n(x)dx$.

## Step 1: Express $f_n(x)$ using complex exponentials

Using Euler's identity, I can rewrite each cosine term:
$$\cos((2i-1)x) = \frac{e^{i(2i-1)x} + e^{-i(2i-1)x}}{2}$$

This gives:
$$f_n(x) = \prod_{i=1}^{n}\frac{e^{i(2i-1)x} + e^{-i(2i-1)x}}{2} = \frac{1}{2^n}\sum_{(\epsilon_1,...,\epsilon_n) \in \{-1,1\}^n} e^{ix\sum_{i=1}^{n}\epsilon_i(2i-1)}$$

where the sum is over all possible sign combinations $\epsilon_i \in \{-1,1\}$.

## Step 2: Evaluate the integral

When integrating over $[0,2\pi]$, we have:
$$\int_0^{2\pi}e^{ikx}dx = \begin{cases}
2\pi & \text{if }k=0 \\
0 & \text{if }k\neq 0
\end{cases}$$

Therefore:
$$\int_0^{2\pi}f_n(x)dx = \frac{2\pi}{2^n}|S_n|$$

where $S_n$ is the set of sign combinations $(\epsilon_1,...,\epsilon_n)$ such that $\sum_{i=1}^{n}\epsilon_i(2i-1) = 0$.

## Step 3: Analyze $S_n$ for odd and even values of $n$

For odd $n$:
- Each term $\epsilon_i(2i-1)$ is odd (as each $(2i-1)$ is odd)
- A sum of an odd number of odd terms is always odd
- Therefore, $\sum_{i=1}^{n}\epsilon_i(2i-1)$ can never be zero
- This means $|S_n| = 0$ for all odd $n$

For even $n$:
- The sum can potentially be zero
- Using probabilistic methods and the central limit theorem, it can be shown that $\frac{|S_n|}{2^n} = O(n^{-3/2})$
- As $n \to \infty$, this ratio approaches zero

## Step 4: Determine the $\liminf$

The sequence of integrals is:
- For odd $n$: $\int_0^{2\pi}f_n(x)dx = 0$
- For even $n$: $\int_0^{2\pi}f_n(x)dx = \frac{2\pi}{2^n}|S_n|$, which approaches 0 as $n \to \infty$

Since there is a subsequence (the odd terms) that is constantly zero, and all values in the sequence are non-negative, we have:

$$\liminf_{n\to\infty}\int_0^{2\pi}f_n(x)dx = 0$$