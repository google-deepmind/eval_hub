 Call $S=A+B+C$ so the equation is:
$$2S^2=100A+10B+C$$
\noindent and since the right term is a three number digits we have the restriction $100 \leq 2S^2 \leq 999$ which yields $\sqrt{50} \leq S \leq \sqrt{499.5}$ if and only if $8 \leq S \leq 22$. \\
But $2S^2=100A+10B+C=S+9(11A+B)$ so $2S^2-S$ is multiple of $9$. Since $2S^2-S=(2S-1)S$ we have two possibilities: either $2S-1$ and $S$ are both multiples of $3$, which is clearly impossible or necessarily $S$ or $2S-1$ is a multiple of $9$. Since $2S-1$ is odd we must only consider $S=9$ or $18$ or $2S-1=9$ or $27$ which yields $S=5$ or $14$. We study each solution:
\begin{itemize}
\item $S=5$ yields $2 \cdot 5^2 = 50$ which has only two digits. So this is not a solution.

\item $S=9$ yields $2 \cdot 9^2 = 162$ which satisfies that $2(1+6+2)^2=162$. 

\item $S=14$ yields $2 \cdot 14^2 = 392$ which satisfies that $2(3+9+2)^2=392$. 

\item $S=18$ yields $2 \cdot 18^2 = 648$ which satisfies that $2(6+4+8)^2=648$.
\end{itemize}

So there are three numbers of three digits satisfying the condition: $162,392,648$.