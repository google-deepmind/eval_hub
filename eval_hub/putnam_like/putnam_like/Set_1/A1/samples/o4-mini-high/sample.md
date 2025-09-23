```markdown
**Solution.**  
Let 
\[
\D =\{\,n : n=pq,\;p,q\in\P\,\}
\]
be the set of semiprimes (allowing squares \(p^2\)).  We claim that the longest possible run of consecutive integers all lying in \(\D\) has length 3, and no four‐term run exists.

1.  **There is a run of length 3.**  
    For example
    \[
      33=3\cdot11,\quad 34=2\cdot17,\quad 35=5\cdot7
    \]
    are three consecutive integers, each of which is a product of two primes.  Thus
    \(\{33,34,35\}\subset\D\), so runs of length 3 occur.

2.  **No run of length 4 can occur.**  
    Among any four consecutive integers one is divisible by 4.  If a semiprime
    \(n=pq\) is divisible by 4 then either
    \[
      2\mid p,\;2\mid q\quad\Longrightarrow\quad n=2\cdot2=4,
    \]
    or else one of \(p,q\) is 2 and the other is composite, which is impossible.
    Hence the *only* semiprime divisible by 4 is \(4=2^2\).  But any block of four
    consecutive numbers contains exactly one multiple of 4, so to have four
    semiprimes in a row that multiple of 4 would have to be 4 itself.  Checking
    the only possible block that contains \(4\),
    \[
      (1,2,3,4)\quad\text{or}\quad(2,3,4,5)\quad\text{or}\quad(3,4,5,6),
    \]
    we see that at least one of those four is not even in \(\D\).  Therefore no
    four consecutive integers can all lie in \(\D\).

Combining (1) and (2) shows that the maximal length of a run of consecutive
semiprimes is
\[
  \boxed{3}.
\]
```