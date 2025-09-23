```markdown
# Solution

Let \(I\) denote the improper integral
\[
I \;=\;
\int_{\alpha}^{\infty}
\frac{f(x - \alpha) - f(x + \alpha)}{f(x)} \, dx.
\]
Since \(f\) is strictly decreasing, continuous on \([0,\infty)\), and 
\(\lim_{x\to\infty}f(x)=0\), we have \(f(x)>0\) for all \(x\ge0\).

---

## 1. A block estimate on each interval \([n\alpha,(n+1)\alpha]\)

Fix a positive integer \(n\).  For 
\(x\in[n\alpha,(n+1)\alpha]\) the monotonicity of \(f\) gives
\[
\begin{aligned}
f(x-\alpha)\;\ge\;f(n\alpha),
&\qquad
f(x+\alpha)\;\le\;f\bigl((n+1)\alpha\bigr),
\\
f(x)\;\le\;f(n\alpha).
\end{aligned}
\]
Therefore
\[
\frac{f(x - \alpha) - f(x + \alpha)}{f(x)}
\;\ge\;
\frac{f(n\alpha) - f\bigl((n+1)\alpha\bigr)}{f(n\alpha)}
\;=\;
1 \;-\;\frac{f\bigl((n+1)\alpha\bigr)}{f(n\alpha)}.
\]
Integrating over \(x\in[n\alpha,(n+1)\alpha]\) yields
\[
\int_{n\alpha}^{(n+1)\alpha}
\frac{f(x - \alpha) - f(x + \alpha)}{f(x)}\,dx
\;\ge\;
\alpha
\Bigl(
1 - \frac{f\bigl((n+1)\alpha\bigr)}{f(n\alpha)}
\Bigr).
\]

---

## 2. Summing over blocks

Summing the above estimate for \(n=1,2,\dots,N\) gives
\[
\int_{\alpha}^{(N+1)\alpha}
\frac{f(x - \alpha) - f(x + \alpha)}{f(x)}\,dx
\;\ge\;
\alpha
\sum_{n=1}^N
\Bigl(
1 - \frac{f\bigl((n+1)\alpha\bigr)}{f(n\alpha)}
\Bigr).
\]
Set
\[
c_n \;=\;\frac{f\bigl((n+1)\alpha\bigr)}{f(n\alpha)},
\qquad
\delta_n \;=\;1 - c_n.
\]
Since \(f\) is strictly decreasing,
\[
0 < c_n < 1,
\quad
\delta_n>0,
\]
and the sum on the right becomes
\[
\sum_{n=1}^N \delta_n.
\]

---

## 3. Infinite product → infinite sum

Observe the telescoping product
\[
\prod_{n=1}^N c_n
\;=\;
\prod_{n=1}^N
\frac{f\bigl((n+1)\alpha\bigr)}{f(n\alpha)}
\;=\;
\frac{f\bigl((N+1)\alpha\bigr)}{f(\alpha)}.
\]
As \(N\to\infty\), \(f\bigl((N+1)\alpha\bigr)\to0\), so
\(\displaystyle\prod_{n=1}^\infty c_n=0\).
A standard fact about infinite products of numbers in \((0,1)\) is that
\[
\prod_{n=1}^\infty c_n = 0
\quad\Longleftrightarrow\quad
\sum_{n=1}^\infty (1 - c_n) = \sum_{n=1}^\infty \delta_n = \infty.
\]
Hence
\[
\sum_{n=1}^N \delta_n \;\longrightarrow\; +\infty
\quad\text{as }N\to\infty.
\]

---

## 4. Conclusion

Putting the above estimates together, we get
\[
\int_{\alpha}^{(N+1)\alpha}
\frac{f(x - \alpha) - f(x + \alpha)}{f(x)}\,dx
\;\ge\;
\alpha
\sum_{n=1}^N \delta_n
\;\longrightarrow\;
+\infty
\quad(N\to\infty).
\]
Therefore the original improper integral diverges to \(+\infty\):
\[
\boxed{
\int_{\alpha}^{\infty}
\frac{f(x - \alpha) - f(x + \alpha)}{f(x)}\,dx
\;=\;\infty.
}
\]
```