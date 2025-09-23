```markdown
**Proof.**  
We start by representing the factor \(\frac1{(k+1)^3}\) as a triple integral.  Indeed for any integer \(k\ge0\),  
\[
\frac1{(k+1)^3}
=\int_0^1\!\int_0^1\!\int_0^1 x^k y^k z^k \,dx\,dy\,dz.
\]
Hence
\[
\sum_{k=0}^n\binom nk\frac{(-1)^k}{(k+1)^3}
=\int_0^1\!\int_0^1\!\int_0^1
\sum_{k=0}^n\binom nk(-1)^k(xyz)^k
\,dx\,dy\,dz
=\int_0^1\!\int_0^1\!\int_0^1(1-xyz)^n\,dx\,dy\,dz.
\]
Next we do the \(x\)–integral in closed form.  For any fixed \(y,z\in(0,1)\),
\[
\int_0^1(1-xyz)^n\,dx
=\left[-\frac{(1-xyz)^{n+1}}{yz\,(n+1)}\right]_{x=0}^1
=\frac{1-(1-yz)^{n+1}}{(n+1)\,yz}.
\]
Therefore
\[
\sum_{k=0}^n\binom nk\frac{(-1)^k}{(k+1)^3}
=\frac1{n+1}
\int_0^1\!\int_0^1\frac{1-(1-yz)^{n+1}}{yz}
\,dy\,dz.
\]
We split this as the difference of two iterated integrals,
\[
\frac1{n+1}
\Bigl[
\underbrace{\int_0^1\!\int_0^1\frac{dy\,dz}{yz}}_{=\infty}
\;-\;\int_0^1\!\int_0^1\frac{(1-yz)^{n+1}}{yz}\,dy\,dz
\Bigr].
\]
Both pieces diverge, but their difference is finite.  To see this, expand the second integrand by the binomial theorem,
\[
\frac{(1-yz)^{n+1}}{yz}
=\sum_{m=0}^{n+1}\binom{n+1}{m}(-1)^m\,(yz)^{m-1}.
\]
Hence
\[
\int_0^1\!\int_0^1\frac{(1-yz)^{n+1}}{yz}\,dy\,dz
=\sum_{m=0}^{n+1}\binom{n+1}{m}(-1)^m
\Bigl(\int_0^1y^{m-1}dy\Bigr)\Bigl(\int_0^1z^{m-1}dz\Bigr).
\]
For \(m\ge1\) each inner integral equals \(1/m\), while the term \(m=0\)
is exactly the same divergent \(\int_0^1\!\int_0^1(yz)^{-1}dy\,dz\).  Hence
\[
\int_0^1\!\int_0^1\frac{1-(1-yz)^{n+1}}{yz}\,dy\,dz
=\sum_{m=1}^{n+1}(-1)^{m-1}\binom{n+1}{m}\frac1{m^2}.
\]
Putting everything together,
\[
\sum_{k=0}^n\binom nk\frac{(-1)^k}{(k+1)^3}
=\frac1{n+1}
\sum_{m=1}^{n+1}(-1)^{m-1}\binom{n+1}{m}\frac1{m^2}.
\]
On the other hand, observe that
\[
\frac1{n+1}\sum_{k=0}^n\sum_{j=0}^k\frac1{(k+1)(j+1)}
=\frac1{n+1}\sum_{m=1}^{n+1}\sum_{\ell=1}^{m}\frac1{m\,\ell}
=\frac1{n+1}\sum_{m=1}^{n+1}\frac{H_m}{m},
\]
where \(H_m=\sum_{\ell=1}^m1/\ell\) is the \(m\)th harmonic number.  A standard binomial–harmonic identity shows
\[
\sum_{m=1}^{n+1}(-1)^{m-1}\binom{n+1}{m}\frac1{m^2}
=\sum_{m=1}^{n+1}\frac{H_m}{m}.
\]
Thus the two expressions coincide, and the claim follows.  
\(\boxed{}\)
```