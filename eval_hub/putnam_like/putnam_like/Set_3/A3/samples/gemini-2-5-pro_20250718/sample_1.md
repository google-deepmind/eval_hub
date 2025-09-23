This problem describes a process known as a **Pólya's Urn** model. We will solve this by first finding the probability of a specific sequence of draws, and then using that to find the total probability of all sequences that satisfy the given condition.

### Initial Setup

*   **Initial state:** The box contains 3 balls: 1 Green (G), 1 Red (R), 1 Blue (B).
*   **Process:** A ball is drawn, its color is noted, and it is returned to the box along with another ball of the same color.
*   **Total draws (moves):** $n = 90$.
*   **Objective:** Find the probability that the red ball was drawn exactly $k_R = 45$ times.

Let's denote the number of red, green, and blue balls initially as $N_R(0)=1$, $N_G(0)=1$, $N_B(0)=1$. The total number of balls is $N(0)=3$.

After each draw, the total number of balls in the box increases by one. So, before the $k$-th draw, there are $3 + (k-1)$ balls in the box.

### Step 1: Probability of a Specific Sequence of Draws

Let's consider an arbitrary sequence of 90 draws, for example, $S = (C_1, C_2, \dots, C_{90})$, where each $C_i$ is either R, G, or B. The probability of this specific sequence is:

$P(S) = P(C_1) \times P(C_2 | C_1) \times P(C_3 | C_1, C_2) \times \dots \times P(C_{90} | C_1, \dots, C_{89})$

Let's analyze the numerator and the denominator of this product.

*   **Denominator:** The denominator of the probability of the $k$-th draw is the total number of balls in the box before that draw, which is $3 + (k-1)$. So, the denominator of $P(S)$ is the product of the total number of balls at each step:
    $3 \times 4 \times 5 \times \dots \times (3 + 90 - 1) = 3 \times 4 \times \dots \times 92 = \frac{92!}{2!}$

*   **Numerator:** The numerator of the probability of the $k$-th draw is the number of balls of the color drawn.
    Let the sequence $S$ contain $k_R$ red draws, $k_G$ green draws, and $k_B$ blue draws, where $k_R + k_G + k_B = 90$.
    *   The first time we draw a red ball, there is 1 red ball in the box.
    *   The second time we draw a red ball, there are 2 red balls in the box.
    *   ...
    *   The $k_R$-th time we draw a red ball, there are $k_R$ red balls in the box.
    The product of the numerators for the red draws, regardless of their position in the sequence, will be $1 \times 2 \times \dots \times k_R = k_R!$.
    Similarly, the product of numerators for the green draws will be $k_G!$, and for the blue draws will be $k_B!$.

Combining these, the probability of any specific sequence $S$ with $k_R$ red, $k_G$ green, and $k_B$ blue draws is:
$P(S) = \frac{k_R! \cdot k_G! \cdot k_B!}{\frac{92!}{2!}} = \frac{2 \cdot k_R! \cdot k_G! \cdot k_B!}{92!}$

A key property of Pólya's Urn models is that all sequences with the same number of draws of each color are equally likely.

### Step 2: Define the Event of Interest

We are interested in the event $E$ where the red ball is drawn exactly 45 times. This means $k_R = 45$.
The remaining $90 - 45 = 45$ draws must be either green or blue. So, we must have $k_G + k_B = 45$.

The total probability of event $E$ is the sum of probabilities of all sequences that satisfy this condition.
$P(E) = \sum_{\text{sequences with } k_R=45} P(S)$

We can group these sequences by the specific counts of green and blue balls. Let $E_{k_G, k_B}$ be the event that we get exactly $k_R=45$ red, $k_G$ green, and $k_B$ blue balls, where $k_G+k_B=45$. Then:
$P(E) = \sum_{k_G=0}^{45} P(E_{45, k_G, 45-k_G})$

### Step 3: Calculate the Probability for a Fixed Partition $(k_R, k_G, k_B)$

Let's fix the counts to be $(k_R, k_G, k_B) = (45, k_G, 45-k_G)$.
The probability of one specific sequence with these counts is:
$P(\text{one sequence}) = \frac{2 \cdot 45! \cdot k_G! \cdot (45-k_G)!}{92!}$

The number of distinct sequences with these counts is given by the multinomial coefficient:
$\text{Number of sequences} = \binom{90}{45, k_G, 45-k_G} = \frac{90!}{45! \cdot k_G! \cdot (45-k_G)!}$

The total probability for this specific partition $(45, k_G, 45-k_G)$ is:
$P(E_{45, k_G, 45-k_G}) = (\text{Number of sequences}) \times P(\text{one sequence})$
$P(E_{45, k_G, 45-k_G}) = \left(\frac{90!}{45! \cdot k_G! \cdot (45-k_G)!}\right) \times \left(\frac{2 \cdot 45! \cdot k_G! \cdot (45-k_G)!}{92!}\right)$

The terms $45!$, $k_G!$, and $(45-k_G)!$ cancel out beautifully:
$P(E_{45, k_G, 45-k_G}) = \frac{90! \cdot 2}{92!} = \frac{2 \cdot 90!}{92 \cdot 91 \cdot 90!} = \frac{2}{92 \cdot 91} = \frac{1}{46 \cdot 91}$

Notice that this probability is independent of the specific value of $k_G$.

### Step 4: Sum the Probabilities for All Possible Partitions

Now we must sum this probability over all possible ways the 45 non-red balls can be distributed between green and blue. The number of green balls, $k_G$, can range from 0 to 45. This gives $45 - 0 + 1 = 46$ possible partitions:
*   (45 R, 0 G, 45 B)
*   (45 R, 1 G, 44 B)
*   ...
*   (45 R, 45 G, 0 B)

The total probability is the sum of the probabilities of these 46 mutually exclusive events:
$P(E) = \sum_{k_G=0}^{45} P(E_{45, k_G, 45-k_G}) = \sum_{k_G=0}^{45} \frac{1}{46 \cdot 91}$

Since we are adding the same constant term 46 times:
$P(E) = 46 \times \frac{1}{46 \cdot 91} = \frac{46}{46 \cdot 91} = \frac{1}{91}$

---
### Alternative Method (Simplified Urn)

We can simplify the problem from the start by categorizing the balls into two types: "Red" (R) and "Not Red" (NR).

*   **Initial state:** 1 R ball and 2 NR balls. Total of 3 balls.
*   **Process:** Draw a ball. If it's R, add an R ball. If it's NR, add an NR ball (we don't need to distinguish between G and B).
*   **Objective:** Find the probability of getting exactly 45 R draws in 90 total draws. This implies we must also get 45 NR draws.

Let's find the probability of one specific sequence with 45 R's and 45 NR's.
*   **Denominator:** Same as before, $\frac{92!}{2!}$.
*   **Numerator for R draws:** The number of R balls starts at 1. The product of numerators for the 45 R draws is $1 \cdot 2 \cdot \dots \cdot 45 = 45!$.
*   **Numerator for NR draws:** The number of NR balls starts at 2. The product of numerators for the 45 NR draws is $2 \cdot 3 \cdot \dots \cdot (2+45-1) = 2 \cdot 3 \cdot \dots \cdot 46 = 46!$.

The probability of one specific sequence is:
$P(\text{one sequence}) = \frac{45! \cdot 46!}{\frac{92!}{2!}} = \frac{2 \cdot 45! \cdot 46!}{92!}$

The number of sequences with 45 R's and 45 NR's is given by the binomial coefficient:
$\text{Number of sequences} = \binom{90}{45} = \frac{90!}{45! \cdot 45!}$

The total probability is:
$P(\text{45 R in 90 draws}) = \binom{90}{45} \times \frac{2 \cdot 45! \cdot 46!}{92!}$
$P(\text{45 R in 90 draws}) = \frac{90!}{45! \cdot 45!} \times \frac{2 \cdot 45! \cdot 46!}{92!}$

Cancel out one of the $45!$ terms:
$P(\text{45 R in 90 draws}) = \frac{90! \cdot 2 \cdot 46!}{45! \cdot 92!}$

Now, expand the factorials: $46! = 46 \cdot 45!$ and $92! = 92 \cdot 91 \cdot 90!$:
$P(\text{45 R in 90 draws}) = \frac{90! \cdot 2 \cdot (46 \cdot 45!)}{45! \cdot (92 \cdot 91 \cdot 90!)}$

Cancel $90!$ and $45!$:
$P(\text{45 R in 90 draws}) = \frac{2 \cdot 46}{92 \cdot 91} = \frac{92}{92 \cdot 91} = \frac{1}{91}$

Both methods yield the same result.

### Final Answer
The probability that among 90 moves the red ball was drawn exactly 45 times is **1/91**.