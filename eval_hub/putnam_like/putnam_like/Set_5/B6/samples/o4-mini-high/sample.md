```markdown
# Solution

Define a random subset of \(S=\{1,2,\dots,n\}\) as follows.  Let
\[
U_1,\dots,U_n\;\stackrel{\mathrm{iid}}{\sim}\;\mathrm{Unif}[0,1],
\]
and for each \(t\in[0,1]\) set
\[
A(t)\;=\;\bigl\{\,i:U_i\le t\bigr\}\subseteq S.
\]
Then for any fixed \(A\subseteq S\),
\[
\Pr\bigl(A(t)=A\bigr)
=\prod_{i\in A}\Pr(U_i\le t)\,\prod_{i\notin A}\Pr(U_i>t)
=t^{|A|}(1-t)^{\,n-|A|}.
\]
Hence
\[
\Pr\bigl(A(t)\in\mathcal F\bigr)
=\sum_{A\in\mathcal F}t^{|A|}(1-t)^{\,n-|A|}
\;=\;f(t).
\]

Now if \(0\le s<t\le1\), then
\[
A(s)=\{\,i:U_i\le s\}\;\subseteq\;\{\,i:U_i\le t\}=A(t).
\]
Since \(\mathcal F\) is *downward‐closed* (\(A\in\mathcal F\) and \(B\subset A\)
imply \(B\in\mathcal F\)), we get the implication
\[
A(t)\in\mathcal F
\quad\Longrightarrow\quad
A(s)\in\mathcal F.
\]
Therefore
\[
f(s)\;=\;\Pr\bigl(A(s)\in\mathcal F\bigr)
\;\ge\;\Pr\bigl(A(t)\in\mathcal F\bigr)
\;=\;f(t),
\]
showing that \(f\) is non‐increasing on \([0,1]\).
\(\quad\blacksquare\)
```