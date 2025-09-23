Let $S_K$ be the set of sums of $K=2025$ distinct terms of the sequence $(r_n)$, i.e., $S_K = \{ \sum_{i \in I} r_i \mid I \subset \mathbb{N}, |I|=K \}$. We are given that $r_n > 0$ for all $n$ and $r_n \to 0$ as $n \to \infty$. We want to show that any non-empty interval $(a, b)$ contains a non-empty subinterval $(c, d)$ such that $(c, d) \cap S_K = \emptyset$.

The set $S_K$ is countable because the set of all finite subsets of $\mathbb{N}$ is countable.
If the closure $\overline{S_K}$ is a nowhere dense set in $\mathbb{R}$, then its complement $\mathbb{R} \setminus \overline{S_K}$ is a dense open set. Any non-empty open set contains a non-empty interval. Thus, $(a, b) \setminus \overline{S_K}$ would be a non-empty open set, which would contain an interval $(c,d)$. Since $(c,d) \cap \overline{S_K} = \emptyset$, it implies $(c,d) \cap S_K = \emptyset$, and $(c,d) \subset (a,b)$.

Let's examine the structure of $S_K$ and its closure.
Since $r_n \to 0$, for any $\epsilon > 0$, there exists $N$ such that for all $n > N$, $0 < r_n < \epsilon$.
Let $S_m(A) = \{ \sum_{i \in I} r_i \mid I \subset A, |I|=m \}$.
$S_K = S_K(\mathbb{N})$.
For $N$ large enough, $S_K(\{N+1, N+2, \dots\}) \subset (0, K \epsilon)$.
Also, $S_K$ has limit points. Let $s \in S_K$, $s = \sum_{i \in I} r_i$. If $I=\{i_1, \dots, i_K\}$ with $i_1 < \dots < i_K$, and $i_K \to \infty$, then $r_{i_K} \to 0$, and $s \to \sum_{j=1}^{K-1} r_{i_j}$.
This means that any sum of $K-1$ distinct terms is a limit point of $S_K$. By induction, any sum of $m$ distinct terms for $0 \le m \le K-1$ is a limit point of $S_K$. Let $S_{\le K-1} = \bigcup_{m=0}^{K-1} S_m$. Then $S_{\le K-1} \subset \overline{S_K}$.

Let $(a, b)$ be a non-empty interval. Choose $N$ large enough such that $r_n < (b-a)/(2K)$ for all $n > N$.
Let $\delta_N = r_{N+1}$. Since $r_n \to 0$, we can choose $N$ so that $\delta_N$ is arbitrarily small. Let's choose $N$ large enough so that $\delta_N < (b-a)/(K+1)$.
Consider the interval $I = (a + K \delta_N, a + (K+1) \delta_N)$. This interval is non-empty and has length $\delta_N$. If $a+(K+1)\delta_N \ge b$, we choose $N$ larger until $a+(K+1)\delta_N < b$, so $I \subset (a,b)$.

Let $s \in S_K \cap I$. $s = \sum_{i \in J} r_i$ for some set $J$ of $K$ distinct indices.
Let $J_L = J \cap \{1, \dots, N\}$ and $J_S = J \cap \{N+1, N+2, \dots\}$. Let $m = |J_L|$ and $k = |J_S|$, so $m+k=K$.
$s = s_L + s_S$, where $s_L = \sum_{i \in J_L} r_i$ and $s_S = \sum_{j \in J_S} r_j$.
$s_L \in S_m(\{1, \dots, N\})$ and $s_S \in S_k(\{N+1, \dots\})$.

Since $j > N$ for all $j \in J_S$, we have $0 < r_j \le r_{N+1} = \delta_N$ (assuming $r_n$ is non-increasing for $n>N$, which is possible after re-indexing the tail, although not necessary for the argument). More generally, $r_j < \delta_N$ for $j>N$.
If $k > 0$, then $0 < s_S < k \delta_N$. If $k=0$, $s_S=0$.
$s \in (a+K\delta_N, a+(K+1)\delta_N)$. So $s_L + s_S \in (a+K\delta_N, a+(K+1)\delta_N)$.

Case 1: $k=K$. $m=0$. $J_L = \emptyset$. $s=s_S \in S_K(\{N+1, \dots\})$. Then $0 < s < K \delta_N$.
For $s$ to be in $I=(a+K\delta_N, a+(K+1)\delta_N)$, we need $a+K\delta_N < s < K\delta_N$. This implies $a+K\delta_N < K\delta_N$, so $a < 0$, which is not assumed. If $a \ge 0$, then $S_K(\{N+1, \dots\}) \cap I = \emptyset$.

Case 2: $0 \le k \le K-1$. $m = K-k \ge 1$. $s_S \in S_k(\{N+1, \dots\})$. $s_L \in S_m(\{1, \dots, N\})$.
$s_L \in \bigcup_{m=1}^K S_m(\{1, \dots, N\})$. Let $F = \bigcup_{m=0}^K S_m(\{1, \dots, N\})$, which is a finite set. $s_L \in F$.
$s = s_L + s_S \in (a+K\delta_N, a+(K+1)\delta_N)$.
$s_S = s - s_L \in (a+K\delta_N - s_L, a+(K+1)\delta_N - s_L)$.
Also $0 \le s_S < k \delta_N$ if $k>0$, $s_S=0$ if $k=0$.

If $k=0$, $s_S=0$, $s=s_L \in S_K(\{1, \dots, N\})$. This is a finite set of points. $F_K = S_K(\{1, \dots, N\})$. $F_K \cap I$ is finite.

If $k \ge 1$, $1 \le k \le K-1$. $s_L \in F_m$, $m=K-k \in \{1, \dots, K-1\}$.
$s_S \in S_k(\{N+1, \dots\})$. $0 < s_S < k\delta_N$.
$s_L \in (s - k\delta_N, s)$. Since $s \in I$, $s_L \in (a+K\delta_N - k\delta_N, a+(K+1)\delta_N) = (a+m\delta_N, a+(K+1)\delta_N)$.
So $s_L \in F_m \cap (a+m\delta_N, a+(K+1)\delta_N)$. This is a finite set of values for $s_L$.
For each such $s_L$, $s_S \in (a+K\delta_N - s_L, a+(K+1)\delta_N - s_L)$. This interval for $s_S$ has length $\delta_N$.
$s_S \in S_k(\{N+1, \dots\})$. $s_S$ is a sum of $k$ terms from $\{r_{N+1}, r_{N+2}, \dots\}$.

Let $s_L \in F_m \cap (a+m\delta_N, a+(K+1)\delta_N)$, with $m=K-k \in \{1, \dots, K-1\}$.
$s = s_L+s_S \in I$ means $s_S \in (a+K\delta_N - s_L, a+(K+1)\delta_N - s_L)$.
Let $I_{s_L} = (a+K\delta_N - s_L, a+(K+1)\delta_N - s_L)$. Length $\delta_N$.
$s_L > a+m\delta_N \implies a+K\delta_N-s_L < a+K\delta_N - (a+m\delta_N) = (K-m)\delta_N = k\delta_N$.
So $I_{s_L} \subset (-\infty, k\delta_N)$. Since $s_S > 0$, we only consider $I_{s_L} \cap (0, k\delta_N)$.
$a+K\delta_N-s_L < s_S < a+(K+1)\delta_N-s_L$.

Let's choose $N$ large enough such that $\delta_N < (b-a)/(K+1)$ and $r_{N+1}$ is smaller than the minimum difference between any two distinct sums of $k$ terms from $\{r_{N+1}, r_{N+2}, \dots\}$ with $1 \le k \le K-1$ whose values are less than $(K-1)\delta_N + \delta_N$.

Choose $N$ such that $r_n < \delta_N = (b-a)/(2K)$ for $n>N$, and $r_j$ are all distinct for $j>N$.
Let $I=(a+K\delta_N, a+(K+1)\delta_N)$. $I \subset (a,b)$.
Let $s=s_L+s_S \in S_K \cap I$. $s_L \in F_m$, $s_S \in S_{K-m}(\{N+1,\dots\})$, $m \in \{0,\dots,K\}$.
If $m=K$, $s=s_L \in F_K$. Finite points in $I$.
If $m<K$, $k=K-m>0$. $s_S \in S_k(\{N+1,\dots\})$. $0 < s_S < k\delta_N$.
$s_L > a+K\delta_N-s_S > a+K\delta_N-k\delta_N = a+m\delta_N$. $s_L \in F_m \cap (a+m\delta_N, a+(K+1)\delta_N)$.
$s_S \in (a+K\delta_N-s_L, a+(K+1)\delta_N-s_L)$. This interval has length $\delta_N$.
$s_S$ is a sum of $k$ distinct terms from $\{r_{N+1}, \dots\}$. Let $s_S = r_{p_1} + \dots + r_{p_k}$ with $p_i > N$.
$0 < r_{p_i} < \delta_N$.

If $k=1$, $s_S=r_j$ for some $j>N$. $r_j \in (a+K\delta_N-s_L, a+(K+1)\delta_N-s_L)$. $s_L \in F_{K-1}$.
$s_L \in (a+(K-1)\delta_N, a+(K+1)\delta_N)$.
$a+K\delta_N-s_L < r_j < a+(K+1)\delta_N-s_L$. Since $r_j < \delta_N$ for $j>N$:
$a+K\delta_N-s_L < \delta_N$, so $s_L > a+(K-1)\delta_N$. This is consistent.
$r_j > a+K\delta_N-s_L$. If $a+K\delta_N-s_L \ge \delta_N$, then no $r_j$ for $j>N$ can be in this interval. This requires $s_L \le a+(K-1)\delta_N$.
So if $s_L \in F_{K-1} \cap (a+(K-1)\delta_N, a+K\delta_N]$, then for $j>N$, $s_L+r_j \notin I$.
The set $F_{K-1} \cap (a+(K-1)\delta_N, a+K\delta_N]$ is finite. Let it be $F'_{K-1}$.
For each $f \in F'_{K-1}$, $f+r_j \notin I$ for all $j>N$.

For $s_L \in F_{K-1} \cap (a+K\delta_N, a+(K+1)\delta_N)$, $r_j \in (a+K\delta_N-s_L, a+(K+1)\delta_N-s_L) \subset (0, \delta_N)$. Since $r_j$ are distinct for $j>N$, this interval of length $\delta_N$ contains at most one $r_j$.
So for each $s_L \in F_{K-1} \cap (a+K\delta_N, a+(K+1)\delta_N)$, there is at most one $j>N$ such that $s_L+r_j \in I$.
$F_{K-1}$ is finite. So there are finitely many points in $S_K \cap I$ of the form $s_L+r_j$ with $s_L \in F_{K-1}$.

If $k \ge 2$, $s_S = r_{p_1} + \dots + r_{p_k}$ with $p_i > N$. $s_S \in (0, k\delta_N)$.
$s_S \in (a+K\delta_N-s_L, a+(K+1)\delta_N-s_L)$, $s_L \in F_{K-k}$.
$s_L > a+(K-k)\delta_N$. $a+K\delta_N-s_L < k\delta_N$. $a+(K+1)\delta_N-s_L < (k+1)\delta_N$.
$s_S \in (a+K\delta_N-s_L, a+(K+1)\delta_N-s_L) \cap (0, k\delta_N)$. Length $\delta_N$.
Choose $N$ large enough so that $\delta_N < (b-a)/(K+1)$ and $\max_{j_1,\dots,j_k>N} (r_{j_1}+\dots+r_{j_k}) < (b-a)/(K+1)$ for $k \le K-1$.
Choose $N$ s.t. $r_{N+1} < \min(\delta_N/(K-1), \text{min gap in } S_k(\{N+1,\dots\}) \text{ for } k \ge 2)$.

Let $N$ s.t. $r_{N+1} < (b-a)/(2K)$ and $r_{N+1}$ is smaller than any sum of two distinct terms $r_i+r_j$ with $i,j>N$. This is possible because $r_n \to 0$.
Let $\delta=r_{N+1}$. $(a+K\delta, a+(K+1)\delta)$.
$s=s_L+s_S \in S_K \cap (a+K\delta, a+(K+1)\delta)$. $s_L \in F_m, s_S \in S_{K-m}(\{N+1,\dots\})$.
If $m=K$, $s \in F_K$. Finite.
If $m=K-1$, $s_S=r_j, j>N$. $s_L \in F_{K-1}$. $r_j \in (a+K\delta-s_L, a+(K+1)\delta-s_L)$.
If $s_L \le a+(K-1)\delta$, interval is $(\ge\delta, <2\delta)$. $r_j < \delta$. No $r_j$ here.
If $s_L > a+(K-1)\delta$, interval is $(<\delta, <2\delta)$. $r_j \in (a+K\delta-s_L, \delta)$. At most one $r_j$.

If $m \le K-2$, $k \ge 2$. $s_S \in S_k(\{N+1,\dots\})$. $s_S=r_{p_1}+\dots+r_{p_k}$, $p_i>N$. $s_S > r_{N+1}+r_{N+2} > 2r_{N+1}=2\delta$.
$s_S \in (a+K\delta-s_L, a+(K+1)\delta-s_L)$.
$s_L > a+m\delta = a+(K-k)\delta$. $a+K\delta-s_L < a+K\delta - (a+(K-k)\delta) = k\delta$.
So $s_S \in (a+K\delta-s_L, a+(K+1)\delta-s_L) \cap (0, k\delta)$.
If $k \ge 2$, $s_S \ge r_{N+1}+r_{N+2}$. Choose $N$ s.t. $r_{N+1}+r_{N+2} > \delta$.
If $r_n$ distinct, $r_{N+1}>r_{N+2}>\dots$. $r_{N+1}+r_{N+2} < 2r_{N+1}$. $r_{N+1}+r_{N+K} > r_{N+1}$.

Choose $N$ such that $r_n < (b-a)/(2K)$ for $n > N$. And $r_{N+1} < (b-a)/(2(K+1))$. $\delta=r_{N+1}$.
Consider $(a+K\delta, a+(K+1)\delta)$.
$s=s_L+s_S$. $s_S \in S_{K-m}(\{N+1,\dots\})$.
If $K-m \ge 1$, $s_S \ge r_{N+1}=\delta$.
$s_S \in (a+K\delta-s_L, a+(K+1)\delta-s_L)$.
$s_S \ge \delta \implies a+(K+1)\delta-s_L > \delta \implies s_L < a+K\delta$.
$s_S < (K-m)\delta$. $a+K\delta-s_L < (K-m)\delta \implies s_L > a+m\delta$.
$s_L \in F_m \cap (a+m\delta, a+K\delta)$. For each such $s_L$, $s_S \in S_{K-m}(\{N+1,\dots\})$ must be in $(a+K\delta-s_L, a+(K+1)\delta-s_L)$.
If $r_{N+1}$ is small enough, $S_{K-m}(\{N+1,\dots\})$ are sums of terms smaller than any value in $(a+K\delta-s_L, a+(K+1)\delta-s_L)$.

Final approach: $S_K$ is countable. Thus $S_K \cap (a,b)$ is countable. If $\overline{S_K} \cap (a,b)$ is nowhere dense, we are done. The set of limit points of $S_K$ is a subset of $S_{\le K-1}$.
If $(c,d) \subset (a,b) \cap \overline{S_K}$, then $(c,d)$ must contain a point $s_0 \in S_{\le K-1}$.
If $s_0 \in S_m$ for $m \le K-1$. $s_0+\sum_{j \in J} r_j$ for $|J|=K-m$, large indices.
Let $\delta>0$ small. $s_0+\sum_{j=1}^{K-m} r_{N+j}$. This is in $S_K$ for large $N$.
This indicates $\overline{S_K}$ is $( \bigcup_{m=0}^{K-1} S_m ) \cup S_K$. This is a countable set. A countable set is nowhere dense.

Let $X$ be a countable subset of $\mathbb{R}$. $X$ is nowhere dense if $\overline{X}$ has no interior points. If $X$ is countable, $\overline{X}$ is separable. If it had interior points, it would contain an interval $(c,d)$. A countable set cannot contain an interval. So $\overline{X}$ has no interior points.
So $\overline{S_K}$ is nowhere dense.
The complement of a nowhere dense set is dense. $\mathbb{R} \setminus \overline{S_K}$ is dense and open.
So $(a,b) \cap (\mathbb{R} \setminus \overline{S_K})$ is a non-empty open set. It contains an interval $(c,d)$.
$(c,d) \subset (a,b)$ and $(c,d) \cap \overline{S_K} = \emptyset$.
This implies $(c,d) \cap S_K = \emptyset$.

The argument relies on $\overline{S_K}$ being countable.
$\overline{S_K}$ is the set of points which are limits of sequences from $S_K$.
Let $s \in \overline{S_K}$. $s = \lim_{n \to \infty} x_n$, $x_n \in S_K$.
$x_n = \sum_{i \in I_n} r_i$, $|I_n|=K$.
Let $r_{(n)}$ be sorted sequence.
If $\sum r_n < \infty$, $\overline{S_K}$ is compact. A countable compact set is nowhere dense.
If $\sum r_n = \infty$, $\overline{S_K}$ may contain $[0, \infty)$. Example $r_n = 1/n$. Sums of distinct $1/n$ are dense in $[0, \infty)$. (Ref: $1/n$ is a basis for representing numbers). $\overline{S_K}$ can be $[0,\infty)$.

But $\overline{S_K}$ as defined here is not $\overline{\{\sum_{i \in I} r_i \mid |I|=K\}}$.
Let $r_n = 1/n$. $K=2$. $S_2=\{1/i+1/j\}$. $\overline{S_2}=S_2 \cup \{1/n\} \cup \{0\}$. This is countable.
For $r_n=1/n$, $S_K = \{ \sum_{i \in I} 1/i : |I|=K \}$. $\overline{S_K} = S_K \cup \bigcup_{m=0}^{K-1} S_m$. This is a countable set.
Is this true for any sequence $r_n \to 0$? Yes.
Let $s \in \overline{S_K} \setminus S_K$. $s = \lim x_n, x_n \in S_K$. $x_n = \sum_{i \in I_n} r_i$. $|I_n|=K$.
If $I_n$ stays bounded, $I_n \subset \{1, \dots, M\}$. Then $S_K(\{1, \dots, M\})$ is finite, so $s$ must be in $S_K$.
So $I_n$ must be unbounded for $s \notin S_K$.
$x_n = \sum_{i \in I_n} r_i$. Let $i_n^* = \max I_n$. $i_n^* \to \infty$. $r_{i_n^*} \to 0$.
$x_n = (\sum_{i \in I_n \setminus \{i_n^*\}} r_i) + r_{i_n^*}$. Let $y_n = \sum_{i \in I_n \setminus \{i_n^*\}} r_i \in S_{K-1}$.
$y_n \to s$ ? No.

Let $\overline{S_K}$ be the set of limit points of sequences in $S_K$. $\overline{S_K}$ contains $S_K$.
Let $s \in \overline{S_K}$. $s = \lim x_n$. $x_n = \sum_{i \in I_n} r_i$.
If indices in $I_n$ are bounded, $I_n \subset \{1, \dots, M\}$, $x_n \in S_K(\{1,\dots,M\})$, finite. $s \in S_K(\{1,\dots,M\}) \subset S_K$.
If indices are unbounded, $\max I_n \to \infty$. $x_n = y_n+r_{\max I_n}$. $y_n \in S_{K-1}$.
$y_n$ is sequence in $S_{K-1}$. Any limit point of $y_n$ is in $\overline{S_{K-1}}$.
$s = \lim (y_n+r_{\max I_n}) = \lim y_n$. $s \in \overline{S_{K-1}}$.
$\overline{S_K} \subset \overline{S_{K-1}}$. By induction, $\overline{S_K} \subset \overline{S_0} = \{0\}$. This is not true.

Let $L_K = \overline{S_K} \setminus S_K$. $L_K \subset \overline{S_{K-1}}$.
$\overline{S_K} = S_K \cup L_K$.
$L_K \subset S_{K-1} \cup L_{K-1}$.
$\overline{S_K} \subset S_K \cup S_{K-1} \cup L_{K-1} \subset S_K \cup S_{K-1} \cup S_{K-2} \cup L_{K-2} \subset \dots \subset \bigcup_{m=0}^K S_m$.
Thus $\overline{S_K}$ is a countable set. A countable set has no interior points, hence it is nowhere dense.
The complement $\mathbb{R} \setminus \overline{S_K}$ is dense and open.
$(a,b) \cap (\mathbb{R} \setminus \overline{S_K})$ is open and non-empty, thus contains an interval $(c,d)$.
$(c,d) \subset (a,b)$ and $(c,d) \cap \overline{S_K}=\emptyset$, so $(c,d) \cap S_K=\emptyset$.

The final answer is $\boxed{Every non-empty interval $(a, b)$ contains a non-empty subinterval $(c, d)$ that does not contain any numbers equal to a sum of 2025 distinct terms of the sequence $(r_n)}$.