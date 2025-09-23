The problem asks for the computation of $(V_H-1)(V_R-1) + \tau(X)$. From the problem description and the diagram, the hexagonal faces have $V_H = 6$ vertices and the rectangular faces have $V_R = 4$ vertices. The main task is to determine the space $X$ and compute the order of its homology torsion, $\tau(X)$.

First, we identify the topological space $X$. The polyhedron is a hexagonal prism. The identifications are specified on its boundary.
1.  The top hexagonal face is identified with the bottom hexagonal face. This corresponds to taking a product of a hexagon with an interval, $H \times [0,1]$, and identifying the top $H \times \{1\}$ with the bottom $H \times \{0\}$. This creates a circular dimension, suggesting a product space with $S^1$.
2.  The side faces (rectangles) are identified in pairs based on color. A red face is identified with the other red face, green with green, and blue with blue. This corresponds to identifying the boundary edges of the hexagon $H$. The hexagon's edges are labeled in pairs as red, green, blue. Following the arrows, we see that opposite edges of the hexagon are identified with the same orientation. Identifying the opposite edges of a hexagon in this manner yields a non-orientable closed surface of genus 3, which is the connected sum of three real projective planes, $N_3 = \mathbb{R}P^2 \# \mathbb{R}P^2 \# \mathbb{R}P^2$.

Combining these observations, the space $X$ is the product of the surface $N_3$ and a circle $S^1$. So, $X \cong N_3 \times S^1$.

Next, we compute the homology groups of $X$ using the Künneth formula for a product space. The homology of $X = N_3 \times S^1$ is given by:
$$ H_n(X) \cong \bigoplus_{p+q=n} (H_p(N_3) \otimes H_q(S^1)) \oplus \bigoplus_{p+q=n-1} \text{Tor}(H_p(N_3), H_q(S^1)) $$
The homology groups of $S^1$ are $H_0(S^1) = \mathbb{Z}$, $H_1(S^1) = \mathbb{Z}$, and $H_i(S^1)=0$ for $i>1$. Since these are all torsion-free, the Tor part of the Künneth formula is zero.
$$ H_n(X) \cong \bigoplus_{p+q=n} H_p(N_3) \otimes H_q(S^1) $$
The homology groups of $N_3$ (non-orientable surface of genus 3) are:
$H_0(N_3) = \mathbb{Z}$
$H_1(N_3) = \mathbb{Z}^{3-1} \oplus \mathbb{Z}_2 = \mathbb{Z}^2 \oplus \mathbb{Z}_2$
$H_2(N_3) = 0$ (since $N_3$ is non-orientable and closed).

Now we compute the homology of $X$:
$H_0(X) = H_0(N_3) \otimes H_0(S^1) = \mathbb{Z} \otimes \mathbb{Z} = \mathbb{Z}$.
$H_1(X) = (H_1(N_3) \otimes H_0(S^1)) \oplus (H_0(N_3) \otimes H_1(S^1)) = ((\mathbb{Z}^2 \oplus \mathbb{Z}_2) \otimes \mathbb{Z}) \oplus (\mathbb{Z} \otimes \mathbb{Z}) = (\mathbb{Z}^2 \oplus \mathbb{Z}_2) \oplus \mathbb{Z} = \mathbb{Z}^3 \oplus \mathbb{Z}_2$.
$H_2(X) = (H_2(N_3) \otimes H_0(S^1)) \oplus (H_1(N_3) \otimes H_1(S^1)) = (0 \otimes \mathbb{Z}) \oplus ((\mathbb{Z}^2 \oplus \mathbb{Z}_2) \otimes \mathbb{Z}) = \mathbb{Z}^2 \oplus \mathbb{Z}_2$.
$H_3(X) = (H_2(N_3) \otimes H_1(S^1)) = 0 \otimes \mathbb{Z} = 0$.

Finally, we find $\tau(X)$, the order of the torsion part of $H_*(X) = H_0(X) \oplus H_1(X) \oplus H_2(X) \oplus \dots$. The torsion subgroup of $H_*(X)$ is the direct sum of the torsion subgroups of each $H_i(X)$.
Torsion part of $H_1(X)$ is $\mathbb{Z}_2$.
Torsion part of $H_2(X)$ is $\mathbb{Z}_2$.
The total torsion subgroup is $\mathbb{Z}_2 \oplus \mathbb{Z}_2$. The order of this group is $\tau(X) = |\mathbb{Z}_2 \oplus \mathbb{Z}_2| = 2 \times 2 = 4$.

Now we can compute the final number:
$(V_H-1)(V_R-1) + \tau(X) = (6-1)(4-1) + 4 = 5 \times 3 + 4 = 15 + 4 = 19$.