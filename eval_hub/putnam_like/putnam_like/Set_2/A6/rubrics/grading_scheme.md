Solution step (1 point):
We will prove that $f(1)=1$. Put $y=1$ and let $f(1)=c$. Then our functional equation takes the form:
$$
\frac{f(x)+c}{f(x)}=\frac{1}{f(x+1)}-2x.
$$
Thus, we get
$$
f(x+1)=\frac{f(x)}{(1+2x)f(x)+c}
$$
Substituting $1$, $2$ and $3$ for $x$, we get:
$$
\begin{aligned}
f(2)&=\frac{f(1)}{(1+2)f(1)+c}=\frac{c}{4c}=\frac{1}{4},\\
f(3)&=\frac{f(2)}{(1+4)f(2)+c}=\frac{\frac{1}{4}}{\frac{5}{4}+c}=\frac{1}{5+4c},\\
f(4)&=\frac{f(3)}{(1+6)f(3)+c}=\frac{\frac{1}{5+4c}}{\frac{7}{5+4c}+c}=\frac{1}{7+5c+4c^2}.
\end{aligned}
$$
Furthermore, putting $x=2$ and $y=2$, we obtain
$$
\frac{2f(2)}{f(4)}=\frac{1}{f(4)}-8,
$$
and hence
$$
2f(2)+8f(4)=1.
$$
Now, we arrive at the following equality:
$$
\frac{1}{2}+\frac{8}{7+5c+4c^2}=1.
$$
Solving the above equation, we have $c=1$, and hence
$$
f(1)=1.
$$

Solution step (1 point):
We will prove that
$$
f(x+n)=\frac{f(x)}{(n^2+2nx)f(x)+1}\text{ for all }n\geq 1.
$$
We will use the method of induction. For $n=1$, the above formula is true.
Now suppose that the formula is true for
$n=k$. Then, we have
$$
\begin{aligned}
f(x+k+1)=f((x+k)+1)&=\frac{f(x+k)}{(1+2(x+k))f(x+k)+1}\\
&=\frac{\frac{f(x)}{(k^2+2kx)f(x)+1}}{(1+2(x+k))\frac{f(x)}{(k^2+2kx)f(x)+1}+1}\\
&=\frac{f(x)}{(1+2(x+k))f(x)+((k^2+2kx)f(x)+1)}\\
&=\frac{f(x)}{((k+1)^2+2(k+1)x)f(x)+1},
\end{aligned}
$$
which shows that the formula holds for all $n\in \mathbb{N}$. Substituting $x=1$, we get
$$
f(1+n)=\frac{f(1)}{(n^2+2n1)f(1)+1}=\frac{1}{n^2+2n+1}=\frac{1}{(n+1)^2}\text{ for all }n\in \mathbb{N}.
$$

Solution step (1 point):
We will show that
$$
f\left(\frac{1}{n}\right)=n^2=\frac{1}{\frac{1}{n^2}}\text{ for all }n\in \mathbb{N}^+.
$$
Indeed, substituting $x=\frac{1}{n}$, we have
$$
f\left(\frac{1}{n}+n\right)=\frac{f\left(\frac{1}{n}\right)}{\left(n^2+2n\frac{1}{n}\right)f\left(\frac{1}{n}\right)+1}=
\frac{f\left(\frac{1}{n}\right)}{\left(n^2+2\right)f\left(\frac{1}{n}\right)+1}.
$$
Next, putting $y=\frac{1}{x}$, we obtain
$$
\frac{f(x)+f\left(\frac{1}{x}\right)}{f(1)}=\frac{1}{f\left(x+\frac{1}{x}\right)}-2.
$$
Thus, we have
$$
f(n)+f\left(\frac{1}{n}\right)+2=\frac{1}{f\left(n+\frac{1}{n}\right)}
=\frac{\left(n^2+2\right)f\left(\frac{1}{n}\right)+1}{f\left(\frac{1}{n}\right)}=
n^2+2+\frac{1}{f\left(\frac{1}{n}\right)}.
$$
Since $f(n)=\frac{1}{n^2}$, it follows that
$$
\frac{1}{n^2}+f\left(\frac{1}{n}\right)=n^2+\frac{1}{f\left(\frac{1}{n}\right)}.
$$
Let $z:=f\left(\frac{1}{n}\right)$. Then the above equation takes the following form:
$$
\frac{1}{n^2}+z=n^2+\frac{1}{z}.
$$
Then
$$
\frac{1}{n^2}+z=n^2+\frac{1}{z}\Longleftrightarrow z^2+z\left(\frac{1}{n^2}-n^2\right)-1=0\Longleftrightarrow z=n^2\vee z=-\frac{1}{n^2}.
$$
Since $z>0$, it follows that
$$
f\left(\frac{1}{n}\right)=z=n^2 \text{ for all }n\in \mathbb{N}^+.
$$

Solution step (6 points):
We will prove that if $q$ is rational, then
$$
f(q)=\frac{1}{q^2}.
$$
For  $q=\frac{m}{n}$ with $\text{gcd}(m,n)=1$ and $m,n\in \mathbb{N}^+$ we substitute $x=n$ and $y=\frac{1}{m}$ to get
$$
\frac{f(n)+f\left(\frac{1}{m}\right)}{f\left(\frac{n}{m}\right)}=\frac{1}{f\left(n+\frac{1}{m}\right)}-2\frac{n}{m}.
$$
Next, putting $x=\frac{1}{m}$, we obtain
$$
f\left(\frac{1}{m}+n\right)=\frac{f\left(\frac{1}{m}\right)}{(n^2+2n\frac{1}{m})f(\frac{1}{m})+1}=
\frac{m^2}{(n^2+\frac{2n}{m})m^2+1}=\frac{1}{n^2+\frac{2n}{m}+\frac{1}{m^2}}=\frac{1}{\left(n+\frac{1}{m}\right)^2}.
$$
Now, we get
$$
\frac{\frac{1}{n^2}+m^2}{f(\frac{n}{m})}=\left(n+\frac{1}{m}\right)^2-2\frac{n}{m}
=n^2+\frac{1}{m^2}.
$$
Consequently, we have
$$
f(q)=f\left(\frac{n}{m}\right)=\frac{\frac{1}{n^2}+m^2}{n^2+\frac{1}{m^2}}=\frac{m^2}{n^2}\cdot\frac{1+\frac{1}{n^2m^2}}{1+\frac{1}{n^2m^2}}=
\left(\frac{m}{n}\right)^2=\frac{1}{\left(\frac{n}{m}\right)^2}=\frac{1}{q^2}.
$$

Solution step (2 points):
We will show that if $x\in \mathbb{R}^+$, then
$$
f(x)=\frac{1}{x^2}\text{ for all }x\in \mathbb{R}^+.
$$
Let $x\in \mathbb{R}^+$. Then
$$
x=\lim_{n\to\infty }q_n,
$$
for some sequence $(q_n)$ of rational numbers. Since $f(x)$ must be continuous, it follows that
$$
f(x)=f(\lim_{n\to\infty}q_n)=\lim_{n\to\infty} f(q_n)=\lim_{n\to\infty} \frac{1}{(q_n)^2}=\frac{1}{x^2}.
$$
Thus, $f(x)=\frac{1}{x^2}$ is a unique function.
