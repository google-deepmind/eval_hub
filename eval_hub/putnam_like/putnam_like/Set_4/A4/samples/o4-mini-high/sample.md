```markdown
**Solution.**

Let \(p>2\) be a prime divisor of 
\[
a^{2^k} + b^{2^k}.
\]
Since \(\gcd(a,b)=1\), we have \(\gcd(a,p)=\gcd(b,p)=1\), so \(a\) and \(b\) are invertible modulo \(p\).  Set
\[
g \;\equiv\; a\,b^{-1} \pmod p.
\]
Then
\[
g^{2^k}
\;\equiv\;
a^{2^k} \,b^{-2^k}
\;\equiv\;
-1
\pmod p.
\]
Squaring both sides gives
\[
g^{2^{k+1}}
\equiv(-1)^2\equiv1\pmod p,
\]
and since \(g^{2^k}\not\equiv1\pmod p\), the order of \(g\) in \((\mathbb Z/p\mathbb Z)^\times\) is exactly \(2^{k+1}\).  By Fermat’s little theorem this order must divide \(p-1\), so
\[
2^{k+1}\;\Bigm|\;p-1.
\]
Hence we can write
\[
p-1 \;=\; 2^d\,m,
\]
where \(d \ge k+1\) and \(m\) is an odd positive integer.  Equivalently,
\[
\boxed{p = 2^d m + 1, \quad d\ge k+1,\; m\text{ odd}.}
\]
This completes the proof.
```