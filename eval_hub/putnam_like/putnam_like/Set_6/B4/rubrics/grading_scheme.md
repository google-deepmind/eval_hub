This step is worth 2 points.
Note that $\sqrt{5}-2<1$ and hence $(\sqrt{5}-2)^{2n}<1$ for every positive integer $n$. Therefore if $(\sqrt{5}+2)^{2n}+(\sqrt{5}-2)^{2n}$ is an integer, then it is a desired number.

This step is worth 6 points.
Consider a sequence $a_n = (\sqrt{5}+2)^{2n}+(\sqrt{5}-2)^{2n}$. We express it as a second order recurrence. Obviously $a_0=2$ and $a_1=14.$

Assume that $a_n=\alpha a_{n-1} + \beta a_{n-2}$. Then the characteristic polynomial is given by the following formula: $t^2-\alpha t - \beta = 0$. We also know that $(\sqrt{5}+2)^{2}$ and $(\sqrt{5}-2)^{2}$ are its roots. Therefore
$$
t^2-\alpha t - \beta = (t-(\sqrt{5}+2)^{2})(t-(\sqrt{5}-2)^{2}), \qquad t\in\mathbb{R}.
$$
Consequently, 
$$
\alpha = (\sqrt{5}+2)^{2} + (\sqrt{5}-2)^{2} = 18
$$
and
$$
\beta = - (\sqrt{5}+2)^{2}(\sqrt{5}-2)^{2} = -1.
$$
Finally the sequence $(a_n)$ can be expressed by the following formula
$$
\begin{cases}
a_0=2,\: a_1 = 18,\\
a_n = 18a_{n-1} - a_{n-2}.
\end{cases}
$$

This step is worth 2 points.
The sequence $(a_n)$ is given by the recurrence with integer coefficients and integer initial terms, so all its terms are integers. By step 1, $a_n$ is the smallest integer greater than $(\sqrt{5}+2)^{2n}$.