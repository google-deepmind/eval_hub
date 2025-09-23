The multiplicity system $\underline{m}=\left(m_{1}, \ldots, m_{5}\right)$ of the singularity is given by the equation
$$
\left[\begin{array}{ccccc}
-2 & 1 & 0 & 0 & 0 \\
1 & -1 & 1 & 0 & 0 \\
0 & 1 & -5 & 1 & 0 \\
0 & 0 & 1 & -1 & 1 \\
0 & 0 & 0 & 1 & -2
\end{array}\right] \cdot\left[\begin{array}{l}
m_{1} \\
m_{2} \\
m_{3} \\
m_{4} \\
m_{5}
\end{array}\right]=\left[\begin{array}{l}
0 \\
1 \\
0 \\
1 \\
0
\end{array}\right]
$$

Hence $\underline{m}=(5,10,4,10,5)$. By A'Campo's formula the Euler caharcteristic of the Milnor fiber $F$ can be computed as $\chi(F)=\sum_{i=1}^{5} m_{i}\left(2-\delta_{i}\right)$ where $\delta_{i}$ is the degree of the $i^{\text {th }}$ vertex of the resolution graph (counting edges with arrows at the other end as well). It follows that $\chi=-10$ and hence that $F$ is a genus 5 surface with two disks removed. This shows that $\mu=\operatorname{rank}_{\mathbb{Z}} H_{1}(F)=11$.

Different Solution. This is the resolution graph of the singularity given by the equation $\left(x^{2}-y^{3}\right)\left(x^{3}-y^{2}\right)=0$. There exists a formula for the Milnor number: $\mu=\mu_{1}+\mu_{2}+2 \cdot i_{1,2}-1$, where $\mu_{i}$ is the Milnor number of the components and $i_{1,2}$ is their intersection multiplicity. Now, $\mu_{1}=\mu_{2}=\operatorname{dim}_{\mathbb{C}} \frac{\mathcal{O}_{\mathbb{C}^{2}, o}}{\left(x, y^{2}\right)}=2$ by definition of the Milnor number and $i_{1,2}=\operatorname{dim}_{\mathbb{C}} \frac{\mathcal{O}_{\mathbb{C}^{2}, o}}{\left(x^{2}-y^{3}, x^{3}-y^{2}\right)}=4$. Hence $\mu=2+2+2 \cdot 4-1=11$.
