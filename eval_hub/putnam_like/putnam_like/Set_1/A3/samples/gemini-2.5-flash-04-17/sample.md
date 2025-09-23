Let $f(x) = \sum_{i=0}^\infty a_i x^i$ with $a_i \in \{0,1\}$.
We are given that for some $n \in \mathbb{N}$, $f(1/2^n) \in \mathbb{Q}$.
$f(1/2^n) = \sum_{i=0}^\infty a_i (1/2^n)^i = \sum_{i=0}^\infty \frac{a_i}{2^{ni}}$.
This series is the base $2^n$ expansion of $f(1/2^n)$: $f(1/2^n) = a_0.a_1 a_2 a_3 \dots_{2^n}$.
A number is rational if and only if its base $B$ expansion is eventually periodic for any integer base $B \geq 2$. Since $f(1/2^n)$ is rational, its base $2^n$ expansion is eventually periodic. This means the sequence of coefficients $(a_i)_{i \geq 0}$ is eventually periodic.
Thus, there exist integers $N \geq 0$ and $p \geq 1$ such that $a_{i+p} = a_i$ for all $i \geq N$.

Now consider $f(x)$ for $x$ in the interval of convergence. Since $a_i \in \{0,1\}$, $|a_i| \le 1$. The radius of convergence $R$ is at least $1/\limsup |a_i|^{1/i} \ge 1$. For $q \ge 3$ odd, $2/q \in (0,1]$, so $f(2/q)$ converges.
We can write $f(x)$ by splitting the sum into an aperiodic part and a periodic part:
$f(x) = \sum_{i=0}^{N-1} a_i x^i + \sum_{i=N}^\infty a_i x^i$.
The second sum is a geometric series sum:
$\sum_{i=N}^\infty a_i x^i = \sum_{k=0}^\infty \sum_{j=0}^{p-1} a_{N+kp+j} x^{N+kp+j}$.
Since $a_{N+kp+j} = a_{N+j}$ for $k \ge 0$, this is
$= \sum_{k=0}^\infty \sum_{j=0}^{p-1} a_{N+j} x^{N+j+kp} = \sum_{j=0}^{p-1} a_{N+j} x^{N+j} \sum_{k=0}^\infty (x^p)^k$.
For $|x|<1$, the geometric series converges to $\frac{1}{1-x^p}$.
So, $\sum_{i=N}^\infty a_i x^i = \left(\sum_{j=0}^{p-1} a_{N+j} x^{N+j}\right) \frac{1}{1-x^p}$.
Let $P(x) = \sum_{i=0}^{N-1} a_i x^i$ and $Q(x) = \sum_{j=0}^{p-1} a_{N+j} x^{N+j}$. Note $Q(x)=x^N \sum_{j=0}^{p-1} a_{N+j} x^j$. Let $Q_0(x) = \sum_{j=0}^{p-1} a_{N+j} x^j$.
Then $f(x) = P(x) + Q(x) \frac{1}{1-x^p} = P(x) + x^N Q_0(x) \frac{1}{1-x^p}$.

Now substitute $x = 2/q$ where $q \geq 3$ is an odd natural number.
$P(2/q) = \sum_{i=0}^{N-1} a_i (2/q)^i$. This is a finite sum of rational numbers, so $P(2/q) \in \mathbb{Q}$.
If $N=0$, $P(x)=0$. If $N \geq 1$, $P(2/q) = \sum_{i=0}^{N-1} a_i \frac{2^i}{q^i} = \frac{\sum_{i=0}^{N-1} a_i 2^i q^{N-1-i}}{q^{N-1}}$. Let $N_P = \sum_{i=0}^{N-1} a_i 2^i q^{N-1-i}$. $N_P$ is an integer. $P(2/q) = N_P/q^{N-1}$.

$Q_0(2/q) = \sum_{j=0}^{p-1} a_{N+j} (2/q)^j = \sum_{j=0}^{p-1} a_{N+j} \frac{2^j}{q^j} = \frac{\sum_{j=0}^{p-1} a_{N+j} 2^j q^{p-1-j}}{q^{p-1}}$. Let $N_{Q_0} = \sum_{j=0}^{p-1} a_{N+j} 2^j q^{p-1-j}$. $N_{Q_0}$ is an integer. $Q_0(2/q) = N_{Q_0}/q^{p-1}$.

$1-(2/q)^p = 1 - 2^p/q^p = \frac{q^p-2^p}{q^p}$. Since $q \ge 3$ odd and $p \ge 1$, $q^p$ is odd, $2^p$ is even, so $q^p-2^p$ is odd and non-zero.

Case 1: $N=0$. The sequence $(a_i)$ is purely periodic. $f(x) = Q_0(x) / (1-x^p)$.
$f(2/q) = \frac{N_{Q_0}/q^{p-1}}{(q^p-2^p)/q^p} = \frac{N_{Q_0}}{q^{p-1}} \frac{q^p}{q^p-2^p} = \frac{N_{Q_0} q}{q^p-2^p}$.
This is a rational number since $N_{Q_0}$ and $q$ are integers and $q^p-2^p$ is a non-zero integer. Let $f(2/q) = \alpha'/\beta'$ where $\alpha' = N_{Q_0} q$ and $\beta' = q^p-2^p$.
Since $q$ is odd, $q^p$ is odd. Since $p \geq 1$, $2^p$ is even. $\beta' = q^p-2^p$ is odd.
So $f(2/q)$ can be written as a fraction with an odd denominator.

Case 2: $N \geq 1$.
$f(2/q) = P(2/q) + (2/q)^N Q_0(2/q) \frac{1}{1-(2/q)^p}$
$f(2/q) = \frac{N_P}{q^{N-1}} + \frac{2^N}{q^N} \frac{N_{Q_0}}{q^{p-1}} \frac{q^p}{q^p-2^p}$
$f(2/q) = \frac{N_P}{q^{N-1}} + \frac{2^N N_{Q_0} q}{q^{N-1}(q^p-2^p)}$.
This is a sum of two rational numbers, so it is rational.
$f(2/q) = \frac{N_P(q^p-2^p) + 2^N N_{Q_0} q}{q^{N-1}(q^p-2^p)}$.
Let $\alpha' = N_P(q^p-2^p) + 2^N N_{Q_0} q$ and $\beta' = q^{N-1}(q^p-2^p)$. $\alpha', \beta'$ are integers.
Since $N \geq 1$, $N-1 \ge 0$. $q$ is odd, so $q^{N-1}$ is odd. $q^p-2^p$ is odd.
Thus $\beta' = q^{N-1}(q^p-2^p)$ is a product of odd integers, which is odd.
So in both cases ($N=0$ and $N \ge 1$), $f(2/q)$ can be written as a fraction $\alpha'/\beta'$ where $\beta'$ is odd. This shows $f(2/q) \in \mathbb{Q}$.

Let $f(2/q) = \alpha/\beta$ where $\alpha, \beta$ are integers and $\mathrm{gcd}(\alpha, \beta)=1$.
We have $f(2/q) = \alpha'/\beta'$ where $\beta'$ is an odd integer.
So $\alpha/\beta = \alpha'/\beta'$. This means $\beta = \beta' / \mathrm{gcd}(\alpha', \beta')$.
Since $\beta'$ is odd, all of its prime factors are odd. $\mathrm{gcd}(\alpha', \beta')$ is a divisor of $\beta'$, so $\mathrm{gcd}(\alpha', \beta')$ must also be odd.
Since $\beta = \beta' / \mathrm{gcd}(\alpha', \beta')$, $\beta$ is the ratio of two odd integers. This implies $\beta$ must be odd.

The final answer is $\boxed{f \left( \frac{2}{q} \right) \in \mathbb{Q} \text{ and if we write } f \left( \frac{2}{q} \right) = \frac{\alpha}{\beta} \text{ for some integers } \alpha, \beta \text{ with } \mathrm{gcd}\, (\alpha, \beta) = 1, \text{ then } \beta \text{ is odd.}}$.