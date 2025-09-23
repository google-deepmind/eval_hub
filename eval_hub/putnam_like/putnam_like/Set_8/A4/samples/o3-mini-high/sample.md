```latex
\documentclass{article}
\usepackage{amsmath}
\begin{document}

We are given an asymmetric coin where the probability of heads, denoted by \(p\), is itself a random variable uniformly distributed on the interval \([0,1]\).

For a fixed value of \(p\), the number of tosses \(T\) needed to get the first heads follows a geometric distribution with success parameter \(p\). Hence, the conditional expectation is
\[
\mathbb{E}[T \mid p] = \frac{1}{p}.
\]

Since \(p\) is uniformly distributed over \([0,1]\), its density function is
\[
f(p) = 1 \quad \text{for } 0 \le p \le 1.
\]
Thus, the overall expectation of \(T\) is the average of \(\mathbb{E}[T \mid p]\) with respect to \(p\):
\[
\mathbb{E}[T] = \int_0^1 \mathbb{E}[T \mid p] \, f(p) \, dp = \int_0^1 \frac{1}{p} \, dp.
\]

Evaluating the integral, we observe:
\[
\int_0^1 \frac{1}{p} \, dp = \lim_{\varepsilon \to 0^+} \int_\varepsilon^1 \frac{1}{p} \, dp = \lim_{\varepsilon \to 0^+} \left[ \ln p \right]_\varepsilon^1 = \lim_{\varepsilon \to 0^+} (0 - \ln \varepsilon) = \infty.
\]

Thus, the expected number of tosses to obtain the first heads is infinite.

\end{document}
```