

The real polynomials \( P \) satisfying the equation \( x P(x-2) = (x - 2024)P(x) \) for all \( x \in \mathbb{R} \) are determined as follows:

1. **Initial Analysis**:
   - Setting \( x = 0 \) implies \( P(0) = 0 \), so \( x \) is a factor of \( P(x) \). Let \( P(x) = x Q(x) \).

2. **Recursive Substitution**:
   - Substituting \( P(x) = x Q(x) \) into the equation leads to \( (x - 2) Q(x - 2) = (x - 2024) Q(x) \).
   - Iteratively applying this process, each substitution reveals new roots at \( x = 2k \) for \( k = 0, 1, 2, \ldots, 1011 \).

3. **Termination Condition**:
   - The process terminates when \( 2k = 2024 \), yielding \( k = 1012 \). At this point, the remaining polynomial must be constant.

4. **General Form**:
   - The polynomial \( P(x) \) is a product of linear factors corresponding to roots at \( 0, 2, 4, \ldots, 2022 \), scaled by a constant.

**Solution**:
All real solutions are the zero polynomial and polynomials of the form:
\[
P(x) = C \cdot x(x - 2)(x - 4) \cdots (x - 2022)
\]
where \( C \) is a real constant.

**Final Answer**
\boxed{P(x) = C \prod_{k=0}^{1011} (x - 2k) \quad \text{for some constant } C \in \mathbb{R} \text{ or } P(x) = 0}}