Let $(a_1,a_2,\dots,a_8)$ be as in the problem. 
 
Notice that $2|a_2-a_1$, otherwise at least two of the progression's terms will be even, and only one can be. Similarly we have $3|a_2-a_1$. If $a_2-a_1$ is not divisible by $5$, then at least one term of the progression will be divisible by $5$. It must be equal to $5$, hence it must be the first one -- the difference in the progression is at least $6$, so otherwise we would have $a_1<0$. But if $5|a_1$, then $5|a_6$. Hence $a_6$ would not be prime. This means that $5|a_2-a_1$. If $a_2-a_1$ is not divisible by $7$, then at least one term in the sequence will be divisible by $7$. Same as before, it will have to be $a_1$, but then $7|a_8$. Hence by contradiction we get that $7|a_2-a_1$. 


Hence $210=2\cdot 3\cdot 5\cdot 7 | a_2-a_1$. There exists a sequence $(a_1,\dots,a_8)$ satisfying the conditions with $a_2-a_1 = 210$ and $a_1 = 199$ -- see the eighth term in \url{https://oeis.org/A033189}. In that case $a_8 = 199 + 7\cdot 210 = 1669$. This is the smallest possible $a_8$ for $a_2-a_1 = 210$.


Now if $a_2-a_1 > 210$, we have $a_2-a_1\ge 420$. Then 
$$a_8 = a_1 + 7(a_2-a1) > 7\cdot 420 = 2940 > 1669.$$
Hence $1669$ is the minimal possible $a_8$ we can attain.