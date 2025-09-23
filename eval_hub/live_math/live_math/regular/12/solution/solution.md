We know that $1 + 2 + \dots + n = \frac{n(n+1)}{2}$. If the second last digit of $\frac{n(n+1)}{2}$ is $8$, then in particular the reminder modulo $25$ is in the interval $[5,14]$. Then 
$$8 \cdot \frac{n(n+1)}{2} = 4n^2 + 4n = (2n+1)^2 - 1$$
has one of the following reminders modulo $25$:
$$15, 23, 6, 14, 22, 5, 13, 21, 4, 12.$$
Now a quick computation shows that the following are the quadratic residues modulo $25$:
$$1, 4, 9, 16, 0, 11, 24, 14, 6, 21, 19$$
Hence $(2n+1)^2 - 1$ might be only congruent to one of the numbers
$$15, 23, 13, 5.$$
This happens when $2n+1$ has one of the following remainders modulo $25$:
$$4, 21, 7, 18, 8, 17, 9, 16.$$
Hence $n$ is congruent to one of:
$$14, 10, 6, 21, 16, 8, 4, 20$$
The sequence of numbers $n$ with that property is
$$4, 6, 8, 10, 14, 16, 20, 21, 29, 31, 33, 35, 39, \dots$$
Note that $\frac{12\cdot 13}{2} = 78$ and $\frac{13\cdot 14}{2} = 91$, hence the number $\frac{n(n+1)}{2}$ has to be more than two digits. This means that $n\ge 14$. We check then the numbers $16, 20, 21, 29, 31, 33, 35, 39$ and we see that the first one where 8 is the second last digit of $1+2+ \dots +n$ is $39$.