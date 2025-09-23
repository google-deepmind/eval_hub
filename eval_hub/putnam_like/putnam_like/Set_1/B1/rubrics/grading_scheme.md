Solution step (1 point):
Observe that $x = 0$ satisfies the equation. Hence, from now on, we assume that $x \neq 0$. 

Solution step (1 point):
We rewrite the equation as
$$10^{x^2} - 6^{x^2} = 5^{x^2} - 1.$$

Solution step (7 points):
Define $f(t) := t^{x^2}$. Then the equation has the form
$$f(10) - f(6) = f(5) - f(1).$$
From the mean value theorem there are $t_1 \in [6,10]$ and $t_2 \in [1,5]$ such that
$$f'(t_1) = f'(t_2).$$
On particular $t_1 > t_2$. Hence $x^2 t_1^{x^2 - 1} = x^2 t_2^{x^2 - 1}$, which may be rewritten as $(t_1 / t_2)^{x^2 - 1} = 1$. Hence $x^2 = 1$. 

Solution step (1 point):
To summarize, all real solutions to the equation are $-1$, $0$ and $1$.