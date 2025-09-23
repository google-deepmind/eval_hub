

To solve the problem, we analyze the integral of the product of cosines and use properties of Fourier expansions and probabilistic methods.

**Step-by-Step Explanation:**

1. **Integral Representation:**
   The integral of \( f_n(x) = \prod_{i=1}^{n} \cos((2i-1)x) \) over \( [0, 2\pi] \) can be expressed using the Fourier series expansion of the product of cosines. Expanding each cosine term as a sum of exponentials:
   \[
   \cos((2i-1)x) = \frac{e^{i(2i-1)x} + e^{-i(2i-1)x}}{2}.
   \]
   Multiplying these terms results in a sum of exponentials with frequencies \( \pm(2i-1)x \). The integral over \( [0, 2\pi] \) is non-zero only for the constant term (frequency 0), giving:
   \[
   \int_0^{2\pi} f_n(x) dx = 2\pi \cdot \frac{\text{Number of solutions to } \sum_{k=1}^n s_k(2k-1) = 0}{2^n},
   \]
   where \( s_k \in \{\pm1\} \).

2. **Analyzing Solutions:**
   The number of solutions \( N(n) \) to \( \sum_{k=1}^n s_k(2k-1) = 0 \) determines the integral. For odd \( n \), the sum must be odd (since the sum of an odd number of odd terms is odd), making \( N(n) = 0 \). For even \( n \), solutions may exist but are rare.

3. **Probability and Central Limit Theorem:**
   The sum \( S_n = \sum_{k=1}^n s_k(2k-1) \) behaves like a random walk with step sizes \( 2k-1 \). The variance of \( S_n \) grows as \( \Theta(n^3) \), and by the Central Limit Theorem, the probability density at 0 decays as \( \Theta(n^{-3/2}) \). Thus, \( N(n) \approx \frac{2^n}{n^{3/2}} \).

4. **Integral Decay:**
   Substituting \( N(n) \) into the integral expression:
   \[
   \int_0^{2\pi} f_n(x) dx \approx \frac{2\pi}{2^n} \cdot \frac{2^n}{n^{3/2}} = \frac{C}{n^{3/2}} \to 0 \quad \text{as } n \to \infty.
   \]

5. **Lim Inf Conclusion:**
   Since the integral decays to zero for even \( n \) and is zero for odd \( n \), the lim inf is zero.

**Answer:**

The lim inf of the integral is \(\boxed{0}\).