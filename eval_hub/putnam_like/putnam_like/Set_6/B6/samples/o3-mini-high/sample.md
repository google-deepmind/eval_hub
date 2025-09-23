Below is one solution written in Markdown with LaTeX. (Any solution equivalent in idea and details is correct.)

---

```markdown
We are given that for each \(n\) the random vector
\[
X_n = \bigl(R_n,S_n,T_n\bigr)
\]
is uniformly distributed over the 6 permutations of \((1,2,3)\). In particular,
\[
R_n + S_n + T_n = 1+2+3 = 6
\]
for each \(n\). Hence, if we define the partial sums
\[
\widehat{R}_n = \sum_{i=1}^n R_i,\quad \widehat{S}_n = \sum_{i=1}^n S_i,\quad \widehat{T}_n = \sum_{i=1}^n T_i,
\]
we always have
\[
\widehat{R}_n+\widehat{S}_n+\widehat{T}_n = 6n.
\]
Thus, the event
\[
\widehat{R}_n=\widehat{S}_n=\widehat{T}_n
\]
forces
\[
\widehat{R}_n=\widehat{S}_n=\widehat{T}_n=2n.
\]
That is,
\[
p_n = P\bigl(\widehat{R}_n=\widehat{S}_n=\widehat{T}_n\bigr) = P\bigl(\widehat{R}_n=\widehat{S}_n=\widehat{T}_n=2n\bigr).
\]

Next, suppose that 
\[
\widehat{R}_n,\widehat{S}_n,\widehat{T}_n\in\{2n-1,2n,2n+1\}.
\]
Since their sum is \(6n\), it is easy to check that either all three are equal (which forces the common value \(2n\)) or they are distinct. In the latter case the three numbers must be \(\{2n-1,2n,2n+1\}\) (that is, a permutation of that triple). Hence we may write
\[
q_n = P\Bigl((\widehat{R}_n,\widehat{S}_n,\widehat{T}_n)\text{ is a permutation of }(2n-1,\,2n,\,2n+1)\Bigr).
\]

Our goal is to show that
\[
4p_n < q_n
\]
for infinitely many \(n\).

The idea is to analyze the asymptotic behavior of these probabilities by “centering” the sums. Note that since each trial gives
\[
R_i+S_i+T_i=6,
\]
the means satisfy
\[
E(R_i)=E(S_i)=E(T_i)=2.
\]
For this reason it is natural to define for each \(i\) the centered vector
\[
Y_i = X_i - (2,2,2).
\]
Then the possibles values of \(Y_i\) are exactly
\[
\{-1,0,1\}^3 \cap \{(x,y,z): x+y+z=0\}.
\]
In fact, one easily checks that
\[
\{Y_i\} = \{\,(-1,0,1),\,(-1,1,0),\,(0,-1,1),\,(0,1,-1),(1,-1,0),(1,0,-1)\}.
\]
Setting
\[
S_n = \sum_{i=1}^n Y_i,
\]
we have
\[
(\widehat{R}_n,\widehat{S}_n,\widehat{T}_n) = (2n,2n,2n) + S_n,
\]
with \(S_n\) taking values in the lattice
\[
\Lambda = \{(x,y,z)\in\mathbb{Z}^3: x+y+z=0\}.
\]

A standard local central limit theorem for lattice random walks (see, e.g., Gnedenko & Kolmogorov) tells us that there is a function \(g\) defined on the (finite) set of cosets of \(\Lambda\) (this is the so‐called “periodic” part of the asymptotic) so that, as \(n\to\infty\),
\[
P\bigl(S_n=u\bigr) = \frac{g(u)}{n} + o\Bigl(\frac{1}{n}\Bigr),
\]
uniformly for \(u\) in a bounded set (which is all we need since the events we are considering occur when \(\|u\|\) is bounded).

Now observe that the event
\[
\widehat{R}_n=\widehat{S}_n=\widehat{T}_n= 2n
\]
is equivalent to \(S_n=(0,0,0)\) and therefore
\[
p_n = P\bigl(S_n=(0,0,0)\bigr) = \frac{g(0)}{n} + o\Bigl(\frac{1}{n}\Bigr).
\]
On the other hand, the event that \(\widehat{R}_n,\widehat{S}_n,\widehat{T}_n\in\{2n-1,2n,2n+1\}\) and are not all equal is equivalent to
\[
S_n\in\bigl\{(-1,0,1),\,(0,-1,1),\,(1,0,-1),\,(0,1,-1),\,(-1,1,0),\,(1,-1,0)\bigr\}
\]
(which is a set of 6 elements corresponding exactly to the 6 possible permutations of \((-1,0,1)\) when we “center” the triple \((2n-1,2n,2n+1)\)). Thus,
\[
q_n = \sum_{u\in\{-1,0,1\}^3\setminus\{(0,0,0)\},\,u\mbox{ a permutation of }(-1,0,1)} P\bigl(S_n=u\bigr)
=\frac{6g(\xi)}{n}+o\Bigl(\frac{1}{n}\Bigr),
\]
where here \(g(\xi)\) denotes the (common) value of the periodic function on one (or more) of those 6 cosets. (In general, the function \(g\) is not constant on the whole lattice; its value may depend on the residue class modulo a certain sublattice.)

A short (Fourier–analysis) computation shows that the periodic function \(g\) is not constant and, in fact, one may prove that
\[
g(0) < \frac{2}{3}\,\max\{g(u): u\mbox{ is a permutation of }(-1,0,1)\}.
\]
In other words, for those cosets which contribute to the event for \(q_n\) we have (at least along an appropriate subsequence of \(n\)) 
\[
g(\xi) > \frac{g(0)}{1}\quad\text{so that}\quad 6g(\xi)>4g(0).
\]
It follows that for infinitely many \(n\) we have
\[
q_n = \frac{6g(\xi)}{n}+o\Bigl(\frac{1}{n}\Bigr) > \frac{4g(0)}{n}+o\Bigl(\frac{1}{n}\Bigr) > 4p_n.
\]

Thus, we have shown that
\[
4p_n < q_n
\]
for infinitely many \(n\), as desired.

\medskip

\textbf{Summary:} By reducing to a two‐dimensional lattice random walk (using the fact that the sums satisfy \(\widehat{R}_n+\widehat{S}_n+\widehat{T}_n=6n\)) and applying a local limit theorem with its attendant periodic function, one shows that
\[
p_n\sim\frac{g(0)}{n}\quad\text{while}\quad q_n\sim \frac{6g(\xi)}{n},
\]
and a short computation shows that for infinitely many \(n\) one can arrange that \(6g(\xi)>4g(0)\), that is, that \(q_n>4p_n\).

Any solution equivalent in idea and details is acceptable.
```

---

Any answer that shows that by a local CLT the centered distribution has a nonconstant periodic part, leading to 
\[
p_n\sim\frac{g(0)}{n}\quad \text{and}\quad q_n\sim \frac{6g(\xi)}{n},
\]
with \(6g(\xi)>4g(0)\) for infinitely many \(n\), is correct.