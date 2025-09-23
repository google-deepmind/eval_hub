

The set \( Y \) consists of all possible sums of cubes of sequences in \( X \), where each sequence in \( X \) is composed of positive real numbers summing to \( c \). To describe \( Y \):

1. **Supremum Analysis**:  
   The maximum possible value of \( \sum_{n=0}^\infty x_n^3 \) occurs when the sequence is "concentrated" in a single term. Let \( x_0 \to c^- \) and distribute the remaining mass \( \epsilon = c - x_0 \) across infinitely many small terms. As \( \epsilon \to 0 \), the sum of cubes approaches \( c^3 \). However, since all terms must be positive, the supremum is **not attained**, but \( Y \) can get arbitrarily close to \( c^3 \).

2. **Infimum Analysis**:  
   To minimize \( \sum_{n=0}^\infty x_n^3 \), spread the mass \( c \) thinly over infinitely many terms. For example, consider sequences \( x_n = \frac{c}{(n+1)^p} \) normalized to sum to \( c \). As \( p \to 1^+ \), the decay of \( x_n \) slows, and \( \sum x_n^3 \) becomes dominated by many tiny terms. This sum can be made arbitrarily small, approaching 0. Hence, the infimum is 0, but it is **not attained** due to strict positivity.

3. **Conclusion**:  
   \( Y \) includes all values between 0 and \( c^3 \), excluding the endpoints. Thus, \( Y \) is the open interval \( (0, c^3) \).

\[
\boxed{Y = \left(0, c^3\right)}
\]