Solution step (2 points).
Note that
$$
\lim_{x\to\infty} f(x) = \lim_{x\to\infty} \frac{e^{g(x)} f(x)}{e^{g(x)}} = (*). 
$$

Solution step (8 points).
Then, thanks to $e^{g(x)} \to \infty$ as $x\to\infty$, we can use the L'Hôpital's rule to get
$$
(*) = \lim_{x\to\infty} \frac{(e^{g(x)} f(x))'}{(e^{g(x)})'} = \lim_{x\to\infty} \frac{e^{g(x)} g'(x) f(x) + e^{g(x)} f'(x)}{e^{g(x)} g'(x)} = \lim_{x\to\infty} \left( f(x) + \frac{f'(x)}{g'(x)} \right) = 0.
$$