Solution:
Let $A = \left(\prod_{i=1}^n a_i\right)^\frac 1n$, $B = \left(\prod_{i=1}^n b_i\right)^\frac 1n$, and $C = \left(\prod_{i=1}^n c_i\right)^\frac 1n$.
Let $S_i = a_i+b_i+c_i$ for $i=1,\ldots,n$.
The inequality we want to prove is
\[ A+B+C \leq \left(\prod_{i=1}^n S_i\right)^\frac 1n \]

First, consider the case where $S_i = 0$ for at least one index $i \in \{1, \ldots, n\}$.
Since $a_i, b_i, c_i$ are nonnegative real numbers, $S_i = a_i+b_i+c_i = 0$ implies that $a_i=0$, $b_i=0$, and $c_i=0$.
If $a_i=0$ for some $i$, then the product $\prod_{j=1}^n a_j = 0$, so $A = 0^{1/n} = 0$.
Similarly, if $b_i=0$, then $B=0$, and if $c_i=0$, then $C=0$.
Since $a_i=b_i=c_i=0$, we have $A=B=C=0$.
The left hand side (LHS) of the inequality is $A+B+C = 0+0+0 = 0$.
The right hand side (RHS) of the inequality is $\left(\prod_{j=1}^n S_j\right)^\frac 1n$. Since $S_i=0$ for some $i$, the product $\prod_{j=1}^n S_j = 0$.
So the RHS is $0^{1/n} = 0$.
The inequality becomes $0 \leq 0$, which is true.
Thus, the inequality holds if $S_i=0$ for any $i$.

Now, assume that $S_i > 0$ for all $i=1,\ldots,n$.
Let $x_i = \frac{a_i}{S_i}$, $y_i = \frac{b_i}{S_i}$, $z_i = \frac{c_i}{S_i}$.
Since $a_i, b_i, c_i \ge 0$ and $S_i > 0$, we have $x_i, y_i, z_i \ge 0$.
Also, for each $i$, we have
\[ x_i+y_i+z_i = \frac{a_i}{S_i} + \frac{b_i}{S_i} + \frac{c_i}{S_i} = \frac{a_i+b_i+c_i}{S_i} = \frac{S_i}{S_i} = 1. \]
Let $P_S = \left(\prod_{i=1}^n S_i\right)^\frac 1n$. Since $S_i > 0$ for all $i$, we have $P_S > 0$.
We can divide the inequality by $P_S$:
\[ \frac{A}{P_S} + \frac{B}{P_S} + \frac{C}{P_S} \leq 1 \]
Let's rewrite the terms on the LHS:
\[ \frac{A}{P_S} = \frac{\left(\prod_{i=1}^n a_i\right)^\frac 1n}{\left(\prod_{i=1}^n S_i\right)^\frac 1n} = \left(\frac{\prod_{i=1}^n a_i}{\prod_{i=1}^n S_i}\right)^\frac 1n = \left(\prod_{i=1}^n \frac{a_i}{S_i}\right)^\frac 1n = \left(\prod_{i=1}^n x_i\right)^\frac 1n \]
Similarly,
\[ \frac{B}{P_S} = \left(\prod_{i=1}^n y_i\right)^\frac 1n \]
\[ \frac{C}{P_S} = \left(\prod_{i=1}^n z_i\right)^\frac 1n \]
So the inequality we need to prove is equivalent to
\[ \left(\prod_{i=1}^n x_i\right)^\frac 1n + \left(\prod_{i=1}^n y_i\right)^\frac 1n + \left(\prod_{i=1}^n z_i\right)^\frac 1n \leq 1 \]
where $x_i, y_i, z_i \ge 0$ and $x_i+y_i+z_i=1$ for all $i$.

Let $X = \left(\prod_{i=1}^n x_i\right)^\frac 1n$, $Y = \left(\prod_{i=1}^n y_i\right)^\frac 1n$, $Z = \left(\prod_{i=1}^n z_i\right)^\frac 1n$.
By the Arithmetic Mean - Geometric Mean (AM-GM) inequality, for any nonnegative numbers $w_1, \ldots, w_n$, we have $\left(\prod_{i=1}^n w_i\right)^\frac 1n \leq \frac{1}{n} \sum_{i=1}^n w_i$.
Applying the AM-GM inequality to the sequences $(x_i)$, $(y_i)$, and $(z_i)$:
\[ X = \left(\prod_{i=1}^n x_i\right)^\frac 1n \leq \frac{1}{n} \sum_{i=1}^n x_i \]
\[ Y = \left(\prod_{i=1}^n y_i\right)^\frac 1n \leq \frac{1}{n} \sum_{i=1}^n y_i \]
\[ Z = \left(\prod_{i=1}^n z_i\right)^\frac 1n \leq \frac{1}{n} \sum_{i=1}^n z_i \]
Summing these three inequalities, we get:
\[ X+Y+Z \leq \frac{1}{n} \sum_{i=1}^n x_i + \frac{1}{n} \sum_{i=1}^n y_i + \frac{1}{n} \sum_{i=1}^n z_i \]
\[ X+Y+Z \leq \frac{1}{n} \sum_{i=1}^n (x_i + y_i + z_i) \]
Since $x_i+y_i+z_i = 1$ for all $i=1,\ldots,n$, the sum becomes:
\[ X+Y+Z \leq \frac{1}{n} \sum_{i=1}^n 1 = \frac{1}{n} \cdot n = 1 \]
Thus, we have shown that $X+Y+Z \leq 1$. This proves the inequality for the case where $S_i > 0$ for all $i$.

Combining both cases ($S_i=0$ for some $i$, and $S_i>0$ for all $i$), the inequality holds for all nonnegative real numbers $a_i, b_i, c_i$.

Final Answer: The final answer is $\boxed{\left(\prod_{i=1}^n a_i\right)^\frac 1n+\left(\prod_{i=1}^n b_i\right)^\frac 1n+\left(\prod_{i=1}^n c_i\right)^\frac 1n\leq \left(\prod_{i=1}^n (a_i+b_i+c_i)\right)^\frac 1n}$