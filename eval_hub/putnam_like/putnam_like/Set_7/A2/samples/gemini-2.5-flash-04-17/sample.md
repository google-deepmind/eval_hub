Let $G$ be a finite multiplicative group of complex numbers with $|G| \geq 2$. We want to show that $\sum_{z \in G} z = 0$.

Let $S = \sum_{z \in G} z$.

Since $|G| \geq 2$, $G$ must contain at least two distinct elements. The identity element for a multiplicative group of complex numbers is $1$. So $1 \in G$. Since $|G| \geq 2$, there must exist at least one element $g \in G$ such that $g \neq 1$.

Let $g$ be any element of $G$. Consider the set of products $\{gz \mid z \in G\}$. Since $g \in G$ and $G$ is closed under multiplication, $gz \in G$ for all $z \in G$.
Furthermore, the mapping $\phi_g: G \to G$ defined by $\phi_g(z) = gz$ is a bijection. To see this, it is sufficient to show it is injective because $G$ is finite. If $gz_1 = gz_2$ for $z_1, z_2 \in G$, then multiplying by $g^{-1}$ (which exists in $G$ since $G$ is a group) on the left gives $g^{-1}(gz_1) = g^{-1}(gz_2)$, which simplifies to $(g^{-1}g)z_1 = (g^{-1}g)z_2$, so $1z_1 = 1z_2$, which is $z_1 = z_2$. Thus, $\phi_g$ is injective, and since $G$ is finite, it is also surjective.

This means that the set $\{gz \mid z \in G\}$ is exactly the same set as $G$, just possibly in a different order. Therefore, the sum of the elements in $\{gz \mid z \in G\}$ is equal to the sum of the elements in $G$.
$$ \sum_{z \in G} gz = \sum_{z \in G} z $$
The left side of the equation can be rewritten by factoring out $g$:
$$ g \left( \sum_{z \in G} z \right) = \sum_{z \in G} z $$
Let $S = \sum_{z \in G} z$. The equation becomes:
$$ gS = S $$
Rearranging the terms, we get:
$$ gS - S = 0 $$
$$ (g-1)S = 0 $$

This equation holds for any $g \in G$. Since $|G| \geq 2$, there exists an element $g \in G$ such that $g \neq 1$. For this particular element $g$, the term $(g-1)$ is a non-zero complex number.

We have the product of two complex numbers, $(g-1)$ and $S$, equal to zero. Since complex numbers form a field, the property that if a product of two numbers is zero then at least one of the numbers must be zero holds. As $(g-1) \neq 0$, it must be that $S = 0$.

Thus, $\sum_{z \in G} z = 0$.

The final answer is $\boxed{\sum_{z \in G} z = 0}$.