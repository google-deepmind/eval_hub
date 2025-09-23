This step is worth 7 points.
First, we calculate the following integral:
$$I_n:=\int_0^{\pi/2}\sin^n(x)\ dx.$$
Integrating by parts, we get
$$
\begin{aligned}
&\int_0^{\pi/2}\sin^n dx=\int_0^{\pi/2}\sin^{n-1}x \ d(-\cos x)=\\
&=-\sin^{n-1}x\cos x\bigg|_0^{\pi/2}+(n-1)\int_0^{\pi/2}\sin^{n-2}x\cos^2 x\ dx=\\
&=(n-1)\int_0^{\pi/2}\sin^{n-2}x(1-\sin^2 x\ dx=\\
&=(n-1)\int_0^{\pi/2}\sin^{n-2}x dx -(n-1)\int_0^{\pi/2}\sin^n x\ dx.
\end{aligned}
$$
Thus
$$
I_n=\int_0^{\pi/2}\sin^n dx=\frac{n-1}{n}\int_0^{\pi/2}\sin^{n-1}\ dx=\frac{n-1}{n}I_{n-2}
$$
with
$$
I_0=\int_0^{\pi/2}dx=\frac{\pi}{2} \text{ and }I_1=\int_0^{\pi/2}\sin(x)\ dx=1.
$$
Consequently, we get
$$
I_n=
\begin{cases}
\frac{(n-1)!!}{n!!}\cdot \frac{\pi}{2}, & \text{if } n \text{ is even,} \\
\frac{(n-1)!!}{n!!}, & \text{if } n \text{ is odd.}
\end{cases}
$$

This step is worth 3 points.
Since
$$
e^x=\sum_{k=0}^{\infty}\frac{x^k}{k!},
$$
it follows that
$$
\begin{aligned}
\int_0^{\pi/2}e^{\sin x}\ dx&=\int_0^{\pi/2}\sum_{k=0}^{\infty}\frac{(\sin x)^k}{k!}\ dx=\\&=\sum_{k=0}^{\infty}\frac{1}{k!}\int_0^{\pi/2}\sin^k x\ dx=
\frac{\pi}{2}+\sum_{k=1}^{\infty} \frac{I_k}{k!}=\\
&=\frac{\pi}{2}+\sum_{k=1}^{\infty} \frac{I_{2k}}{(2k)!}+\sum_{k=1}^{\infty} \frac{I_{2k-1}}{(2k-1)!}=\\
&=\frac{\pi}{2}+\sum_{k=1}^{\infty}\frac{(2k-1)!!}{(2k)!(2k)!!}\frac{\pi}{2}+\sum_{k=1}^{\infty}\frac{(2k-2)!!}{(2k-1)!(2k-1)!!}=\\
&=\frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{(2k-1)!!}{(2k)!(2k)!!}\right)+\sum_{k=0}^{\infty}\frac{(2k)!!}{(2k+1)!(2k+1)!!}.
\end{aligned}
$$
