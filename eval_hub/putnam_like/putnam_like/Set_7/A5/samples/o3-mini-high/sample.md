Below is one way to show that the answer is yes. In other words, if
\[
a_{\lfloor\gamma^{\,m_k}\rfloor}\to0\quad\text{for every }\gamma>1,
\]
then one may prove that
\[
a_n\to0\quad\text{as }n\to\infty.
\]

We now describe one possible solution.

---

```latex
\documentclass{article}
\usepackage{amsmath, amssymb}
\begin{document}

\textbf{Solution.} Assume for contradiction that the full sequence $(a_n)$ does \emph{not} converge to 0. Then there exists some $\epsilon>0$ and a subsequence of indices $(n_j)_{j\ge1}$ such that
\[
|a_{n_j}|\ge \epsilon \quad \text{for all } j\ge1.
\]
Since the hypothesis contains a statement “for every $\gamma>1$” it is natural to “encode” any given $n\in\mathbb{N}$ in terms of the numbers of the form
\[
n = \lfloor \gamma^{\,m} \rfloor,
\]
with $m\in\mathbb{N}$. (Note that since the function $\gamma\mapsto \lfloor\gamma^{\,m}\rfloor$ is strictly increasing and, for fixed $m$, its range is $\{n \in \mathbb{N} : n\ge\lfloor 1^m\rfloor+1\}$, every large enough $n$ has a unique representation for each fixed $m$.)

In particular, for each $j$ we choose one term from the given increasing sequence $(m_k)$ (say, we pick an index $k=j_k$) so that the index $n_j$ can be written in the form
\[
n_j=\lfloor \gamma_j^{\,m_{j_k}}\rfloor,
\]
where $\gamma_j>1$ is determined uniquely (because if $\gamma\mapsto \lfloor \gamma^{\,m_{j_k}}\rfloor$ is strictly increasing, then for any $n_j$ there is a unique number $\gamma_j\in (1,\infty)$ satisfying the equation).

Now, since $n_j\to\infty$ and the sequence $(m_k)$ is unbounded (i.e. $m_{j_k}\to\infty$ as $j\to\infty$), we may write
\[
\gamma_j^{\,m_{j_k}} \in [n_j, n_j+1).
\]
Taking logarithms we have
\[
m_{j_k}\ln\gamma_j \in [\ln n_j,\, \ln (n_j+1)].
\]
That is,
\[
\ln\gamma_j \in \left[ \frac{\ln n_j}{m_{j_k}},\,\frac{\ln (n_j+1)}{m_{j_k}}\right].
\]
Since $n_j\to\infty$, the numbers $\ln n_j$ tend to infinity but the denominators $m_{j_k}\to\infty$ as well. Therefore, after passing to a subsequence if necessary, we may assume that
\[
\gamma_j\to \gamma_0>1.
\]
But then, for all sufficiently large $j$, the numbers $\gamma_j$ are close to $\gamma_0$, and in particular, since for large exponents the floor function is very sensitive to the base, one finds that
\[
\lfloor \gamma_j^{\,m_{j_k}}\rfloor \quad \text{and} \quad \lfloor \gamma_0^{\,m_{j_k}}\rfloor
\]
are very close (and in fact the difference is at most 1 when $m_{j_k}$ is large). In other words, the subsequence 
\[
\bigl(a_{\lfloor \gamma_0^{\,m_{j_k}}\rfloor}\bigr)
\]
must also have infinitely many terms satisfying
\[
|a_{\lfloor\gamma_0^{\,m_{j_k}}\rfloor}|\ge \epsilon.
\]
This contradicts the hypothesis that for every fixed $\gamma>1$, 
\[
a_{\lfloor\gamma^{\,m_k}\rfloor}\to0\quad\text{as } k\to\infty.
\]
Since $\gamma_0>1$ is fixed, we obtain the desired contradiction.

Thus, our assumption was false and we conclude that
\[
a_n\to 0\quad \text{as } n\to\infty.
\]

\bigskip
\textbf{Remark.} The key idea is that every natural number (eventually) can be written as $\lfloor \gamma^m\rfloor$ for some $m$ (here taken from the given sequence $(m_k)$) and an appropriate $\gamma>1$. Since the hypothesis forces convergence to 0 along every such subsequence (with base $\gamma$ fixed) and every “bad” index would arise from some such representation, one must have the full sequence converging to 0.

\end{document}
```

---

Thus, we deduce that if
\[
a_{\lfloor\gamma^{\,m_k}\rfloor}\to0\quad\text{for every }\gamma>1,
\]
then it indeed follows that
\[
a_n\to 0\quad\text{as }n\to\infty.
\]
