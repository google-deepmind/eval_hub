Here is a short self‐contained construction.  We will inductively place the balls 
$$B_n:=B(z_n,r_n)\,,\qquad r_n=\frac1n$$ 
inside a fixed large disk 
$$S=B(0,3)\subset\R^2$$ 
so that they remain pairwise disjoint, and then check that for every continuous $\varphi$ one has 
\[
\frac n\pi\int_{B_n}\varphi(x)\,dx\;\longrightarrow\;0\,. 
\]

---

**1. The greedy‐packing lemma.**  
Note first that 
\[
\sum_{n=1}^\infty\Area\bigl(B(z_n,2r_n)\bigr)
\;=\;\sum_{n=1}^\infty\pi(2r_n)^2
\;=\;4\pi\sum_{n=1}^\infty\frac1{n^2}
\;<\;4\pi\;\frac{\pi^2}{6}
\;=\;\frac{2\pi^3}{3}
\;<\;9\pi
\;=\;\Area(S)\,. 
\]
Hence the total area of the *dilated* balls $B(z_n,2r_n)$ is strictly less than $\Area(S)=9\pi$.

We now choose the centers $z_n\in S$ by induction:  
–  Start with $n=1$ and pick *any* $z_1\in S$.  
–  Having chosen $z_1,\dots,z_{n-1}$ so that the balls $B(z_k,2r_k)$ are disjoint and lie in $S$, set
\[
A_{n-1}\;=\;\bigcup_{k=1}^{n-1}B(z_k,2r_k)\,.
\]
Since 
\[
\Area\bigl(A_{n-1}\bigr)
\;\le\;\sum_{k=1}^{n-1}\Area\bigl(B(z_k,2r_k)\bigr)
\;<\;\sum_{k=1}^\infty\Area\bigl(B(z_k,2r_k)\bigr)
\;<\;\Area(S)\,,
\]
the set $S\setminus A_{n-1}$ is non‐empty.  Choose any
\[
z_n\;\in\;S\;\setminus\;A_{n-1}\,.
\]
By construction
\[
|z_n-z_k|\;>\;2\,r_k
\quad(k<n),
\]
and hence in particular
\[
|z_n-z_k|\;>\;r_k+r_n\,, 
\]
so that the *actual* balls $B(z_n,r_n)$ and $B(z_k,r_k)$ do not overlap.  This completes the induction and yields a sequence of **pairwise‐disjoint** balls
\[
B_n=B\bigl(z_n,\tfrac1n\bigr)\subset S\,, 
\qquad n=1,2,\dots
\]
Since $S$ is compact, the sequence $(z_n)$ has at least one accumulation point $z^*\in S$.  

---

**2. Vanishing of the integrals.**  
Fix any continuous $\varphi:\R^2\to\R$.  Since $z_n\in S$ for all $n$ and $S$ is compact, $\varphi$ is uniformly continuous and bounded on $S$.  Write
\[
M=\sup_{x\in S}|\varphi(x)|,
\qquad
\omega(\delta)
=\sup\{|\varphi(x)-\varphi(y)|:|x-y|\le\delta,\;x,y\in S\},
\]
so $\omega(\delta)\to0$ as $\delta\to0$.  Then for each $n$ and each $x\in B(z_n,r_n)$,
\[
\varphi(x)
=\varphi(z_n)+\bigl[\varphi(x)-\varphi(z_n)\bigr]
\;=\;\varphi(z_n)+O\bigl(\omega(r_n)\bigr)\,,
\]
and hence
\[
\int_{B(z_n,r_n)}\varphi(x)\,dx
\;=\;\varphi(z_n)\,\Area(B_n)
\;+\;O\bigl(\omega(r_n)\bigr)\,\Area(B_n)
\;=\;\varphi(z_n)\,\frac{\pi}{n^2}+O\!\Bigl(\omega\bigl(\tfrac1n\bigr)\frac\pi{n^2}\Bigr).
\]
Multiply by $n/\pi$ to get
\[
\frac n\pi
\int_{B(z_n,1/n)}\varphi
\;=\;\frac{\varphi(z_n)}{n}
\;+\;O\!\Bigl(\frac{\omega(1/n)}{n}\Bigr).
\]
Since $|\varphi(z_n)|\le M$ is bounded and $\omega(1/n)\to0$, the right‐hand side tends to $0$.  Hence
\[
\frac n\pi\int_{B(z_n,1/n)}\varphi(x)\,dx
\;\longrightarrow\;0,
\]
as claimed, for *every* continuous~$\varphi$.

---

**Conclusion.**  By this greedy‐packing argument we have exhibited a sequence of centers $z_n$ so that

1.  The balls $B(z_n,1/n)$ are pairwise disjoint.
2.  For every continuous $\varphi:\R^2\to\R$ one has 
   \(\displaystyle\frac n\pi\int_{B(z_n,1/n)}\varphi(x)\,dx\to0.\)

This answers the problem in the affirmative.