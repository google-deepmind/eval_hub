Let $S = \{1, 2, \ldots, n\}$. $\mathcal{F}$ is a family of subsets of $S$ such that if $A \in \mathcal{F}$ and $B \subset A$, then $B \in \mathcal{F}$. This type of family is known as a down-set or an abstract simplicial complex.
The function $f:[0,1] \to \mathbb{R}$ is defined as
\[ f(t) = \sum_{A \in \mathcal{F}} t^{|A|} (1-t)^{|S \setminus A|} \]
We want to prove that $f(t)$ is a non-increasing function of $t$.

We can provide a probabilistic interpretation for $f(t)$. Let $X_1, \ldots, X_n$ be independent and identically distributed Bernoulli random variables with parameter $t$, i.e., $P(X_i=1)=t$ and $P(X_i=0)=1-t$. Let $X_t$ be the random subset of $S$ defined by $X_t = \{i \in S : X_i = 1\}$.
For any given subset $A \subseteq S$, the probability that $X_t = A$ is given by
\[ P(X_t = A) = \prod_{i \in A} P(X_i=1) \prod_{j \in S \setminus A} P(X_i=0) = t^{|A|} (1-t)^{|S \setminus A|} \]
The function $f(t)$ can be written as
\[ f(t) = \sum_{A \in \mathcal{F}} P(X_t = A) \]
This sum represents the probability that the random set $X_t$ belongs to the family $\mathcal{F}$.
\[ f(t) = P(X_t \in \mathcal{F}) \]

We want to show that $f(t)$ is non-increasing, i.e., for any $t_1, t_2 \in [0,1]$ with $t_1 \le t_2$, we have $f(t_1) \ge f(t_2)$.
Let $t_1 \le t_2$. We construct a coupling of the random sets $X_{t_1}$ and $X_{t_2}$.
Let $U_1, \ldots, U_n$ be independent random variables uniformly distributed on $[0,1]$. Define the random sets $X_{t_1}$ and $X_{t_2}$ based on these uniform variables:
\[ X_{t_1} = \{i \in S : U_i \le t_1\} \]
\[ X_{t_2} = \{i \in S : U_i \le t_2\} \]
For any $i \in S$, $P(i \in X_{t_1}) = P(U_i \le t_1) = t_1$, and $P(i \in X_{t_2}) = P(U_i \le t_2) = t_2$. This construction correctly generates the desired random sets.

Now, consider the relationship between $X_{t_1}$ and $X_{t_2}$ for a given outcome of $(U_1, \ldots, U_n)$. Since $t_1 \le t_2$, if $U_i \le t_1$, then $U_i \le t_2$. This means that if $i \in X_{t_1}$, then $i \in X_{t_2}$. Therefore, for every outcome $\omega$ in the sample space, we have $X_{t_1}(\omega) \subseteq X_{t_2}(\omega)$.

Now let's consider the event $X_{t_2} \in \mathcal{F}$. This means that for a given outcome $\omega$, the set $X_{t_2}(\omega)$ is an element of $\mathcal{F}$.
Since $X_{t_1}(\omega) \subseteq X_{t_2}(\omega)$, and $\mathcal{F}$ is a down-set, the property $A \in \mathcal{F}, B \subset A \Rightarrow B \in \mathcal{F}$ implies that if $X_{t_2}(\omega) \in \mathcal{F}$, then $X_{t_1}(\omega)$ must also be in $\mathcal{F}$.
This means that the event $\{ \omega : X_{t_2}(\omega) \in \mathcal{F} \}$ is a subset of the event $\{ \omega : X_{t_1}(\omega) \in \mathcal{F} \}$.
\[ \{ X_{t_2} \in \mathcal{F} \} \subseteq \{ X_{t_1} \in \mathcal{F} \} \]
By the monotonicity property of probability measures, if event $E_1 \subseteq E_2$, then $P(E_1) \le P(E_2)$. Applying this to our events, we get:
\[ P(X_{t_2} \in \mathcal{F}) \le P(X_{t_1} \in \mathcal{F}) \]
Recalling that $f(t) = P(X_t \in \mathcal{F})$, this inequality is $f(t_2) \le f(t_1)$.
Since this holds for any $t_1, t_2 \in [0,1]$ with $t_1 \le t_2$, the function $f(t)$ is non-increasing on $[0,1]$.

Alternative Proof using calculus:
Let $a_k = |\{A \in \mathcal{F} : |A| = k\}|$. Then $f(t) = \sum_{k=0}^n a_k t^k (1-t)^{n-k}$.
We compute the derivative of $f(t)$ with respect to $t$:
\begin{align*} f'(t) &= \sum_{k=0}^n a_k [ k t^{k-1} (1-t)^{n-k} - (n-k) t^k (1-t)^{n-k-1} ] \\ &= \sum_{k=1}^n a_k k t^{k-1} (1-t)^{n-k} - \sum_{k=0}^{n-1} a_k (n-k) t^k (1-t)^{n-k-1} \end{align*}
In the first sum, we change the index by letting $j=k-1$. Then $k=j+1$, and the sum becomes $\sum_{j=0}^{n-1} a_{j+1} (j+1) t^j (1-t)^{n-j-1}$.
In the second sum, we let $j=k$. The sum is $\sum_{j=0}^{n-1} a_j (n-j) t^j (1-t)^{n-j-1}$.
Combining these, we get
\[ f'(t) = \sum_{j=0}^{n-1} [ a_{j+1} (j+1) - a_j (n-j) ] t^j (1-t)^{n-j-1} \]
We need to show that $f'(t) \le 0$ for $t \in [0,1]$.
Consider the property of $\mathcal{F}$. Let $A \in \mathcal{F}$ with $|A|=k$. Any subset $B \subset A$ with $|B|=k-1$ must be in $\mathcal{F}$.
Let $E = \{(A, x) : A \in \mathcal{F}, |A|=k, x \in A\}$. The size of $E$ is $k a_k$.
Let $F = \{(B, x) : B \in \mathcal{F}, |B|=k-1, x \in S \setminus B\}$. The size of $F$ is $(n-(k-1)) a_{k-1} = (n-k+1) a_{k-1}$.
Define a map $\phi: E \to F$ by $\phi(A, x) = (A \setminus \{x\}, x)$.
If $(A, x) \in E$, then $A \in \mathcal{F}$ and $|A|=k$. Let $B = A \setminus \{x\}$. Then $|B|=k-1$. Since $\mathcal{F}$ is a down-set, $B \in \mathcal{F}$. Also $x \in A$, so $x \notin A \setminus \{x\} = B$. Thus $x \in S \setminus B$. So $(B, x) \in F$. The map $\phi$ is well-defined.
The map $\phi$ is injective: If $\phi(A, x) = \phi(A', x')$, then $(A \setminus \{x\}, x) = (A' \setminus \{x'\}, x')$. This implies $x=x'$ and $A \setminus \{x\} = A' \setminus \{x'\}$. Let $B = A \setminus \{x\}$. Then $A = B \cup \{x\}$ and $A' = B \cup \{x'\}$. Since $x=x'$, $A=A'$. Thus $(A, x) = (A', x')$.
Since $\phi$ is an injective map from $E$ to $F$, we must have $|E| \le |F|$.
So, $k a_k \le (n-k+1) a_{k-1}$ for $k=1, \ldots, n$.
Let $j=k-1$, so $k=j+1$. The inequality becomes $(j+1) a_{j+1} \le (n-(j+1)+1) a_j = (n-j) a_j$.
This holds for $j=0, \ldots, n-1$.
Thus, $a_{j+1}(j+1) - a_j(n-j) \le 0$ for all $j=0, \ldots, n-1$.
Let $C_j = a_{j+1}(j+1) - a_j(n-j)$. Then $C_j \le 0$.
The derivative is $f'(t) = \sum_{j=0}^{n-1} C_j t^j (1-t)^{n-j-1}$.
For $t \in (0,1)$, $t^j > 0$ and $(1-t)^{n-j-1} > 0$. Since $C_j \le 0$, each term in the sum is non-positive.
Therefore, $f'(t) \le 0$ for $t \in (0,1)$.
For the endpoints:
$f'(0) = C_0 = a_1(1) - a_0(n-0) = a_1 - n a_0$. If $\mathcal{F} \neq \emptyset$, $a_0=1$. $f'(0) = a_1 - n$. The inequality for $j=0$ states $a_1 \le n a_0 = n$. So $f'(0) \le 0$. If $\mathcal{F} = \emptyset$, $f(t)=0$ and $f'(t)=0$.
$f'(1) = C_{n-1} = a_n(n) - a_{n-1}(n-(n-1)) = n a_n - a_{n-1}$. The inequality for $j=n-1$ states $a_n(n) \le a_{n-1}(n-(n-1)) = a_{n-1}$. So $f'(1) \le 0$.
Since $f'(t) \le 0$ for all $t \in [0,1]$, $f(t)$ is non-increasing on $[0,1]$.

Final Answer: The final answer is $\boxed{f(t) \text{ is non-increasing}}$