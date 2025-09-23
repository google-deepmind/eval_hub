```markdown
**Solution.**  We have a Pólya‐urn with three colors (G, R, B), one ball of each color initially.  At each move you draw a ball and return it together with one extra ball of the same color.  A well‐known fact is that under this scheme the sequence of colors is exchangeable and the **number of red draws** in \(n\) moves, say \(X\), has a **beta‐binomial** (or “Pólya”) distribution with parameters
\[
\alpha_{\rm R}=1,\quad \alpha_{\text{(others)}}=2,\quad n=90.
\]
Equivalently, one shows that  
\[
P(X=k)
=\binom{n}{k}\,\frac{B(1+k,\;2+(n-k))}{B(1,2)}
=\frac{2\,(n-k+1)}{(n+1)(n+2)}.
\]
In particular for \(n=90\) and \(k=45\)  
\[
P\{X=45\}
=\frac{2\,(90-45+1)}{(90+1)(90+2)}
=\frac{2\cdot46}{91\cdot92}
=\frac{92}{91\cdot92}
=\frac1{91}\approx0.01099.
\]

**Answer.** The required probability is
\[
\boxed{\;P(\text{45 red draws in 90 moves})=\frac1{91}.\;}
\]
```