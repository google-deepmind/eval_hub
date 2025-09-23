# Solution

I'll tackle this step-by-step by analyzing the expected value of the final drawn ball.

## Understanding the Problem

We have $n$ boxes, each containing $k$ balls labeled with number $k$ for $k = 1, 2, ..., m$. We perform a sequence of moves:
1. Draw a ball from box 1 and put it into box 2
2. Draw a ball from box 2 and put it into box 3
3. Continue until drawing a ball from box $n$

The question asks for which values of $m$ the expected value of the final drawn number is an integer.

## Computing the Expected Value

Let me define $X_i$ as the random variable representing the number on the ball drawn from box $i$ (either to transfer to box $i+1$ or to write down in case of box $n$).

### For Box 1
Initially, box 1 has $k$ balls with number $k$ for each $k = 1,2,...,m$.
- Total number of balls: $1+2+...+m = \frac{m(m+1)}{2}$
- Probability of drawing a ball with number $k$: $\frac{k}{\frac{m(m+1)}{2}}$

So the expected value is:
$$E[X_1] = \sum_{k=1}^{m} k \cdot \frac{k}{\frac{m(m+1)}{2}} = \frac{\sum_{k=1}^{m} k^2}{\frac{m(m+1)}{2}}$$

Using the formula $\sum_{k=1}^{m} k^2 = \frac{m(m+1)(2m+1)}{6}$:

$$E[X_1] = \frac{\frac{m(m+1)(2m+1)}{6}}{\frac{m(m+1)}{2}} = \frac{2m+1}{3}$$

### For Box $i$ (where $i \geq 2$)
Box $i$ has its original distribution of balls plus one ball from box $i-1$. Let's derive a recursive relation for $E[X_i]$.

After receiving a ball from box $i-1$, box $i$ has $\frac{m(m+1)}{2} + 1$ balls. The probability of drawing the transferred ball is $\frac{1}{\frac{m(m+1)}{2} + 1}$, and this ball has an expected value of $E[X_{i-1}]$.

Therefore:
$$E[X_i] = \frac{1}{\frac{m(m+1)}{2} + 1} \cdot E[X_{i-1}] + \frac{1}{\frac{m(m+1)}{2} + 1} \cdot \sum_{k=1}^{m} k \cdot k$$

$$E[X_i] = \frac{E[X_{i-1}] + \frac{m(m+1)(2m+1)}{6}}{\frac{m(m+1)}{2} + 1}$$

For simplicity, let's denote $S = \frac{m(m+1)}{2}$ and $T = \frac{m(m+1)(2m+1)}{6}$. The recursive formula becomes:
$$E[X_i] = \frac{E[X_{i-1}] + T}{S + 1}$$

Given that $E[X_1] = \frac{T}{S} = \frac{2m+1}{3}$, let's compute $E[X_2]$:
$$E[X_2] = \frac{E[X_1] + T}{S + 1} = \frac{\frac{T}{S} + T}{S + 1} = \frac{T(\frac{S+1}{S})}{S + 1} = \frac{T}{S} = \frac{2m+1}{3}$$

We can verify that this pattern continues, so $E[X_i] = \frac{2m+1}{3}$ for all $i$ including $i = n$.

## Determining when $E[X_n]$ is an Integer

The expected value $\frac{2m+1}{3}$ is an integer if and only if $2m+1$ is divisible by 3.
This happens when $2m+1 \equiv 0 \pmod{3}$, which is equivalent to $m \equiv 1 \pmod{3}$.

Therefore, the values of $m$ for which the expected value is an integer are:
$$m = 1, 4, 7, 10, \ldots$$

Or generally, $m = 3k+1$ for any non-negative integer $k$.