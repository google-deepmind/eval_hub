```latex
\documentclass{article}
\usepackage{amsmath}
\begin{document}

We wish to show that
\[
\lim_{y\to\infty} \int_{-\infty}^{\infty} e^{-x^2/2}\cos(yx) \, dx = 0.
\]

There are two common approaches to this problem.

\bigskip

\textbf{Method 1: Using the Fourier Transform.}

Recall the well-known formula for the Fourier transform of the Gaussian:
\[
\int_{-\infty}^{\infty} e^{-x^2/2} e^{iyx} \, dx = \sqrt{2\pi}\, e^{-y^2/2}.
\]
Since the cosine function is the real part of the complex exponential, we have
\[
\int_{-\infty}^{\infty} e^{-x^2/2}\cos(yx) \, dx = \Re\Bigl(\sqrt{2\pi}\, e^{-y^2/2}\Bigr)
= \sqrt{2\pi}\, e^{-y^2/2}.
\]
Taking the limit as \( y\to\infty \),
\[
\lim_{y\to\infty} \sqrt{2\pi}\, e^{-y^2/2} = \sqrt{2\pi} \cdot 0 = 0.
\]

\bigskip

\textbf{Method 2: Using the Riemann-Lebesgue Lemma.}

The Riemann-Lebesgue lemma states that if \( f \in L^1(\mathbb{R}) \), then
\[
\lim_{y\to\infty} \int_{-\infty}^{\infty} f(x)\cos(yx)\, dx = 0.
\]
Since
\[
\int_{-\infty}^{\infty} e^{-x^2/2}\, dx = \sqrt{2\pi} < \infty,
\]
the function \( e^{-x^2/2} \) is integrable over \( \mathbb{R} \). Thus, applying the lemma with \( f(x)=e^{-x^2/2} \) immediately gives
\[
\lim_{y\to\infty} \int_{-\infty}^{\infty} e^{-x^2/2}\cos(yx) \, dx = 0.
\]

\bigskip

In both approaches, we conclude that
\[
\lim_{y\to\infty} \int_{-\infty}^{\infty} e^{-x^2/2}\cos(yx) \, dx = 0.
\]

\end{document}
```