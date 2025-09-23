

To solve the problem of finding the probability that \(\left\lfloor \frac{\ln(X)}{\ln(Y)} \right\rfloor\) is even, where \(X\) and \(Y\) are uniformly distributed over \((0, 1)\), we proceed as follows:

1. **Transformation to Exponential Variables**:
   Let \(a = -\ln(X)\) and \(b = -\ln(Y)\). Since \(X\) and \(Y\) are uniform on \((0, 1)\), \(a\) and \(b\) are independent exponential random variables with rate parameter 1.

2. **Ratio of Exponentials**:
   The ratio \(Z = \frac{a}{b}\) has a beta prime distribution with parameters \((1, 1)\). The probability density function (PDF) of \(Z\) is \(f_Z(z) = \frac{1}{(1 + z)^2}\) for \(z > 0\).

3. **Integral Over Even Intervals**:
   We need to compute the probability that \(\lfloor Z \rfloor\) is even. This corresponds to integrating \(f_Z(z)\) over intervals \([2k, 2k + 1)\) for \(k = 0, 1, 2, \ldots\):
   \[
   P\left(\left\lfloor \frac{\ln(X)}{\ln(Y)} \right\rfloor \text{ is even}\right) = \sum_{k=0}^{\infty} \int_{2k}^{2k+1} \frac{1}{(1 + z)^2} \, dz
   \]

4. **Evaluating the Integrals**:
   Each integral evaluates to:
   \[
   \int_{2k}^{2k+1} \frac{1}{(1 + z)^2} \, dz = \left[ -\frac{1}{1 + z} \right]_{2k}^{2k+1} = \frac{1}{2k + 1} - \frac{1}{2k + 2}
   \]

5. **Summing the Series**:
   Summing these results over all \(k\):
   \[
   \sum_{k=0}^{\infty} \left( \frac{1}{2k + 1} - \frac{1}{2k + 2} \right) = \left( 1 - \frac{1}{2} \right) + \left( \frac{1}{3} - \frac{1}{4} \right) + \left( \frac{1}{5} - \frac{1}{6} \right) + \cdots
   \]
   This is the alternating harmonic series, which converges to \(\ln(2)\).

Thus, the probability that \(\left\lfloor \frac{\ln(X)}{\ln(Y)} \right\rfloor\) is even is \(\boxed{\ln 2}\).