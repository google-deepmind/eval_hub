```latex
\documentclass{article}
\usepackage{amsmath, amssymb}
\begin{document}

Let $G$ be a finite multiplicative subgroup of $\mathbb{C}$ with $|G| \geq 2$. We wish to show that
\[
\sum_{z \in G} z = 0.
\]

\textbf{Proof:}

Since $G$ is a finite group, pick an element $z_0 \in G$ with $z_0 \neq 1$ (this is possible because $|G|\ge2$). Define
\[
S = \sum_{w \in G} w.
\]
Because $G$ is a group, the map
\[
w \mapsto z_0 w
\]
is a permutation of $G$. Hence, multiplying each element in the sum by $z_0$ rearranges the sum:
\[
z_0 S = \sum_{w \in G} z_0 w = S.
\]
Subtracting $S$ from both sides yields
\[
(z_0 - 1)S = 0.
\]
Since $z_0 \neq 1$, the factor $(z_0 - 1)$ is nonzero, and it follows that
\[
S = 0.
\]
Therefore,
\[
\sum_{z \in G} z = 0,
\]
which completes the proof.

\end{document}
```