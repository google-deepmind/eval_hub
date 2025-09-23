This step is worth 8 points.
Let $s_1, s_2 \in [p,q]$ and fix $\alpha \in (0,1)$. Then, from the H\"older inequality
$$
\begin{aligned}
\Psi \left( (1-\alpha) s_1 + \alpha s_2 \right) &= \ln \left( \int |f(x)|^{(1-\alpha) s_1} |f(x)|^{\alpha s_2} \, dx \right) \\
 &\leq \ln \left(  \left( \int |f(x)|^{s_1} \, dx \right)^{1-\alpha} \left( \int |f(x)|^{s_2} \, dx \right)^\alpha \right).
\end{aligned}
$$

This step is worth 2 points.
Then, using the properties of $\ln$ we get
$$
\begin{aligned}
&\quad \ln \left(  \left( \int |f(x)|^{s_1} \, dx \right)^{1-\alpha} \left( \int |f(x)|^{s_2} \, dx \right)^\alpha \right) \\
&= \ln \left(  \left( \int |f(x)|^{s_1} \, dx \right)^{1-\alpha} \right) + \ln \left( \left( \int |f(x)|^{s_2} \, dx \right)^\alpha \right) \\
&= (1-\alpha) \ln \left( \int |f(x)|^{s_1} \, dx \right) + \alpha \ln \left(\int |f(x)|^{s_2} \, dx \right) \\
&= (1-\alpha) \Psi(s_1) + \alpha \Psi(s_2)
\end{aligned}
$$
and the proof is complete.