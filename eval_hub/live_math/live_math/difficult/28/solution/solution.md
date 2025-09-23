Clearly for an arithmetic progression like in the problem, we have $a_7-a_1 = 6(a_2-a_1)$. We have to then find a maximal number which always divides $a_2-a_1$ in such a case. We will prove that it is equal to $30$. It is enough to consider increasing progressions -- the decreasing progression can be inverted, and for the constant the difference is $0$, hence divisible by anything.
 
Notice that $2|a_2-a_1$, otherwise at least two of the progression's terms will be even, and only one can be. Similarly we have $3|a_2-a_1$. If $a_2-a_1$ is not divisible by $5$, then at least one term of the progression will be divisible by $5$. It must be equal to $5$, hence it must be the first one -- the difference in the progression is at least $6$, so otherwise we would have $a_1<0$. But if $5|a_1$, then $5|a_6$. Hence $a_6$ would not be prime. This means that $5|a_1-a_2$. Summing up, we get $30|a_1-a_2$. 


Now we have to prove the maximality of $30$. There exists an arithmetic progression of primes of length $7$ starting from $7$ with difference $150$, and also a progression of length $10$ starting from $199$ with difference $210$ -- see \url{https://oeis.org/A033189}. As $\operatorname{gcd}(150,210) = 30$, we see that $30$ is the largest number that always divides the difference of the progression.


The answer is then $6\cdot 30 = 180$.