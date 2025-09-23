This step is worth 1 point.
We consider the opposite situation and find probability $p$ that at least one vertex angle is acute. Note that the probability that any of the angles is right is equal to 0, since the uniform distribution is absolutely continuous with respect to Lebesgue measure. Hence the desired probability is equal to $1-p$.

This step is worth 2 points.
First we show that at most 2 vertex angles can be acute and they have to occur consecutively. To this end note that the angle at $P_k$ is acute if all other points lay on an open semicircle. Assume that $P,$ $Q$, $R$ are consecutive vertexes and angles in $P$ and $R$ are acute. Then all vertexes except $P$ lays on an open semicircle, and all vertexes except $R$ lay on an open semicircle. It means that this two open semicircles cover all circle, which is impossible.

This step is worth 4 points.
Let $P$, $Q$ be consecutive (in the clockwise order) vertexes such that the angle at $P$ is acute and the one at $Q$ is not. Let $P'$ be the antipode of $P$ and $Q'$ is the antipode of $Q$. Then we know that
* all other 2023 points lay on the arc $QQ'$ not containing $P$, since the angle at $P$ is acute;
* there exists at least one vertex lays on the arc $QP'$ not containing $P$, since the angle at $Q$ is not acute;
The probability of occurring this situation is $\left(\frac{1}{2}\right)^{2023} - x^{2023}$, where $x$ is the length of the arc $P'Q'$ not containing $P$ divided by the length of the circle. Knowing that $x\in(0,\frac{1}{2})$ we have that when $P$ and $Q$ are chosen, then probability that at least one angle is acute is equal to
$$
\int_0^\frac{1}{2}\left(\left(\frac{1}{2}\right)^{2023} - x^{2023}\right)dx = \frac{2023}{2^{2024}\cdot 2024}.
$$

This step is worth 3 points.
Since there are $2025\cdot 2024=4098600$ possible choices of $P$ and $Q$,
$$
p = \frac{4096575}{2^{2024}}
$$
and hence the answer is $1-\frac{4096575}{2^{2024}}.$