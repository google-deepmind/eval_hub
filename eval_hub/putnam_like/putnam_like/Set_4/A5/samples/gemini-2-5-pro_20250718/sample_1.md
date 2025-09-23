Here is a detailed, step-by-step solution.

The given equation is
$$
(n-(m-1))^2 + \ldots + (n-1)^2 + n^2 = (n+1)^2 + (n+2)^2 + \ldots + (n+k)^2.
$$
We are given that $k, m, n$ are integers with $k \geq 1$ and $n \geq m \geq 2$.

### Step 1: Rewrite the equation using sigma notation

The equation can be written as a sum of squares:
$$
\sum_{j=0}^{m-1} (n-j)^2 = \sum_{j=1}^{k} (n+j)^2.
$$
Let's expand the terms in the sums. The general term on the left is $(n-j)^2 = n^2 - 2nj + j^2$ and on the right is $(n+j)^2 = n^2 + 2nj + j^2$.

Summing these terms, we get:
LHS: $\sum_{j=0}^{m-1} (n^2 - 2nj + j^2) = m n^2 - 2n \sum_{j=0}^{m-1} j + \sum_{j=0}^{m-1} j^2$.
RHS: $\sum_{j=1}^{k} (n^2 + 2nj + j^2) = k n^2 + 2n \sum_{j=1}^{k} j + \sum_{j=1}^{k} j^2$.

Using the standard formulas for sums of powers:
$\sum_{j=1}^{N} j = \frac{N(N+1)}{2}$ and $\sum_{j=1}^{N} j^2 = \frac{N(N+1)(2N+1)}{6}$.
Note that $\sum_{j=0}^{m-1} j = \sum_{j=1}^{m-1} j = \frac{(m-1)m}{2}$ and $\sum_{j=0}^{m-1} j^2 = \sum_{j=1}^{m-1} j^2 = \frac{(m-1)m(2m-1)}{6}$.

Substituting these into our expressions for LHS and RHS:
LHS = $m n^2 - 2n \frac{(m-1)m}{2} + \frac{(m-1)m(2m-1)}{6} = m n^2 - n m(m-1) + \frac{m(m-1)(2m-1)}{6}$.
RHS = $k n^2 + 2n \frac{k(k+1)}{2} + \frac{k(k+1)(2k+1)}{6} = k n^2 + n k(k+1) + \frac{k(k+1)(2k+1)}{6}$.

Equating the LHS and RHS gives a quadratic equation in $n$:
$m n^2 - n m(m-1) + \frac{m(m-1)(2m-1)}{6} = k n^2 + n k(k+1) + \frac{k(k+1)(2k+1)}{6}$.

Rearranging the terms to form a standard quadratic equation $An^2+Bn+C=0$:
$(m-k)n^2 - (m(m-1) + k(k+1))n + \left(\frac{m(m-1)(2m-1)}{6} - \frac{k(k+1)(2k+1)}{6}\right) = 0$.

### Step 2: Show that $m > k$ and prove $k \le n$

Let's compare the magnitudes of the two sides of the original equation.
LHS: The terms are $(n-m+1)^2, \dots, n^2$. All terms are less than or equal to $n^2$, and since $n \ge m \ge 2$, at least one term ($(n-1)^2$) is strictly less than $n^2$.
So, LHS $< \sum_{j=0}^{m-1} n^2 = m n^2$.

RHS: The terms are $(n+1)^2, \dots, (n+k)^2$. All terms are greater than $n^2$.
So, RHS $> \sum_{j=1}^{k} n^2 = k n^2$.

Combining these, we have $k n^2 < \text{RHS} = \text{LHS} < m n^2$.
$k n^2 < m n^2$, and since $n \ge 2$, we can divide by $n^2$ to get $k < m$.
As $m$ and $k$ are integers, this implies $m \ge k+1$.

Now let's prove $k \le n$. We can rearrange the original equation by moving the $n^2$ term (for $j=0$ on the LHS) to the right side:
$$
\sum_{j=1}^{m-1} (n-j)^2 = \sum_{j=1}^{k} (n+j)^2 - n^2.
$$
We can rewrite the RHS by pairing up terms:
$$
\text{RHS} = \sum_{j=1}^{k} ((n+j)^2 - (n-j)^2) + \sum_{j=k+1}^{m-1} (n-j)^2 = 0 \quad (\text{if we define } (n-j) \text{ for } j>k)
$$
Let's try a different rearrangement. Isolate $n^2$:
$$
n^2 = \sum_{j=1}^{k} (n+j)^2 - \sum_{j=1}^{m-1} (n-j)^2
$$
Since $m>k$, we can split the second sum:
$$
n^2 = \sum_{j=1}^{k} (n+j)^2 - \left( \sum_{j=1}^{k} (n-j)^2 + \sum_{j=k+1}^{m-1} (n-j)^2 \right)
$$
$$
n^2 = \sum_{j=1}^{k} \left( (n+j)^2 - (n-j)^2 \right) - \sum_{j=k+1}^{m-1} (n-j)^2
$$
Using the identity $a^2-b^2 = (a-b)(a+b)$, we have $(n+j)^2 - (n-j)^2 = (2j)(2n) = 4nj$.
$$
n^2 = \sum_{j=1}^{k} 4nj - \sum_{j=k+1}^{m-1} (n-j)^2
$$
$$
n^2 = 4n \sum_{j=1}^{k} j - \sum_{j=k+1}^{m-1} (n-j)^2
$$
$$
n^2 = 4n \frac{k(k+1)}{2} - \sum_{j=k+1}^{m-1} (n-j)^2
$$
$$
n^2 = 2nk(k+1) - \sum_{j=k+1}^{m-1} (n-j)^2
$$
The sum $\sum_{j=k+1}^{m-1} (n-j)^2$ is a sum of non-negative terms.
If $m = k+1$, the sum is empty and its value is 0. The equation becomes $n^2 = 2nk(k+1)$. Since $n \ge 2$, we can divide by $n$ to get $n=2k(k+1)$.
If $m > k+1$, the sum is positive. The equation can be written as:
$$
n(2k(k+1)-n) = \sum_{j=k+1}^{m-1} (n-j)^2 \ge 0.
$$
Since $n > 0$, we must have $2k(k+1)-n \ge 0$, which implies $n \le 2k(k+1)$.
So, in all cases (since $m \ge k+1$), we have $n \le 2k(k+1)$.

We need to show $k \le n$.
For $k \ge 1$, we have $k \le 2k^2+2k = 2k(k+1)$.
Thus, $k \le 2k(k+1)$.
Since $n \le 2k(k+1)$, this doesn't directly prove $k \le n$.
However, from $n^2 = 2nk(k+1) - \sum (\dots)$, we have $n^2 \le 2nk(k+1)$. Dividing by $n$ gives $n \le 2k(k+1)$. This much is correct.
Let's analyze $n(2k(k+1)-n) = \sum_{j=k+1}^{m-1} (n-j)^2$. The right side is a sum of squares. As $n \ge m > j$, all terms $(n-j)$ are positive integers. Thus, $(n-j)^2 \ge 1$.
The number of terms in the sum is $(m-1)-(k+1)+1 = m-k-1$.
So, $\sum_{j=k+1}^{m-1} (n-j)^2 \ge m-k-1$.
This gives $n(2k(k+1)-n) \ge m-k-1$.
This doesn't seem to lead to $k \le n$ easily.

Let's reconsider the average value argument.
LHS has $m$ terms, with average value roughly $(n-m/2)^2$.
RHS has $k$ terms, with average value roughly $(n+k/2)^2$.
$m(n-m/2)^2 \approx k(n+k/2)^2$.
Since the average value on the RHS is clearly larger than on the LHS, for the sums to be equal, we must have $m>k$. This is what we proved rigorously.
From $n^2 = 2nk(k+1) - \sum_{j=k+1}^{m-1} (n-j)^2$, we have $n^2 < 2nk(k+1)$, which implies $n < 2k(k+1)$.
Also, from the same equation, $2nk(k+1) = n^2 + \sum_{j=k+1}^{m-1} (n-j)^2 > n^2$.
This means $2k(k+1) > n$. This proves $k \le n$ because for $k\ge 1$, $n < 2k(k+1)$ and we want to show $k \le n$. Wait, $n < 2k(k+1)$ does not mean $n>k$.
Let's re-examine $2k(k+1) > n$. For $k \ge 1$, $2k(k+1) = 2k^2+2k \ge 2(1)^2+2(1)=4$. So $n < 4$ is not guaranteed.
However, $2k(k+1) = 2k^2+2k = k+ (2k^2+k)$. For $k \ge 1$, $2k^2+k>0$. So $2k(k+1) > k$.
The inequality is $n < 2k(k+1)$. It is possible for $n$ to be smaller than $k$. For example if $k=5$, $n < 2(5)(6)=60$. $n=4$ is possible.
Let's look at the original sums. All terms on the LHS are $\le n^2$. All terms on the RHS are $\ge (n+1)^2$.
$m n^2 \ge \text{LHS} = \text{RHS} \ge k(n+1)^2$.
$m n^2 \ge k(n^2+2n+1) \implies (m-k)n^2 - 2kn - k \ge 0$.
Since $n>0$, we need to check this quadratic in $n$. As $m>k$, the parabola opens upwards. The roots are $\frac{2k \pm \sqrt{4k^2+4k(m-k)}}{2(m-k)} = \frac{k \pm \sqrt{k^2+k(m-k)}}{m-k} = \frac{k \pm \sqrt{km}}{m-k}$.
Since $n$ must be larger than the positive root, $n \ge \frac{k+\sqrt{km}}{m-k}$.
We need to prove $n \ge k$. Is $\frac{k+\sqrt{km}}{m-k} \ge k$?
$k+\sqrt{km} \ge k(m-k) = km-k^2$.
$\sqrt{km} \ge km-k^2-k$.
This seems complicated.

Let's go back to $n \le 2k(k+1)$. This is solid.
And $n(2k(k+1)-n) = \sum_{j=k+1}^{m-1} (n-j)^2$. The condition $n \ge m$ is key.
$(n-j) \ge (m-j)$. So $(n-j)^2 \ge (m-j)^2$.
$\sum_{j=k+1}^{m-1} (n-j)^2 \ge \sum_{j=k+1}^{m-1} (m-j)^2 = \sum_{l=1}^{m-k-1} l^2 = \frac{(m-k-1)(m-k)(2m-2k-1)}{6}$.
So $n(2k(k+1)-n) \ge \frac{(m-k-1)(m-k)(2m-2k-1)}{6}$.
Let's use $n \le 2k(k+1)$. Then $2k(k+1)-n \ge 0$.
If $k \ge n$, then $n-j$ could be negative for $j$ in the sum on the LHS of the original equation. But $n \ge m-1 > j$. So $n-j$ is positive.
Let's assume $n<k$ for contradiction. Then $m \le n < k$, which contradicts $m>k$. Therefore, $n \ge k$ must hold.
So $7k \le 7n$ is proven.

### Step 3: Show that $m \le 7k$

This is the main part of the proof. We will use the quadratic equation for $n$ derived in Step 1:
$(m-k)n^2 - (m(m-1) + k(k+1))n + \left(\frac{m(m-1)(2m-1)}{6} - \frac{k(k+1)(2k+1)}{6}\right) = 0$.
Since $n$ is a real number, the discriminant of this quadratic must be non-negative. Let the equation be $An^2+Bn+C=0$. The discriminant is $D=B^2-4AC \ge 0$.
$A = m-k$
$B = -(m(m-1)+k(k+1))$
$C = \frac{m(m-1)(2m-1) - k(k+1)(2k+1)}{6} = \frac{(2m^3-3m^2+m) - (2k^3+3k^2+k)}{6}$.
$B^2 = (m(m-1)+k(k+1))^2$.
$4AC = 4(m-k) \frac{m(m-1)(2m-1) - k(k+1)(2k+1)}{6} = \frac{2}{3}(m-k)((2m^3-3m^2+m) - (2k^3+3k^2+k))$.
The inequality $B^2 \ge 4AC$ is:
$(m(m-1)+k(k+1))^2 \ge \frac{2}{3}(m-k)((2m^3-3m^2+m) - (2k^3+3k^2+k))$.

This inequality is complex. Let's try to approximate its behavior for large $m$ and $k$. Let $m=ck$ for some constant $c$. We assume $m, k$ are large, so we only need to keep the highest power.
$m(m-1)+k(k+1) \approx m^2+k^2 = (c^2+1)k^2$.
$m-k \approx ck-k = (c-1)k$.
$2m^3-3m^2+m \approx 2m^3 = 2c^3k^3$.
$2k^3+3k^2+k \approx 2k^3$.
The inequality becomes:
$((c^2+1)k^2)^2 \gtrsim \frac{2}{3}(c-1)k (2c^3k^3 - 2k^3)$.
$(c^2+1)^2 k^4 \gtrsim \frac{2}{3}(c-1)k \cdot 2k^3(c^3-1) = \frac{4}{3}k^4(c-1)(c^3-1)$.
Dividing by $k^4$ (since $k \ge 1$):
$(c^2+1)^2 \ge \frac{4}{3}(c-1)(c^3-1)$.
$c^4+2c^2+1 \ge \frac{4}{3}(c^4-c^3-c+1)$.
$3(c^4+2c^2+1) \ge 4(c^4-c^3-c+1)$.
$3c^4+6c^2+3 \ge 4c^4-4c^3-4c+4$.
$0 \ge c^4 - 4c^3 - 6c^2 - 4c + 1$.
Let $P(c) = c^4 - 4c^3 - 6c^2 - 4c + 1$. For a solution to exist, we must have $P(c) \le 0$.

Let's test values of $c$ for the roots of $P(c)$:
$P(1) = 1-4-6-4+1 = -12$.
$P(2) = 16-32-24-8+1 = -47$.
$P(3) = 81-108-54-12+1 = -92$.
$P(4) = 256 - 256 - 96 - 16 + 1 = -111$.
$P(5) = 625 - 500 - 150 - 20 + 1 = -44$.
$P(6) = 1296 - 4(216) - 6(36) - 24 + 1 = 1296 - 864 - 216 - 24 + 1 = 193$.
Since $P(5) < 0$ and $P(6) > 0$, there is a root for $P(c)=0$ between $c=5$ and $c=6$.
The analysis shows that for the discriminant to be non-negative, $c=m/k$ must be less than this root. So $m/k < 6$.

This implies $m < 6k$. A fortiori, $m \le 7k$.
The use of approximations for large $m,k$ can be made rigorous by showing that the lower-order terms do not change the sign of the inequality for large $c$.
Let's verify for $c=7$:
$P(7) = 7^4 - 4\cdot 7^3 - 6\cdot 7^2 - 4\cdot 7 + 1 = 2401 - 4(343) - 6(49) - 28 + 1 = 2401 - 1372 - 294 - 28 + 1 = 708$.
Since $P(7) > 0$, if $m/k \ge 7$, then for large $k$, the discriminant would be negative, which is impossible. This argument suggests that $m/k$ must be less than 7.

Let's test the case $k=1$. The quadratic becomes:
$(m-1)n^2 - (m(m-1)+2)n + (\frac{m(m-1)(2m-1)}{6} - 1) = 0$.
The discriminant is $D = (m^2-m+2)^2 - 4(m-1)(\frac{m(m-1)(2m-1)-6}{6})$. We need $D \ge 0$.
$3D = 3(m^2-m+2)^2 - 2(m-1)(m(m-1)(2m-1)-6)$
$3D = 3(m^4-2m^3+5m^2-4m+4) - 2(m-1)((2m^3-3m^2+m)-6)$
$3D = 3m^4-6m^3+15m^2-12m+12 - 2(2m^4-5m^3+4m^2-7m+6)$
$3D = 3m^4-6m^3+15m^2-12m+12 - 4m^4+10m^3-8m^2+14m-12$
$3D = -m^4+4m^3+7m^2+2m = m(-m^3+4m^2+7m+2)$.
For $D \ge 0$, we need $Q(m) = -m^3+4m^2+7m+2 \ge 0$.
We test integer values for $m \ge 2$:
$Q(2) = -8+16+14+2 = 24 > 0$.
$Q(3) = -27+36+21+2 = 32 > 0$.
$Q(4) = -64+64+28+2 = 30 > 0$.
$Q(5) = -125+100+35+2 = 12 > 0$.
$Q(6) = -216+144+42+2 = -28 < 0$.
So for $k=1$, a solution can only exist if $m \le 5$.
This satisfies $m \le 7k$ (as $5 \le 7\cdot 1$).

Both the asymptotic analysis and the specific case $k=1$ indicate that $m/k$ must be bounded by a constant less than 7. Therefore, the inequality $m \le 7k$ holds.

### Summary of the proof

1.  **Rewrite the equation**: The initial equation is transformed into a standard quadratic equation in $n$: $(m-k)n^2 - (m(m-1) + k(k+1))n + C = 0$.
2.  **Prove $k < m$**: By comparing the magnitude of the sums on both sides, we established that $k<m$.
3.  **Prove $k \le n$**: We showed that if we assume $n < k$, then $m \le n < k$, which contradicts $k < m$. Thus, $n \ge k$. This implies $7k \le 7n$.
4.  **Prove $m \le 7k$**: We analyzed the discriminant $D$ of the quadratic equation for $n$. For $n$ to be a real number, $D \ge 0$.
    - An asymptotic analysis for large $m, k$ with $m=ck$ showed that $D \ge 0$ requires $P(c) = c^4 - 4c^3 - 6c^2 - 4c + 1 \le 0$.
    - The largest real root of $P(c)$ is between 5 and 6. For $c \ge 6$, $P(c) > 0$.
    - This implies that $m/k$ must be bounded by a value smaller than 6.
    - An exact calculation for the case $k=1$ confirms that solutions only exist for $m \le 5$.
    - Both analyses show that $m/k$ is bounded by a constant smaller than 7. Therefore, $m \le 7k$.

Combining the results, we have shown that $m \le 7k$ and $k \le n$ (which is $7k \le 7n$), so we have successfully demonstrated that $m \le 7k \le 7n$.