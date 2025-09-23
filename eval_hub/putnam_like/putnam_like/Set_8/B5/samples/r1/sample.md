

To solve the problem, we need to determine for which positive integers \( m \) the expected value of the number drawn from the \( n \)-th box is an integer. 

### Key Steps and Analysis:

1. **Initial Setup and Expectation Calculation**:
   - Each box initially contains \( k \) balls numbered \( k \) for \( k = 1, 2, \ldots, m \).
   - The total number of balls in each box is \( S = \frac{m(m+1)}{2} \).
   - The expected value of a ball drawn from the first box is:
     \[
     E_1 = \frac{\sum_{k=1}^m k^2}{S} = \frac{\frac{m(m+1)(2m+1)}{6}}{\frac{m(m+1)}{2}} = \frac{2m + 1}{3}
     \]

2. **Propagation of Expectation**:
   - When a ball is drawn from the first box (expectation \( E_1 \)) and placed into the second box, the composition of the second box changes. However, due to the linearity of expectation, the new expected value of the second box remains \( E_1 \). This is shown by:
     \[
     E_2 = \frac{S \cdot E_1 + E_1}{S + 1} = E_1
     \]
   - This recursive process continues for each subsequent box, implying that the expectation remains \( E_1 \) regardless of the number of transfers \( n \).

3. **Final Expected Value**:
   - The expected value of the number drawn from the \( n \)-th box is \( \frac{2m + 1}{3} \). For this to be an integer, \( 2m + 1 \) must be divisible by 3:
     \[
     2m + 1 \equiv 0 \pmod{3} \implies 2m \equiv -1 \pmod{3} \implies 2m \equiv 2 \pmod{3} \implies m \equiv 1 \pmod{3}
     \]

### Conclusion:
The expected value is an integer if and only if \( m \) is congruent to 1 modulo 3. 

**Answer**:  
All positive integers \( m \) congruent to \( 1 \mod 3 \).  
Formally,  
\[
\boxed{m \equiv 1 \pmod{3}}
\]