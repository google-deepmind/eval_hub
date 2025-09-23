The piece shown in the figure is a T-tetromino, which is composed of four $1 \times 1$ squares. Therefore, the area of one piece is 4 square units. The board is a square with side length 10, so its total area is $10 \times 10 = 100$ square units. The maximum number of pieces that could possibly fit on the board is the total area of the board divided by the area of a single piece: $\frac{100}{4} = 25$. This would mean the pieces perfectly tile the square.

Let's check if it's possible to tile a $10 \times 10$ board with 25 T-tetrominoes using a coloring argument.
Consider a standard chessboard coloring of the $10 \times 10$ board. The board has 100 squares in total, with 50 black squares and 50 white squares.
A T-tetromino, regardless of its orientation, will always cover either 1 black square and 3 white squares, or 3 black squares and 1 white square. In both cases, the number of black squares covered by a single piece is odd.

Let $N$ be the total number of pieces. If we place $N=25$ pieces, the total number of black squares covered would be the sum of the black squares covered by each of the 25 pieces. Since each piece covers an odd number of black squares, the sum of 25 odd numbers is an odd number.
However, the $10 \times 10$ board has 50 black squares, which is an even number.
This leads to a contradiction: the number of black squares that would be covered must be odd, but the number of available black squares is even. Therefore, it is impossible to tile a $10 \times 10$ board with 25 T-tetrominoes.

The maximum number of pieces must be less than 25. Let's try to place 24 pieces.
The total area covered by 24 pieces would be $24 \times 4 = 96$ square units. This means 4 squares on the board would be left uncovered.
We need to show that it is possible to place 24 pieces. We can do this by construction.
Consider the $10 \times 10$ board. We can tile an $8 \times 10$ rectangular subgrid. An $8 \times 10$ rectangle has an area of 80, so it can be tiled by $\frac{80}{4} = 20$ T-tetrominoes. This is possible because the $8 \times 10$ rectangle can be divided into $2 \times 4$ rectangles, and each $2 \times 4$ rectangle can be tiled by two T-tetrominoes.
After tiling the $8 \times 10$ subgrid, a $2 \times 10$ strip remains. We can tile a $2 \times 8$ portion of this strip. A $2 \times 8$ rectangle has an area of 16 and can be tiled by $\frac{16}{4} = 4$ T-tetrominoes.
By doing this, we have placed a total of $20 + 4 = 24$ pieces. The uncovered area is a $2 \times 2$ square at one end of the $2 \times 10$ strip.

Since it is impossible to place 25 pieces and possible to place 24 pieces, the maximum number of pieces is 24.
The maximal possible sum of the areas of all the placed pieces is the number of pieces multiplied by the area of one piece:
$$ 24 \times 4 = 96 $$

Thus, the maximal possible sum of areas is 96.