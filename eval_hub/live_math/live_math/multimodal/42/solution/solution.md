Let the figure be a grid of squares. The problem involves placing numbers $1, 2, \dots, 25$, so there are a total of 25 squares. The logic of the solution implies the grid is a pyramid shape with 5 rows. Let's denote the rows from top to bottom as row 1 to row 5. The number of squares in each row is:
- Row 1: 1 square
- Row 2: 3 squares
- Row 3: 5 squares
- Row 4: 7 squares
- Row 5: 9 squares
The total number of squares is $1+3+5+7+9 = 25$.

Let $M_i$ be the maximum number in row $i$. We are looking for the probability that $M_1 < M_2 < M_3 < M_4 < M_5$.

For this condition to be satisfied, the largest number of all, 25, must be the largest of the maxima. Therefore, $M_5$ must be 25. This implies that the number 25 must be placed somewhere in row 5.
Row 5 has 9 squares, and there are 25 squares in total. The probability that the number 25 is placed in row 5 is:
$$ P_5 = \frac{\text{Number of squares in row 5}}{\text{Total number of squares}} = \frac{9}{25} $$

Given that 25 is in row 5, we now consider the remaining 24 numbers $\{1, 2, \dots, 24\}$ and the remaining 24 squares. The top 4 rows consist of $1+3+5+7 = 16$ squares. These squares will be filled with 16 numbers chosen randomly from the set $\{1, 2, \dots, 24\}$. For the condition $M_1 < M_2 < M_3 < M_4$ to hold, the maximum of these 16 numbers must be located in row 4.
Regardless of which 16 numbers are in the top four rows, their placement is random. The largest of these 16 numbers can be in any of the 16 positions with equal probability. Since row 4 has 7 squares, the probability that the maximum of these 16 numbers is in row 4 is:
$$ P_4 = \frac{\text{Number of squares in row 4}}{\text{Total squares in rows 1-4}} = \frac{7}{16} $$

Continuing this logic, we consider the top 3 rows, which have $1+3+5 = 9$ squares. Given the previous conditions are met, the maximum of the 9 numbers in these rows must be located in row 3. Row 3 has 5 squares. The probability of this is:
$$ P_3 = \frac{\text{Number of squares in row 3}}{\text{Total squares in rows 1-3}} = \frac{5}{9} $$

Next, consider the top 2 rows, which have $1+3 = 4$ squares. The maximum of the 4 numbers in these rows must be in row 2. Row 2 has 3 squares. The probability of this is:
$$ P_2 = \frac{\text{Number of squares in row 2}}{\text{Total squares in rows 1-2}} = \frac{3}{4} $$

Finally, the top row has only one square, so its number is trivially the maximum of that row (probability is 1).

The total probability is the product of these individual probabilities:
$$ P = P_5 \times P_4 \times P_3 \times P_2 = \frac{9}{25} \times \frac{7}{16} \times \frac{5}{9} \times \frac{3}{4} $$
$$ P = \frac{9 \times 7 \times 5 \times 3}{25 \times 16 \times 9 \times 4} $$
We can cancel the 9s:
$$ P = \frac{7 \times 5 \times 3}{25 \times 16 \times 4} = \frac{105}{1600} $$
To simplify the fraction, we can divide the numerator and denominator by common factors. $25 = 5^2$, so we can simplify by 5:
$$ P = \frac{7 \times 3}{5 \times 16 \times 4} = \frac{21}{5 \times 64} = \frac{21}{320} $$
This fraction is in its simplest form, so $p=21$ and $q=320$. The numbers $p$ and $q$ are coprime because the prime factors of $p=21$ are 3 and 7, while the prime factors of $q=320 = 32 \times 10 = 2^6 \times 5$ are 2 and 5.

The problem asks for the value of $q-p$:
$$ q - p = 320 - 21 = 299 $$