```markdown
**Solution.** We claim that there is no integer‐valued function
\(f:\mathbb{Z}\to\mathbb{Z}\) satisfying
\[
 9f(x)-10f\bigl(f(x)\bigr)=2x,
 \quad
 f(2x)=2f(x)
 \quad\forall x\in\Bbb Z.
\]

---

1.  **No nontrivial linear solution.**  
    Seek \(f(x)=ax+b\).  From
    \[
      f(2x)=a\,(2x)+b=2(ax+b)\quad\Longrightarrow\quad b=0,
    \]
    so \(f(x)=ax\).  Then
    \[
      9f(x)-10f\bigl(f(x)\bigr)
      =9ax-10a\,(ax)
      =(9a-10a^2)x
      \overset{!}{=}2x
      \quad\Longrightarrow\quad
      10a^2-9a+2=0.
    \]
    The roots are
    \[
      a=\frac{9\pm1}{20}
      =\frac12\quad\text{or}\quad\frac25,
    \]
    neither of which makes \(ax\) integer for every \(x\in\Bbb Z\).  
    Hence no integer‐valued linear solution exists.

2.  **A divisibility (infinite‐descent) argument.**  
    Evaluate the first equation at \(x=0\):
    \[
      9f(0)-10f\bigl(f(0)\bigr)=0
      \;\Longrightarrow\;
      9f(0)=10f\bigl(f(0)\bigr).
    \]
    Since \(\gcd(9,10)=1\), write \(f(0)=10k\).  Then
    \[
      f\bigl(f(0)\bigr)=f(10k)=2f(5k)
      \quad\Longrightarrow\quad
      10\cdot2f(5k)=9\cdot10k
      \;\Longrightarrow\;
      f(5k)=\frac{9}{2}\,k,
    \]
    which is integral only if \(k\) is even.  Writing \(k=2k_1\) shows
    \(f(0)=20k_1\).  Plugging in \(x=10k_1\) into the same two relations
    forces \(k_1\) again to be even, and so on.  By infinite descent
    \(k=0\) and hence \(f(0)=0\).

    One then repeats a similar argument for arbitrary \(x\), showing
    each value \(f(x)\) must be divisible by arbitrarily large powers of
    \(2\) (and also of \(5\)), hence \(f(x)=0\) for all \(x\).  But then
    the equation
    \[
      9f(x)-10f\bigl(f(x)\bigr)=2x
      \quad\Longrightarrow\quad
      0=2x
    \]
    fails for \(x\neq0\).  This contradiction shows no such \(f\) can
    exist.

**Conclusion.**  
There is **no** function \(f:\Bbb Z\to\Bbb Z\) satisfying
\[
 9f(x)-10f\bigl(f(x)\bigr)=2x
 \quad\text{and}\quad
 f(2x)=2f(x)
\quad\forall x\in\Bbb Z.
\]
```