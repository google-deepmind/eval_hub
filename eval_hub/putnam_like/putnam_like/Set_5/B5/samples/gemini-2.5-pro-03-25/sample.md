Let $P(z)=z^8-5z^3+10$. We want to find the number of zeros of $P(z)$ in the set $A=\{z\in\mathcal{C}\,:\, \frac \pi 2 \leq \arg z\leq \pi\}$. The set $A$ corresponds to the second quadrant of the complex plane, including the positive imaginary axis and the negative real axis. The argument function is defined in $[0, 2\pi)$.

We use the Argument Principle. Let $N_A$ be the number of zeros of $P(z)$ in the interior of the region $A$, denoted $A^o = \{z\in\mathcal{C}\,:\, \frac \pi 2 < \arg z < \pi\}$. The boundary of this region, $\partial A$, consists of the positive imaginary axis $L_1 = \{it : t \ge 0\}$ and the negative real axis $L_2 = \{-t : t \ge 0\}$, and the origin $\{0\}$. The Argument Principle states that if $P(z)$ has no zeros on $\partial A$, then the number of zeros in $A^o$ is given by $N_A = \frac{1}{2\pi} \Delta_{\partial A} \arg P(z)$, where $\Delta_{\partial A} \arg P(z)$ is the change in the argument of $P(z)$ as $z$ traverses the boundary of $A$ in the counterclockwise direction.

The boundary $\partial A$ can be described as a path starting from the origin $z=0$, moving along the positive imaginary axis to $i\infty$, then traversing a large arc $C_\infty$ in the second quadrant from $i\infty$ to $-\infty$, and finally returning along the negative real axis from $-\infty$ to the origin $z=0$.

Let's first check if $P(z)$ has any zeros on the boundary $\partial A$.
1.  For $z=0$, $P(0)=10 \ne 0$.
2.  For $z$ on the positive imaginary axis, let $z=it$ with $t>0$.
    $P(it) = (it)^8 - 5(it)^3 + 10 = i^8 t^8 - 5i^3 t^3 + 10 = t^8 - 5(-i)t^3 + 10 = (t^8+10) + i(5t^3)$.
    For $P(it)=0$, we must have both the real and imaginary parts equal to zero. $5t^3=0$ implies $t=0$, but we consider $t>0$. Also, $t^8+10=0$ has no real solutions for $t$. Thus, $P(z)$ has no zeros on the positive imaginary axis (for $t>0$).
3.  For $z$ on the negative real axis, let $z=-t$ with $t>0$.
    $P(-t) = (-t)^8 - 5(-t)^3 + 10 = t^8 - 5(-t^3) + 10 = t^8 + 5t^3 + 10$.
    Since $t>0$, $t^8 > 0$ and $5t^3 > 0$, so $P(-t) = t^8+5t^3+10 \ge 10 > 0$. Thus, $P(z)$ has no zeros on the negative real axis (for $t>0$).
Since $P(z)$ has no zeros on the boundary $\partial A$, the number of zeros in $A$ is the same as the number of zeros in the interior $A^o$.

We now compute the change in argument $\Delta_{\partial A} \arg P(z)$. Let's parameterize the boundary with a large radius $R$ and a small radius $\epsilon$. The contour consists of four parts:
- $L_{1,\epsilon, R}$: line segment from $i\epsilon$ to $iR$. $z=it$, $t: \epsilon \to R$.
- $C_R$: arc of circle $|z|=R$ from $iR$ to $-R$. $z=Re^{i\theta}$, $\theta: \pi/2 \to \pi$.
- $L_{2,\epsilon, R}$: line segment from $-R$ to $-\epsilon$. $z=-t$, $t: R \to \epsilon$.
- $C_\epsilon$: arc of circle $|z|=\epsilon$ from $-\epsilon$ to $i\epsilon$. $z=\epsilon e^{i\theta}$, $\theta: \pi \to \pi/2$.

We analyze the change in argument of $P(z)$ along each part as $\epsilon \to 0$ and $R \to \infty$.
1.  Along $L_1 = \{it : t \in [0, \infty)\}$. We trace from $t=0$ to $t=\infty$. $P(it) = (t^8+10) + i5t^3$. At $t=0$, $P(0)=10$, $\arg P(0)=0$. For $t>0$, $P(it)$ is in the first quadrant. As $t\to\infty$, $P(it) \sim t^8$, which is large and real positive. $\arg P(it) = \arctan(\frac{5t^3}{t^8+10})$. This starts at 0, increases slightly, and then decreases back to 0. The net change in argument along $L_1$ from $0$ to $\infty$ is $\lim_{t\to\infty} \arg P(it) - \arg P(0) = 0-0=0$. Let this change be $\Delta_1$.
2.  Along $C_\infty$. Let $z=Re^{i\theta}$, with $R\to\infty$ and $\theta$ going from $\pi/2$ to $\pi$. For large $|z|=R$, $P(z) = z^8 - 5z^3 + 10 \approx z^8$.
    $P(z) \approx (Re^{i\theta})^8 = R^8 e^{i8\theta}$.
    The argument of $P(z)$ is approximately $8\theta$. As $\theta$ changes from $\pi/2$ to $\pi$, the argument $8\theta$ changes from $8(\pi/2)=4\pi$ to $8\pi$.
    The change in argument along $C_\infty$ is $\Delta_2 = 8\pi - 4\pi = 4\pi$.
    More formally, $P(z) = z^8(1 - 5z^{-5} + 10z^{-8})$. Let $w(z) = -5z^{-5} + 10z^{-8}$. For large $R$, $|w(z)| \le 5R^{-5} + 10R^{-8} < 1$. So $1+w(z)$ is in the right half plane, hence $\arg(1+w(z)) \in (-\pi/2, \pi/2)$.
    $\arg P(z) = \arg(z^8) + \arg(1+w(z)) = 8\theta + \phi(\theta)$, where $\phi(\theta) \in (-\pi/2, \pi/2)$.
    The continuous change in argument from $\theta=\pi/2$ to $\theta=\pi$ is $(8\pi + \phi(\pi)) - (8(\pi/2) + \phi(\pi/2))$.
    At $\theta=\pi/2$, $z=iR$. $w(iR) = -5(iR)^{-5} + 10(iR)^{-8} = -5i^{-5}R^{-5} + 10i^{-8}R^{-8} = -5(-i)R^{-5} + 10R^{-8} = 10R^{-8} + i5R^{-5}$. $\phi(\pi/2) = \arg(1+10R^{-8}+i5R^{-5}) \to 0^+$ as $R\to\infty$. Let $\phi(\pi/2)=\epsilon_1$.
    At $\theta=\pi$, $z=-R$. $w(-R) = -5(-R)^{-5} + 10(-R)^{-8} = 5R^{-5} + 10R^{-8}$. $\phi(\pi) = \arg(1+5R^{-5}+10R^{-8}) = 0$.
    The change is $(8\pi+0) - (4\pi+\epsilon_1) = 4\pi - \epsilon_1$. As $R\to\infty$, the change $\Delta_2 \to 4\pi$.
3.  Along $L_2 = \{-t : t \in [0, \infty)\}$. We trace from $t=\infty$ back to $t=0$. $P(-t) = t^8+5t^3+10$. This is always real and positive. $P(-t)$ starts at $+\infty$ for $t=\infty$ and decreases to $P(0)=10$. The path $P(-t)$ lies entirely on the positive real axis. The argument is constant, $\arg P(-t)=0$. The net change in argument along $L_2$ is $\Delta_3 = 0$. (Note: we must use the continuous argument. At $z=-R$, the argument is $8\pi+\phi(\pi) = 8\pi$. So $\arg P(-t)$ should be $8\pi$ for $t>0$. As $t\to 0$, $P(-t) \to 10$, so argument ends at $8\pi$. The change is $8\pi - 8\pi = 0$. Alternatively, if we took the argument value from $C_R$ to be $4\pi$, then the argument along $L_2$ would be $4\pi$. Change $4\pi - 4\pi=0$).

The total change in argument along the boundary $\partial A$ is $\Delta_{\partial A} \arg P(z) = \Delta_1 + \Delta_2 + \Delta_3 = 0 + 4\pi + 0 = 4\pi$.
The number of zeros in the interior $A^o$ is $N_A = \frac{1}{2\pi} \Delta_{\partial A} \arg P(z) = \frac{1}{2\pi} (4\pi) = 2$.
Since there are no zeros on the boundary $\partial A$, the number of zeros in the set $A = A^o \cup \partial A$ is also 2.

Final check using symmetry: $P(z)=z^8-5z^3+10$ has real coefficients, so if $z$ is a zero, then its conjugate $\bar{z}$ is also a zero. If $z=re^{i\theta}$ is a zero with $\theta \in (\pi/2, \pi)$ (second quadrant), then $\bar{z}=re^{-i\theta}=re^{i(2\pi-\theta)}$ has argument $2\pi-\theta \in (\pi, 3\pi/2)$ (third quadrant). This means the number of zeros in the second quadrant equals the number of zeros in the third quadrant ($N_2 = N_3$). Similarly, $N_1=N_4$. The total number of zeros is 8 (since it's a degree 8 polynomial). $N_1+N_2+N_3+N_4 = 8$. We have $2N_1 + 2N_2 = 8$, so $N_1+N_2=4$. Our calculation gives $N_2=2$. This implies $N_1=2$. So there are 2 zeros in each open quadrant. This is consistent.

The number of zeros in $A=\{z\in\mathcal{C}\,:\, \frac \pi 2 \leq \arg z\leq \pi\}$ is 2.

Final answer should be an integer.

```latex
Let $P(z)=z^8-5z^3+10$. We want to find the number of zeros of $P(z)$ in the set $A=\{z\in\mathcal{C}\,:\, \frac \pi 2 \leq \arg z\leq \pi\}$, where $\arg z \in [0, 2\pi)$. This set $A$ represents the second quadrant of the complex plane, including the positive imaginary axis and the negative real axis.

We use the Argument Principle. Let $N$ be the number of zeros of $P(z)$ in the interior of $A$, denoted by $A^o = \{z\in\mathcal{C}\,:\, \frac \pi 2 < \arg z < \pi\}$. The principle states that $N = \frac{1}{2\pi} \Delta_{\partial A} \arg P(z)$, provided that $P(z)$ has no zeros on the boundary $\partial A$.

The boundary $\partial A$ consists of the positive imaginary axis $L_1 = \{it : t \ge 0\}$, the negative real axis $L_2 = \{-t : t \ge 0\}$, and the origin $\{0\}$. Let's check for zeros on $\partial A$.
\begin{enumerate}
    \item At $z=0$: $P(0)=10 \ne 0$.
    \item On $L_1$ (excluding $z=0$): Let $z=it$ for $t>0$. $P(it) = (it)^8 - 5(it)^3 + 10 = t^8 - 5(-i)t^3 + 10 = (t^8+10) + i(5t^3)$. For $P(it)=0$, both real and imaginary parts must be zero. $5t^3=0 \implies t=0$, which is excluded. Also, $t^8+10=0$ has no real solutions. So $P(z) \ne 0$ on $L_1 \setminus \{0\}$.
    \item On $L_2$ (excluding $z=0$): Let $z=-t$ for $t>0$. $P(-t) = (-t)^8 - 5(-t)^3 + 10 = t^8 + 5t^3 + 10$. Since $t>0$, $t^8>0$ and $5t^3>0$, so $P(-t) \ge 10 > 0$. So $P(z) \ne 0$ on $L_2 \setminus \{0\}$.
\end{enumerate}
Since $P(z)$ has no zeros on the boundary $\partial A$, the number of zeros in $A$ is equal to the number of zeros in its interior $A^o$.

We compute the change in argument $\Delta_{\partial A} \arg P(z)$ by traversing the boundary in a counterclockwise direction. This involves tracing $P(z)$ as $z$ goes from $0$ to $i\infty$ along $L_1$, then along an infinite arc $C_\infty$ from $i\infty$ to $-\infty$, and finally from $-\infty$ to $0$ along $L_2$.
\begin{enumerate}
    \item Path $L_1$: $z=it$ for $t$ from $0$ to $\infty$. $P(it) = (t^8+10)+i5t^3$. $P(0)=10$. For $t>0$, $P(it)$ is in the first quadrant. $\arg P(it) = \arctan\left(\frac{5t^3}{t^8+10}\right)$. $\arg P(0)=0$. As $t\to\infty$, $\arg P(it) \to 0$. The argument starts at 0, increases slightly, then decreases back to 0. The net change is $\Delta_{L_1} = 0$.
    \item Path $C_\infty$: $z=Re^{i\theta}$ for $R\to\infty$, $\theta$ from $\pi/2$ to $\pi$. For large $R$, $P(z) \approx z^8 = R^8 e^{i8\theta}$. The argument $\arg P(z) \approx 8\theta$. As $\theta$ varies from $\pi/2$ to $\pi$, $8\theta$ varies from $8(\pi/2)=4\pi$ to $8\pi$. The change in argument is $\Delta_{C_\infty} = 8\pi - 4\pi = 4\pi$.
    \item Path $L_2$: $z=-t$ for $t$ from $\infty$ to $0$. $P(-t)=t^8+5t^3+10$. This path lies on the positive real axis, going from $+\infty$ to $10$. The argument is constant along this path. To maintain continuity from the previous path ($C_\infty$), the argument starts at $8\pi$ (or $4\pi$ depending on the continuous branch choice, but the change is what matters). Let's say the argument is $k \cdot 2\pi$. As $t \to 0$, $P(-t) \to 10$, so the argument remains $k \cdot 2\pi$. The net change is $\Delta_{L_2} = 0$.
\end{enumerate}
The total change in argument along the boundary $\partial A$ is $\Delta_{\partial A} \arg P(z) = \Delta_{L_1} + \Delta_{C_\infty} + \Delta_{L_2} = 0 + 4\pi + 0 = 4\pi$.
The number of zeros in the interior $A^o$ is $N = \frac{1}{2\pi} \Delta_{\partial A} \arg P(z) = \frac{1}{2\pi}(4\pi) = 2$.
Since there are no zeros on the boundary $\partial A$, the number of zeros in the closed set $A$ is also 2.

Final Answer: The final answer is $\boxed{2}$
```