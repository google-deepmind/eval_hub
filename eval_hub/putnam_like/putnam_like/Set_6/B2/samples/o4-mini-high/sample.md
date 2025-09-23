```markdown
**Solution**

Let \(X_m\) be the indicator of “heads” on the \(m\)‑th coin, so 
\[
\Pr(X_m=1)=\frac1{2m+1}, 
\quad 
\Pr(X_m=0)=\frac{2m}{2m+1}.
\]
We wish to compute
\[
\Pr\bigl(\text{even number of heads}\bigr)
=\Pr\Bigl(\sum_{m=1}^n X_m\equiv0\pmod2\Bigr).
\]
A standard trick is to use the identity
\[
\Pr(\text{even}) \;=\;\frac12\Bigl(1+\mathbb{E}[(-1)^{\sum X_m}]\Bigr)
=\frac12\Bigl(1+\prod_{m=1}^n\mathbb{E}[(-1)^{X_m}]\Bigr).
\]
Since \(\mathbb{E}[(-1)^{X_m}]=1-2\Pr(X_m=1)=1-\frac{2}{2m+1}=\frac{2m-1}{2m+1}\), we get
\[
\Pr(\text{even})
=\frac12\Bigl(1+\prod_{m=1}^n\frac{2m-1}{2m+1}\Bigr).
\]
Notice the product telescopes:
\[
\prod_{m=1}^n\frac{2m-1}{2m+1}
=\frac{1\cdot3\cdot5\cdots(2n-1)}{3\cdot5\cdots(2n+1)}
=\frac1{2n+1}.
\]
Hence
\[
\Pr(\text{even number of heads})
=\frac12\Bigl(1+\frac1{2n+1}\Bigr)
=\frac{n+1}{2n+1}.
\]
```

**Answer.**  
\[
\boxed{\Pr(\text{even number of heads})=\frac{n+1}{2n+1}.}
\]