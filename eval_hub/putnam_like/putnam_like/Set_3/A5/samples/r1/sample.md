

To evaluate the limit
\[
\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)\,dx,
\]
we can utilize properties of the Fourier transform. The integral in question is the real part of the Fourier transform of \( e^{-x^2/2} \).

**Step 1: Express the Cosine Term via Euler's Formula**
\[
\cos(yx) = \frac{e^{iyx} + e^{-iyx}}{2}.
\]
Substituting this into the integral gives:
\[
\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)\,dx = \frac{1}{2} \left( \int_{-\infty}^{\infty}e^{-x^2/2 + iyx}\,dx + \int_{-\infty}^{\infty}e^{-x^2/2 - iyx}\,dx \right).
\]

**Step 2: Compute the Fourier Transform of the Gaussian**
The Fourier transform of \( e^{-x^2/2} \) is:
\[
\mathcal{F}\{e^{-x^2/2}\}(y) = \int_{-\infty}^{\infty} e^{-x^2/2} e^{-iyx}\,dx = \sqrt{2\pi} \, e^{-y^2/2}.
\]
Using this result, the integrals become:
\[
\int_{-\infty}^{\infty}e^{-x^2/2 \pm iyx}\,dx = \sqrt{2\pi} \, e^{-y^2/2}.
\]

**Step 3: Combine the Results**
Substituting back:
\[
\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)\,dx = \frac{1}{2} \left( \sqrt{2\pi} e^{-y^2/2} + \sqrt{2\pi} e^{-y^2/2} \right) = \sqrt{2\pi} \, e^{-y^2/2}.
\]

**Step 4: Take the Limit as \( y \to \infty \)**
\[
\lim_{y\to\infty} \sqrt{2\pi} \, e^{-y^2/2} = 0,
\]
since \( e^{-y^2/2} \to 0 \) exponentially fast as \( y \to \infty \).

**Conclusion:**
\[
\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)\,dx = 0.
\]

```markdown
\boxed{0}
```