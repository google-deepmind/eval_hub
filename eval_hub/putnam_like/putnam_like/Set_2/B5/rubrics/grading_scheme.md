Solution step (worth 2 points):
We have
$$
\begin{aligned}
\int_0^1\int_0^z\int_0^y\frac{1}{z}\cdot\frac{1}{y}\cdot x^kdxdydz
&=\int_0^1 \frac{1}{z}\left(\int_0^z\frac{1}{y}\left(\int_0^yx^kdx\right)dy\right)dz=\\
&=\int_0^1 \frac{1}{z}\left(\int_0^z\frac{1}{y}\left(\frac{1}{k+1}\left.x^{k+1}\right|_0^y\right)dy\right)dz=\\
&=\int_0^1 \frac{1}{z}\left(\int_0^z\frac{1}{y}\left(\frac{1}{k+1}y^{k+1}\right)dy\right)dz=\\
&=\frac{1}{k+1}\int_0^1 \frac{1}{z}\left(\int_0^zy^{k}dy\right)dz=\\
&=\frac{1}{k+1}\int_0^1 \frac{1}{z}\left(\frac{1}{k+1}\left.y^{k+1}\right|_0^z\right)dz=\\
&=\frac{1}{k+1}\int_0^1 \frac{1}{z}\left(\frac{1}{k+1}z^{k+1}\right)dz=\\
&=\frac{1}{(k+1)^2}\int_0^1 z^{k}dz\\
&=\frac{1}{(k+1)^2}\left(\frac{1}{k+1}\left.z^{k+1}\right|_0^1\right)=\\
&=\frac{1}{(k+1)^3}.
\end{aligned}
$$

Solution step (worth 8 points):
Thus
$$
\begin{aligned}
\sum_{k=1}^n \binom{n}{k}\frac{(-1)^k}{(k+1)^3}&=\sum_{k=1}^n \binom{n}{k}\cdot (-1)^k\cdot\frac{1}{(k+1)^3}=\\
&=\sum_{k=1}^n \binom{n}{k}\cdot (-1)^k\cdot \int_0^1\int_0^z\int_0^y\frac{1}{z}\cdot\frac{1}{y}\cdot x^kdxdydz=\\
&=\sum_{k=1}^n \binom{n}{k}\cdot (-1)^k\cdot \int_0^1 \frac{1}{z}\left(\int_0^z\frac{1}{y}\left(\int_0^yx^kdx\right)dy\right)dz=\\
&=\int_0^1 \frac{1}{z}\left(\int_0^z\frac{1}{y}\left(\int_0^y \sum_{k=1}^n \binom{n}{k} (-1)^kx^kdx\right)dy\right)dz=\\
&=\int_0^1 \frac{1}{z}\left(\int_0^z\frac{1}{y}\left(\int_0^y \sum_{k=1}^n \binom{n}{k}1^{n-k}\cdot (-x)^kdx\right)dy\right)dz=\\
&=\int_0^1 \frac{1}{z}\left(\int_0^z\frac{1}{y}\left(\int_0^y (1-x)^ndx\right)dy\right)dz.
\end{aligned}
$$
Now, by making simple substitutions in the integrals, we obtain
$$
\begin{aligned}
&\int_0^1 \frac{1}{z}\left(\int_0^z\frac{1}{y}\left(\int_0^y (1-x)^ndx\right)dy\right)dz=\\
&=\int_0^1 \frac{1}{1-r}\left(\int_r^1\frac{1}{1-s}\left(\int_s^1 t^ndt\right)ds\right)dr=\\
&=\int_0^1 \frac{1}{1-r}\left(\int_r^1\frac{1}{1-s}\left(\frac{1-s^{n+1}}{n+1}\right)ds\right)dr=\\
&=\frac{1}{n+1}\int_0^1 \frac{1}{1-r}\left(\int_r^1\frac{1-s^{n+1}}{1-s}ds\right)dr=\\
&=\frac{1}{n+1}\int_0^1 \frac{1}{1-r}\left(\int_r^1\sum_{k=0}^n s^kds\right)dr=\\
&=\frac{1}{n+1}\int_0^1 \frac{1}{1-r}\sum_{k=0}^n\left(\int_r^1 s^kds\right)dr=\\
&=\frac{1}{n+1}\int_0^1 \frac{1}{1-r}\sum_{k=0}^n\left(\frac{1-r^{k+1}}{k+1}\right)dr=\\
&=\frac{1}{n+1}\sum_{k=0}^n\frac{1}{k+1}\int_0^1 \frac{1-r^{k+1}}{1-r}dr=\\
&=\frac{1}{n+1}\sum_{k=0}^n\frac{1}{k+1}\int_0^1 \sum_{j=0}^kr^jdr=\\
&=\frac{1}{n+1}\sum_{k=0}^n\frac{1}{k+1}\sum_{j=0}^k\int_0^1 r^jdr=\\
&=\frac{1}{n+1}\sum_{k=0}^n\frac{1}{k+1}\sum_{j=0}^k\frac{1}{j+1}=\\
&=\frac{1}{n+1}\sum_{k=0}^n\sum_{j=0}^k\frac{1}{k+1}\frac{1}{j+1}.
\end{aligned}
$$
This completes the solution.
