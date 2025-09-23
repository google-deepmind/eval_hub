Let $P(z_1, z_2)$ be the assertion $f(f(z_1)+z_2)=z_1+f(z_2)$.

$P(0, z_2) \implies f(f(0)+z_2) = 0+f(z_2) = f(z_2)$.
Let $c=f(0)$. Then $f(c+z_2) = f(z_2)$ for all $z_2 \in \mathbb{V}$. This means $f$ is periodic with period $c$.

$P(z_1, 0) \implies f(f(z_1)+0) = z_1+f(0)$.
So $f(f(z_1)) = z_1+c$ for all $z_1 \in \mathbb{V}$.

Apply $f$ to the equation $f(f(z_1))=z_1+c$:
$f(f(f(z_1))) = f(z_1+c)$.
Let $w=f(z_1)$. Then $f(w)=z_1+c$. Applying $f$ again, we get $f(f(w))=f(z_1+c)$, so $w+c = f(z_1+c)$.
Substituting $w=f(z_1)$, we get $f(z_1)+c = f(z_1+c)$ for all $z_1 \in \mathbb{V}$.

We have two properties involving $c$:
1) $f(z+c) = f(z)+c$ for all $z \in \mathbb{V}$.
2) $f(z+c) = f(z)$ for all $z \in \mathbb{V}$ (from $f(c+z_2)=f(z_2)$).

Comparing these two equations, we get $f(z)+c = f(z)$, which implies $c=0$.
Thus, $f(0)=0$.

Substituting $c=0$ into $f(f(z_1))=z_1+c$, we get $f(f(z_1))=z_1$ for all $z_1 \in \mathbb{V}$.
This means $f$ is an involution and a bijection.

Now the original equation $f(f(z_1)+z_2)=z_1+f(z_2)$ becomes $f(f(z_1)+z_2) = f(f(z_1))+f(z_2)$.
Let $u=f(z_1)$. Since $f$ is surjective, $u$ can be any vector in $\mathbb{V}$.
The equation becomes $f(u+z_2) = f(u)+f(z_2)$ for all $u, z_2 \in \mathbb{V}$.
This is the Cauchy functional equation.

Since $\mathbb{V}$ is a vector space over the field of rational numbers $\mathbb{Q}$, any function $f: \mathbb{V} \to \mathbb{V}$ satisfying the Cauchy functional equation is $\mathbb{Q}$-linear. That is, $f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$ for all $\alpha, \beta \in \mathbb{Q}$ and $x, y \in \mathbb{V}$.

So, the functional equation implies that $f$ must be a $\mathbb{Q}$-linear map satisfying $f \circ f = id_\mathbb{V}$.

Let's check if any $\mathbb{Q}$-linear map $f: \mathbb{V} \to \mathbb{V}$ satisfying $f \circ f = id_\mathbb{V}$ is a solution to the original equation $f(f(z_1)+z_2)=z_1+f(z_2)$.
Since $f$ is $\mathbb{Q}$-linear, $f(f(z_1)+z_2) = f(f(z_1)) + f(z_2)$.
Since $f(f(z_1))=z_1$, this becomes $z_1+f(z_2)$.
This is the right-hand side of the original equation.
Thus, any $\mathbb{Q}$-linear map $f: \mathbb{V} \to \mathbb{V}$ such that $f \circ f = id_\mathbb{V}$ is a solution.

We can characterize such functions. Let $f$ be a $\mathbb{Q}$-linear map on $\mathbb{V}$ such that $f^2 = id_\mathbb{V}$.
Consider the subspaces:
$V_1 = \{v \in \mathbb{V} \mid f(v)=v\}$ (eigenspace for eigenvalue 1)
$V_{-1} = \{v \in \mathbb{V} \mid f(v)=-v\}$ (eigenspace for eigenvalue -1)

For any $z \in \mathbb{V}$, we can write $z = \frac{z+f(z)}{2} + \frac{z-f(z)}{2}$.
Let $z_1 = \frac{z+f(z)}{2}$. $f(z_1) = f(\frac{z+f(z)}{2}) = \frac{1}{2}(f(z)+f(f(z))) = \frac{1}{2}(f(z)+z) = z_1$. So $z_1 \in V_1$.
Let $z_2 = \frac{z-f(z)}{2}$. $f(z_2) = f(\frac{z-f(z)}{2}) = \frac{1}{2}(f(z)-f(f(z))) = \frac{1}{2}(f(z)-z) = -z_2$. So $z_2 \in V_{-1}$.
Thus, any vector $z \in \mathbb{V}$ can be written as a sum of a vector from $V_1$ and a vector from $V_{-1}$. $\mathbb{V} = V_1 + V_{-1}$.

If $v \in V_1 \cap V_{-1}$, then $f(v)=v$ and $f(v)=-v$. This implies $v=-v$, so $2v=0$. Since $\mathbb{V}$ is over $\mathbb{Q}$, $v=0$.
So $V_1 \cap V_{-1} = \{0\}$.

Therefore, $\mathbb{V}$ is the direct sum of $V_1$ and $V_{-1}$: $\mathbb{V} = V_1 \oplus V_{-1}$.
Any $z \in \mathbb{V}$ has a unique decomposition $z=z_1+z_2$ with $z_1 \in V_1$ and $z_2 \in V_{-1}$.
For such a decomposition, $f(z) = f(z_1+z_2) = f(z_1)+f(z_2) = z_1-z_2$.

Conversely, given any direct sum decomposition $\mathbb{V} = V_1 \oplus V_{-1}$, we can define a function $f: \mathbb{V} \to \mathbb{V}$ by $f(z_1+z_2) = z_1-z_2$ for $z_1 \in V_1, z_2 \in V_{-1}$. This function is $\mathbb{Q}$-linear and satisfies $f^2=id_\mathbb{V}$.

So the solutions are precisely the $\mathbb{Q}$-linear maps $f: \mathbb{V} \to \mathbb{V}$ such that $f \circ f = id_\mathbb{V}$. These maps are in one-to-one correspondence with direct sum decompositions of $\mathbb{V}$ into two subspaces $V_1$ and $V_{-1}$, where $V_1$ is the subspace where $f$ acts as identity and $V_{-1}$ is the subspace where $f$ acts as negation.

The final answer is $\boxed{f: \mathbb{V} \to \mathbb{V} \text{ is a } \mathbb{Q}\text{-linear map such that } f \circ f = id_\mathbb{V}}$.