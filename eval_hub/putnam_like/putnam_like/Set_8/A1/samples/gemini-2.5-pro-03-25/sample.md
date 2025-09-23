Solution:
Let $\alpha = 1/\sqrt{3}$. We are given $q \in (0,1)$ is a rational number. Let $q = a/b$, where $a, b$ are positive integers with $\gcd(a,b)=1$ and $0 < a < b$. We want to show that
\[
\left|q - \frac{1}{\sqrt{3}}\right| > \frac{1}{9b^2}.
\]
Consider the polynomial $P(x) = 3x^2 - 1$. The number $\alpha = 1/\sqrt{3}$ is a root of $P(x)$, since $P(1/\sqrt{3}) = 3(1/\sqrt{3})^2 - 1 = 3(1/3) - 1 = 1 - 1 = 0$.

Let $q = a/b$. Evaluate $P(q)$:
\[
P(q) = P(a/b) = 3\left(\frac{a}{b}\right)^2 - 1 = \frac{3a^2}{b^2} - 1 = \frac{3a^2 - b^2}{b^2}.
\]
Since $a$ and $b$ are integers, $3a^2 - b^2$ is an integer.
Could $3a^2 - b^2 = 0$? If $3a^2 - b^2 = 0$, then $3a^2 = b^2$. Since $q \in (0,1)$, we have $a \ge 1$. Then $b/a = \sqrt{3}$. But $\sqrt{3}$ is an irrational number, and $a, b$ are integers, so this is impossible.
Therefore, $3a^2 - b^2$ must be a non-zero integer. This implies that $|3a^2 - b^2| \ge 1$.

Now consider the absolute value of $P(q)$:
\[
|P(q)| = \left|\frac{3a^2 - b^2}{b^2}\right| = \frac{|3a^2 - b^2|}{b^2} \ge \frac{1}{b^2}.
\]

By the Mean Value Theorem, applied to the function $P(x)$ on the interval between $q$ and $\alpha$, there exists a number $c$ strictly between $q$ and $\alpha$ such that
\[
P(q) - P(\alpha) = P'(c) (q - \alpha).
\]
Since $P(\alpha)=0$, we have $P(q) = P'(c)(q-\alpha)$.
The derivative of $P(x)$ is $P'(x) = 6x$. So, $P(q) = 6c (q - \alpha)$.
Taking the absolute value of both sides:
\[
|P(q)| = |6c| |q - \alpha|.
\]
We can express $|q - \alpha|$ as:
\[
|q - \alpha| = \frac{|P(q)|}{|6c|}.
\]
Using the inequality $|P(q)| \ge 1/b^2$, we get:
\[
|q - \alpha| \ge \frac{1/b^2}{|6c|} = \frac{1}{6|c|b^2}.
\]
We need to find a bound for $|c|$. The number $c$ lies strictly between $q$ and $\alpha$.
We are given $q \in (0, 1)$. We know $\alpha = 1/\sqrt{3}$. Since $1 < 3 < 4$, we have $1 < \sqrt{3} < 2$. So $1/2 < 1/\sqrt{3} < 1$. Thus $\alpha \in (1/2, 1)$.
Since $q \in (0,1)$ and $\alpha \in (0,1)$, the number $c$ must lie in the interval $(0, 1)$.
Therefore, $0 < c < 1$, which implies $|c| = c < 1$.
Then $6|c| = 6c < 6$.
Substituting this into the inequality for $|q - \alpha|$:
\[
|q - \alpha| \ge \frac{1}{6cb^2} > \frac{1}{6b^2}.
\]
We want to show that $|q - \alpha| > 1/(9b^2)$.
Since $6 < 9$, we have $1/6 > 1/9$.
Therefore,
\[
|q - \alpha| > \frac{1}{6b^2} > \frac{1}{9b^2}.
\]
Thus, we have shown that
\[
\left|q - \frac{1}{\sqrt{3}}\right| > \frac{1}{9b^2}.
\]

Final Answer: The final answer is $\boxed{\left|q-\frac{1}{\sqrt{3}}\right| > \frac{1}{9b^2}}$