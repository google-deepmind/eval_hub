```markdown
Let $N=2024$.
The boxes are numbered from 0 to $N$. There are $N+1$ boxes in total.
Box $k$, for $k \in \{0, 1, \ldots, N\}$, contains $k$ white balls and $N-k$ black balls. The total number of balls in box $k$ is $k + (N-k) = N$.

Maria chooses one box randomly. Since there are $N+1$ boxes, the probability of choosing box $k$ is
$$P(\text{box } k) = \frac{1}{N+1} \quad \text{for } k = 0, 1, \ldots, N.$$

After choosing a box, Maria draws 3 balls with replacement from that box.
Let $W$ be the event that all three balls drawn are white.
Given that box $k$ is chosen, the probability of drawing a white ball in a single draw is $\frac{k}{N}$.
Since the draws are independent (with replacement), the probability of drawing 3 white balls from box $k$ is
$$P(W | \text{box } k) = \left(\frac{k}{N}\right)^3.$$

To find the total probability of drawing 3 white balls, we use the law of total probability, summing over all possible boxes:
$$P(W) = \sum_{k=0}^{N} P(W | \text{box } k) P(\text{box } k)$$
Substitute the probabilities we found:
$$P(W) = \sum_{k=0}^{N} \left(\frac{k}{N}\right)^3 \frac{1}{N+1}$$
$$P(W) = \frac{1}{N+1} \sum_{k=0}^{N} \frac{k^3}{N^3}$$
$$P(W) = \frac{1}{N^3(N+1)} \sum_{k=0}^{N} k^3$$

The sum of the first $N$ cubes (starting from 0) is given by the formula $\sum_{k=0}^{N} k^3 = \sum_{k=1}^{N} k^3 = \left(\frac{N(N+1)}{2}\right)^2$.
Substitute this sum into the expression for $P(W)$:
$$P(W) = \frac{1}{N^3(N+1)} \left(\frac{N(N+1)}{2}\right)^2$$
$$P(W) = \frac{1}{N^3(N+1)} \frac{N^2(N+1)^2}{4}$$
$$P(W) = \frac{N^2(N+1)^2}{4N^3(N+1)}$$

Now, we simplify the expression by cancelling common factors. We can cancel $N^2$ from the numerator and denominator, and $(N+1)$ from the numerator and denominator:
$$P(W) = \frac{N+1}{4N}$$

Finally, we substitute the given value $N=2024$:
$$P(W) = \frac{2024+1}{4 \times 2024}$$
$$P(W) = \frac{2025}{8096}$$

The fraction $\frac{2025}{8096}$ is in simplest form because the prime factorization of $2025 = 3^4 \times 5^2$ and the prime factorization of $8096 = 2^5 \times 11 \times 23$ have no common factors.

The final answer is $\boxed{\frac{2025}{8096}}$.
```