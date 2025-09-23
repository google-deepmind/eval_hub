```markdown
**Solution**

Let \(A_k\) be the event that Maria chooses box \(k\).  Since she picks a box uniformly at random,
\[
\Pr(A_k)=\frac1{2025},\quad k=0,1,\dots,2024.
\]
In box \(k\) there are \(k\) white balls and \(2024-k\) black balls, so the probability of drawing a white ball in one draw (with replacement) is
\[
\frac{k}{2024}.
\]
Thus, given \(A_k\), the probability of drawing three white balls in a row is
\[
\Bigl(\tfrac{k}{2024}\Bigr)^3.
\]
By the law of total probability,
\[
P(\text{3 white}) \;=\;\sum_{k=0}^{2024}\Pr(A_k)\,\Pr(\text{3 white}\mid A_k)
\;=\;\frac1{2025}\sum_{k=0}^{2024}\Bigl(\tfrac{k}{2024}\Bigr)^3.
\]
We use the identity \(\sum_{k=0}^N k^3=\bigl(\tfrac{N(N+1)}2\bigr)^2\) with \(N=2024\):
\[
\sum_{k=0}^{2024}k^3
=\Bigl(\frac{2024\cdot2025}{2}\Bigr)^2.
\]
Hence
\[
\sum_{k=0}^{2024}\Bigl(\tfrac{k}{2024}\Bigr)^3
=\frac{1}{2024^3}\sum_{k=0}^{2024}k^3
=\frac{1}{2024^3}\,\Bigl(\frac{2024\cdot2025}{2}\Bigr)^2
=\frac{2025^2}{4\cdot2024}.
\]
Therefore
\[
P(\text{3 white})
=\frac1{2025}\,\frac{2025^2}{4\cdot2024}
=\frac{2025}{4\cdot2024}
=\frac{2025}{8096}.
\]
So the desired probability is
\[
\boxed{\frac{2025}{8096}\approx0.2501.}
\]
```