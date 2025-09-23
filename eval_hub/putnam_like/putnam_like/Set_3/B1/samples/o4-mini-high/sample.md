```markdown
**Solution.**  
Label by \(R_G(x_1,\dots,x_n)\) the final number obtained from \((x_1,\dots,x_n)\) by \(n-1\) iterations of taking adjacent geometric means, and by \(R_A(x_1,\dots,x_n)\) the analogous result when one takes adjacent arithmetic means.  We will show

1.  At each step
    \[
      \sqrt{x_i\,x_{i+1}}
      \;\le\;
      \frac{x_i + x_{i+1}}{2},
    \]
    with strict inequality whenever \(x_i\neq x_{i+1}\).  Hence for any strictly increasing sequence the geometric‐mean process stays strictly below the arithmetic‐mean process, i.e.
    \[
      R_G(x_1,\dots,x_n)\;<\;R_A(x_1,\dots,x_n).
    \]

2.  After \(n-1\) iterations of adjacent arithmetic means one recovers the ordinary arithmetic mean of the original entries.  Indeed one checks by induction (or by the binomial‐expansion argument below) that
    \[
      R_A(x_1,\dots,x_n)
      \;=\;
      \frac{\binom{n-1}{0}x_1+\binom{n-1}{1}x_2+\cdots+\binom{n-1}{n-1}x_n}
           {2^{\,n-1}}.
    \]
    In particular, for \((1,2,\dots,n)\) the numerator is
    \[
      \sum_{k=0}^{n-1}\binom{n-1}{k}(k+1)
      \;=\;
      (n+1)\,2^{\,n-2}
      \quad\Longrightarrow\quad
      R_A(1,2,\dots,n)
      =\frac{(n+1)\,2^{\,n-2}}{2^{\,n-1}}
      =\frac{n+1}{2}.
    \]

Combining these two observations gives
\[
  \mathrm{result}
  \;=\;
  R_G(1,2,\dots,n)
  \;<\;
  R_A(1,2,\dots,n)
  =\frac{n+1}{2},
\]
as required.
```

**Explanation of the binomial identity.**  
One uses
\[
  \sum_{k=0}^{n-1}\binom{n-1}{k}
  =2^{\,n-1},
  \quad
  \sum_{k=0}^{n-1}k\,\binom{n-1}{k}
  =(n-1)\,2^{\,n-2}.
\]
Hence
\[
  \sum_{k=0}^{n-1}(k+1)\binom{n-1}{k}
  =(n-1)\,2^{\,n-2}+2^{\,n-1}
  =(n+1)\,2^{\,n-2}.
\]
Dividing by \(2^{\,n-1}\) gives \(\tfrac{n+1}{2}\).