```markdown
# Solution

We want to evaluate the limit

\[
L \;=\;\lim_{n\to\infty} \frac{1}{n^2}\sum_{k=1}^n\sum_{l=1}^k e^{l/k}.
\]

---

## 1. Rewriting as a Riemann sum

Set
\[
S_n \;=\; \frac{1}{n^2}\sum_{k=1}^n\sum_{l=1}^k e^{l/k}.
\]
Observe that
\[
S_n
=\sum_{k=1}^n \frac{k}{n^2}\,
 \Bigl(\frac{1}{k}\sum_{l=1}^k e^{l/k}\Bigr).
\]
Note that for each fixed large \(k\),
\[
\frac{1}{k}\sum_{l=1}^k e^{l/k}
\;\longrightarrow\;
\int_{0}^{1} e^x\,dx
\;=\; e-1.
\]
Also we rewrite
\[
\frac{k}{n^2}
=\frac{1}{n}\,\frac{k}{n},
\]
so that as \(n\to\infty\), the sum
\[
S_n
\approx \sum_{k=1}^n \bigl(e-1\bigr)\,\frac{k}{n}\,\frac{1}{n}
\;\longrightarrow\;
(e-1)\int_{0}^{1}t\,dt
=\frac{e-1}{2}.
\]

---

## 2. Conclusion

Hence the desired limit is

\[
\boxed{
\lim_{n\to\infty} \frac{1}{n^2}\sum_{k=1}^n\sum_{l=1}^k e^{l/k}
\;=\;
\frac{e-1}{2}.
}
\]
```