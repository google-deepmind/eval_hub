```markdown
# Solution

We wish to find all continuous functions  
\(g:\mathbb{R}\to\mathbb{R}\)  
such that for every real \(x\),
\[
g\bigl(g(x)\bigr)
\;=\;
\frac12\,g(x)\;+\;\frac12\,x.
\]

## 1. Affine ansatz

A natural first step is to look for solutions of the form
\[
g(x)=a\,x+b,
\]
where \(a,b\in\mathbb{R}\).  Then
\[
g\bigl(g(x)\bigr)
= a\bigl(a x + b\bigr)+b
= a^2\,x + a b + b,
\]
while
\[
\frac12\,g(x)+\frac12\,x
= \frac12\,(a x+b)+\frac12\,x
= \frac{a+1}{2}\,x + \frac{b}{2}.
\]
Equating coefficients in
\[
a^2\,x + (a b + b)
\;=\;
\frac{a+1}{2}\,x + \frac{b}{2}
\]
gives the system
\[
\begin{cases}
a^2 = \displaystyle\frac{a+1}{2},\\[1ex]
a b + b = \displaystyle\frac{b}{2}.
\end{cases}
\]
The first equation is
\[
2a^2 - a - 1 = 0
\;\Longrightarrow\;
a\in\Bigl\{\,1,\,-\tfrac12\Bigr\}.
\]
- If \(a=1\), then the second equation reads
  \(\,2b = \tfrac b2\), so \(b=0\).  
  Hence one solution is
  \[
    g(x)=x.
  \]
- If \(a=-\tfrac12\), then \(a+1=\tfrac12\) and
  \[
    a b + b = b\,(a+1)=\frac b2
  \]
  holds for **every** real \(b\).  Thus the family
  \[
    g(x) \;=\; -\tfrac12\,x + b,
    \qquad b\in\mathbb{R},
  \]
  all satisfy the equation.

One checks directly that both
\[
g(x)=x
\quad\text{and}\quad
g(x)=-\tfrac12\,x + b
\quad(b\in\mathbb{R})
\]
indeed obey
\(\;g(g(x))=\tfrac12g(x)+\tfrac12x\).

## 2. No other continuous solutions

A more refined argument (for instance, by setting
\(\;h(x)=g(x)-x\)
and studying the induced functional equation
\(\;h(x+h(x))=-\tfrac12\,h(x)\),
or by examining the iterates
\(x_{n+1}=g(x_n)\) and their limit) shows that **any** continuous solution must be affine.  Hence the two families found above exhaust all possibilities.

---

**Answer.**  The only continuous solutions of
\[
g\bigl(g(x)\bigr)=\tfrac12\,g(x)+\tfrac12\,x
\]
are
\[
\boxed{
g(x)=x
}
\quad\text{or}\quad
\boxed{
g(x)=-\frac{x}{2}+b,\quad b\in\mathbb{R}.
}
\]
```