```markdown
**Solution**

We wish to evaluate the double sum

\[
S(n)\;=\;\sum_{k=0}^{\lfloor n/2\rfloor}
\sum_{\ell=\max\{1,2k\}}^n \frac{1}{4^k}\binom{\ell}{2k}.
\]

1.  Inner‐sum via a standard binomial identity:

    For any nonnegative integers \(m\le n\) one has
    \[
      \sum_{\ell=m}^n \binom{\ell}{m}
      \;=\;\binom{n+1}{m+1}.
    \]
    Hence for \(k\ge1\),
    \[
      \sum_{\ell=2k}^n \binom{\ell}{2k}
      = \binom{n+1}{2k+1}.
    \]
    When \(k=0\) the sum \(\sum_{\ell=1}^n\binom{\ell}{0}=n\),
    whereas \(\binom{n+1}{1}=n+1\).  Thus
    \[
      \sum_{\ell=\max\{1,2k\}}^n\binom{\ell}{2k}
      = \binom{n+1}{2k+1}\quad(k\ge1),
      \qquad
      \sum_{\ell=1}^n\binom{\ell}{0}=n
      =\binom{n+1}{1}-1.
    \]
    Altogether
    \[
      S(n)
      = \sum_{k=0}^{\lfloor n/2\rfloor}\frac{1}{4^k}\,\binom{n+1}{2k+1}
        \;-\;1.
    \]

2.  Summing the remaining single sum by the binomial theorem:

    Consider
    \[
      (1+t)^{n+1} \;=\;
      \sum_{m=0}^{n+1}\binom{n+1}{m}t^m
      \;=\;
      \sum_{k\ge0}\binom{n+1}{2k}t^{2k}
      \;+\;
      \sum_{k\ge0}\binom{n+1}{2k+1}t^{2k+1}.
    \]
    Likewise
    \[
      (1-t)^{n+1}
      = \sum_{k\ge0}\binom{n+1}{2k}t^{2k}
      \;-\;
      \sum_{k\ge0}\binom{n+1}{2k+1}t^{2k+1}.
    \]
    Subtracting gives
    \[
      (1+t)^{n+1} - (1-t)^{n+1}
      = 2\sum_{k\ge0}\binom{n+1}{2k+1}t^{2k+1}.
    \]
    Now set \(t=\tfrac12\).  Then
    \[
      \sum_{k=0}^{\lfloor n/2\rfloor}
      \frac{\binom{n+1}{2k+1}}{4^k}
      = \sum_{k\ge0}\binom{n+1}{2k+1}\Bigl(\tfrac12\Bigr)^{2k}
      = (3/2)^{n+1} - (1/2)^{n+1}.
    \]
    Therefore
    \[
      S(n)
      = \Bigl(\tfrac32\Bigr)^{n+1} - \Bigl(\tfrac12\Bigr)^{n+1} - 1
      = \frac{3^{n+1}-2^{n+1}-1}{2^{\,n+1}}.
    \]

**Final Answer.**  
\[
\boxed{
\sum_{k=0}^{\lfloor n/2\rfloor}
\sum_{\ell=\max\{1,2k\}}^n \frac{1}{4^k}\binom{\ell}{2k}
\;=\;
\Bigl(\tfrac32\Bigr)^{n+1}-\Bigl(\tfrac12\Bigr)^{n+1}-1
\;=\;
\frac{3^{n+1}-2^{n+1}-1}{2^{\,n+1}}.
}
\]
```