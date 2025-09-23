Let the grid cells be indexed by $(i, j)$ for $1 \le i, j \le 2n$, where $i$ is the row index and $j$ is the column index.
The number in cell $(i, j)$ is given by the specified column-major numbering scheme. The cells in column $j$ are numbered from $(j-1)2n + 1$ to $(j-1)2n + 2n = j \cdot 2n$. Within column $j$, the number increases with the row index $i$.
Thus, the number in cell $(i, j)$ is $N(i, j) = (j-1)2n + i$.

Let $c(i, j)$ be an indicator variable which is $1$ if the cell $(i, j)$ is black and $0$ if it is white.
The problem states that half the cells are black, so $\sum_{i=1}^{2n} \sum_{j=1}^{2n} c(i, j) = \frac{1}{2} (2n \times 2n) = 2n^2$.
The problem also states that half the cells in each row are black. Since each row has $2n$ cells, this means that for each row $i$ ($1 \le i \le 2n$), $\sum_{j=1}^{2n} c(i, j) = \frac{1}{2} (2n) = n$.
Similarly, half the cells in each column are black. Since each column has $2n$ cells, this means that for each column $j$ ($1 \le j \le 2n$), $\sum_{i=1}^{2n} c(i, j) = \frac{1}{2} (2n) = n$.
These conditions imply the first condition on the total number of black cells, as $\sum_{i=1}^{2n} \sum_{j=1}^{2n} c(i, j) = \sum_{i=1}^{2n} n = 2n^2$ and $\sum_{j=1}^{2n} \sum_{i=1}^{2n} c(i, j) = \sum_{j=1}^{2n} n = 2n^2$.
Any $(0,1)$-matrix $C = [c(i,j)]$ with all row sums and column sums equal to $n$ represents a valid coloring. Such matrices are known to exist.

The sum of all numbers in the black cells is $S = \sum_{i=1}^{2n} \sum_{j=1}^{2n} c(i, j) N(i, j)$.
Substitute the expression for $N(i, j)$:
$S = \sum_{i=1}^{2n} \sum_{j=1}^{2n} c(i, j) ((j-1)2n + i)$.
We can split the sum into two parts:
$S = \sum_{i=1}^{2n} \sum_{j=1}^{2n} c(i, j) (j-1)2n + \sum_{i=1}^{2n} \sum_{j=1}^{2n} c(i, j) i$.

Consider the first part: $\sum_{i=1}^{2n} \sum_{j=1}^{2n} c(i, j) (j-1)2n$.
We can swap the order of summation and factor out $(j-1)2n$:
$\sum_{j=1}^{2n} \sum_{i=1}^{2n} c(i, j) (j-1)2n = \sum_{j=1}^{2n} (j-1)2n \left( \sum_{i=1}^{2n} c(i, j) \right)$.
Using the column sum constraint, $\sum_{i=1}^{2n} c(i, j) = n$:
$\sum_{j=1}^{2n} (j-1)2n \cdot n = 2n^2 \sum_{j=1}^{2n} (j-1)$.
The sum $\sum_{j=1}^{2n} (j-1) = 0 + 1 + \dots + (2n-1) = \frac{(2n-1)2n}{2} = n(2n-1)$.
So the first part of $S$ is $2n^2 \cdot n(2n-1) = 2n^3(2n-1) = 4n^4 - 2n^3$.

Consider the second part: $\sum_{i=1}^{2n} \sum_{j=1}^{2n} c(i, j) i$.
We can swap the order of summation and factor out $i$:
$\sum_{j=1}^{2n} \sum_{i=1}^{2n} c(i, j) i = \sum_{i=1}^{2n} \sum_{j=1}^{2n} c(i, j) i = \sum_{i=1}^{2n} i \left( \sum_{j=1}^{2n} c(i, j) \right)$.
Using the row sum constraint, $\sum_{j=1}^{2n} c(i, j) = n$:
$\sum_{i=1}^{2n} i \cdot n = n \sum_{i=1}^{2n} i$.
The sum $\sum_{i=1}^{2n} i = \frac{2n(2n+1)}{2} = n(2n+1)$.
So the second part of $S$ is $n \cdot n(2n+1) = n^2(2n+1) = 2n^3 + n^2$.

Combining the two parts, the total sum of the numbers in the black cells is:
$S = (4n^4 - 2n^3) + (2n^3 + n^2) = 4n^4 + n^2$.

This sum $S$ is independent of the specific choice of the matrix $C = [c(i,j)]$, as long as it satisfies the conditions that $c(i,j) \in \{0,1\}$ and all row and column sums are equal to $n$. This is because the numbering scheme $N(i,j)$ can be written as a sum of a function of $i$ and a function of $j$, i.e., $N(i,j) = f(i) + g(j)$ where $f(i)=i$ and $g(j)=(j-1)2n$. For any such numbering scheme, the sum $\sum_{i,j} c(i,j) (f(i)+g(j))$ is constant for any matrix $C$ with fixed row and column sums.

Since the sum $S$ is constant for any valid coloring, the minimal and the maximal possible sum are equal to this constant value.

The minimal sum is $4n^4 + n^2$.
The maximal sum is $4n^4 + n^2$.

The final answer is $\boxed{4n^4+n^2}$.