

The probability that exactly 45 red balls are drawn in 90 moves is given by:

\boxed{\dfrac{1}{91}}

**Step-by-Step Explanation:**

1. **Modeling the Problem:**
   - The process follows a **Pólya urn model** where drawing a ball of a certain color increases its count by 1.
   - Initially, there are 1 red (R), 1 green (G), and 1 blue (B) ball (total 3 balls).

2. **Symmetry Consideration:**
   - Non-red balls (G and B) start with a combined count of 2. Each non-red draw increases its count analogously to a single "non-red" category.
   - The problem reduces to a **two-color Pólya urn** with:
     - **Red (R):** Initial count = 1
     - **Non-red (G+B):** Initial count = 2

3. **General Formula:**
   - The probability of drawing exactly \(k\) red balls in \(n\) trials from a Pólya urn is:
     \[
     P(n, k) = \frac{\binom{n}{k} \cdot (r)_k \cdot (b)_{n-k}}{(t)_n}
     \]
     where:
     - \(r = 1\), \(b = 2\), \(t = r + b = 3\)
     - \((x)_y\) is the rising factorial: \(x(x+1)(x+2)\dots(x+y-1)\)

4. **Substitute Values:**
   - \(n = 90\), \(k = 45\)
   - Compute terms:
     \[
     \begin{aligned}
     \binom{90}{45} &= \frac{90!}{45! \cdot 45!} \\
     (1)_{45} &= 45! \\
     (2)_{45} &= \frac{46!}{1!} \\
     (3)_{90} &= \frac{92!}{2!} \\
     \end{aligned}
     \]

5. **Simplify the Probability Expression:**
   \[
   P(90, 45) = \frac{\frac{90!}{45! \cdot 45!} \cdot 45! \cdot \frac{46!}{1!}}{\frac{92!}{2!}} = \frac{90! \cdot 46! \cdot 2!}{45! \cdot 92!}
   \]
   
6. **Cancel Common Factors:**
   - Notice \(46! = 46 \cdot 45!\) and \(92! = 92 \cdot 91 \cdot 90!\):
     \[
     \frac{90! \cdot 46 \cdot 45! \cdot 2}{45! \cdot 92 \cdot 91 \cdot 90!} = \frac{46 \cdot 2}{92 \cdot 91} = \frac{92}{92 \cdot 91} = \frac{1}{91}
     \]

**Conclusion:** The probability of drawing exactly 45 red balls in 90 moves is \(\frac{1}{91}\).