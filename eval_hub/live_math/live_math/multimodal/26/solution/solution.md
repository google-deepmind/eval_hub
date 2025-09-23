The 4-manifold $X$ is described by a handle decomposition given by the Kirby diagram. We can determine the chain complex of $X$ from this diagram.

1.  **Identify handles:** The diagram has:
    *   One 0-handle (implicit, corresponding to the base $B^4$).
    *   Four 1-handles (the unknotted circles with a dot).
    *   Three 2-handles (the knotted/linked components with integer framings: 5, -3, 4).
    There are no 3-handles or 4-handles.

2.  **Form the chain complex:** The cellular chain complex with integer coefficients is therefore of the form:
    $$ 0 \to C_2(X) \xrightarrow{\partial_2} C_1(X) \xrightarrow{\partial_1} C_0(X) \to 0 $$

    where $C_2(X) \cong \mathbb{Z}^3$, $C_1(X) \cong \mathbb{Z}^4$, and $C_0(X) \cong \mathbb{Z}$. The chain groups $C_i(X)$ are zero for $i \geq 3$.

3.  **Define boundary maps:**
    *   The map $\partial_1: C_1(X) \to C_0(X)$ is the zero map because there is only one 0-handle, so every 1-handle is attached to it at both ends.
    *   The map $\partial_2: C_2(X) \to C_1(X)$ is determined by the linking numbers between the attaching circles of the 2-handles and the belt spheres of the 1-handles. The matrix for this map is given as:
        $$ \partial_2 = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix} $$

4.  **Compute homology groups:** The homology groups are calculated from the chain complex. The results are:
    *   $H_0(X) = \text{coker}(\partial_1) = C_0(X) / \text{Im}(\partial_1) = \mathbb{Z}/0 \cong \mathbb{Z}$
    *   $H_1(X) = \ker(\partial_1) / \text{Im}(\partial_2) = C_1(X) / \text{Im}(\partial_2) \cong \mathbb{Z}^2 \oplus \mathbb{Z}_4$
    *   $H_2(X) = \ker(\partial_2) / \text{Im}(\partial_3) = \ker(\partial_2) \cong \mathbb{Z}^2$
    *   $H_3(X) = H_4(X) = 0$ since $C_3(X) = C_4(X) = 0$.

5.  **Extract ranks and torsion:** From the computed homology groups, we find:
    *   $\text{rank}(H_0(X)) = 1$
    *   $\text{rank}(H_1(X)) = 2$
    *   $\text{rank}(H_2(X)) = 2$
    *   The torsion part of the homology is $\text{Tors}(H_*(X)) = \mathbb{Z}_4$. The order of the torsion part is $\tau(X) = |\mathbb{Z}_4| = 4$.

6.  **Calculate the final number:** We substitute these values into the given expression:
    $$ \text{rank}(H_0(X)) + \text{rank}(H_1(X)) + \text{rank}(H_2(X)) + 2\tau(X) = 1 + 2 + 2 + 2(4) = 1 + 2 + 2 + 8 = 13. $$