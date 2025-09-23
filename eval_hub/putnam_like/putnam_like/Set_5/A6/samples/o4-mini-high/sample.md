**Solution.**  

Parametrize points on the positive branch of the rectangular hyperbola 
\[
\mathcal H\colon y=\frac1x,\quad x>0
\]
by 
\[
P=(p,1/p),\quad Q=(q,1/q),\quad p,q>0,\;p\neq q.
\]
The slope of the tangent at \((x,y)\) is \(y'=-1/x^2\).  Hence the equations of the tangents at \(P\) and \(Q\) are
\[
\begin{cases}
y-\tfrac1p=-\tfrac1{p^2}(x-p),
\\
y-\tfrac1q=-\tfrac1{q^2}(x-q).
\end{cases}
\]
A little algebra shows their intersection
\[
R=(x_R,y_R)
\;=\;
\Bigl(\tfrac{2pq}{p+q},\;\tfrac{2}{p+q}\Bigr).
\]

We wish to compute the circum‑radius of \(\triangle PQR\).  One convenient form is
\[
r=\frac{abc}{4\triangle},
\]
where \(a=|QR|\), \(b=|RP|\), \(c=|PQ|\) and \(\triangle\) is the area of \(PQR\).  After a straightforward (but somewhat lengthy) computation one finds

\[
r(p,q)
=\frac{\sqrt{\,(p^4+1)\,(q^4+1)\,(p^2q^2+1)\,}}
     {2\,p\,q\,(p+q)}\,. 
\tag{$*$}
\]

We now show
\[
\inf_{p\neq q>0}r(p,q)
=\inf_{p>0}\lim_{q\to p}r(p,q)
=\min_{p>0}\frac{(p^4+1)^{3/2}}{4p^3}.
\]
Indeed, as \(q\to p\) the triangle becomes “infinitesimally thin’’ and one checks
\[
\lim_{q\to p}r(p,q)
=\frac{(p^4+1)^{3/2}}{4p^3}.
\]
Finally, to minimize
\[
R_0(p)=\frac{(p^4+1)^{3/2}}{4p^3},\quad p>0,
\]
set
\[
\ln R_0(p)
=\tfrac32\ln(p^4+1)-3\ln p-\ln4,
\]
so
\[
\frac{d}{dp}\ln R_0
=\frac{6p^3}{p^4+1}-\frac3p
\;\overset!=\;0
\;\Longrightarrow\;
p^4=1
\;\Longrightarrow\;
p=1.
\]
At \(p=1\) one finds
\[
R_0(1)=\frac{(1^4+1)^{3/2}}{4\cdot1^3}
=\frac{2^{3/2}}4
=\frac{\sqrt2}{2}.
\]
One checks moreover that for every fixed \(p\neq1\) one has \(R_0(p)>R_0(1)\), and for every \(p\neq q\) the exact radius \((*)\) is strictly above its limiting value as \(q\to p\).  Hence the infimum of \(r(p,q)\) (over all \(p\neq q>0\)) is exactly
\[
\boxed{\inf_{P,Q}r(P,Q)=\frac{\sqrt2}{2}.}
\]