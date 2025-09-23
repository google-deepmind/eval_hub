```markdown
**Solution.**

We want to compute
\[
S_n \;=\;\sum_{k=1}^n \sin\!\Bigl(\tfrac{\pi}{2}\,\frac{n+2k-1}{n(n-1)}\Bigr).
\]
Define
\[
a \;=\;\frac{\pi}{2\,n(n-1)},\qquad
\beta \;=\;2a \;=\;\frac{\pi}{n(n-1)},\qquad
\alpha \;=\;a\,(n+1).
\]
Then the \(k\)th term can be rewritten as
\[
\sin\!\Bigl(\tfrac\pi2\frac{n+2k-1}{n(n-1)}\Bigr)
=\sin\!\bigl(a\,(n-1+2k)\bigr)
=\sin\!\bigl(\alpha+(k-1)\beta\bigr).
\]
Hence by the standard finite‐arithmetic‐progression formula for sine,
\[
S_n
=\sum_{k=1}^n \sin\!\bigl(\alpha+(k-1)\beta\bigr)
=\frac{\sin\!\bigl(\tfrac{n\beta}{2}\bigr)\,
       \sin\!\bigl(\alpha+\tfrac{(n-1)\beta}{2}\bigr)}
     {\sin\!\bigl(\tfrac{\beta}{2}\bigr)}.
\]
A quick calculation shows
\[
\frac{n\beta}{2} \;=\;\frac{\pi}{2(n-1)},\qquad
\alpha+\frac{(n-1)\beta}{2} \;=\;\frac{\pi}{n-1},\qquad
\frac{\beta}{2} \;=\;\frac{\pi}{2\,n(n-1)}.
\]
Hence the exact closed form is
\[
S_n
=\frac{\sin\!\bigl(\tfrac\pi{2(n-1)}\bigr)\,\sin\!\bigl(\tfrac\pi{n-1}\bigr)}
     {\sin\!\bigl(\tfrac\pi{2n(n-1)}\bigr)}.
\]
As \(n\to\infty\) all of the sine‐arguments go to zero, and using 
\(\sin x\sim x\) for small \(x\) we get
\[
S_n\;\sim\;\frac{\bigl(\frac\pi{2(n-1)}\bigr)\,
               \bigl(\frac\pi{\,n-1\,}\bigr)}
              {\frac\pi{2\,n(n-1)}}
\;=\;\pi\,\frac{n}{\,n-1\,}
\;\longrightarrow\;\pi.
\]
Therefore,
\[
\boxed{
\lim_{n\to\infty}\sum_{k=1}^n
\sin\!\Bigl(\tfrac{\pi}{2}\,\frac{n+2k-1}{n(n-1)}\Bigr)
\;=\;\pi.
}
\]
```