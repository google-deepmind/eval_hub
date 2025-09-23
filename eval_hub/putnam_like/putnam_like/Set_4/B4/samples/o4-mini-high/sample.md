```markdown
**Solution.**  
We use spherical coordinates in \(\R^n\).  Writing \(x = r\,\omega\) with \(r\ge0\) and \(\omega\in S^{n-1}\), the volume element is \(dx=r^{n-1}dr\,d\sigma(\omega)\), and
\[
\int_{B(0,1)}|x_1|^{2k}\,dx
\;=\;
\int_0^1\!\int_{S^{n-1}}|r\,\omega_1|^{2k}\,r^{n-1}\,d\sigma(\omega)\,dr
\;=\;\Bigl(\int_0^1r^{2k+n-1}dr\Bigr)\,
\Bigl(\int_{S^{n-1}}|\omega_1|^{2k}d\sigma(\omega)\Bigr).
\]

1. **Radial integral.**  
\[
\int_0^1r^{2k+n-1}\,dr \;=\;\frac1{2k+n}\,. 
\]

2. **Angular integral.**  
By symmetry each coordinate of \(\omega\) is equidistributed, so
\[
\int_{S^{n-1}}|\omega_1|^{2k}\,d\sigma(\omega)
=\omega_n\;\E\bigl[|\omega_1|^{2k}\bigr],
\]
where \(\omega_n=|S^{n-1}|\).  A standard fact (or Beta‐function calculation) shows
\[
\E\bigl[|\omega_1|^{2k}\bigr]
=\frac{B(\tfrac12+k,\;\tfrac{n-1}2)}{B(\tfrac12,\;\tfrac{n-1}2)}.
\]
Using the recurrence
\(\;B(a+1,b)=\tfrac{a}{\,a+b\,}\,B(a,b)\),
one obtains
\[
\frac{B(\tfrac12+k,\;\tfrac{n-1}2)}{B(\tfrac12,\;\tfrac{n-1}2)}
\;=\;
\prod_{j=0}^{k-1}\frac{\tfrac12+j}{\tfrac n2+j}
\;=\;
\prod_{j=0}^{k-1}\frac{2j+1}{\,n+2j\,}
\;\ge\;
\prod_{j=0}^{k-1}\frac1n
\;=\;
\frac1{n^k}.
\]

3. **Conclusion.**  
Combining the two pieces,
\[
\int_{B(0,1)}|x_1|^{2k}\,dx
=\frac1{2k+n}\;\omega_n\;
\frac{B(\tfrac12+k,\tfrac{n-1}2)}{B(\tfrac12,\tfrac{n-1}2)}
\;\ge\;
\frac{\omega_n}{n^k\,(2k+n)}.
\]
This proves the desired inequality.
```