Below is one acceptable solution. (Any sequence of centers that are “spread out enough” will work.)

Recall that we wish to choose a sequence \(\{z_n\}\subset\mathbb{R}^2\) so that

1. The balls
\[
B(z_n,1/n)=\{x\in\mathbb{R}^2:|x-z_n|<1/n\}
\]
are pairwise disjoint (that is, if \(n\neq m\) then
\[
B(z_n,1/n)\cap B(z_m,1/m)=\emptyset);
\]
2. For every continuous function \(\varphi:\mathbb{R}^2\to\mathbb{R}\) (or—if you prefer—every bounded or compactly supported continuous function) we have
\[
\frac{n}{\pi}\int_{B(z_n,1/n)}\varphi(x)\,dx\to0\quad\text{as }n\to\infty.
\]

Observe that the area of the ball \(B(z_n,1/n)\) is
\[
|B(z_n,1/n)|=\pi\Bigl(\frac1{n}\Bigr)^2=\frac{\pi}{n^2}\,.
\]
Thus if \(\varphi\) is bounded with, say, \(|\varphi(x)|\le M\) for all \(x\) then
\[
\Bigl|\frac{n}{\pi}\int_{B(z_n,1/n)}\varphi(x)\,dx\Bigr|\le \frac{n}{\pi}\, M\,\frac{\pi}{n^2}=\frac{M}{n}\,,
\]
which tends to \(0\) as \(n\to\infty\). (Also, if \(\varphi\) has compact support we may choose \(z_n\) to eventually lie outside of the support so that the integral is identically zero for large \(n\); in any event the factor \(1/n\) in front always forces the limit to be \(0\) when the integral over \(B(z_n,1/n)\) is controlled.)

Thus the only “non‐trivial” requirement is to have the balls \(B(z_n,1/n)\) be disjoint. One way to do this is to choose the centers so that
\[
|z_n-z_m|\ge \frac{1}{n}+\frac{1}{m}\quad\text{for all }n\neq m\,.
\]

An explicit example is given by the sequence

\[
z_n=\Biggl(\sum_{k=1}^{n}\Bigl(\frac{1}{k}+\frac{1}{k+1}\Bigr),\,0\Biggr),\quad n\ge1\,.
\]

A brief justification that the balls are disjoint is as follows. Notice that
\[
|z_{n+1}-z_n|=\frac{1}{n+1}+\frac{1}{n+2}\,,
\]
and more generally one may check by induction that for \(n<m\)
\[
|z_m-z_n|\ge \frac{1}{n}+\frac{1}{m}\,.
\]
Thus, in view of the fact that the radius of \(B(z_n,1/n)\) is \(1/n\), one readily deduces that if \(n\neq m\)
\[
B(z_n,1/n)\cap B(z_m,1/m)=\emptyset\,.
\]

Finally, for any bounded (or compactly supported) continuous function \(\varphi\) we then have
\[
\frac{n}{\pi}\int_{B(z_n,1/n)}\varphi(x)\,dx\to0
\]
as \(n\to\infty,\) since, as we saw, even in the worst‐case scenario
\[
\Bigl|\frac{n}{\pi}\int_{B(z_n,1/n)}\varphi(x)\,dx\Bigr|\le \frac{M}{n}\,.
\]

Thus, the answer is: Yes, such a sequence exists; for example, one may take

\[
\boxed{z_n=\left(\sum_{k=1}^{n}\Bigl(\frac{1}{k}+\frac{1}{k+1}\Bigr),\,0\right).}
\]

Any sequence of centers that is “sparse enough” to guarantee the disjointness of the balls will work, and the scaling factor \(n/\pi\) always ensures that
\[
\frac{n}{\pi}\int_{B(z_n,1/n)}\varphi(x)\,dx\to0
\]
for every bounded (or compactly supported) continuous function \(\varphi\).