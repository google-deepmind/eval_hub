The question is equivalent to asking what is the probability of choosing 4 pieces among 12 in a way that no 2 pieces out of those 4 are adjacent in rows. We have to consider the following 3 cases.\\
       1. We have 2 pairs of non-adjacent pieces in 2 different rows -- we can choose them on $\binom{4}{2} =6$ ways;\\
       2. We choose one piece from every row -- we can do it on $3^4 = 81$ ways;\\
       3. We choose two different rows and take one piece from each of them, and we choose one more row and take 2 non-adjacent pieces from it -- we can do it on $\binom{4}{2}\cdot 3^2 \cdot \binom{2}{1} \cdot 1 = \frac{4\cdot 3}{2}\cdot 3^2 \cdot 2 = 4 \cdot 3^3 = 108$.
       Summarizing, the probability is $\frac{6+81+108}{\binom{12}{4}} = \frac{13}{33}$. Thus the answer is 46.\\