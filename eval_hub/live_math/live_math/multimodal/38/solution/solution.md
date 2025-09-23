Let $a_n$ be the number of ways to tile a $4 \times n$ board with $1 \times 4$ tiles. We want to find the value of $a_{16}$.

We can establish a recurrence relation for $a_n$ by considering how the rightmost column(s) of the board can be tiled. There are two mutually exclusive possibilities:

1. The rightmost column is covered by a single $4 \times 1$ tile placed vertically. The remaining board is a $4 \times (n-1)$ rectangle, which can be tiled in $a_{n-1}$ ways.
2. The rightmost column is covered by $1 \times 4$ tiles placed horizontally. For this to happen, all four cells in the column must be covered by horizontal tiles. This means four horizontal tiles are placed next to each other, covering a $4 \times 4$ area at the right end of the board. The remaining board is a $4 \times (n-4)$ rectangle, which can be tiled in $a_{n-4}$ ways.

Summing these possibilities gives the recurrence relation for $n \ge 4$:
$$a_n = a_{n-1} + a_{n-4}$$

Next, we establish the base cases:
- $a_0 = 1$: There is one way to tile a $4 \times 0$ board (the empty tiling).
- $a_1 = 1$: A $4 \times 1$ board can only be tiled with one vertical $4 \times 1$ tile.
- $a_2 = 1$: A $4 \times 2$ board can only be tiled with two vertical $4 \times 1$ tiles.
- $a_3 = 1$: A $4 \times 3$ board can only be tiled with three vertical $4 \times 1$ tiles. In each of these cases, horizontal tiles cannot be used as they are 4 units long.

Using the recurrence relation and the base cases, we can compute the sequence of values for $a_n$ up to $n=16$.
- $a_4 = a_3 + a_0 = 1 + 1 = 2$
- $a_5 = a_4 + a_1 = 2 + 1 = 3$
- $a_6 = a_5 + a_2 = 3 + 1 = 4$
- $a_7 = a_6 + a_3 = 4 + 1 = 5$
- $a_8 = a_7 + a_4 = 5 + 2 = 7$
- $a_9 = a_8 + a_5 = 7 + 3 = 10$
- $a_{10} = a_9 + a_6 = 10 + 4 = 14$
- $a_{11} = a_{10} + a_7 = 14 + 5 = 19$
- $a_{12} = a_{11} + a_8 = 19 + 7 = 26$
- $a_{13} = a_{12} + a_9 = 26 + 10 = 36$
- $a_{14} = a_{13} + a_{10} = 36 + 14 = 50$
- $a_{15} = a_{14} + a_{11} = 50 + 19 = 69$
- $a_{16} = a_{15} + a_{12} = 69 + 26 = 95$

The results can also be summarized in a table:
$$
\begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
n & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16\\
\hline
a_n & 1 & 1 & 1 & 1 & 2 & 3 & 4 & 5 & 7 & 10 & 14 & 19 & 26 & 36 & 50 & 69 & 95\\
\hline
\end{array}
$$
Thus, there are 95 ways to tile a $4 \times 16$ board.