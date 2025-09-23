This step is worth 1 point. We have
$$
f(f(f(z_1) + z_2)) =f(z_1+f(z_2)) = f(f(z_2)+z_1)=z_2+f(z_1)=f(z_1)+z_2.
$$
Let
$$
z_3:=f(z_1)+z_2.
$$
Then
$$
f^2(z_3)=z_3.
$$
Since $z_3$ can take all values in $\mathbb{V}$, it follows that
$$
f^2(z) = z \text{ for all } z \in \mathbb{V}.
$$
Thus, $f(z)$ is an involution on $\mathbb{V}$.


This step is worth 1 point.
Substituting $f(z_1)$ instead of $z_1$ in the given equation, we get
$$
f(f^2(z_1) + z_2)  = f(f(f(z_1))+z_2)=f(z_1) + f(z_2).
$$
Since $f^2(z_1)=z_1$, we have
$$
f(z_1+z_2)=f(z_1) + f(z_2),
$$
i.e., $f(z)$ has to be additive.


This step is worth 6 points.
The question now is to describe all additive involutions on $\mathbb{V}$.
It is a simple and well-known fact that any additive function $f$ on $\mathbb{V}$ satisfies
$f(qz) = qf(z)$ for all $q \in \mathbb{Q}$. Let
$$
A = \{z \in \mathbb{V} \mid f(z) = z\}, \quad B = \{z \in \mathbb{V} \mid f(z) = -z\}.
$$
We have
$$\tag{1}
A \cap B = \{0\}.
$$
Moreover, $\mathbb{Q}A \subseteq A$ and $A + A \subseteq A$, as well as $\mathbb{Q}B \subseteq B$ and $B + B \subseteq B$, due to the additivity of $f$. This implies that $A$ and $B$ are subspaces of $\mathbb{V}$ when viewed as a vector space over the field of rational numbers $\mathbb{Q}$.

Let us now fix $z \in \mathbb{V}$ and define
$$
z^+ = \frac{1}{2}(z + f(z)) \quad \text{and} \quad z^- = \frac{1}{2}(z - f(z)).
$$
Then, we have
$$\tag{2}
z = z^+ + z^-.
$$
Furthermore, we can conclude that
$$\tag{3}
f(z^+) = f\left(\frac{1}{2}(z + f(z))\right) = \frac{1}{2}f(z) + \frac{1}{2}f^2(z) = \frac{1}{2}f(z) + \frac{1}{2}z = z^+,
$$
and
$$\tag{4}
f(z^-) = f\left(\frac{1}{2}(z - f(z))\right) = \frac{1}{2}f(z) - \frac{1}{2}f^2(z) = \frac{1}{2}f(z) - \frac{1}{2}z = -z^-.
$$
Consequently, (1), (2), (3) and (4) imply that
$$
A\oplus B=\mathbb{V}.
$$


This step is worth 2 points.
We will now show that any pair of linear subspaces $A, B \subset \mathbb{V}$ such that
$$
A\oplus B=\mathbb{V}
$$
defines a function $f$ which satisfies the equation
$$
f(f(z_1) + z_2) = z_1 + f(z_2).
$$
Let $A$ and $B$ be as above.
Given that $A \cap B = \{0\}$ and $A + B = \mathbb{V}$, every $z \in \mathbb{V}$ has a unique representation as
$$
z = z_A + z_B,
$$
where $z_A \in A$ and $z_B \in B$. Define a function $f: \mathbb{V}\to \mathbb{V}$ by
$$
f(z) := z_A - z_B.
$$
Now we will show that such a function $f(z)$ satisfies the condition of the problem. Indeed,  let
$z^1, z^2 \in \mathbb{V}$ be arbitrary, and let
$$
z^1 = z_A^1 + z_B^1 \text{ and }z^2 = z_A^2 + z_B^2.
$$
Then:
$$
\begin{aligned}
f(f(z^1) + z^2) &= f(f(z_A^1 + z_B^1) + z_A^2 + z_B^2)\\& = f(z_A^1 -z_B^1+z_A^2 + z_B^2 )
\\&= f(z_A^1 +z_A^2 + z_B^2-z_B^1)\\&=z_A^1 +z_A^2 -(z_B^2-z_B^1),
\end{aligned}
$$
where $z_A^1 + z_A^2 \in A$ and $z_B^2 - z_B^1 \in B$. Finally, we have
$$
f(f(z^1) + z^2) =z_A^1 +z_A^2 -(z_B^2-z_B^1) = z_A^1 +z_B^1 +z_B^2-z_B^2=z^1 + f(z^2)
$$