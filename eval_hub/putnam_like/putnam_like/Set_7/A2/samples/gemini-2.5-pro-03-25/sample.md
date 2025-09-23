Solution:

Let $G$ be a finite multiplicative group of complex numbers with $|G| = n \geq 2$. We want to show that the sum of its elements is zero, i.e., $S = \sum_{z \in G} z = 0$.

Since $G$ is a group under multiplication and its elements are complex numbers, we know the following properties hold:
1. Closure: For any $z_1, z_2 \in G$, the product $z_1 z_2 \in G$.
2. Identity: The multiplicative identity $1$ is in $G$.
3. Inverse: For every $z \in G$, its inverse $z^{-1}$ is also in $G$.
4. $G$ is a finite set, $G = \{z_1, z_2, \dots, z_n\}$.
5. Since $G$ is a multiplicative group of complex numbers, $0 \notin G$.

Let $S$ be the sum of all elements in $G$:
$$ S = \sum_{z \in G} z $$
Since $|G| = n \geq 2$, there must exist at least one element in $G$ that is not the identity element $1$. Let $w$ be such an element, so $w \in G$ and $w \neq 1$.

Consider the product $wS$:
$$ wS = w \left( \sum_{z \in G} z \right) = \sum_{z \in G} (wz) $$
Let's examine the set $wG = \{wz : z \in G\}$.
Since $w \in G$ and $G$ is closed under multiplication, for any $z \in G$, the product $wz$ is also an element of $G$. Thus, $wG \subseteq G$.

Now consider the map $f: G \to G$ defined by $f(z) = wz$. We show this map is a bijection (a permutation of $G$).
Suppose $z_1, z_2 \in G$ such that $f(z_1) = f(z_2)$. Then $wz_1 = wz_2$.
Since $w \in G$, $w$ is a non-zero complex number, and its inverse $w^{-1}$ exists in $G$. Multiplying the equation by $w^{-1}$ on the left, we get:
$$ w^{-1}(wz_1) = w^{-1}(wz_2) $$
$$ (w^{-1}w)z_1 = (w^{-1}w)z_2 $$
$$ 1 \cdot z_1 = 1 \cdot z_2 $$
$$ z_1 = z_2 $$
This shows that the map $f$ is injective.
Since $G$ is a finite set, an injective map from $G$ to itself must also be surjective. Thus, $f$ is a bijection.

Since $f$ is a bijection from $G$ to $G$, the set $wG = \{wz : z \in G\}$ is the same as the set $G$.
Therefore, the sum of the elements in $wG$ is the same as the sum of the elements in $G$:
$$ \sum_{z' \in wG} z' = \sum_{z \in G} z $$
We have previously established that $wS = \sum_{z \in G} (wz)$. The elements $wz$ for $z \in G$ are exactly the elements of $wG$.
So, $wS = \sum_{z' \in wG} z'$.
Combining these, we get:
$$ wS = S $$
Subtracting $S$ from both sides gives:
$$ wS - S = 0 $$
$$ (w-1)S = 0 $$
We chose $w \in G$ such that $w \neq 1$. Therefore, the complex number $w-1$ is not equal to zero.
We have a product of two complex numbers, $w-1$ and $S$, which equals zero. Since $\mathbb{C}$ is a field (and thus an integral domain), if a product is zero, at least one of the factors must be zero.
Since $w-1 \neq 0$, it must be the case that $S=0$.

Thus, we have shown that $\sum_{z \in G} z = 0$.

Final Answer: The final answer is $\boxed{\sum_{z \in G} z = 0}$