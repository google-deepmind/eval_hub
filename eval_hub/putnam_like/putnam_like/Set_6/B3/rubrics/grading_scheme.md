Solution step (2 points):
Assume that $f$ is not constant. Then there exists $\varepsilon>0$ such that $|f(x)-f(0)|>\varepsilon$ for some $x\in\mathbb{R}$. Without loss of generality, assume that $x>0$.

Solution step (3 points):
Let $b=\min(\inf\{x>0\,:\, |f(x)-f(0)|>\varepsilon\}, \frac{1}{2})$. Notice that $b>0$ since $f$ is continuous in $0$. Moreover
$$
|f(x)-f(0)|\leq |f(b)-f(0)|,\qquad x\in[0,b].
$$

Solution step (3 points):
By the mean value theorem we see that there exists $a\in(0,b)$ such that
$$
|f(b)-f(0)| \leq |f'(a)||b-0| \leq \frac{1}{2}|f(a)-f(0)|.
$$

Solution step (2 points):
Therefore we have
$$
|f(a)-f(0)| < \frac{1}{2}|f(a)-f(0)|,
$$
which is a contradiction. Hence $f$ has to be constant.