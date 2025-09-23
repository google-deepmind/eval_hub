# Solution

I'll show that for any finite multiplicative group $G$ of complex numbers with $|G| \geq 2$, the sum of all elements equals zero.

### Proof:

Let $G$ be a finite multiplicative group of complex numbers with $|G| \geq 2$. Since $G$ is a group, it contains the multiplicative identity $1$. And since $|G| \geq 2$, there exists at least one element $g \in G$ such that $g \neq 1$.

Let's denote the sum of all elements in $G$ as:
$$S = \sum_{z \in G} z$$

Now, consider the product $g \cdot S$:
$$g \cdot S = g \cdot \sum_{z \in G} z = \sum_{z \in G} gz$$

Since $G$ is a group, multiplication by $g$ is a bijection from $G$ to itself. In other words, as $z$ ranges over all elements of $G$, $gz$ also ranges over all elements of $G$ (just in a different order). Therefore:
$$\sum_{z \in G} gz = \sum_{z \in G} z = S$$

This gives us:
$$g \cdot S = S$$

Rearranging:
$$(g-1) \cdot S = 0$$

Since we chose $g \neq 1$, we know that $g-1 \neq 0$. Therefore, the only possibility is:
$$S = 0$$

Thus, we have proven that:
$$\sum_{z \in G} z = 0$$

as required.