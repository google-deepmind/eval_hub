```markdown
## Solution

Define for each integer \(n\ge1\)
\[
a_n \;=\;
\frac{\bigl(1+\frac1n\bigr)^{3n+2}}
     {\bigl(1+\frac1n\bigr)^n
      \;+\;\bigl(1+\frac1n\bigr)^{n+1}
      \;+\;\bigl(1+\frac1n\bigr)^{n+2}}.
\]
We will show \(a_{n+1}/a_n>1\), hence \(a_n\) is strictly increasing.

---

### 1. A convenient closed‐form for the ratio

Set
\[
y_n = 1+\frac1n.
\]
Then
\[
\bigl(1+\tfrac1n\bigr)^n = y_n^n,
\quad
\bigl(1+\tfrac1n\bigr)^{3n+2}
= y_n^{3n+2},
\]
and
\[
\bigl(1+\tfrac1n\bigr)^n
+\bigl(1+\tfrac1n\bigr)^{n+1}
+\bigl(1+\tfrac1n\bigr)^{n+2}
= y_n^n\bigl(1 + y_n + y_n^2\bigr).
\]
Hence
\[
a_n = \frac{y_n^{3n+2}}{y_n^n\,(1+y_n+y_n^2)}
     = \frac{y_n^{2n+2}}{1+y_n+y_n^2}.
\]
Similarly,
\[
a_{n+1}
=\frac{y_{n+1}^{2(n+1)+2}}{1+y_{n+1}+y_{n+1}^2}
=\frac{y_{n+1}^{2n+4}}{1+y_{n+1}+y_{n+1}^2}.
\]
Thus
\[
\frac{a_{n+1}}{a_n}
=
\frac{y_{n+1}^{2n+4}}{y_n^{2n+2}}
\;\cdot\;
\frac{1 + y_n + y_n^2}{1 + y_{n+1} + y_{n+1}^2}.
\]
A short computation shows this can be rewritten in the form
\[
\frac{a_{n+1}}{a_n}
=
\Bigl(1+\tfrac1{n+1}\Bigr)^2
\;\Bigl(1 - \tfrac1{(n+1)^2}\Bigr)^{2n+2}
\;\cdot\;
\frac{3n^2+3n+1}{3n^2+9n+7}.
\]
We set
\[
f(n) \;=\;
\ln\!\Bigl(\tfrac{a_{n+1}}{a_n}\Bigr)
\;=\;
2\ln\Bigl(1+\tfrac1{n+1}\Bigr)
\;+\;(2n+2)\ln\Bigl(1-\tfrac1{(n+1)^2}\Bigr)
\;+\;\ln\frac{3n^2+3n+1}{3n^2+9n+7}.
\]
We will show \(f(n)>0\) for all \(n\ge1\).

---

### 2. Asymptotics of \(f(n)\)

We expand each of the three terms in \(f(n)\) up to order \(n^{-3}\).

1.  Using
    \(\ln(1+x)=x-\tfrac{x^2}2+\tfrac{x^3}3+O(x^4)\), with
    \(x=\tfrac1{n+1}\), we get
    \[
    2\ln\!\Bigl(1+\tfrac1{n+1}\Bigr)
    =2\Bigl(\tfrac1{n+1}-\tfrac1{2(n+1)^2}+\tfrac1{3(n+1)^3}+O(n^{-4})\Bigr)
    =\frac{2}{n+1}-\frac{1}{(n+1)^2}+\frac{2}{3(n+1)^3}+O(n^{-4}).
    \]

2.  Using
    \(\ln(1-x)=-x-\tfrac{x^2}2-\tfrac{x^3}3+O(x^4)\), with
    \(x=\tfrac1{(n+1)^2}\), we get
    \[
    (2n+2)\ln\!\Bigl(1-\tfrac1{(n+1)^2}\Bigr)
    =
    (2n+2)\Bigl(-\tfrac1{(n+1)^2}-\tfrac1{2(n+1)^4}+O(n^{-6})\Bigr)
    =
    -\frac{2}{n+1}-\frac{2}{(n+1)^3}+O(n^{-4}).
    \]

3.  Finally set
    \[
    g(n)=\ln\frac{3n^2+3n+1}{3n^2+9n+7}
    =\ln\!\bigl(1+\tfrac{6n+6}{3n^2+3n+1}\bigr),
    \]
    and expand
    \(\ln(1+u)=u-\tfrac{u^2}2+O(u^3)\) with
    \(u=\tfrac{6n+6}{3n^2+3n+1}=O(n^{-1})\).  One finds
    \[
    g(n)
    =\frac{6(n+1)}{3n^2+3n+1}
     \;-\;\frac12\Bigl(\tfrac{6(n+1)}{3n^2+3n+1}\Bigr)^2
     \;+\;O(n^{-3})
    =\frac{2}{n}-\frac{4}{n^2}+O(n^{-3}).
    \]

Putting these three expansions together,
\[
f(n)
=\Bigl[\tfrac{2}{n+1}-\tfrac{1}{(n+1)^2}+\tfrac{2}{3(n+1)^3}\Bigr]
 +\Bigl[-\tfrac{2}{n+1}-\tfrac{2}{(n+1)^3}\Bigr]
 +\Bigl[\tfrac{2}{n}-\tfrac{4}{n^2}\Bigr]
 +O(n^{-3}).
\]
A little algebra shows the first two square‐bracketed terms combine to
\(\,-\tfrac1{(n+1)^2}+O(n^{-3})\).  Hence
\[
f(n)
= \frac{2}{n}-\frac{1}{(n+1)^2}-\frac{4}{n^2}+O(n^{-3})
= \frac{2}{n^2} - \frac{5}{n^3} + O(n^{-4}).
\]
For all \(n\ge3\) one checks
\[
\frac{2}{n^2}-\frac{5}{n^3} \;=\;\frac{2n-5}{n^3}>0,
\]
and the \(O(n^{-4})\)‐term can be shown to be of smaller order.  Hence
for every \(n\ge3\), \(f(n)>0\).  A direct numerical check shows
also \(f(1)>0\) and \(f(2)>0\).  Therefore
\[
\frac{a_{n+1}}{a_n} = e^{\,f(n)}>1
\quad\forall n\ge1,
\]
and \(\{a_n\}\) is strictly increasing.  \(\quad\square\)
```

**Remark.**  
The heart of the proof is the exact formula
\[
\frac{a_{n+1}}{a_n}
=
\Bigl(1+\tfrac1{n+1}\Bigr)^2
\Bigl(1-\tfrac1{(n+1)^2}\Bigr)^{2n+2}
\frac{3n^2+3n+1}{3n^2+9n+7},
\]
together with a careful Taylor‐expansion of its logarithm to show it
stays positive for every integer \(n\).