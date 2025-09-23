The allowed operations are cyclic shifts of the rows and columns. By applying these operations, any cube from a position $(i, j)$ can be moved to the top-left position $(1, 1)$. The resulting grid configuration represents one of the possible color patterns.

The problem asks for the number of *different* color patterns. Two initial positions $(i, j)$ and $(i', j')$ produce the same overall pattern if the grid has a periodic structure. The grid pattern repeats every 4 rows and every 4 columns. This means shifting the grid 4 units vertically or 4 units horizontally leaves the grid unchanged. This establishes a $4 \times 4$ periodicity.

This $4 \times 4$ periodicity implies that the entire $8 \times 8$ grid is effectively determined by a single $4 \times 4$ subgrid, which repeats to fill the whole grid. Consequently, any cube at position $(i, j)$ generates the same pattern as cubes at positions $(i+4, j)$, $(i, j+4)$, and $(i+4, j+4)$ (where indices are taken modulo 8).

We are interested in patterns where the top-left cube is blue. Due to the periodicity, the number of distinct patterns satisfying this condition is equal to the number of blue cubes within one fundamental $4 \times 4$ block. We can choose the top-left $4 \times 4$ subgrid as our fundamental block.

Counting the blue cubes in this $4 \times 4$ subgrid, we find there are 7. Each of these 7 blue cubes corresponds to a unique starting position within the fundamental block that can be moved to the top-left, generating a distinct pattern.

Therefore, there are 7 different color patterns that can be obtained with a blue cube in the top-left position.