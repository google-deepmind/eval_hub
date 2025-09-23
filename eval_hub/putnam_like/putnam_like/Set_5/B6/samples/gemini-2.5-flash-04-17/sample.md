Let $S = \{1, 2, \ldots, n\}$. $\mathcal{F}$ is a family of subsets of $S$ such that if $A \in \mathcal{F}$ and $B \subset A$, then $B \in \mathcal{F}$. This property means that $\mathcal{F}$ is a down-set in the poset of subsets of $S$ ordered by inclusion.

The function $f:[0,1]\to\mathbb{R}$ is defined by
\[
f(t) = \sum_{A \in \mathcal{F}} t^{|A|}(1-t)^{|S\setminus A|}.
\]
We want to prove that $f(t)$ is non-increasing, i.e., for any $t_1, t_2 \in [0,1]$ with $t_1 < t_2$, we have $f(t_1) \ge f(t_2)$.

Let's consider a probabilistic interpretation of $f(t)$. Let $R_t$ be a random subset of $S$ where each element $i \in S$ is included in $R_t$ independently with probability $t$. For any subset $A \subseteq S$, the probability that $R_t$ is equal to $A$ is given by
\[
P(R_t = A) = \prod_{i \in A} t \cdot \prod_{i \notin A} (1-t) = t^{|A|} (1-t)^{n-|A|}.
\]
The function $f(t)$ can be written as the probability that the random set $R_t$ belongs to the family $\mathcal{F}$:
\[
f(t) = \sum_{A \in \mathcal{F}} P(R_t = A) = P(R_t \in \mathcal{F}).
\]

To show that $f(t)$ is non-increasing, we compare $f(t_1)$ and $f(t_2)$ for $t_1 < t_2$. We can use a coupling argument. Let $U_1, U_2, \ldots, U_n$ be independent random variables, each uniformly distributed in $[0,1]$. For $t \in [0,1]$, define the random set $R_t$ by
\[
R_t = \{i \in S \mid U_i \le t\}.
\]
Then $P(i \in R_t) = P(U_i \le t) = t$, and the events $\{i \in R_t\}$ for different $i$ are independent. So $R_t$ is a random subset of $S$ as described above, and $P(R_t=A) = t^{|A|}(1-t)^{n-|A|}$.
Thus, $f(t) = P(R_t \in \mathcal{F})$.

Now, let $t_1, t_2 \in [0,1]$ with $t_1 \le t_2$. Consider the random sets $R_{t_1}$ and $R_{t_2}$ defined using the same sequence of uniform random variables $U_1, \ldots, U_n$:
$R_{t_1} = \{i \in S \mid U_i \le t_1\}$
$R_{t_2} = \{i \in S \mid U_i \le t_2\}$
For any $i \in S$, if $i \in R_{t_1}$, then $U_i \le t_1$. Since $t_1 \le t_2$, $U_i \le t_2$, which implies $i \in R_{t_2}$. Therefore, $R_{t_1} \subseteq R_{t_2}$ for any realization of the random variables $U_1, \ldots, U_n$.

Now consider the event that $R_{t_2} \in \mathcal{F}$. If $R_{t_2} \in \mathcal{F}$ occurs, then we know $R_{t_1} \subseteq R_{t_2}$. Since $\mathcal{F}$ is a down-set, by definition, if a set is in $\mathcal{F}$, all its subsets are also in $\mathcal{F}$. As $R_{t_1}$ is a subset of $R_{t_2}$ and $R_{t_2} \in \mathcal{F}$, it must be that $R_{t_1} \in \mathcal{F}$.
Thus, the event $\{R_{t_2} \in \mathcal{F}\}$ implies the event $\{R_{t_1} \in \mathcal{F}\}$. This means that as events in the probability space, $\{R_{t_2} \in \mathcal{F}\} \subseteq \{R_{t_1} \in \mathcal{F}\}$.

For any two events $E_1, E_2$ such that $E_2 \subseteq E_1$, we have $P(E_2) \le P(E_1)$. Applying this to our events:
$P(R_{t_2} \in \mathcal{F}) \le P(R_{t_1} \in \mathcal{F})$.
By the definition of $f(t)$, this is $f(t_2) \le f(t_1)$.

This holds for any $t_1, t_2 \in [0,1]$ with $t_1 \le t_2$. Therefore, $f(t)$ is a non-increasing function on $[0,1]$.

The final answer is $\boxed{f(t) \text{ is non-increasing}}$.