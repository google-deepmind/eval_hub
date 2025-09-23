The space $X$ is the result of cutting the embedded Möbius strip along the red lines shown in the diagram. The provided solution states that this cutting process results in 8 distinct connected components. Specifically, there are 7 components that are homeomorphic to cylinders and 1 component that remains a Möbius strip.

Each of these 8 components is a 2-dimensional surface embedded in $\mathbb{R}^3$. We can find the homology of the complement space $\mathbb{R}^3 \setminus X$ by considering a homotopy equivalent space. Each of the 8 surface components of $X$ can be deformation retracted to its 'core', which is a simple closed loop (homeomorphic to a circle).

Thus, the space $X$ is homotopy equivalent to a link $L$ in $\mathbb{R}^3$ consisting of 8 disjoint components (knots). The complement space $\mathbb{R}^3 \setminus X$ is therefore homotopy equivalent to the link complement $\mathbb{R}^3 \setminus L$.

$$ H_1(\mathbb{R}^3 \setminus X, \mathbb{Z}) \cong H_1(\mathbb{R}^3 \setminus L, \mathbb{Z}) $$

A fundamental result from knot theory, which follows from Alexander Duality, states that the first homology group of the complement of an $n$-component link in $\mathbb{R}^3$ is the free abelian group on $n$ generators, $\mathbb{Z}^n$.

In this problem, our link $L$ has 8 components, so $n=8$. Therefore, the first homology group is:

$$ H_1(\mathbb{R}^3 \setminus X, \mathbb{Z}) \cong \mathbb{Z}^8 $$

The rank of a finitely generated abelian group is the rank of its free part. For the group $\mathbb{Z}^8$, the rank is 8.