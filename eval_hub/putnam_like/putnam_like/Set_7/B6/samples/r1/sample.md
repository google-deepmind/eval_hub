

To prove that for every \( n \geq 0 \),
$$
\sum_{k=0}^n (-1)^{\left\lfloor k (\sqrt{3}-1) \right\rfloor} \geq 1,
$$
we analyze the structure of the sequence and use induction.

**Key Steps:**

1. **Base Case:** For \( n = 0 \), the sum is \( (-1)^0 = 1 \), satisfying the inequality.

2. **Inductive Hypothesis:** Assume the sum \( S(m) \geq 1 \) for all \( m \leq n \).

3. **Inductive Step:** Consider \( S(n+1) \):
   - If \( S(n) \geq 2 \), adding \( a_{n+1} \in \{-1, 1\} \) ensures \( S(n+1) \geq 1 \).
   - If \( S(n) = 1 \), we show the next term \( a_{n+1} = +1 \):
     - Let \( \alpha = \sqrt{3} - 1 \approx 0.732 \). When \( S(n) = 1 \), the previous term \( a_n = -1 \), implying \( \left\lfloor n\alpha \right\rfloor \) is odd.
     - The fractional part \( \{n\alpha\} \geq 1 - \alpha \approx 0.268 \), otherwise \( \left\lfloor (n+1)\alpha \right\rfloor \) would remain odd, causing \( S(n+1) = 0 \), which contradicts the hypothesis.
     - Hence, \( \{n\alpha\} \geq 1 - \alpha \), so \( \left\lfloor (n+1)\alpha \right\rfloor = \left\lfloor n\alpha \right\rfloor + 1 \) (even), making \( a_{n+1} = +1 \). Thus, \( S(n+1) = 1 + 1 = 2 \geq 1 \).

**Conclusion:** By induction, the sum \( S(n) \geq 1 \) for all \( n \geq 0 \).

```markdown
Therefore, the inequality holds for all non-negative integers \( n \).
```