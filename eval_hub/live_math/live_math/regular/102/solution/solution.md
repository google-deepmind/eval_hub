The sum $\sum_{i=1}^{n} \frac{1}{(i+2)(i+3)}$ can be simplified in the following way.
        \begin{align*}
            \sum_{i=1}^{n} \frac{1}{(i+2)(i+3)} = \sum_{i=1}^{n} \frac{1}{i+2} - \frac{1}{i+3} = \frac{1}{3} - \frac{1}{n+3} = \frac{n}{3(n+3)}.
        \end{align*}
        Using this simplified formula, we reformulate the condition from the problem to
        \begin{align*}
            \sum_{i=m+1}^{n} \frac{1}{(i+2)(i+3)} &= \sum_{i=1}^{n} \frac{1}{(i+2)(i+3)} - \sum_{i=1}^{m} \frac{1}{(i+2)(i+3)}\\ &= 
            \frac{n}{3(n+3)} - \frac{m}{3(m+3)} = \frac{n-m}{(n+3)(m+3)}.
        \end{align*}
        We want $n=2m+3$, so
        \begin{align*}
            \frac{2m+3 - m}{(2m+6)(m+3)} &= \frac{1}{26}\\
            \frac{1}{2m+6} &= \frac{1}{26}\\
            m &= 10.
        \end{align*}
        From this we conclude that $n = 23$, and thus $n-m = 13$.