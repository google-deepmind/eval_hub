Solution step (4 points):
Consider the given $2n \times 2n$ grid with its colouring, but for now, assume that each cell is numbered according to its row. Since in each row one has $n$ black cells, the sum of all numbers in the black cells is then equal to
$$
B = n(1+2+\ldots + 2n) = n\frac{2n(2n+1)}{2}=n^2(2n+1).
$$

Solution step (3 points):
Observe that the numbers in the $i$-th column is $2n(i-1)$ greater than the number in the corresponding cell of the grid from the step 1. Since there are $n$ black cells in each column, the sum of the numbers in all black cells of the $i$-th column is $2n^2(i-1)$ greater than the corresponding sum for the grid from the step 1. Hence the sum of all numbers in the black cells is then equal to
$$
B + \sum_{i=1}^{2n} 2n^2(i-1) = B + 2n^2\frac{2n(2n-1)}{2} = B + 2n^3(2n-1).
$$

Solution step (3 points):
It is easy to see that
$$
B + 2n^3(2n-1) = n^2(4n^2+1)
$$
and this sum is independent on the way of coloring the grid. Hence the minimal and the maximal possible sum of all numbers in the black cells are both equal to $n^2(4n^2+1).$