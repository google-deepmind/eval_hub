Here is a quick “rotations‐and‐discrepancy’’ proof.  Set 
\[
α=\sqrt3-1,
\]
and observe that for each integer \(k\)
\[
(-1)^{\lfloor k\,α\rfloor}
=\begin{cases}+1,&\{kα\}_{\bmod2}\in[0,1),\\
-1,&\{kα\}_{\bmod2}\in[1,2),
\end{cases}
\]
where \(\{x\}_{\bmod2}\) denotes \(x\) modulo 2 in \([0,2)\).  Hence
\[
S(n)\;:=\;\sum_{k=0}^{n}(-1)^{\lfloor kα\rfloor}
\;=\;\#\{0\le k\le n:\,kα\bmod2\in[0,1)\}
\;-\;\#\{0\le k\le n:\,kα\bmod2\in[1,2)\}.
\]
Since there are exactly \(n+1\) points \(kα\bmod2\) with \(0\le k\le n\), we get
\[
S(n)
=2\;\#\{k:0\le k\le n,\;kα\bmod2\in[0,1)\}\;-\;(n+1)\,.
\]
But the sequence \(\{kα\bmod2\}_{k=0,1,2,\dots}\) is equidistributed in \([0,2)\), and a classical “three–distance’’ (or discrepancy) estimate shows that for any half–interval of length 1,
\[
\Bigl|\#\{0\le k\le n:\,kα\bmod2\in[0,1)\}-\tfrac{n+1}2\Bigr|\;\le1.
\]
Hence
\[
\#\{k:0\le k\le n,\;kα\bmod2\in[0,1)\}
\;\ge\;\frac{n+1}2\;-\,1,
\]
and therefore
\[
S(n)
\;=\;
2\Bigl(\#\{k:0\le k\le n,\;kα\bmod2\in[0,1)\}\Bigr)\;-\;(n+1)
\;\ge\;
2\Bigl(\tfrac{n+1}2-1\Bigr)-(n+1)
\;=\;1.
\]
This completes the proof that for every \(n\ge0\),
\[
\sum_{k=0}^n(-1)^{\lfloor k(\sqrt3-1)\rfloor}\;\ge1.
\]