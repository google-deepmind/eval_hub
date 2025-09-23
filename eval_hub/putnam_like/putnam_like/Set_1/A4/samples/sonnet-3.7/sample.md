# Solution: Non-abelian group of order $2n$

To prove that the group $G$ defined by the presentation 
$$\langle x, y : x^n=e, y^2=e, xyxy=e \rangle$$
is a non-abelian group of order $2n$ where $n \geq 3$, I'll show both its order and its non-abelian property.

## Part 1: Finding the order of $G$

Let's begin by deriving a useful relation from the given presentation.

From $xyxy = e$, we can multiply both sides by $y^{-1}$ on the right to get:
$$xyxy \cdot y^{-1} = e \cdot y^{-1}$$
$$xyx = y^{-1}$$

Since $y^2 = e$, we know that $y^{-1} = y$. So:
$$xyx = y$$

This can be rearranged to:
$$xy = yx^{-1}$$

Using this relation, I'll show that every element in $G$ can be uniquely written in one of the forms:
- $x^i$ for $i = 0, 1, 2, \ldots, n-1$, or
- $yx^i$ for $i = 0, 1, 2, \ldots, n-1$

To see why, note that our relation $xy = yx^{-1}$ allows us to rewrite $xy$ as $yx^{-1}$. This means we can push any occurrence of $y$ to the left in a product. Furthermore, since $y^2 = e$, we'll have at most one $y$ in any simplified expression.

For example:
- $yx^i \cdot y = y \cdot (y \cdot x^{-i}) = y^2 \cdot x^{-i} = e \cdot x^{-i} = x^{-i}$
- $x^i \cdot y = y \cdot x^{-i}$ (using our derived relation)

This shows that any product of the generators can be reduced to one of our claimed forms.

Now, are all these elements distinct?
- The elements $x^i$ for $i = 0, 1, 2, \ldots, n-1$ are distinct because $x$ has order $n$.
- Similarly, the elements $yx^i$ for $i = 0, 1, 2, \ldots, n-1$ are distinct.
- No element $x^i$ can equal any element $yx^j$. If they were equal, we'd have $x^i = yx^j$, which would imply $y = x^{i-j}$. But this contradicts the order properties: $y$ has order 2, while $x^{i-j}$ would have an order dividing $n$.

Therefore, $G$ has exactly $2n$ distinct elements.

## Part 2: Proving $G$ is non-abelian

For $G$ to be abelian, we would need $xy = yx$. But we've already established that $xy = yx^{-1}$.

So, for $xy = yx$ to be true, we must have:
$$yx^{-1} = yx$$
$$x^{-1} = x$$

This equation holds only when $x^2 = e$, which means $x$ would have order 2. But we're given that $n \geq 3$, so $x$ has order at least 3, making $x \neq x^{-1}$.

Thus, $xy \neq yx$, proving that $G$ is non-abelian.

## Conclusion

The group $G$ defined by the presentation $\langle x, y : x^n=e, y^2=e, xyxy=e \rangle$ is a non-abelian group of order $2n$ for $n \geq 3$.