Let $p$ be a prime number -- we will later plug in $p=31$. We prove by induction on $k$ that the number of $k$-tuples $(x_1,\dots,x_k)\in \{1,2,\dots,p-1\}^k$ such that $x_1+\dots+x_k-1$ is not divisible by $p$, is equal to 
 $$\frac{(p-1)^{k+1}+(-1)^{k}}{p}.$$


For $k=1$ the number is clearly $p-2 = \frac{(p-1)^2-1}{p}$. Now assume we know the formula for a given $k$. We want to count $k+1$-tuples satisfying the conditions. There are $(p-1)^{k+1}$ tuples of numbers from $\{1,2,\dots,p-1\}$. We will subtract those for which $x_1+x_2+\dots+x_{k+1} \equiv 1\pmod{p}$. Note that for given $(x_1,x_2,\dots,x_k)\in \{1,2,\dots,p-1\}^k$ we can find at most one $x_{k+1}\in \{1,2,\dots,p-1\}$ such that $x_1+x_2+\dots+x_{k+1} \equiv 1\pmod{p}$. It has to be congruent to $1-(x_1+x_2+\dots+x_k)$ modulo $p$. Hence it exists in $\{1,2,\dots,p-1\}$ if and only if $x_1+x_2+\dots+x_k\neq 1\pmod{p}$. This means that we have to subtract the number of $k$-tuples satisfying the conditions of the problem. Hence the number of admissible $k+1$-tuples is


 $$(p-1)^{k+1} - \frac{(p-1)^{k+1}+(-1)^{k}}{p} = \frac{(p-1)^{k+1}\cdot p - (p-1)^{k+1}+(-1)^{k+1}}{p} = \frac{(p-1)^{k+2}+(-1)^{k+1}}{p},$$
 which proves the inductive hypothesis.
 
 Hence the answer is
 
 $$\frac{30^{11}+1}{31} = 571441935483871.$$
 