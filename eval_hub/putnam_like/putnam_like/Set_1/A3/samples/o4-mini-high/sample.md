```markdown
# Solution

We shall show two things:

1.  Rationality of \(f(2/q)\) for every odd \(q\ge3\).
2.  When written in lowest terms \(\displaystyle f(2/q)=\frac\alpha\beta\), the denominator \(\beta\) is odd.

---

## 1. Rationality of \(f(1/2^n)\) forces eventual periodicity of \((a_i)\)

Write
\[
f\!\bigl(x\bigr)\;=\;\sum_{i=0}^\infty a_i\,x^i,
\]
with \(a_i\in\{0,1\}\).  Then
\[
f\!\Bigl(\tfrac1{2^n}\Bigr)
\;=\;\sum_{i=0}^\infty a_i\bigl(2^{-n}\bigr)^i
\;=\;a_0+a_1\,2^{-n}+a_2\,2^{-2n}+\cdots
\]
is precisely the base-\(2^n\) “digit‐expansion” with digits \(a_i\).  A classical fact is:

> A real number in \([0,1]\) has a eventually periodic expansion in base \(B\)  
> if and only if it is rational.

Since by hypothesis \(f(1/2^n)\in\Bbb Q\), the sequence of digits \((a_i)\) must be **eventually periodic**.  Hence there exist integers
\[
m\ge0,\quad d\ge1
\]
such that
\[
a_{i+d}=a_i
\quad
\text{for all }i\ge m.
\]

---

## 2. Decomposition of \(f(x)\) into a finite part and a periodic tail

Split the power series at index \(m\).  Define two polynomials
\[
P_0(x)\;=\;\sum_{i=0}^{m-1}a_i\,x^i,
\qquad
P_1(x)\;=\;\sum_{j=0}^{d-1}a_{\,m+j}\,x^j.
\]
Then for \(i\ge m\) we have \(a_i=a_{\,m+(i-m)\bmod d}\), and one checks
\[
\sum_{i=m}^\infty a_i\,x^i
=
x^m\sum_{k=0}^\infty\sum_{j=0}^{d-1}a_{\,m+j}\,x^{\,k d+j}
=
x^m\,P_1(x)\,\sum_{k=0}^\infty \bigl(x^d\bigr)^k
=
\frac{x^m\,P_1(x)}{1-x^d}.
\]
Hence
\[
\boxed{
f(x)
\;=\;
P_0(x)\;+\;\frac{x^m\,P_1(x)}{1-x^d}\,,
}
\]
which is a rational function in \(x\).

---

## 3. Evaluation at \(x=\tfrac2q\)

Let \(q\ge3\) be odd.  Substitute \(x=2/q\) into the above:
\[
f\!\Bigl(\tfrac2q\Bigr)
=
P_0\!\Bigl(\tfrac2q\Bigr)
\;+\;
\frac{\,(2/q)^m\,P_1(2/q)\,}{1 - (2/q)^d}
\,.
\]
Each of these terms is manifestly rational.  Thus \(f(2/q)\in\Bbb Q\).

---

## 4. The denominator is odd

We now check that in lowest terms the denominator has no factor \(2\).  Note:

- \(P_0(2/q)\) is a sum of terms \(a_i\,(2/q)^i\), so its denominator divides \(q^{\,m-1}\).  Since \(q\) is odd, no factor \(2\) appears.

- The second term is
  \[
    \frac{(2/q)^m\,P_1(2/q)}{1-(2/q)^d}
    \;=\;
    \frac{2^m}{q^m}\;\cdot\;\frac{P_1(2/q)}{1-(2/q)^d}.
  \]
  Here
  \[
    P_1\!\Bigl(\tfrac2q\Bigr)
    \;=\;
    \sum_{j=0}^{d-1}a_{m+j}\,\frac{2^j}{q^j}
    \;=\;\frac{B}{q^{\,d-1}}
    \quad(B\in\Bbb Z),
  \]
  and
  \[
    1-(2/q)^d
    \;=\;
    \frac{\,q^d-2^d\,}{q^d}.
  \]
  Putting these together one finds the common denominator
  \[
    q^m\;q^{\,d-1}\;\bigl(q^d-2^d\bigr)
    \;=\;
    q^{\,m+d-1}\bigl(q^d-2^d\bigr),
  \]
  which is a product of odd integers.  Hence no power of \(2\) can occur in the denominator of \(f(2/q)\).

---

### Conclusion

For every odd \(q\ge3\), the value \(f(2/q)\) is rational, and when written in lowest terms \(\displaystyle f(2/q)=\frac\alpha\beta\) we see that \(\beta\) is odd.
```

**Explanation of Key Steps**

1. Rationality of \(f(1/2^n)\) implies the binary‐\(2^n\) digit sequence \((a_i)\) is eventually periodic.  
2. An eventually periodic sequence of coefficients yields a rational generating function of the form
   \[
     f(x)=P_0(x)+\frac{x^m\,P_1(x)}{1-x^d}.
   \]
3. Substituting \(x=2/q\) gives a rational number whose denominator factors only of \(q\) and \(q^d-2^d\), all odd.  
4. Hence \(f(2/q)\) is rational with an odd denominator.