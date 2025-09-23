```markdown
**Solution.** We shall count the number of zeros of 
\[
P(z)=z^8-5z^3+10
\]
in the closed sector 
\[
A=\bigl\{z\in\C:\tfrac\pi2\le\arg z\le\pi\bigr\}
\]
by applying the argument principle on a large truncated wedge and then letting its radii go to $0$ and $\infty$.  

1.  **The contour.**  For $0<\varepsilon\ll1\ll R$ consider the positively oriented boundary
\[
\Gamma = 
\Bigl\{Re^{i\theta}:\tfrac\pi2\le\theta\le\pi\Bigr\}
\;\cup\;
\bigl\{\varepsilon e^{i\theta}:\pi\ge\theta\ge\tfrac\pi2\bigr\}
\;\cup\;
\bigl\{re^{i\pi}:\varepsilon\le r\le R\bigr\}
\;\cup\;
\bigl\{re^{i\frac\pi2}:\,R\ge r\ge\varepsilon\bigr\}.
\]
By the argument principle, the number $N$ of zeros of $P$ in the sector is
\[
N \;=\;\frac1{2\pi}\,\Delta_{\Gamma}\!\arg P(z).
\]

2.  **Contribution of the large arc** $\;z=Re^{i\theta},\;\frac\pi2\le\theta\le\pi$.  
For $R\to\infty$, 
\[
P(z)=z^8\bigl(1+O(R^{-5})\bigr),
\]
so 
\[
\arg P(Re^{i\theta})\;=\;\arg\bigl(z^8\bigr)+o(1)
\;=\;8\,\theta +o(1).
\]
Hence as $\theta$ runs from $\pi/2$ to $\pi$, 
\[
\Delta_{\rm large\;arc}\arg P
\;=\;
8\bigl(\pi-\tfrac\pi2\bigr)
\;=\;
4\pi.
\]

3.  **Contribution of the small arc** $\;z=\varepsilon e^{i\theta},\;\pi\ge\theta\ge\pi/2$.  
For $\varepsilon\to0$, 
\[
P(z)=10\bigl(1+O(\varepsilon^3)\bigr),
\]
so $\arg P\approx0$ all along the small arc and 
\[
\Delta_{\rm small\;arc}\arg P=0.
\]

4.  **Contribution of the radial sides.**  
– On the side $\arg z=\pi$, $z=-r$, $r\in[\varepsilon,R]$, 
\[
P(-r)=r^8+5r^3+10>0,
\]
so $\arg P(-r)=0$ throughout and no net change.  
– On the side $\arg z=\frac\pi2$, $z=ir$, $r\in[\varepsilon,R]$, 
\[
P(ir)=(ir)^8-5(ir)^3+10
=r^8+5i\,r^3+10\,,
\]
whose imaginary part $5r^3$ is always positive.  Thus $P(ir)$ moves continuously in the upper half‐plane from $10$ (at $r=\varepsilon$) back to the positive real direction (as $r\to R$), so again 
\[
\Delta_{\arg z=\pi/2}\arg P=0.
\]

5.  **Total change and conclusion.**  Summing up,
\[
\Delta_{\Gamma}\arg P
=\underbrace{4\pi}_{\rm large\;arc}
+0+0+0
\;=\;4\pi,
\]
hence by the argument principle
\[
N \;=\;\frac{1}{2\pi}\,\Delta_{\Gamma}\arg P
\;=\;\frac{4\pi}{2\pi}
\;=\;2.
\]
Therefore, **\(P(z)\) has exactly \(\boxed{2}\) zeros in the sector \(\tfrac\pi2\le\arg z\le\pi\).**