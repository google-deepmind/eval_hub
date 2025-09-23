```markdown
**Solution.**

Label the boxes \(1,2,\dots,n\).  Fix \(m\) and write
\[
M=\sum_{k=1}^m k=\frac{m(m+1)}2.
\]
Let \(P_r(i)\) be the probability that the ball drawn from box \(r\) has label \(i\).  Initially in box \(1\) there are \(k\) balls labeled \(k\), so
\[
P_1(i)=\frac{i}{M}\,.
\]
When one moves the ball from box \(r-1\) into box \(r\), box \(r\) acquires exactly one extra ball (the one just transferred), so at the time of drawing from box \(r\) the total number of balls in box \(r\) is \(M+1\), and its count of label \(i\) is
\[
\bigl(\text{initially }i\bigr)\;+\;\bigl[\text{incoming ball has label }i\bigr],
\]
whence
\[
P_r(i)
=\mathbb{E}\!\Bigl[\frac{i+\mathbf1_{\{\text{prev.\ ball}=i\}}}{M+1}\Bigr]
=\frac{i+P_{r-1}(i)}{M+1}\,.
\]
One checks by induction that
\[
P_r(i)=\frac{i}{M}
\quad\text{for all }r\ge1.
\]
Hence the final draw (from box \(n\)) has
\[
\Pr\{\,\text{label}=i\}=\frac{i}{M},
\]
and its expectation is
\[
\mathbb{E}[X]
=\sum_{i=1}^m i\cdot\frac{i}{M}
=\frac{1}{M}\sum_{i=1}^m i^2
=\frac{\frac{m(m+1)(2m+1)}6}{\frac{m(m+1)}2}
=\frac{2m+1}{3}\,.
\]
Therefore \(\mathbb{E}[X]\) is an integer precisely when
\[
\frac{2m+1}{3}\in\mathbb{Z}
\quad\Longleftrightarrow\quad
2m+1\equiv0\pmod3
\quad\Longleftrightarrow\quad
m\equiv1\pmod3.
\]
```

**Answer.** The expected value is
\[
\mathbb{E}[X]=\frac{2m+1}{3},
\]
which is an integer exactly when 
\[
m\equiv1\pmod3.
\]
