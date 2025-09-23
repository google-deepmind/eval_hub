Solution step (3 points):
Let random event $B$ means that Maria draws 3 white balls and $B_k$ that she drew from the $k$-th box. 

Obviously $P(B|B_0)=0$. If $k\geq 0$ we have
$$
P(B|B_k) = \frac{k^3}{2024^3}.
$$

Solution step (3 points):
By the law of total probability we have
$$
P(B)=\sum_{k=0}^{2024}P(B|B_k)P(B_k).
$$
Obviously $P(B_k)=\frac{1}{2025}$, so
$$
P(B)= \frac{1}{2025\cdot 2024^3}\sum_{k=1}^{2024}k^3.
$$

Solution step (4 points):
By standard calculations we have that 
$$
\sum_{k=1}^{2024}k^3 = \left(\frac{2024\cdot 2025}{2}\right)^2
$$
and hence
$$
P(B)=\frac{2025}{4\cdot 2024}=\frac{2025}{8096}.
$$