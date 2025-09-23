# Solution

To show that 
$$\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx=0$$

I'll use the Fourier transform approach.

## Step 1: Compute the integral using Fourier transforms
The Fourier transform of the Gaussian function $e^{-x^2/2}$ is given by:
$$\mathcal{F}[e^{-x^2/2}](\omega) = \sqrt{2\pi}e^{-\omega^2/2}$$

The cosine transform of a function $f(x)$ is related to its Fourier transform by:
$$\mathcal{F}_c[f(x)](\omega) = \int_{-\infty}^{\infty}f(x)\cos(\omega x)dx = \frac{1}{2}(\mathcal{F}[f(x)](\omega) + \mathcal{F}[f(x)](-\omega))$$

Applying this to our Gaussian function:
$$\mathcal{F}_c[e^{-x^2/2}](y) = \frac{1}{2}(\sqrt{2\pi}e^{-y^2/2} + \sqrt{2\pi}e^{-(-y)^2/2}) = \sqrt{2\pi}e^{-y^2/2}$$

Therefore:
$$\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx = \sqrt{2\pi}e^{-y^2/2}$$

## Step 2: Take the limit as $y$ approaches infinity
As $y \to \infty$, we have $e^{-y^2/2} \to 0$, so:
$$\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx = \lim_{y\to\infty}\sqrt{2\pi}e^{-y^2/2} = 0$$

Therefore, we have shown that:
$$\lim_{y\to\infty}\int_{-\infty}^{\infty}e^{-x^2/2}\cos(yx)dx = 0$$

## Alternative approach (Riemann-Lebesgue Lemma)
We could also solve this using the Riemann-Lebesgue lemma, which states that for any $f \in L^1(\mathbb{R})$:
$$\lim_{y\to\infty}\int_{-\infty}^{\infty}f(x)e^{iyx}dx = 0$$

Since $e^{-x^2/2} \in L^1(\mathbb{R})$, and $\cos(yx) = \frac{e^{iyx}+e^{-iyx}}{2}$, applying the lemma gives us the same result: the limit equals zero.