This step is worth 2 points.
* (a) Yes. Let $P_2(x) = a_2 x^2 + a_1 x + a_0$. Then it is enough to take $P(x) = a_0 x^2 + a_1 x + a_2$. Indeed, we have
$$
k^2 P \left( \frac{1}{k^2} \right) = k^2 \left( a_0 \frac{1}{k^2} + a_1 \frac{1}{k} + a_2 \right) = a_0 + a_1 k + a_2 k^2 = P_2(k).
$$

This step is worth 8 points.
* (b) No. Suppose by contradiction that such a polynomial $Q$ exists. Let $P_1(x) = b_1 x + b_0$ and $P_2(x) = a_2 x^2 + a_1 x + a_0$. Consider the polynomial
$$
W(x) = (a_2 + a_1 x + a_0 x^2) x Q(x) - (b_1 x + b_0 x^2).
$$
Then, for every $k \in \mathbb{Z}$,
$$
\begin{aligned}
W\left( \frac{1}{k} \right) &= \left(a_2 + \frac{a_1}{k} + \frac{a_0}{k^2}\right) \frac{1}{k} Q\left(\frac{1}{k}\right) - \left(\frac{b_1}{k} + \frac{b_0}{k^2}\right) \\
&= \left(a_2 + \frac{a_1}{k} + \frac{a_0}{k^2}\right) \frac{b_1 k + b_0}{a_2 k^2 + a_1 k + a_0} - \left(\frac{b_1}{k} + \frac{b_0}{k^2}\right) \\
&= \frac{a_2 k^2 + a_1 k + a_0}{k^2} \cdot \frac{b_1 k + b_0}{a_2 k^2 + a_1 k + a_0} - \frac{b_1 k + b_0}{k^2} \\
&= \frac{b_1 k + b_0}{k^2} - \frac{b_1 k + b_0}{k^2} = 0.
\end{aligned}
$$
Hence $W$ has infinitely many zeros and therefore $W \equiv 0$. This means that
$$
Q(x) = \frac{b_1 x + b_0 x^2}{x (a_2 + a_1 x + a_0 x^2)} = \frac{b_1 + b_0 x}{a_2 + a_1 x + a_0 x^2},
$$
which is a contradiction with the fact that $Q$ is a polynomial (since the numerator has a smaller degree than the denominator).