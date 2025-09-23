The location of Anna is clearly a Markov chain with 7 states: state 0 is being in front of the house, states $1, 2, \ldots, 5$ are being in the rooms with numbers $1, 2, \ldots,5$ and state 6 is being outside of the house, after passing through all the rooms. Let $\varphi(i)$ be the probability of leaving the haunted house before coming back to the state 0, given that currently we are in state $i$.
We just have to solve the system of equations
\begin{align*}
    \varphi(0) = 0\\
    \varphi(1) = 0.1 \cdot \varphi(0) + 0.9 \cdot \varphi(2)\\
    \varphi(2) = 0.1 \cdot \varphi(1) + 0.9 \cdot \varphi(3)\\
    \varphi(3) = 0.1 \cdot \varphi(2) + 0.9 \cdot \varphi(4)\\
    \varphi(4) = 0.1 \cdot \varphi(3) + 0.9 \cdot \varphi(5)\\
    \varphi(5) = 0.1 \cdot \varphi(4) + 0.9 \cdot \varphi(6)\\
    \varphi(6) = 1.
\end{align*}
Plugging it into wolfram alpha informs us that $\varphi(1) = \frac{59049}{66430}$, so $b-a = 7381$.