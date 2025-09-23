Let $G$ be a finite group of order $|G|=p^n\cdot q^2$, where $p>q>2$ are prime numbers and $n\geq 1$. We are given that the commutator subgroup $[G, G]$ has order $q^2$. We want to prove that there exists a subgroup $H$ of $G$ of order $p^n$ that is both abelian and normal in $G$.

Let $G' = [G, G]$. We are given $|G'|=q^2$. Since $|G'|=q^2$, $G'$ is an abelian group. $G'$ is also a normal subgroup of $G$ by definition of the commutator subgroup.

Let $P$ be a Sylow $p$-subgroup of $G$. By Sylow's theorem, $|P|=p^n$. The number of Sylow $p$-subgroups, $n_p$, must divide $|G|/|P|=q^2$ and satisfy $n_p \equiv 1 \pmod p$.
The divisors of $q^2$ are $1, q, q^2$. So $n_p \in \{1, q, q^2\}$.
$n_p \equiv 1 \pmod p$.
If $n_p=q$, then $q \equiv 1 \pmod p$. Since $p>q$, this congruence can only hold if $q=1$, which is not a prime. Thus $n_p \ne q$.
If $n_p=q^2$, then $q^2 \equiv 1 \pmod p$. This means $p$ divides $q^2-1=(q-1)(q+1)$. Since $p$ is a prime, $p$ must divide $q-1$ or $q+1$. As $p>q$, $p>q-1$, so $p$ cannot divide $q-1$. Therefore, $p$ must divide $q+1$. Since $p>q$, we must have $q+1=kp$ for some integer $k \geq 1$. If $k=1$, $p=q+1$. Since $p$ and $q$ are primes with $p>q$, this is only possible if $q=2$ and $p=3$. However, we are given $q>2$. So $q+1$ cannot be $p$. If $k \geq 2$, $q+1 \geq 2p$. But $p>q$ implies $2p > 2q$, so $q+1 > 2q$, which means $1>q$. This contradicts $q>2$.
Thus, $n_p$ cannot be $q^2$.
The only possibility left is $n_p=1$.
This means $G$ has a unique Sylow $p$-subgroup. Let $P_0$ be this unique Sylow $p$-subgroup. $P_0$ is normal in $G$. $|P_0|=p^n$.

$P_0 \trianglelefteq G$ and $G' \trianglelefteq G$.
Consider the intersection $P_0 \cap G'$. Elements of $P_0$ have order a power of $p$. Elements of $G'$ are products of commutators; $G'$ is a subgroup of order $q^2$, so elements of $G'$ have order a power of $q$. Since $p$ and $q$ are distinct primes, the elements in the intersection must have order $p^a q^b$. Being in $P_0$, $b=0$. Being in $G'$, $a=0$. So the order must be $p^0q^0=1$. Thus $P_0 \cap G' = \{e\}$.

The order of the subgroup $P_0 G'$ is $|P_0||G'|/|P_0 \cap G'| = p^n q^2 / 1 = |G|$. So $G=P_0 G'$.
Since $P_0$ and $G'$ are normal subgroups and $P_0 \cap G' = \{e\}$, $G$ is the internal direct product of $P_0$ and $G'$. $G \cong P_0 \times G'$. This also implies that elements of $P_0$ commute with elements of $G'$. For $x \in P_0, y \in G'$, $[x,y] = x^{-1}y^{-1}xy$. Since $P_0 \trianglelefteq G$, $y^{-1}xy \in P_0$. So $[x,y] = x^{-1}(y^{-1}xy) \in P_0$. Since $G' \trianglelefteq G$, $x^{-1}y^{-1}x \in G'$. So $[x,y] = (x^{-1}y^{-1}x)y \in G'$. Thus $[x,y] \in P_0 \cap G' = \{e\}$. So $xy=yx$.

The commutator subgroup of a direct product $A \times B$ is $[A \times B, A \times B] = [A,A] \times [B,B]$.
In our case, $G \cong P_0 \times G'$. So $[G,G] \cong [P_0,P_0] \times [G',G']$.
We are given $G'=[G,G]$, so $G' \cong [P_0,P_0] \times [G',G']$.
Also, $G'$ is an abelian group of order $q^2$. The commutator subgroup of an abelian group is the trivial group $\{e\}$. So $[G',G']=\{e\}$.
Thus, $G' \cong [P_0,P_0] \times \{e\}$, which means $G' \cong [P_0,P_0]$.
The order of $G'$ is $q^2$, so $|[P_0,P_0]|=q^2$.

$P_0$ is a group of order $p^n$. $[P_0,P_0]$ is a subgroup of $P_0$. The order of any subgroup of $P_0$ must be a power of $p$. So $|[P_0,P_0]|=p^k$ for some integer $k$ with $0 \leq k \leq n$.
We have $q^2 = p^k$.
Since $p$ and $q$ are distinct primes, the equality $q^2=p^k$ can only hold if $k=0$ and $q^2=p^0=1$, or if $p=q$ and $k=2$.
Since $p>q$ and $q>2$, $p$ and $q$ are distinct primes and $q^2 \ge 3^2=9$. So $q^2=1$ is impossible.
Therefore, the condition $q^2=p^k$ forces $k=0$.
$|[P_0,P_0]| = p^0 = 1$.
The commutator subgroup of $P_0$ is trivial. This means $P_0$ is an abelian group.

Let $H=P_0$. We have shown that $P_0$ is a subgroup of $G$ of order $p^n$, $P_0$ is normal in $G$, and $P_0$ is abelian.
Thus, $H=P_0$ satisfies all the required properties.

The existence of a group $G$ with the given properties ($|G|=p^n q^2$, $p>q>2$, $|[G,G]|=q^2$) implies that its unique Sylow $p$-subgroup $P_0$ must satisfy $|[P_0,P_0]|=q^2$. However, $P_0$ being a $p$-group requires $|[P_0,P_0]|$ to be a power of $p$. This led to the conclusion that $P_0$ must be abelian ($|[P_0,P_0]|=1$) and $q^2=1$. The contradiction $q^2=1$ shows that no such group $G$ can exist.

However, the question asks to prove that IF such a group $G$ exists, THEN there exists a subgroup $H$ with the specified properties. Our derivation shows that if such a $G$ exists, then its unique Sylow $p$-subgroup $P_0$ must be abelian.

So, let $H=P_0$.
1. $|H|=p^n$ by definition of $P_0$.
2. $H \trianglelefteq G$ because $P_0$ is the unique Sylow $p$-subgroup.
3. $H$ is abelian because $|[H,H]|=|[P_0,P_0]|=q^2$, and since $H=P_0$ is a $p$-group, its commutator subgroup must have $p$-power order. $q^2=p^k$ implies $k=0$, so $|[P_0,P_0]|=1$, meaning $P_0$ is abelian.

Thus, if such a group $G$ exists, the unique Sylow $p$-subgroup $P_0$ serves as the required subgroup $H$.

The final answer is $\boxed{H=P_0 \text{ where } P_0 \text{ is the unique Sylow } p\text{-subgroup of } G}$.