

The probability that Maria draws three white balls with replacement is calculated by averaging the probability of drawing three white balls from each box, weighted by the probability of selecting each box. 

1. **Probability of choosing box \( k \):** \( \frac{1}{2025} \)
2. **Probability of drawing three white balls from box \( k \):** \( \left( \frac{k}{2024} \right)^3 \)
3. **Total probability:** Sum over all boxes and normalize:
   \[
   P = \frac{1}{2025} \cdot \frac{1}{2024^3} \sum_{k=0}^{2024} k^3
   \]
4. **Sum of cubes formula:** \( \sum_{k=1}^{n} k^3 = \left( \frac{n(n+1)}{2} \right)^2 \). For \( n = 2024 \):
   \[
   \sum_{k=0}^{2024} k^3 = \left( \frac{2024 \cdot 2025}{2} \right)^2
   \]
5. **Substitute the sum into the probability expression:**
   \[
   P = \frac{1}{2025} \cdot \frac{1}{2024^3} \cdot \left( \frac{2024 \cdot 2025}{2} \right)^2
   \]
6. **Simplify the expression:**
   \[
   P = \frac{1}{2025} \cdot \frac{1}{2024^3} \cdot \frac{2024^2 \cdot 2025^2}{4} = \frac{2025}{4 \cdot 2024}
   \]
7. **Final result:** \( \frac{2025}{8096} \)

\[
\boxed{\dfrac{2025}{8096}}
\]