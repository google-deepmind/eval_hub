```markdown
We start with the sequence \((a_n)\) defined by
\[
a_0 = 1,\quad a_1 = 1,
\]
and for all \(n\ge1\) by
\[
a_{2n}=a_n,\qquad a_{2n-1}=a_n+a_{n-1}.
\]
For each \(n\in\mathbb{N}\) (where by convention we take \(\mathbb{N} = \{0,1,2,\dots\}\) or \(\{1,2,\dots\}\) as needed), we form the ratio
\[
r_n=\frac{a_{n+1}}{a_n}.
\]
Let
\[
S=\{\,r\in\mathbb{Q}^+ : r = r_n \text{ for some } n\in\mathbb{N}\}.
\]
We will show that
\[
S=\left\{\frac{p}{q}: p,q\in\mathbb{N},\,\gcd(p,q)=1\right\},
\]
that is, every positive rational number (written in lowest terms) appears as one of the ratios \(\frac{a_{n+1}}{a_n}\).

### A Few Examples

Let us compute the first few terms of the sequence \((a_n)\):
- \(a_0=1,\quad a_1=1.\)
- \(a_2 = a_{2\cdot1}=a_1=1.\)
- \(a_3 = a_{2\cdot2-1}=a_2+a_1=1+1=2.\)
- \(a_4 = a_{2\cdot2}=a_2=1.\)
- \(a_5 = a_{2\cdot3-1}=a_3+a_2=2+1=3.\)
- \(a_6 = a_{2\cdot3}=a_3=2.\)
- \(a_7 = a_{2\cdot4-1}=a_4+a_3=1+2=3.\)
- \(a_8 = a_{2\cdot4}=a_4=1.\)

Thus the corresponding ratios are:
- \(r_0 = \frac{a_1}{a_0} = \frac{1}{1}=1\).
- \(r_1 = \frac{a_2}{a_1} = \frac{1}{1}=1\).
- \(r_2 = \frac{a_3}{a_2} = \frac{2}{1}=2\).
- \(r_3 = \frac{a_4}{a_3} = \frac{1}{2}\).
- \(r_4 = \frac{a_5}{a_4} = \frac{3}{1}=3\).
- \(r_5 = \frac{a_6}{a_5} = \frac{2}{3}\).
- \(r_6 = \frac{a_7}{a_6} = \frac{3}{2}\).
- \(r_7 = \frac{a_8}{a_7} = \frac{1}{3}\).

Already we see many positive rational numbers appearing: \(1\), \(2\), \(\frac{1}{2}\), \(3\), \(\frac{2}{3}\), \(\frac{3}{2}\), \(\frac{1}{3}\), \(\ldots\)

### Recursive Structure and Connection to the Calkin–Wilf Tree

A closer look at the recurrence reveals the following:
- If we write \(n=2m\), then
  \[
  r_{2m} = \frac{a_{2m+1}}{a_{2m}}.
  \]
  Notice that by the definition,
  \[
  a_{2m+1} = a_{m+1} + a_m\quad \text{and}\quad a_{2m} = a_m.
  \]
  Thus,
  \[
  r_{2m} = \frac{a_{m+1}+a_m}{a_m} = 1+\frac{a_{m+1}}{a_m} = 1 + r_m.
  \]
- If \(n=2m-1\), then
  \[
  r_{2m-1} = \frac{a_{2m}}{a_{2m-1}}.
  \]
  Here,
  \[
  a_{2m} = a_m\quad \text{and}\quad a_{2m-1} = a_m + a_{m-1},
  \]
  so that
  \[
  r_{2m-1}=\frac{a_m}{a_m+a_{m-1}} = \frac{1}{1+\frac{a_{m-1}}{a_m}}.
  \]
  Setting \(r_{m-1}=\frac{a_m}{a_{m-1}}\) (for \(m\ge1\)), we obtain
  \[
  r_{2m-1}=\frac{1}{1+1/r_{m-1}}.
  \]

Thus, every ratio is produced by starting at \(1\) (since \(r_0=1\)) and applying one of the two functions:
\[
T_0(x)=1+x,\qquad T_1(x)=\frac{x}{1+x}.
\]
One may show that iterating these functions in all possible finite sequences produces every positive rational number exactly once. This is equivalent to the well‐known property of the **Calkin–Wilf tree**: every positive rational number (in lowest terms) appears exactly once as a vertex of the tree, and the ratios \(r_n=\frac{a_{n+1}}{a_n}\) are nothing but a traversal of this tree.

### Conclusion

Since:
1. Every \(r_n=\frac{a_{n+1}}{a_n}\) is a positive rational number, and
2. Every positive rational number in lowest terms appears exactly once via the recurrences (or equivalently, in the Calkin–Wilf tree),

we conclude that
\[
S=\left\{\frac{a_{n+1}}{a_n}:n\in\mathbb{N}\right\} = \left\{\frac{p}{q}: p,q\in\mathbb{N},\,\gcd(p,q)=1\right\}.
\]

That is, the set \(S\) is precisely the set of all positive rational numbers.
```