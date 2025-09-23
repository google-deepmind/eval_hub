Assume we have coloured every positive integer in one of the $10$ colours. By pigeonhole principle among the numbers $1$, $2$, \dots, $91$ there will be at least $10$ painted in the same colour -- because $91 = 9\cdot 10 + 1$. Their sum is then at most
 $$91 + 90 + \dots + 82 = 5\cdot (82 + 91) = 5\cdot 173 = 865,$$
hence smaller than $866$.


Hence the number $n$ we are looking for is at most $866$. We prove that it is equal $866$, i.e. we can colour the positive integers in $10$ colours such that any $10$ distinct numbers of the same colour have their sum at least $865$. We can do the following. Colour the first nine numbers -- from $1$ to $9$ -- in colour $1$. Then colour the next nine numbers -- from $10$ to $18$ in colour $2$. Continue this way until we colour the numbers from $73$ to $81$ in colour $9$. Then we colour all the numbers higher than $81$ in colour $10$.


For such a colouring, if we want to find ten distinct numbers in the same colour, it has to be the colour $10$, as other colours are used at most $9$ times. Their sum will then be at least $82+83+\dots+91 = 865$.
