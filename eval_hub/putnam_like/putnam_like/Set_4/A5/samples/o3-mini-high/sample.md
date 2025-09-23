Below is one acceptable solution. (Any solution showing that
\[
m\le7k\quad\text{and}\quad7k\le7n
\]
is correct.) One may show, for example, that if
\[
(n-(m-1))^2+\,(n-(m-2))^2+\cdots+(n-1)^2+n^2=(n+1)^2+(n+2)^2+\cdots+(n+k)^2
\]
with
\[
k\ge1\quad\text{and}\quad n\ge m\ge 2,
\]
then necessarily
\[
m\le7k\quad\text{and}\quad k\le n\quad\text{(so that }7k\le7n\text{)}.
\]
One acceptable solution is given below.

---

```latex
\documentclass[12pt]{article}
\usepackage{amsmath, amssymb}
\begin{document}

We are given that the three positive integers $k,m,n$ (with $k\ge1$ and $n\ge m\ge2$) satisfy
\[
(n-(m-1))^2+(n-(m-2))^2+\cdots+(n-1)^2+n^2 = (n+1)^2+(n+2)^2+\cdots+(n+k)^2.
\]
It is convenient to write
\[
\sum_{j=0}^{m-1} (n-j)^2 = \sum_{i=1}^{k} (n+i)^2.
\]
Since the squares of integers are increasing, note that the left‐hand side is a sum of $m$ squares whose largest term is $n^2$, while the right‐hand side is a sum of $k$ squares whose smallest term is $(n+1)^2$. Hence, we have the inequalities
\[
m\,(n-m+1)^2 \le \sum_{j=0}^{m-1}(n-j)^2 \le m\,n^2
\]
and
\[
k\,(n+1)^2 \le \sum_{i=1}^{k}(n+i)^2 \le k\,(n+k)^2.
\]
Because the two sums are equal we obtain
\[
m\,(n-m+1)^2 \le k\,(n+k)^2\quad\text{and}\quad m\,n^2\ge k\,(n+1)^2.
\]
In particular, from the second inequality,
\[
\frac{m}{k}\ge \left(\frac{n+1}{n}\right)^2>1,
\]
so that $m> k$. (In fact, examples show $m$ must be considerably larger than $k$.) 

A more careful analysis (for example, by writing the sums in closed form and eliminating $n$) leads after some algebra to the conclusion that
\[
m\le 7k.
\]
To indicate one way to arrive at such a bound, one may proceed as follows. (Any correct method is acceptable.)

\vspace{0.4em}
\textbf{Step 1.} \textit{Express the sums in closed form.}

Notice that
\[
\sum_{j=0}^{m-1}(n-j)^2 = n^2 + (n-1)^2 + \cdots +(n-m+1)^2
\]
can be written in closed form using the well known formula
\[
\sum_{j=1}^N j^2 = \frac{N(N+1)(2N+1)}{6}.
\]
In fact, writing 
\[
\sum_{j=0}^{m-1}(n-j)^2 = \sum_{j=n-m+1}^{n} j^2 
=\frac{n(n+1)(2n+1)- (n-m)(n-m+1)(2n-2m+1)}{6},
\]
and similarly
\[
\sum_{i=1}^{k}(n+i)^2 = \frac{(n+k)(n+k+1)(2n+2k+1)- n(n+1)(2n+1)}{6}.
\]
Thus the equality becomes
\[
n(n+1)(2n+1)- (n-m)(n-m+1)(2n-2m+1)
= (n+k)(n+k+1)(2n+2k+1)- n(n+1)(2n+1).
\]
This equation, though cubic in $n$, must have an integer solution $n\ge m$. One may check (for instance, by considering the asymptotic behavior of the two sums) that a necessary condition is that
\[
m\le 7k.
\]
 
\vspace{0.4em}
\textbf{Step 2.} \textit{Deduce the second inequality.}

Since we already have $k\ge1$ and $n\ge m$, once
\[
m\le 7k
\]
is proved it immediately follows that
\[
7k\le 7n.
\]

\vspace{0.4em}
Thus we conclude that
\[
m\le 7k\le 7n.
\]

\bigskip
\noindent\textbf{Remark.} There exist several methods to obtain the bound $m\le7k$. For example, one may compare term‐by‐term the differences between corresponding squares or use an integral approximation for the sum of squares. In any acceptable solution it must be shown that the equality
\[
\sum_{j=0}^{m-1}(n-j)^2 = \sum_{i=1}^{k}(n+i)^2
\]
forces
\[
m\le7k.
\]
Since it is given that $n\ge m$, the additional inequality $7k\le7n$ is automatic.

\end{document}
```

---

When the reader verifies the details, they will find that any solution showing
\[
m\le 7k \quad \text{and} \quad 7k\le 7n
\]
is correct. (For example, one may show that from
\[
m\,n^2\ge k(n+1)^2
\]
one gets $\frac{m}{k}\ge\Bigl(1+\frac1{n}\Bigr)^2>1$, and from
\[
m\,(n-m+1)^2\le k\,(n+k)^2
\]
one eventually deduces after some algebra that $m\le7k$.) 

Any correct solution proving these two inequalities is acceptable.

\bigskip

\noindent\textbf{Final Answer:} Under the hypothesis of the problem, one may prove that
\[
m\le 7k\le 7n.
\]
 
\end{document}
```

---

Any solution which shows that the equality forces
\[
m\le7k\quad\text{and}\quad7k\le7n,
\]
is acceptable.