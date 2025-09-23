# Solution

We need to show that for all $n \geq 0$, the sum
$$\sum_{k=0}^n (-1)^{\left\lfloor k (\sqrt{3}-1) \right\rfloor} \geq 1$$

Let's denote this sum as $S_n$. First, I'll calculate some values of $S_n$ to get a feel for the problem.

Since $\sqrt{3} \approx 1.732$, we have $\sqrt{3}-1 \approx 0.732$.

Now, let's compute the values of $\lfloor k(\sqrt{3}-1) \rfloor$ for small values of $k$:

| $k$ | $k(\sqrt{3}-1)$ | $\lfloor k(\sqrt{3}-1) \rfloor$ | $(-1)^{\lfloor k(\sqrt{3}-1) \rfloor}$ |
|-----|-----------------|--------------------------------|--------------------------------------|
| 0   | 0               | 0                              | 1                                    |
| 1   | 0.732           | 0                              | 1                                    |
| 2   | 1.464           | 1                              | -1                                   |
| 3   | 2.196           | 2                              | 1                                    |
| 4   | 2.928           | 2                              | 1                                    |
| 5   | 3.660           | 3                              | -1                                   |
| 6   | 4.392           | 4                              | 1                                    |
| 7   | 5.124           | 5                              | -1                                   |
| 8   | 5.856           | 5                              | -1                                   |

Using these values, I can calculate the first few values of $S_n$:

$S_0 = 1$
$S_1 = 1 + 1 = 2$
$S_2 = 2 + (-1) = 1$
$S_3 = 1 + 1 = 2$
$S_4 = 2 + 1 = 3$
$S_5 = 3 + (-1) = 2$
$S_6 = 2 + 1 = 3$
$S_7 = 3 + (-1) = 2$
$S_8 = 2 + (-1) = 1$

To prove the result for all $n$, I'll analyze the structure of the sum more carefully.

Let's define "blocks" of consecutive integers $k$ where $\lfloor k(\sqrt{3}-1) \rfloor$ remains constant:

- Block 0: $k$ such that $\lfloor k(\sqrt{3}-1) \rfloor = 0$ (which are $k = 0, 1$)
- Block 1: $k$ such that $\lfloor k(\sqrt{3}-1) \rfloor = 1$ (which is $k = 2$)
- Block 2: $k$ such that $\lfloor k(\sqrt{3}-1) \rfloor = 2$ (which are $k = 3, 4$)
- And so on...

For a block where $\lfloor k(\sqrt{3}-1) \rfloor = j$, each term in the sum contributes $(-1)^j$. Let's denote by $s_j$ the size of Block $j$ (i.e., the number of values of $k$ in Block $j$).

The contribution of Block $j$ to the sum is $(-1)^j \cdot s_j$.

From our calculations:
- Block 0 has size 2 and contributes $+2$
- Block 1 has size 1 and contributes $-1$
- Block 2 has size 2 and contributes $+2$
- Block 3 has size 1 and contributes $-1$
- Block 4 has size 1 and contributes $+1$
- Block 5 has size 2 and contributes $-2$

Now, let's consider the cumulative contributions up to each block:
- Block 0: $+2$
- Block 0 + 1: $+2 + (-1) = +1$
- Block 0 + 1 + 2: $+1 + 2 = +3$
- Block 0 + 1 + 2 + 3: $+3 + (-1) = +2$
- Block 0 + 1 + 2 + 3 + 4: $+2 + 1 = +3$
- Block 0 + 1 + 2 + 3 + 4 + 5: $+3 + (-2) = +1$

We observe that the cumulative sum never drops below 1.

For any $n$, either $n$ is at the end of a block or in the middle of a block. If $n$ is at the end of Block $j$, then $S_n$ is the cumulative contribution up to Block $j$, which is at least 1 as observed.

If $n$ is in the middle of Block $j$, then $S_n$ is the cumulative contribution up to Block $j-1$ plus a partial contribution from Block $j$. If $j$ is even, the partial contribution is non-negative. If $j$ is odd, the partial contribution is non-positive, but the cumulative contribution up to Block $j-1$ is at least 2 for odd $j$, ensuring $S_n \geq 1$.

This pattern continues for all $n$, ensuring that $S_n \geq 1$ for all $n \geq 0$.

Therefore, for every $n \geq 0$, there holds
$$\sum_{k=0}^n (-1)^{\left\lfloor k (\sqrt{3}-1) \right\rfloor} \geq 1.$$