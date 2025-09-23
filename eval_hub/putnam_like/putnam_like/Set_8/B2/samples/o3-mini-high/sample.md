```latex
\documentclass{article}
\usepackage{amsmath}
\begin{document}

We are given 2025 boxes labeled \(0, 1, 2, \dots, 2024\). In the \(k\)-th box there are \(k\) white balls and \(2024-k\) black balls.
Maria selects a box uniformly at random and then draws 3 balls with replacement from it. We wish to compute the probability that all three balls drawn are white.

\medskip

For a fixed box \(k\), the probability of drawing a white ball in a single trial is:
\[
\frac{k}{2024}.
\]
Since the draws are independent (because of replacement), the probability of drawing 3 white balls from the \(k\)-th box is:
\[
\left(\frac{k}{2024}\right)^3.
\]

\medskip

As the box is chosen uniformly at random, the overall probability \(P\) that all 3 balls are white is the average over all boxes:
\[
P = \frac{1}{2025} \sum_{k=0}^{2024} \left(\frac{k}{2024}\right)^3 
= \frac{1}{2025 \cdot 2024^3}\sum_{k=0}^{2024} k^3.
\]

\medskip

Recall that the sum of cubes of the first \(n\) positive integers is given by:
\[
\sum_{k=1}^{n} k^3 = \left(\frac{n(n+1)}{2}\right)^2.
\]
Since \(0^3 = 0\), the formula holds with \(n=2024\):
\[
\sum_{k=0}^{2024} k^3 = \left(\frac{2024 \cdot 2025}{2}\right)^2.
\]

\medskip

Substituting this into the expression for \(P\) gives:
\[
P = \frac{1}{2025 \cdot 2024^3} \cdot \left(\frac{2024 \cdot 2025}{2}\right)^2
= \frac{2024^2 \cdot 2025^2}{4 \cdot 2025 \cdot 2024^3}.
\]

\medskip

Simplify by canceling common factors:
\[
P = \frac{2025}{4 \cdot 2024}.
\]

\medskip

Thus, the probability that all three drawn balls are white is:
\[
\boxed{\frac{2025}{4 \cdot 2024}}.
\]

\end{document}
```