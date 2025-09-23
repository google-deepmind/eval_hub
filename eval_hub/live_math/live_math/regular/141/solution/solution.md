Let $N$ be the number of dancers. Let us draw a 4-partite graph, one set of vertices is the set of ballerinas, then we have sets of white tutus, purple tutus, blue tutus and gold tutus. We draw an edge between a vertex representing a ballerina and a vertex representing a tutu if and only if the ballerina owns the tutu. Let $v_i$ be the number of vertices of degree $i$, for $i=1, 2, 3, 4$. Then we have
    \begin{align*}
    \begin{cases}
        v_1 + v_2 + v_3 + v_4 = N\\
        v_1 + 2v_2 + 3v_3 + 4v_4 = 500.
        \end{cases}
    \end{align*}
    Plugging in the given numbers, we obtain $16 + 50 + v_3 + 24 = N$, so $v_3 + 90 = N$. Then we have $16 + 2\cdot 50 + 3v_3 + 4\cdot 24 = 500$, so $3v_3 = 288$, so $v_3 = 96$. Thus we have $N = 186$.   