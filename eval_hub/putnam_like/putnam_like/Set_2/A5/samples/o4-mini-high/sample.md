```markdown
**Solution.**

Let $n_p$ be the number of Sylow‑$p$ subgroups of $G$.  By Sylow’s theorems

1. $n_p\mid q^2$,  
2. $n_p\equiv1\pmod p$.

Since $q^2<p$ and $q^2>0$, the only divisor of $q^2$ congruent to $1\pmod p$ is $1$.  Hence there is a unique Sylow‑$p$ subgroup
\[
H\;=\;\Syl_p(G),
\]
so $|H|=p^n$ and $H\lhd G$.

It remains to show $H$ is abelian.  Note that
\[
[H,H]\;\subseteq\;H\;\cap\;[G,G].
\]
But $|H|=p^n$ and $|[G,G]|=q^2$ are relatively prime, so 
\[
H\;\cap\;[G,G]\;=\;\{1\}.
\]
Therefore 
\[
[H,H]=\{1\},
\]
i.e.\ $H$ is abelian.

Thus $H$ is a normal abelian subgroup of order $p^n$, as required.  
```