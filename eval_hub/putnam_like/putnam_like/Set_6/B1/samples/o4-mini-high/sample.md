```markdown
# Solution

Number the grid so that the cell in row \(i\) and column \(j\) has the label
\[
a_{i,j} \;=\;(j-1)\,2n \;+\; i,
\qquad 1\le i,j\le 2n.
\]
Let
\[
x_{i,j} =
\begin{cases}
1, &\text{if the cell \((i,j)\) is black},\\
0, &\text{otherwise}.
\end{cases}
\]
The condition “half the cells in each row and column are black” reads
\[
\sum_{i=1}^{2n} x_{i,j} = n\quad (\forall j),
\qquad
\sum_{j=1}^{2n} x_{i,j} = n\quad (\forall i).
\]
The total sum of the black‐cell labels is
\[
S \;=\;\sum_{i=1}^{2n}\sum_{j=1}^{2n} x_{i,j}\,a_{i,j}
\;=\;\sum_{i,j}x_{i,j}\bigl((j-1)2n + i\bigr)
=\;2n\sum_{j=1}^{2n}(j-1)\sum_{i=1}^{2n}x_{i,j}
\;+\;\sum_{i=1}^{2n}i\sum_{j=1}^{2n}x_{i,j}.
\]
Since each column has exactly \(n\) black cells and each row has exactly \(n\) black cells, we get
\[
S
=2n\sum_{j=1}^{2n}(j-1)\,n
\;+\; \sum_{i=1}^{2n}i\,n
=2n^2\bigl(0+1+\cdots+(2n-1)\bigr)
\;+\;n\bigl(1+2+\cdots+2n\bigr).
\]
Compute the sums of the first few integers:
\[
0+1+\cdots+(2n-1)=\frac{2n(2n-1)}2,
\qquad
1+2+\cdots+2n=\frac{2n(2n+1)}2.
\]
Hence
\[
S
=2n^2\cdot\frac{2n(2n-1)}2
\;+\;n\cdot\frac{2n(2n+1)}2
=\;n^2(4n^2+1).
\]
Therefore **every** valid coloring has the same total. In particular the minimal and maximal possible sums of all black‐cell labels are
\[
\boxed{n^2(4n^2+1)}.
\]
```