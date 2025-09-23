This step is worth 2 points.
Note that the left-hand side is continuously differentiable, so $f''$ is, and therefore the $f\in \mathcal{C}^3((0,\infty))$. This way we can prove that $f$ is a smooth function.

This step is worth 7 points.
To make the equation easy to be differentiate we introduce the new variables $h$ and $t$ putting $a=e^{-h}t$ and $b=e^{h}t$. Then
$$
T(t,h)=f(e^ht)+f(e^{-h}t)-2f\left(\frac{e^h+e^{-h}}2t\right)-(e^{2h}+e^{-2h}-2)t^2f''(t)=0.
$$
Now we differentiate it twice with respect to $h$.
$$
\begin{split}
0&=\frac{\partial}{\partial h} T(t,h) = tf'(e^ht)e^h-tf'(e^{-h}t)e^{-h}\\
\quad &-2tf'\left(\frac{e^h+e^{-h}}2t\right) \frac{e^h-e^{-h}}2 -2t^2(e^{2h}-e^{-2h})f''(t) \\
0&=\frac{\partial^2}{\partial h^2} T(t,h) = t^2f''(e^ht)e^{2h}+tf'(e^ht)e^h + t^2f''(e^{-h}t)e^{-2h}+tf'(e^ht)e^{-h} \\
&\quad-2t^2 f''\left(\frac{e^h+e^{-h}}2t\right)\left(\frac{e^h-e^{-h}}2\right)^2-2tf'\left(\frac{e^h+e^{-h}}2t\right)\frac{e^h+e^{-h}}2\\
&\quad-4t^2(e^{2h}+e^{-2h})f''(t)
\end{split}
$$

Now, taking the limit with $h\to 0$ we get
$$
0=t^2f''(t)+tf'(t)+t^2f''(t)+tf'(t)-0-2tf'(t)-8t^2f''(t)=-6t^2f''(t)
$$
therefore $f''(t)=0$ for any $t>0$, so $f(t)=Ct+D$ for some $C,D\in\mathbb{R}$.

This step is worth 1 point.
Finally, we can easy verify that $f(t)=Ct+D$ satisfy the given equation
$$
f(b)+f(a)-2f\left(\frac{a+b}2\right)=(Cb+D)+(Ca+D)-2\left(D\frac{a+b}2-C\right)=0=(b-a)^2\cdot 0.
$$