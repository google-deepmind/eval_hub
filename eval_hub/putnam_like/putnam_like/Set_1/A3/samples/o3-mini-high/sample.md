```markdown
We are given the power series

\[
f(x)=\sum_{i\ge0}a_i\,x^i,\qquad\text{with }a_i\in\{0,1\},
\]

and the hypothesis that for some \( n\in\mathbb{N} \) the number

\[
f\Bigl(\frac{1}{2^n}\Bigr)=\sum_{i\ge0}a_i\Bigl(\frac{1}{2^n}\Bigr)^i
\]

is rational.

Recall that if a number has a rational value then its expansion in any integer base is eventually periodic. In our case, the “digits” in the base \( 2^n \) expansion of the number \( f(1/2^n) \) are the numbers \( a_i\in\{0,1\}\) (which are allowed, since in base \( 2^n \) the allowed digits are \(0,1,\dots,2^n-1\)). Therefore there exist integers \( N\ge0 \) and \( p\ge1 \) such that

\[
a_i=a_{i+p}\quad\text{for all } i\ge N.
\]

Thus, we may write

\[
f(x)=\sum_{i=0}^{N-1}a_i\,x^i + x^N\sum_{j\ge0}a_{N+j}\,x^j.
\]

Since the tail \( \{a_{N+j}\}_{j\ge0} \) is periodic of period \( p \), we can group its terms according to the residue modulo \( p \). That is, writing

\[
\sum_{j\ge0}a_{N+j}\,x^j=\sum_{r=0}^{p-1} a_{N+r}\,x^r \sum_{m\ge0} x^{mp},
\]

and using the formula for a geometric series (which converges for \(|x|<1\)),

\[
\sum_{m\ge0} x^{mp}=\frac{1}{1-x^p},
\]

we obtain

\[
f(x)=\sum_{i=0}^{N-1}a_i\,x^i+\frac{x^N}{1-x^p}\sum_{r=0}^{p-1}a_{N+r}\,x^r.
\]

Now, let \( q\ge3 \) be an odd natural number and substitute

\[
x=\frac{2}{q}.
\]

Then

\[
f\Bigl(\frac{2}{q}\Bigr)=\sum_{i=0}^{N-1}a_i\left(\frac{2}{q}\right)^i+\frac{(2/q)^N}{1-(2/q)^p}\sum_{r=0}^{p-1}a_{N+r}\left(\frac{2}{q}\right)^r.
\]

Notice that each term such as \(\left(\frac{2}{q}\right)^i\) is rational (since \(2\) and \(q\) are integers, and \(q\) is odd) and the finite sums and products of rational numbers are rational. Thus, we deduce that

\[
f\Bigl(\frac{2}{q}\Bigr)\in\mathbb{Q}.
\]

It remains to check that when \( f(2/q) \) is written in lowest terms, its denominator is odd. To this end, note that

\[
1-\Bigl(\frac{2}{q}\Bigr)^p=1-\frac{2^p}{q^p}=\frac{q^p-2^p}{q^p}.
\]

Since \( q \) is odd, \( q^p \) is an odd number; also, \(2^p\) is even (for \(p\ge1\)), so \(q^p-2^p\) is odd (an odd number minus an even number is odd). Therefore, the factor

\[
\frac{1}{1-(2/q)^p}=\frac{q^p}{q^p-2^p}
\]

has an odd denominator. Furthermore, any finite sum of terms of the form \((2/q)^k\) is a rational number whose denominator is a power of \( q \) (hence odd) multiplied by some power of \(2\) from the numerator. Consequently, when we combine all the terms, the only factors in the denominator come from powers of \(q\) or from the odd number \(q^p-2^p\); no factor of 2 is introduced in the denominator. (Any factors of 2 appearing in numerators do not cancel any odd factor in the denominator.) Hence, if we write

\[
f\Bigl(\frac{2}{q}\Bigr)=\frac{\alpha}{\beta}
\]

with \(\gcd(\alpha,\beta)=1\), then \(\beta\) is odd.

Thus, we have shown that if \(f(1/2^n)\) is rational then for every odd natural number \(q\ge3\) the number \(f(2/q)\) is rational and its (reduced) denominator is odd.
```