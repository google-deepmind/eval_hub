Solution:
Let $C_1, C_2, \ldots, C_n$ be the $n$ biased coins.
The probability that the $m$-th coin lands heads is given by $p_m = P(H_m) = \frac{1}{2m+1}$.
The probability that the $m$-th coin lands tails is $P(T_m) = 1 - p_m = 1 - \frac{1}{2m+1} = \frac{2m}{2m+1}$.
The coin tosses are independent.
Let $X_m$ be an indicator random variable for the outcome of the $m$-th coin toss, where $X_m=1$ if the coin is heads and $X_m=0$ if the coin is tails.
$P(X_m=1) = p_m = \frac{1}{2m+1}$
$P(X_m=0) = 1-p_m = \frac{2m}{2m+1}$
Let $S_n = \sum_{m=1}^n X_m$ be the total number of heads obtained after tossing the $n$ coins.
We are interested in the probability that $S_n$ is an even number. Let $E_n$ denote this event, so we want to compute $P(E_n)$.

We can use the probability generating function (PGF) method. The PGF of $S_n$ is defined as $P_n(x) = E[x^{S_n}]$.
Since the coin tosses are independent, the PGF of the sum $S_n$ is the product of the PGFs of the individual $X_m$.
The PGF of $X_m$ is $E[x^{X_m}] = P(X_m=0) x^0 + P(X_m=1) x^1 = (1-p_m) + p_m x$.
So, the PGF of $S_n$ is $P_n(x) = \prod_{m=1}^n E[x^{X_m}] = \prod_{m=1}^n (1-p_m + p_m x)$.

Let $P(E_n)$ be the probability that $S_n$ is even, and $P(O_n)$ be the probability that $S_n$ is odd.
$P(E_n) = \sum_{k \text{ even}} P(S_n=k)$
$P(O_n) = \sum_{k \text{ odd}} P(S_n=k)$
We know that $P(E_n) + P(O_n) = \sum_k P(S_n=k) = P_n(1)$. Since $P_n(1) = \prod_{m=1}^n (1-p_m+p_m) = \prod_{m=1}^n 1 = 1$, we have $P(E_n) + P(O_n) = 1$.
Consider the value of the PGF at $x=-1$:
$P_n(-1) = \sum_{k=0}^n P(S_n=k) (-1)^k = \sum_{k \text{ even}} P(S_n=k) - \sum_{k \text{ odd}} P(S_n=k) = P(E_n) - P(O_n)$.

We have a system of two linear equations:
1) $P(E_n) + P(O_n) = 1$
2) $P(E_n) - P(O_n) = P_n(-1)$
Adding the two equations gives $2 P(E_n) = 1 + P_n(-1)$.
Therefore, $P(E_n) = \frac{1 + P_n(-1)}{2}$.

Now we need to compute $P_n(-1)$.
$P_n(-1) = \prod_{m=1}^n (1-p_m + p_m (-1)) = \prod_{m=1}^n (1 - 2p_m)$.
Substitute the given probability $p_m = \frac{1}{2m+1}$:
$1 - 2p_m = 1 - 2\left(\frac{1}{2m+1}\right) = 1 - \frac{2}{2m+1} = \frac{2m+1 - 2}{2m+1} = \frac{2m-1}{2m+1}$.
So, $P_n(-1) = \prod_{m=1}^n \frac{2m-1}{2m+1}$.
This is a telescoping product:
$P_n(-1) = \frac{2(1)-1}{2(1)+1} \times \frac{2(2)-1}{2(2)+1} \times \frac{2(3)-1}{2(3)+1} \times \cdots \times \frac{2n-1}{2n+1}$
$P_n(-1) = \frac{1}{3} \times \frac{3}{5} \times \frac{5}{7} \times \cdots \times \frac{2n-1}{2n+1}$.
In this product, the numerator of each term cancels the denominator of the previous term. After cancellation, we are left with the numerator of the first term (1) and the denominator of the last term ($2n+1$).
$P_n(-1) = \frac{1}{2n+1}$.

Finally, substitute this result back into the formula for $P(E_n)$:
$P(E_n) = \frac{1 + P_n(-1)}{2} = \frac{1 + \frac{1}{2n+1}}{2}$.
$P(E_n) = \frac{\frac{2n+1+1}{2n+1}}{2} = \frac{\frac{2n+2}{2n+1}}{2} = \frac{2(n+1)}{2(2n+1)} = \frac{n+1}{2n+1}$.

Alternatively, we can establish a recurrence relation for $P(E_n)$.
Let $E_n$ be the event that $S_n = \sum_{m=1}^n X_m$ is even.
$S_n = S_{n-1} + X_n$. $S_n$ is even if ($S_{n-1}$ is even and $X_n=0$) or ($S_{n-1}$ is odd and $X_n=1$).
Let $P(E_n)$ denote the probability of event $E_n$. $P(O_n) = 1 - P(E_n)$ is the probability that $S_n$ is odd.
$P(E_n) = P(E_{n-1}) P(X_n=0) + P(O_{n-1}) P(X_n=1)$
$P(E_n) = P(E_{n-1})(1-p_n) + (1-P(E_{n-1}))p_n$
$P(E_n) = P(E_{n-1})(1-2p_n) + p_n$.
Using $p_n = \frac{1}{2n+1}$, we have $1-2p_n = \frac{2n-1}{2n+1}$.
$P(E_n) = P(E_{n-1})\frac{2n-1}{2n+1} + \frac{1}{2n+1}$.
We can prove $P(E_n) = \frac{n+1}{2n+1}$ by induction.
Base case $n=1$: $P(E_1) = P(X_1=0) = 1-p_1 = 1 - \frac{1}{3} = \frac{2}{3}$. The formula gives $\frac{1+1}{2(1)+1} = \frac{2}{3}$. The base case holds.
Inductive step: Assume $P(E_{k}) = \frac{k+1}{2k+1}$ for some $k \ge 1$.
$P(E_{k+1}) = P(E_k)\frac{2(k+1)-1}{2(k+1)+1} + \frac{1}{2(k+1)+1}$
$P(E_{k+1}) = P(E_k)\frac{2k+1}{2k+3} + \frac{1}{2k+3}$.
Substitute the inductive hypothesis $P(E_k) = \frac{k+1}{2k+1}$:
$P(E_{k+1}) = \frac{k+1}{2k+1} \cdot \frac{2k+1}{2k+3} + \frac{1}{2k+3}$
$P(E_{k+1}) = \frac{k+1}{2k+3} + \frac{1}{2k+3} = \frac{k+1+1}{2k+3} = \frac{k+2}{2k+3}$.
This is the formula for $n=k+1$, i.e., $\frac{(k+1)+1}{2(k+1)+1}$. The formula holds by induction.

Final Answer: The final answer is $\boxed{\frac{n+1}{2n+1}}$