Let the grid be denoted by $G$, with $2n$ rows and $2n$ columns. The cell at row $i$ and column $j$ is denoted by $(i, j)$, where $1 \le i, j \le 2n$. The total number of cells is $(2n)^2 = 4n^2$.

The cells are numbered from $1$ to $4n^2$. The numbering starts at the top left cell $(1, 1)$, goes down the first column, then continues at the top of the second column, and so on.
The cell $(i, j)$ contains the number $N(i, j)$.
The first column cells $(1, 1), (2, 1), \dots, (2n, 1)$ contain numbers $1, 2, \dots, 2n$. So $N(i, 1) = i$.
The second column cells $(1, 2), (2, 2), \dots, (2n, 2)$ contain numbers $2n+1, 2n+2, \dots, 4n$. So $N(i, 2) = 2n+i$.
In general, the $j$-th column starts with number $(j-1)2n + 1$. The cell $(i, j)$ is the $i$-th cell in the $j$-th column, so its number is $N(i, j) = (j-1)2n + i$.
Let's check the last cell $(2n, 2n)$. $N(2n, 2n) = (2n-1)2n + 2n = 4n^2 - 2n + 2n = 4n^2$. This is correct.

The cells are colored black and white. Let $C(i, j) = 1$ if the cell $(i, j)$ is black, and $C(i, j) = 0$ if it is white.
The problem states that half the cells are black and half are white. The total number of black cells is $\frac{1}{2}(4n^2) = 2n^2$.
The condition is that exactly half the cells in each row are black, and exactly half the cells in each column are black.
This translates to the following conditions:
For each row $i \in \{1, \dots, 2n\}$, $\sum_{j=1}^{2n} C(i, j) = n$.
For each column $j \in \{1, \dots, 2n\}$, $\sum_{i=1}^{2n} C(i, j) = n$.
These conditions imply the total number of black cells is $\sum_{i=1}^{2n} \sum_{j=1}^{2n} C(i, j) = \sum_{i=1}^{2n} n = 2n \cdot n = 2n^2$, which is consistent.

We want to find the minimal and maximal possible sum of the numbers in the black cells. Let $S$ be this sum.
$S = \sum_{i=1}^{2n} \sum_{j=1}^{2n} C(i, j) N(i, j)$.
Substitute the expression for $N(i, j)$:
$S = \sum_{i=1}^{2n} \sum_{j=1}^{2n} C(i, j) ((j-1)2n + i)$.
Split the sum into two parts:
$S = \sum_{i=1}^{2n} \sum_{j=1}^{2n} C(i, j) (j-1)2n + \sum_{i=1}^{2n} \sum_{j=1}^{2n} C(i, j) i$.
Rearrange the order of summation:
$S = \sum_{j=1}^{2n} (j-1)2n \left( \sum_{i=1}^{2n} C(i, j) \right) + \sum_{i=1}^{2n} i \left( \sum_{j=1}^{2n} C(i, j) \right)$.
Now apply the row and column sum conditions. We know that $\sum_{i=1}^{2n} C(i, j) = n$ for every column $j$, and $\sum_{j=1}^{2n} C(i, j) = n$ for every row $i$.
$S = \sum_{j=1}^{2n} (j-1)2n \cdot n + \sum_{i=1}^{2n} i \cdot n$.
Factor out the constants $2n^2$ and $n$:
$S = 2n^2 \sum_{j=1}^{2n} (j-1) + n \sum_{i=1}^{2n} i$.
The first sum is $\sum_{k=0}^{2n-1} k = \frac{(2n-1)(2n)}{2}$.
The second sum is $\sum_{k=1}^{2n} k = \frac{2n(2n+1)}{2}$.
Substitute these sum formulas:
$S = 2n^2 \left( \frac{(2n-1)(2n)}{2} \right) + n \left( \frac{2n(2n+1)}{2} \right)$.
Simplify the expression:
$S = 2n^3 (2n-1) + n^2 (2n+1)$.
$S = (4n^4 - 2n^3) + (2n^3 + n^2)$.
$S = 4n^4 + n^2$.

The sum $S$ depends only on $n$, the size parameter of the grid. It does not depend on the specific arrangement of black cells $C(i, j)$, as long as the row and column sum conditions are satisfied.
Such valid colorings exist for any $n \ge 1$. For example, the chessboard coloring where $(i,j)$ is black if $i+j$ is even satisfies the conditions.
Since the sum $S$ is constant for any valid coloring configuration, the minimal possible sum and the maximal possible sum are the same, equal to this constant value.

Minimal sum = $4n^4 + n^2$.
Maximal sum = $4n^4 + n^2$.

Let's verify this result by considering the sum of numbers in the white cells. Let $C'(i, j) = 1 - C(i, j)$, so $C'(i, j) = 1$ if cell $(i, j)$ is white.
The row sums for $C'$ are $\sum_{j=1}^{2n} (1 - C(i, j)) = 2n - \sum_{j=1}^{2n} C(i, j) = 2n - n = n$.
The column sums for $C'$ are $\sum_{i=1}^{2n} (1 - C(i, j)) = 2n - \sum_{i=1}^{2n} C(i, j) = 2n - n = n$.
So the configuration of white cells $C'$ also satisfies the same conditions.
The sum of numbers in the white cells, $S_W$, can be calculated using the same formula as for $S$:
$S_W = \sum_{i=1}^{2n} \sum_{j=1}^{2n} C'(i, j) N(i, j) = 4n^4 + n^2$.
The total sum of all numbers in the grid is $S_{total} = \sum_{k=1}^{4n^2} k = \frac{4n^2(4n^2+1)}{2} = 2n^2(4n^2+1) = 8n^4 + 2n^2$.
We should have $S + S_W = S_{total}$.
Indeed, $(4n^4 + n^2) + (4n^4 + n^2) = 8n^4 + 2n^2 = S_{total}$.
This confirms that the sum of black cells is fixed at $S_{total}/2$.

Final Answer: The final answer is $\boxed{4n^4+n^2}$ for both the minimal and maximal sums.

Minimal possible sum: $4n^4 + n^2$.
Maximal possible sum: $4n^4 + n^2$.

```latex
Let the grid be of size $2n \times 2n$. The cell at row $i$ and column $j$ is denoted $(i, j)$, where $1 \le i, j \le 2n$.
The numbering $N(i, j)$ is defined column by column, starting from the top left cell. The numbers in column $j$ range from $(j-1)2n+1$ to $j(2n)$. Thus, the number in cell $(i, j)$ is $N(i, j) = (j-1)2n + i$.

A coloring of the grid is given by a matrix $C$, where $C(i, j) = 1$ if cell $(i, j)$ is black, and $C(i, j) = 0$ if cell $(i, j)$ is white.
The problem states that half the cells ($2n^2$) are black and half are white.
Also, in each row $i$, there are exactly $n$ black cells: $\sum_{j=1}^{2n} C(i, j) = n$.
And in each column $j$, there are exactly $n$ black cells: $\sum_{i=1}^{2n} C(i, j) = n$.

We want to find the minimal and maximal possible sum of the numbers in the black cells. Let $S$ be this sum:
$$ S = \sum_{i=1}^{2n} \sum_{j=1}^{2n} C(i, j) N(i, j) $$
Substitute the expression for $N(i, j)$:
$$ S = \sum_{i=1}^{2n} \sum_{j=1}^{2n} C(i, j) \left( (j-1)2n + i \right) $$
We can split the sum into two parts:
$$ S = \sum_{i=1}^{2n} \sum_{j=1}^{2n} C(i, j) (j-1)2n + \sum_{i=1}^{2n} \sum_{j=1}^{2n} C(i, j) i $$
Rearrange the order of summation to group terms by columns for the first part and by rows for the second part:
$$ S = \sum_{j=1}^{2n} (j-1)2n \left( \sum_{i=1}^{2n} C(i, j) \right) + \sum_{i=1}^{2n} i \left( \sum_{j=1}^{2n} C(i, j) \right) $$
Now, apply the row sum and column sum conditions: $\sum_{i=1}^{2n} C(i, j) = n$ and $\sum_{j=1}^{2n} C(i, j) = n$.
$$ S = \sum_{j=1}^{2n} (j-1)2n \cdot n + \sum_{i=1}^{2n} i \cdot n $$
Factor out constants:
$$ S = 2n^2 \sum_{j=1}^{2n} (j-1) + n \sum_{i=1}^{2n} i $$
Use the formulas for the sum of the first $k$ integers and the sum of the first $k-1$ integers: $\sum_{k=1}^{m} k = \frac{m(m+1)}{2}$ and $\sum_{k=0}^{m-1} k = \frac{(m-1)m}{2}$. Here $m = 2n$.
$$ S = 2n^2 \left( \frac{(2n-1)(2n)}{2} \right) + n \left( \frac{2n(2n+1)}{2} \right) $$
Simplify the expression:
$$ S = 2n^3 (2n-1) + n^2 (2n+1) $$
$$ S = (4n^4 - 2n^3) + (2n^3 + n^2) $$
$$ S = 4n^4 + n^2 $$
The sum $S$ evaluates to a specific value $4n^4 + n^2$ which depends only on $n$. This means that for any valid coloring that satisfies the given conditions, the sum of the numbers in the black cells is always the same.
Therefore, the minimal possible sum and the maximal possible sum are equal to this value.

Minimal sum = $4n^4 + n^2$.
Maximal sum = $4n^4 + n^2$.

Final Answer: The final answer is $\boxed{4n^4+n^2}$ for both the minimal and maximal sums.
```