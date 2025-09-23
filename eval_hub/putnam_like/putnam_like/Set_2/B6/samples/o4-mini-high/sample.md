Here is a quick proof by contour–integration in the first quadrant.  Set 
\[
f(z)\;=\;\frac{e^{iz}}{z+2}\,,
\] 
and let \(\Gamma_R\) be the boundary of the quarter‐disk in the upper‐half–plane∶  
\[ 
\Gamma_R=\Bigl[0\to R\Bigr]
\;\cup\;
\Bigl[R\to R\,i\Bigr]
\;\cup\;
\Bigl[R\,i\to0\Bigr].
\]  
Since \(f\) has no poles inside this region,  
\[
\int_{\Gamma_R}f(z)\,dz =0\,. 
\]  
As \(R\to\infty\), one checks easily that the contribution of the big circular arc tends to zero.  Hence  
\[
\int_{0}^{\infty}\frac{e^{i x}}{x+2}\,dx+\int_{i\infty}^{0}\frac{e^{iz}}{z+2}\,dz
\;=\;0.
\]  
Parameterize the second integral by \(z=i t\), \(t\!:R\to0\); then \(dz=i\,dt\), \(e^{iz}=e^{-t}\), and  
\[
\int_{i\infty}^{0}\frac{e^{iz}}{z+2}\,dz
=\int_{R}^{0}\frac{e^{-t}}{i\,t+2}\,i\,dt
\;\xrightarrow[R\to\infty]{}\;
-\int_{0}^{\infty}e^{-t}\,\frac{i}{2+ i\,t}\,dt.
\]  
But 
\[
\frac{i}{2+i t}
=\frac{i(2-i t)}{4+t^2}
=\frac{t}{\,4+t^2}+2\,\frac{i}{\,4+t^2}\,,
\] 
so splitting real and imaginary parts gives
\[
\int_{0}^{\infty}\frac{e^{i x}}{x+2}\,dx
=\int_{0}^{\infty}e^{-t}\,\frac{t}{\,4+t^2}\,dt
\;+\;i\;\int_{0}^{\infty}e^{-t}\,\frac{2}{\,4+t^2}\,dt.
\]
Taking real parts,  
\[
\int_{0}^{\infty}\frac{\cos x}{x+2}\,dx
=\int_{0}^{\infty}e^{-t}\,\frac{t}{\,t^2+4}\,dt.
\tag{1}
\]
On the other hand one checks by the elementary “Fourier–Laplace’’ identity
\[
\int_{0}^{\infty}e^{-t}\cos(x\,t)\,dt=\frac1{1+x^2},
\]
that
\[
\int_{0}^{\infty}\frac{e^{-2x}}{1+x^2}\,dx
=\int_{0}^{\infty}e^{-t}\Bigl[\!\int_{0}^{\infty}e^{-2x}\cos(tx)\,dx\Bigr]dt
=\;2\int_{0}^{\infty}\frac{e^{-t}}{\,t^2+4}\,dt.
\]
Finally, an elementary integration‐by‐parts shows
\[
2\int_{0}^{\infty}\frac{e^{-t}}{t^2+4}\,dt
\;=\;
\int_{0}^{\infty}\frac{t\,e^{-t}}{t^2+4}\,dt,
\]
and by \((1)\) this last integral is exactly \(\displaystyle\int_{0}^{\infty}\frac{\cos x}{x+2}\,dx\).  Hence 
\[
\boxed{
\int_{0}^{\infty}\frac{e^{-2x}}{1+x^2}\,dx
=\int_{0}^{\infty}\frac{\cos x}{x+2}\,dx.
}
\]