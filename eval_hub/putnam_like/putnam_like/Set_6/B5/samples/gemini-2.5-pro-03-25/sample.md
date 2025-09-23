Solution:
Let $(r_n)_{n=1}^\infty$ be a sequence of positive real numbers such that $\lim_{n\to\infty} r_n = 0$. Let $N = 2025$.
Let $S$ be the set of all sums of $N$ distinct terms of the sequence $(r_n)$.
$S = \{ \sum_{i=1}^N r_{n_i} : n_1, n_2, \dots, n_N \text{ are distinct positive integers} \}$.
We want to show that for any non-empty interval $(a, b)$, there exists a non-empty subinterval $(c, d) \subset (a, b)$ such that $(c, d) \cap S = \emptyset$. This is equivalent to showing that the set $S$ is nowhere dense in $\mathbb{R}$. A set is nowhere dense if the interior of its closure is empty.

Let $S_k$ denote the set of sums of $k$ distinct terms of the sequence $(r_n)$ for $k \ge 1$. Let $S_0 = \{0\}$.
$S_k = \{ \sum_{i=1}^k r_{n_i} : n_1, n_2, \dots, n_k \text{ are distinct positive integers} \}$.
The set $S$ given in the problem is $S_N$.
Let $W_N = \bigcup_{k=0}^N S_k$. $W_N$ is the set of sums of at most $N$ distinct terms of the sequence $(r_n)$.

First, we show that the set of limit points of $S_N$, denoted by $S_N'$, satisfies $S_N' \subset W_N$.
Let $L \in S_N'$. Then $L = \lim_{j\to\infty} s_j$ for a sequence $(s_j)$ in $S_N$, where $s_j = \sum_{i=1}^N r_{n_{i,j}}$. Since $r_n > 0$, $s_j > 0$ for all $j$. Since $r_n \to 0$, the sequence $(r_n)$ is bounded, so $S_N$ is bounded. Thus $L \ge 0$. If $L=0$, then $L \in S_0 \subset W_N$. Assume $L > 0$.

We prove by induction on $k$ that $S_k' \subset W_k = \bigcup_{j=0}^k S_j$.
Base case $k=0$: $S_0 = \{0\}$. The only sequence is $s_j=0$. $L=0$. $W_0 = \{0\}$. $S_0' = \{0\} \subset W_0$.
Inductive step: Assume $S_k' \subset W_k$ holds for all $k < N$. Let $L \in S_N'$. $L = \lim_{j\to\infty} s_j$, $s_j \in S_N$. Assume $L>0$.
Let $\epsilon = L/(2N)$. Since $r_n \to 0$, there exists $M$ such that $r_n < \epsilon$ for all $n > M$.
Each $s_j = \sum_{i=1}^N r_{n_{i,j}}$. Let $I_j = \{n_{1,j}, \dots, n_{N,j}\}$. We can write $s_j$ as:
$s_j = \sum_{n \in I_j \cap \{1, \dots, M\}} r_n + \sum_{n \in I_j \cap \{M+1, \dots\}} r_n$.
Let $t_j = \sum_{n \in I_j \cap \{1, \dots, M\}} r_n$ and $\sigma_j = \sum_{n \in I_j \cap \{M+1, \dots\}} r_n$.
$s_j = t_j + \sigma_j$.
The set of possible values for $t_j$ is finite, as it consists of sums of at most $N$ terms from the finite set $\{r_1, \dots, r_M\}$.
Since $(s_j)$ converges to $L$, it is a Cauchy sequence. There must be a subsequence $(s_{j_p})$ such that $t_{j_p}$ is constant, say $t_{j_p} = t$. Let $t = \sum_{n \in A} r_n$ for some set $A \subset \{1, \dots, M\}$ with $|A| = N_0 \le N$.
For this subsequence, $s_{j_p} = t + \sigma_{j_p}$. Since $s_{j_p} \to L$, we have $\sigma_{j_p} \to L-t$. Let $L' = L-t$.
$\sigma_{j_p} = \sum_{n \in J_{j_p}} r_n$, where $J_{j_p} = I_{j_p} \setminus A$. The indices in $J_{j_p}$ are all greater than $M$. The number of terms in the sum $\sigma_{j_p}$ is $|J_{j_p}| = N - N_0$.
Since $n > M$ for all $n \in J_{j_p}$, we have $r_n < \epsilon$. So $0 \le \sigma_{j_p} \le (N-N_0) \epsilon \le N \epsilon = L/2$.
Taking the limit as $p \to \infty$, we get $0 \le L' \le L/2$. This implies $L/2 \le t \le L$.
The terms $\sigma_{j_p}$ are sums of $N-N_0$ distinct terms from the sequence $\mathcal{R}_M = (r_n)_{n=M+1}^\infty$. So $L' = \lim_{p\to\infty} \sigma_{j_p}$ is a limit point of $S_{N-N_0}(\mathcal{R}_M)$.
$L' \in S_{N-N_0}(\mathcal{R}_M)'$.
By the induction hypothesis applied to the sequence $\mathcal{R}_M$ and the integer $N-N_0 < N$, we have $L' \in W_{N-N_0}(\mathcal{R}_M)$.
This means $L'$ is a sum of $N_1$ distinct terms from $\mathcal{R}_M$, where $0 \le N_1 \le N-N_0$.
$L' = \sum_{n \in B} r_n$ for some $B \subset \{M+1, M+2, \dots\}$ with $|B| = N_1$.
So $L = t + L' = \sum_{n \in A} r_n + \sum_{n \in B} r_n$.
Since $A \subset \{1, \dots, M\}$ and $B \subset \{M+1, \dots\}$, the sets $A$ and $B$ are disjoint.
$L = \sum_{n \in A \cup B} r_n$. The number of terms in this sum is $|A \cup B| = |A| + |B| = N_0 + N_1 \le N_0 + (N-N_0) = N$.
Thus, $L$ is a sum of at most $N$ distinct terms of the original sequence $(r_n)$. So $L \in W_N(\mathcal{R}_0)$.
This completes the induction. We have shown $S_N' \subset W_N$.

Now we show that $W_N$ is closed. Let $L$ be a limit point of $W_N$. $L = \lim_{j\to\infty} w_j$ for $w_j \in W_N$. Each $w_j = \sum_{n \in I_j} r_n$ with $|I_j| = k_j \le N$. We can use a similar argument as above. Any limit point $L$ must be a sum of at most $N$ distinct terms. So $L \in W_N$. Thus $W_N$ is closed. ($W_N' \subset W_N$).

The set $W_N = \bigcup_{k=0}^N S_k$. Each $S_k$ is the set of sums of $k$ distinct indices. The set of finite subsets of $\mathbb{N}$ is countable. So each $S_k$ is countable. $W_N$ is a finite union of countable sets, so $W_N$ is countable.

Suppose $W_N$ contains a non-empty interval $(a, b)$. Since $a < b$, $(a, b)$ is an uncountable set.
However, $W_N$ is countable. A countable set cannot contain an uncountable set. This is a contradiction.
Therefore, $W_N$ cannot contain any non-empty interval.

Since $W_N$ is a closed set and contains no interval, its interior is empty. $\text{int}(W_N) = \emptyset$.
We know that $\bar{S_N} = S_N \cup S_N'$. We proved $S_N' \subset W_N$. So $\bar{S_N} \subset W_N \cup S_N = W_N$.
The interior of $\bar{S_N}$ must be a subset of the interior of $W_N$.
$\text{int}(\bar{S_N}) \subset \text{int}(W_N) = \emptyset$.
So $\bar{S_N}$ has an empty interior. This means $S_N$ is nowhere dense.

Now, let $(a, b)$ be any non-empty interval. Since $\bar{S_N}$ is nowhere dense, it cannot contain $(a, b)$. So there must exist $x \in (a, b)$ such that $x \notin \bar{S_N}$.
Since $\bar{S_N}$ is a closed set, its complement $\mathbb{R} \setminus \bar{S_N}$ is open.
Since $x \in \mathbb{R} \setminus \bar{S_N}$, there exists an open interval $(c, d)$ such that $x \in (c, d)$ and $(c, d) \subset \mathbb{R} \setminus \bar{S_N}$.
We can choose this interval $(c, d)$ small enough such that $(c, d) \subset (a, b)$. For example, let $\epsilon > 0$ such that $(x-\epsilon, x+\epsilon) \subset \mathbb{R} \setminus \bar{S_N}$. Let $\epsilon' = \min(\epsilon, x-a, b-x)$. Then $(c, d) = (x-\epsilon'/2, x+\epsilon'/2)$ is a non-empty subinterval of $(a,b)$ and $(c,d) \subset \mathbb{R} \setminus \bar{S_N}$.
So $(c, d) \cap \bar{S_N} = \emptyset$. Since $S_N \subset \bar{S_N}$, we have $(c, d) \cap S_N = \emptyset$.
We found a non-empty subinterval $(c, d) \subset (a, b)$ that does not contain any numbers equal to a sum of $N=2025$ distinct terms of the sequence $(r_n)$.

Final Answer: The final answer is $\boxed{Every non-empty interval $(a, b)$ contains a non-empty subinterval $(c, d)$ that does not contain any numbers equal to a sum of 2025 distinct terms of the sequence $(r_n)}$