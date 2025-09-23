```markdown
We wish to compute
\[
L=\lim_{n\to\infty} \frac{1}{n^2}\sum_{k=1}^n\sum_{l=1}^k e^{l/k}\,.
\]

A useful strategy is to rearrange the summation by writing
\[
\frac{1}{n^2}\sum_{k=1}^n\sum_{l=1}^k e^{l/k}
=\frac{1}{n^2}\sum_{k=1}^n k\left(\frac{1}{k}\sum_{l=1}^k e^{l/k}\right).
\]
For each fixed \(k\), consider the inner sum
\[
\frac{1}{k}\sum_{l=1}^k e^{l/k}.
\]
If we let
\[
u = \frac{l}{k},
\]
then as \(l\) runs from 1 to \(k\), \(u\) takes values approximately in the interval \([0,1]\) with step \(\Delta u = \frac{1}{k}\). Hence, for large \(k\) the Riemann sum
\[
\frac{1}{k}\sum_{l=1}^k e^{l/k}
\]
approximates the integral
\[
\int_0^1 e^u\,du = e-1\,.
\]
Thus, for large \(k\) we have
\[
\frac{1}{k}\sum_{l=1}^k e^{l/k} \approx e-1\,.
\]

Returning to our original sum, we now have
\[
\frac{1}{n^2}\sum_{k=1}^n\sum_{l=1}^k e^{l/k} \approx 
\frac{1}{n^2}\sum_{k=1}^n k\,(e-1) = (e-1)\frac{1}{n^2}\sum_{k=1}^n k\,.
\]

Recall that
\[
\sum_{k=1}^n k = \frac{n(n+1)}{2}\,,
\]
so that
\[
\frac{1}{n^2}\sum_{k=1}^n k = \frac{n(n+1)}{2n^2} = \frac{n+1}{2n}\,.
\]
Taking the limit as \(n\to\infty\), we find
\[
\lim_{n\to\infty}\frac{n+1}{2n} = \frac{1}{2}\,.
\]

Combining these results, we get
\[
L = (e-1)\cdot\frac{1}{2} = \frac{e-1}{2}\,.
\]

Thus, the limit is
\[
\boxed{\frac{e-1}{2}}\,.
\]
```