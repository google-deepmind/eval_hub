

To show that \(\lim_{x\to\infty} f(x) = 0\) given that \(\lim_{x\to\infty} \left( f(x) + \frac{f'(x)}{g'(x)} \right) = 0\) and \(g(x) \to \infty\) as \(x \to \infty\), we proceed as follows:

1. **Rewrite the Given Condition**:
   The given condition can be written as:
   \[
   f'(x) + f(x) g'(x) = \epsilon(x) g'(x)
   \]
   where \(\epsilon(x) \to 0\) as \(x \to \infty\).

2. **Formulate a Linear ODE**:
   This is a linear differential equation of the form:
   \[
   f'(x) + g'(x) f(x) = \epsilon(x) g'(x)
   \]

3. **Find the Integrating Factor**:
   The integrating factor is \(e^{\int g'(x) \, dx} = e^{g(x)}\). Multiplying both sides by this factor:
   \[
   e^{g(x)} f'(x) + e^{g(x)} g'(x) f(x) = e^{g(x)} \epsilon(x) g'(x)
   \]
   The left-hand side is the derivative of \(e^{g(x)} f(x)\):
   \[
   \frac{d}{dx} \left( e^{g(x)} f(x) \right) = e^{g(x)} \epsilon(x) g'(x)
   \]

4. **Integrate Both Sides**:
   Integrate from \(a\) to \(x\):
   \[
   e^{g(x)} f(x) - e^{g(a)} f(a) = \int_{a}^{x} e^{g(t)} \epsilon(t) g'(t) \, dt
   \]
   Solving for \(f(x)\):
   \[
   f(x) = e^{-g(x)} \left( e^{g(a)} f(a) + \int_{a}^{x} e^{g(t)} \epsilon(t) g'(t) \, dt \right)
   \]

5. **Apply L'Hospital's Rule**:
   Consider the expression for \(f(x)\) as \(x \to \infty\). Define the numerator \(N(x) = e^{g(a)} f(a) + \int_{a}^{x} e^{g(t)} \epsilon(t) g'(t) \, dt\) and the denominator \(D(x) = e^{g(x)}\). Applying L'Hospital's Rule to the limit \(\lim_{x \to \infty} \frac{N(x)}{D(x)}\):
   \[
   \lim_{x \to \infty} \frac{N'(x)}{D'(x)} = \lim_{x \to \infty} \frac{e^{g(x)} \epsilon(x) g'(x)}{e^{g(x)} g'(x)} = \lim_{x \to \infty} \epsilon(x) = 0
   \]

6. **Conclusion**:
   Since the limit of \(f(x)\) is evaluated using L'Hospital's Rule and shown to be 0, we conclude:
   \[
   \lim_{x\to\infty} f(x) = 0
   \]

\boxed{0}