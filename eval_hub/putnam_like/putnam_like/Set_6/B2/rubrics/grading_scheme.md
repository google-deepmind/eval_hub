Solution step (worth 4 points):
By $p_m$ denote the probability of getting heads on $m$-th coin and $q_m=1-p_m$. Observe that
$$
\prod_{m=1}^{n}(q_m-p_m) = \sum_{i=1}^{n_1} e_i - \sum_{i=1}^{n_2} o_i,
$$
where $e_i$ and $o_i$ are products of $q_m$'s and $p_m$'s in which the number of $p_m$'s is even and odd, respectively. Moreover $n_1$ and $n_2$ are some positive integers such that $n_1+n_2 = 2^n$.

Observe that $p_e = \sum_{i=1}^{n_1} e_i$ is a probability that one gets an even number of heads, and $p_o = \sum_{i=1}^{n_2} o_i$ is a probability of getting an odd number of heads.

Solution step (worth 3 points):
Note that $p_e+p_o = 1$ and $p_e-p_o = \prod_{m=1}^{n}(q_m-p_m).$ Therefore 
$$
p_e = \frac{1+\prod_{m=1}^{n}(q_m-p_m)}{2}
$$
and it suffices to calculate $\prod_{m=1}^{n}(q_m-p_m)$.

Solution step (worth 2 points):
Observe that
$$
\prod_{m=1}^{n}(q_m-p_m) = \prod_{m=1}^{n}\left(\frac{2m}{2m+1}-\frac{1}{2m+1}\right) = \prod_{m=1}^{n}\frac{2m-1}{2m+1}.
$$
The last product telescopes down to $\frac{1}{2n+1}$.

Solution step (worth 1 point):
Hence the answer is
$$
p_e = \frac{1+\frac{1}{2n+1}}{2} = \frac{n+1}{2n+1}.
$$