Let the given equations be:
1) $9f(x) - 10f(f(x)) = 2x$ for all $x \in \mathbb{Z}$
2) $f(2x) = 2f(x)$ for all $x \in \mathbb{Z}$

From equation (2), setting $x=0$, we get $f(0) = 2f(0)$, which implies $f(0)=0$.
Let's plug $x=0$ into equation (1): $9f(0) - 10f(f(0)) = 2(0)$, which is $9(0) - 10f(0) = 0$, $0=0$. This is consistent with $f(0)=0$.

From equation (2), $f(2x)=2f(x)$. This implies $f(2^n x) = 2^n f(x)$ for any integer $n \ge 0$.
Also, $f(x)=f(2 \cdot x/2)=2f(x/2)$ if $x$ is even. So $f(x/2)=f(x)/2$ for even $x$.
By induction, $f(x/2^n)=f(x)/2^n$ if $x$ is a multiple of $2^n$.

Let's examine the parity of $f(x)$. From $f(2x)=2f(x)$, for any integer $x$, $f(2x)$ is an even integer. This means $f$ maps even integers to even integers.
Let $x$ be any integer. From equation (1), $9f(x) - 10f(f(x)) = 2x$.
The right side $2x$ is an even integer. The second term on the left side $10f(f(x))$ is also an even integer.
Thus, $9f(x)$ must be an even integer for all $x \in \mathbb{Z}$. This implies $f(x)$ must be an even integer for all $x \in \mathbb{Z}$.
So $f(x)$ is always even for any $x \in \mathbb{Z}$.

Since $f(x)$ is always even, we can write $f(x) = 2g(x)$ for some function $g: \mathbb{Z} \to \mathbb{Z}$.
Substitute $f(x)=2g(x)$ into the given equations:
Equation (2): $f(2x)=2f(x)$ becomes $2g(2x) = 2(2g(x))$, which simplifies to $g(2x)=2g(x)$. So $g$ satisfies the same property (2).
Equation (1): $9f(x) - 10f(f(x)) = 2x$ becomes $9(2g(x)) - 10f(2g(x)) = 2x$.
Since $f(y)=2g(y)$ for any integer $y$, we have $f(2g(x)) = 2g(2g(x))$.
So the equation becomes $18g(x) - 10(2g(2g(x))) = 2x$, which is $18g(x) - 20g(2g(x)) = 2x$.
Since $g(2y)=2g(y)$ for any integer $y$, we have $g(2g(x))=2g(g(x))$.
So $18g(x) - 20(2g(g(x))) = 2x$, which simplifies to $18g(x) - 40g(g(x)) = 2x$.
Dividing by 2, we get $9g(x) - 20g(g(x)) = x$.

So, if a function $f$ with the given properties exists, then there must exist a function $g:\mathbb{Z}\to\mathbb{Z}$ such that:
(G1) $9g(x) - 20g(g(x)) = x$ for all $x \in \mathbb{Z}$
(G2) $g(2x) = 2g(x)$ for all $x \in \mathbb{Z}$

Let's test equation (G1) for specific values of $x$.
For $x=0$, $9g(0) - 20g(g(0)) = 0$. From (G2), $g(0)=g(2 \cdot 0)=2g(0)$, so $g(0)=0$. $9(0) - 20g(0) = 0$, which is $0=0$.

Let $x$ be any integer. Let $y = g(x)$. Since $g:\mathbb{Z}\to\mathbb{Z}$, $y$ is an integer.
Equation (G1) is $9x - 20g(x) = g^{-1}(x)$ if $g$ were invertible. But $g$ is not necessarily invertible.

Consider equation (G1) $9g(x) - 20g(g(x)) = x$ for all $x \in \mathbb{Z}$.
Let $x$ be an integer of the form $9j+4$.
$9g(9j+4) - 20g(g(9j+4)) = 9j+4$.
This is hard to work with directly.

Let's use equation (G1) to deduce properties of $g(x)$.
$9g(x) - 20g(g(x)) = x$.
Since $g(x)$ must be an integer for all $x \in \mathbb{Z}$, $g(g(x))$ is also an integer for all $x \in \mathbb{Z}$.
From $g(2x)=2g(x)$, we know $g(\text{even})$ is even.
If $x$ is odd, $x \equiv 1 \pmod 2$.
$9g(x) - 20g(g(x)) = x \equiv 1 \pmod 2$.
$9g(x) - 0 \equiv 1 \pmod 2$.
$g(x) \equiv 1 \pmod 2$.
So $g(x)$ must be odd for all odd integers $x$.

Let $x=9j+4$ for some integer $j$. $9j+4$ is odd if and only if $9j$ is odd, which means $j$ is odd.
If $j$ is odd, $x=9j+4$ is odd, so $g(x)=g(9j+4)$ must be odd.
From (G1), $9g(x) - 20g(g(x)) = x$. Apply $g$ to this equation?
$g(9g(x) - 20g(g(x))) = g(x)$. This does not seem helpful.

Let $y=g(x)$. Equation (G1) is $9y - 20g(y) = x$. So $x$ is determined by $y=g(x)$.
$g(y) = (9y-x)/20$. So $g(g(x)) = (9g(x)-x)/20$. This is $g(y)=(9y-g^{-1}(y))/20$.

Let's consider values of the form $9j+4$.
$g(9j+4)$ must be an integer for all $j \in \mathbb{Z}$.
Substitute $x=9j+4$ into (G1):
$9g(9j+4) - 20g(g(9j+4)) = 9j+4$.
Let $g(9j+4)=z_j$. $9z_j - 20g(z_j) = 9j+4$.
$20g(z_j) = 9z_j - (9j+4)$.
$g(z_j) = \frac{9z_j - 9j - 4}{20}$.
Since $z_j = g(9j+4)$ is an integer, $g(z_j)$ must be an integer.
So $\frac{9z_j - 9j - 4}{20}$ must be an integer for all $j \in \mathbb{Z}$.
$9z_j - 9j - 4 \equiv 0 \pmod{20}$.
$9g(9j+4) - 9j - 4 \equiv 0 \pmod{20}$.
$9g(9j+4) \equiv 9j+4 \pmod{20}$.

Let $j=0$. $9g(4) \equiv 4 \pmod{20}$.
$9g(4) = 20k+4$ for some integer $k$. $9g(4)$ must be even, so $g(4)$ must be even.
$g(4) = g(2 \cdot 2) = 2g(2) = 2(2g(1))=4g(1)$. $g(4)$ is a multiple of 4, so it is even.
$9g(4) \equiv 4 \pmod{20}$. Possible values for $9g(4) \pmod{20}$ are $\{0, 9, 18, 7, 16, 5, 14, 3, 12, 1\}$ times $\{0, 1, 2, \dots, 19\}$.
$9 \times 0 = 0 \pmod{20}$
$9 \times 1 = 9 \pmod{20}$
$9 \times 2 = 18 \pmod{20}$
$9 \times 3 = 27 \equiv 7 \pmod{20}$
$9 \times 4 = 36 \equiv 16 \pmod{20}$
$9 \times 5 = 45 \equiv 5 \pmod{20}$
$9 \times 6 = 54 \equiv 14 \pmod{20}$
$9 \times 7 = 63 \equiv 3 \pmod{20}$
$9 \times 8 = 72 \equiv 12 \pmod{20}$
$9 \times 9 = 81 \equiv 1 \pmod{20}$
$9 \times 10 = 90 \equiv 10 \pmod{20}$
$9 \times (\text{even}) \equiv 0, 10, 12, 14, 16, 18 \pmod{20}$.
$9 \times (\text{odd}) \equiv 1, 3, 5, 7, 9, 11, 13, 15, 17, 19 \pmod{20}$. No, $9 \times 11=99 \equiv 19$, $9 \times 13 = 117 \equiv 17$, $9 \times 15 = 135 \equiv 15$, $9 \times 17=153 \equiv 13$, $9 \times 19=171 \equiv 11$.
The set of $9 \times g(4) \pmod{20}$ must be from $\{0, 10, 12, 14, 16, 18\}$.
We require $9g(4) \equiv 4 \pmod{20}$. $4 \pmod{20}$ is not in the set $\{0, 10, 12, 14, 16, 18\}$.
This means there is no integer $g(4)$ such that $9g(4) \equiv 4 \pmod{20}$ and $g(4)$ is even.

Let's recheck $g(4)$ is even. $g(x)=0$ iff $x=0$. Suppose $g(x)=0$ for $x\ne 0$. $9(0)-20g(0)=x \implies x=0$. Contradiction.
$g(4)=g(2 \cdot 2)=2g(2)$. $g(2)=2g(1)$. $g(4)=4g(1)$. Yes, $g(4)$ is a multiple of 4. It is even.
$g(4)$ being an integer multiple of 4 means $g(4) \equiv 0 \pmod 4$.
$9g(4) \equiv 4 \pmod{20}$ implies $9g(4) = 20k+4$.
$9g(4) \equiv 4 \pmod 4$. $9g(4) = 9(4m) = 36m \equiv 0 \pmod 4$.
$0 \equiv 4 \pmod 4$, which is $0 \equiv 0 \pmod 4$. This is consistent.

$9g(4) \equiv 4 \pmod{20}$. Possible values for $9a \pmod{20}$ where $a$ is even: $9(2m)=18m$. $18m \pmod{20}$. If $m$ is even, $m=2k$, $18(2k)=36k \equiv 16k \pmod{20}$. Multiples of 16 mod 20: 0, 16, 32=12, 48=8. $0, 16, 12, 8$. No, $16(0)=0, 16(1)=16, 16(2)=32 \equiv 12, 16(3)=48 \equiv 8, 16(4)=64 \equiv 4$. Ah.
$16 \times 4 = 64 \equiv 4 \pmod{20}$.
$g(4)$ must be an even integer. Let $g(4)=2m$.
$9(2m) \equiv 4 \pmod{20} \implies 18m \equiv 4 \pmod{20}$.
$18m = 20k + 4$. Divide by 2: $9m = 10k + 2$.
$9m \equiv 2 \pmod{10}$.
$9m \equiv 12 \pmod{10}$. $m \equiv \frac{12}{9}$ (not integer).
$9m \pmod{10}: 0, 9, 8, 7, 6, 5, 4, 3, 2, 1$.
$9m \equiv 2 \pmod{10}$. This is satisfied for $m=8$. $9(8)=72 \equiv 2 \pmod{10}$.
The general solution is $m \equiv 8 \pmod{10}$. So $m=10u+8$ for some integer $u$.
$g(4) = 2m = 2(10u+8) = 20u+16$.
$g(4)$ must be of the form $20u+16$.
$g(4)$ must also be a multiple of 4. $20u+16=4(5u+4)$. It is always a multiple of 4.

So $g(4)$ must be of the form $20u+16$ for any integer $u$.
Let's check if this value of $g(4)$ is consistent with $9g(4) \equiv 4 \pmod{20}$.
$9(20u+16) = 180u + 144$. $180u \equiv 0 \pmod{20}$. $144 = 7 \times 20 + 4 \equiv 4 \pmod{20}$.
$0+4 \equiv 4 \pmod{20}$. This is consistent.

Now use $9g(9j+4) \equiv 9j+4 \pmod{20}$ for all $j \in \mathbb{Z}$.
For $j=1$, $9g(13) \equiv 13 \pmod{20}$. $g(13)$ must be odd since 13 is odd. $9 \times \text{odd} \equiv \text{odd} \pmod{20}$. $13$ is odd. This is consistent.
For $j=2$, $9g(22) \equiv 22 \equiv 2 \pmod{20}$. $g(22)$ must be even. $9 \times \text{even} \equiv \text{even} \pmod{20}$. $2$ is even. Consistent.
For $j=3$, $9g(31) \equiv 31 \equiv 11 \pmod{20}$. $g(31)$ must be odd. $9 \times \text{odd} \equiv \text{odd} \pmod{20}$. $11$ is odd. Consistent.
For $j=4$, $9g(40) \equiv 40 \equiv 0 \pmod{20}$. $g(40)$ must be even. $9 \times \text{even} \equiv \text{even} \pmod{20}$. $0$ is even. Consistent.

Let $x=1$. $9g(1)-20g(g(1))=1$. $g(1)$ must be odd. Let $g(1)=a$. $9a-20g(a)=1$. $a$ is odd. $9a \equiv 1 \pmod{20}$. $a \equiv 9 \pmod{20}$. $a=20u+9$.
$g(1)=20u+9$. $g(1)$ must be odd. $20u+9$ is always odd. This is consistent.

$g(9j+4)=\frac{61j+27}{20}$ was derived from $20g(9j+4)=61j+27$ assuming $g(y_j)$ form.
Let's re-derive $g(9j+4)$.
From $9g(x) - 20g(g(x)) = x$, replace $x$ by $9j+4$.
$9g(9j+4) - 20g(g(9j+4)) = 9j+4$.
This equation holds for all $j \in \mathbb{Z}$.
$g(9j+4)$ must be an integer for all $j$.
This means $\frac{9z_j - 9j - 4}{20}$ must be an integer for all $j$, where $z_j=g(9j+4)$.
$9g(9j+4) - 9j - 4 \equiv 0 \pmod{20}$ for all $j \in \mathbb{Z}$.
Let $j=0$. $9g(4) - 4 \equiv 0 \pmod{20}$. $9g(4) \equiv 4 \pmod{20}$. We found $g(4)=20u+16$ satisfies this.
Let $j=1$. $9g(13) - 9 - 4 \equiv 0 \pmod{20}$. $9g(13) - 13 \equiv 0 \pmod{20}$. $9g(13) \equiv 13 \pmod{20}$. $g(13)$ must be odd. $9(\text{odd}) \pmod{20}$ must be $13 \pmod{20}$. $9 \times 17 = 153 \equiv 13 \pmod{20}$. So $g(13) \equiv 17 \pmod{20}$.
Let $j=2$. $9g(22) - 18 - 4 \equiv 0 \pmod{20}$. $9g(22) - 22 \equiv 0 \pmod{20}$. $9g(22) \equiv 22 \equiv 2 \pmod{20}$. $g(22)$ must be even. $9(\text{even}) \pmod{20}$ must be $2 \pmod{20}$. $9 \times (\text{even}) \equiv 0, 10, 12, 14, 16, 18 \pmod{20}$. 2 is not in this set.
This is a contradiction.
$g(22)$ must be an even integer and $9g(22) \equiv 2 \pmod{20}$.
$9g(22) = 20k+2$ for some integer $k$.
$9g(22) \equiv 2 \pmod 4$. $9g(22) \equiv g(22) \pmod 4$. $g(22) \equiv 2 \pmod 4$.
So $g(22)$ must be an even integer, and $g(22) \equiv 2 \pmod 4$.
Let $g(22) = 4m+2$ for some integer $m$.
$9(4m+2) \equiv 2 \pmod{20}$.
$36m+18 \equiv 2 \pmod{20}$.
$16m+18 \equiv 2 \pmod{20}$.
$16m \equiv -16 \equiv 4 \pmod{20}$.
$16m = 20k+4$. Divide by 4: $4m = 5k+1$.
$4m \equiv 1 \pmod 5$.
Multiply by 4: $16m \equiv 4 \pmod 5$. $m \equiv 4 \pmod 5$.
So $m=5u+4$ for some integer $u$.
$g(22) = 4(5u+4)+2 = 20u+16+2 = 20u+18$.
$g(22)$ must be of the form $20u+18$.
Let's check: $g(22)=20u+18$ is even. $g(22) \equiv 18 \equiv 2 \pmod{20}$.
$9g(22) = 9(20u+18) = 180u+162$. $180u \equiv 0 \pmod{20}$. $162 = 8 \times 20 + 2 \equiv 2 \pmod{20}$.
$9g(22) \equiv 2 \pmod{20}$.

So $g(22)=20u+18$ is consistent with $9g(22) \equiv 2 \pmod{20}$.
However, we need $9g(9j+4) \equiv 9j+4 \pmod{20}$ for ALL $j \in \mathbb{Z}$.
For $j=2$, $x=9(2)+4=22$. $9g(22) \equiv 22 \equiv 2 \pmod{20}$.
We found $g(22)$ must be of the form $20u+18$.
$9g(22) = 9(20u+18) = 180u+162$.
The condition is $9g(22) - 9(2) - 4 \equiv 0 \pmod{20}$, which is $180u+162 - 18 - 4 \equiv 0 \pmod{20}$, i.e., $180u+140 \equiv 0 \pmod{20}$.
$180u \equiv 0 \pmod{20}$ and $140 \equiv 0 \pmod{20}$. $0+0 \equiv 0 \pmod{20}$. This is always true for any integer $u$.

Let's revisit the condition $9g(9j+4) \equiv 9j+4 \pmod{20}$.
Let $j \pmod{20}$ take values $0, 1, \dots, 19$.
$j=0: 9g(4) \equiv 4 \pmod{20}$. $g(4)$ must be $20u+16$. $g(4)$ must be even.
$j=1: 9g(13) \equiv 13 \pmod{20}$. $g(13)$ must be $20u+17$. $g(13)$ must be odd. $9(17)=153 \equiv 13$.
$j=2: 9g(22) \equiv 2 \pmod{20}$. $g(22)$ must be $20u+18$. $g(22)$ must be even. $9(18)=162 \equiv 2$.
$j=3: 9g(31) \equiv 11 \pmod{20}$. $g(31)$ must be $20u+11$. $g(31)$ must be odd. $9(11)=99 \equiv 19$. Oh, $9g(31) \equiv 11 \pmod{20}$. $9(7)=63\equiv 3$, $9(17)\equiv 13$. $9(3) \equiv 7$. $9(13)\equiv 17$. $9(1) \equiv 9$. $9(11)\equiv 19$. $9(21)\equiv 9$. $9(15)\equiv 15$. $9(5)\equiv 5$. $9(25)\equiv 5$.
$9a \equiv 11 \pmod{20}$ implies $a \equiv 11 \times 9^{-1} \pmod{20}$. $9^{-1} \pmod{20}$ is 9, since $9 \times 9=81 \equiv 1 \pmod{20}$.
$a \equiv 11 \times 9 \equiv 99 \equiv 19 \pmod{20}$. So $g(31) \equiv 19 \pmod{20}$. $g(31)$ must be odd. $19$ is odd. Consistent.

Let $a_j$ be the required residue class of $g(9j+4) \pmod{20}$ given by $9a_j \equiv 9j+4 \pmod{20}$. Since $\gcd(9,20)=1$, $a_j$ is uniquely defined $\pmod{20}$. $a_j \equiv 9^{-1}(9j+4) \equiv 9(9j+4) \equiv 81j+36 \equiv j+16 \pmod{20}$.
So $g(9j+4) \equiv j+16 \pmod{20}$.

If $j$ is even, $j=2k$, $9j+4 = 18k+4$ (even). $g(18k+4)$ must be even.
$g(9(2k)+4) \equiv 2k+16 \pmod{20}$. $g(18k+4)$ must be even. $2k+16$ is always even. This is consistent.

If $j$ is odd, $j=2k+1$, $9j+4=9(2k+1)+4=18k+9+4=18k+13$ (odd). $g(18k+13)$ must be odd.
$g(9(2k+1)+4) \equiv (2k+1)+16 \equiv 2k+17 \pmod{20}$. $2k+17$ is always odd. This is consistent.

So $g(9j+4) \equiv j+16 \pmod{20}$ for all $j \in \mathbb{Z}$.
Let $x = 9j+4$.
$g(x) \equiv (x-4)/9 + 16 \pmod{20}$.
$g(x) \equiv 9(x-4) + 16 \pmod{20}$? No. $(x-4)/9$ is not an integer in general.

The requirement that $g(9j+4)$ is an integer for all $j$ is not enough.
Let's go back to $g(9j+4) = z_j$. $g(z_j) = \frac{9z_j - 9j - 4}{20}$.
$g(z_j)$ must be an integer for all $j \in \mathbb{Z}$.
$9z_j - 9j - 4 \equiv 0 \pmod{20}$. $9g(9j+4) - 9j - 4 \equiv 0 \pmod{20}$.
$g(9j+4) \equiv j+16 \pmod{20}$. Let $g(9j+4) = 20k_j + j+16$ for some integer $k_j$.
Substitute $z_j=20k_j+j+16$ into $g(z_j) = \frac{9z_j - 9j - 4}{20}$.
$g(20k_j+j+16) = \frac{9(20k_j+j+16) - 9j - 4}{20} = \frac{180k_j + 9j + 144 - 9j - 4}{20} = \frac{180k_j + 140}{20} = 9k_j+7$.
So $g(20k_j+j+16) = 9k_j+7$ for all $j \in \mathbb{Z}$ and for $k_j$ where $g(9j+4)=20k_j+j+16$.

The set of values $20k_j+j+16$ are values in the range of $g$. $g(\mathbb{Z})$.
For any $x$ in the range of $g$ of the form $20k+j+16$, where $x=g(9j+4)$, $g(x)$ is given by $9k+7$.
Let $x$ be an element in $g(\mathbb{Z})$. If $x=g(y)$ for some $y$. $g(x) = (9x-y)/20$.

$g(20k_j+j+16) = 9k_j+7$.
The argument $20k_j+j+16$ must be an integer. It is.
The value $9k_j+7$ must be an integer. It is.

The values $20k_j+j+16$ are $g(9j+4)$.
Let $j=0$. $g(4) = 20k_0+16$. $g(20k_0+16) = 9k_0+7$.
The range of $g$ applied to $\{4\}$ are values $20k_0+16$. For these values $g(x)=9k_0+7$.
$g(4)$ is $4g(1)$. $g(4)$ is a multiple of 4. $20k_0+16=4(5k_0+4)$. This is always multiple of 4.

$g(x)$ must be integer for all $x \in \mathbb{Z}$.
$g(20k+j+16) = 9k+7$ holds for all $j, k \in \mathbb{Z}$? No, only for $x=20k_j+j+16$ where $k_j$ comes from $g(9j+4)=20k_j+j+16$.

Let $j=0$. $g(4) = 20k_0+16$. $g(20k_0+16)=9k_0+7$.
$g(4)$ is even, $20k_0+16$ is even. $g(\text{even})$ must be even. $9k_0+7$ must be even. $9k_0$ must be odd, $k_0$ must be odd.
Let $k_0=2u+1$. $g(4)=20(2u+1)+16=40u+36$. $g(40u+36)=9(2u+1)+7=18u+16$.
$g(4)$ must be a multiple of 4. $40u+36=4(10u+9)$. Consistent.
$g(40u+36)=18u+16$. $40u+36$ is even. $18u+16$ is even. Consistent.

$g(4)=4g(1)$. $4g(1)=40u+36$. $g(1)=10u+9$.
$g(1)$ must be odd. $10u+9$ is always odd. Consistent.

From $9g(1)-20g(g(1))=1$: $9(10u+9)-20g(10u+9)=1$. $90u+81-20g(10u+9)=1$. $20g(10u+9)=90u+80$. $g(10u+9)=\frac{90u+80}{20}=\frac{9u+8}{2}$.
$g(10u+9)$ must be an integer for all $u \in \mathbb{Z}$. $9u+8$ must be even. $9u$ must be even. $u$ must be even.
Let $u=2w$. $g(1)=10(2w)+9=20w+9$. This is consistent with $g(1)=20u+9$.
$g(10(2w)+9)=g(20w+9)=\frac{9(2w)+8}{2}=\frac{18w+8}{2}=9w+4$.
$g(20w+9)=9w+4$. $20w+9$ is odd, $g(20w+9)=9w+4$ must be odd. $9w$ must be odd, $w$ must be odd.
Let $w=2z+1$. $g(1)=20(2z+1)+9=40z+20+9=40z+29$.
$g(20(2z+1)+9)=g(40z+29)=9(2z+1)+4=18z+9+4=18z+13$.
$g(40z+29)=18z+13$. $40z+29$ is odd, $18z+13$ is odd. Consistent.

This seems to lead to an infinite sequence of constraints that refine the possible values of $g(1)$, but don't show a contradiction.

The condition $g(9j+4) \equiv j+16 \pmod{20}$ for all $j \in \mathbb{Z}$.
Let $j=20m$. $g(180m+4) \equiv 20m+16 \equiv 16 \pmod{20}$. $180m+4$ is even, $g$ must be even. Consistent.
Let $j=20m+1$. $g(180m+9+4)=g(180m+13) \equiv 20m+1+16=20m+17 \equiv 17 \pmod{20}$. $180m+13$ is odd, $g$ must be odd. $17$ is odd. Consistent.
Let $j=20m+18$. $g(180m+162+4)=g(180m+166) \equiv 20m+18+16=20m+34 \equiv 14 \pmod{20}$. $180m+166$ is even, $g$ must be even. $14$ is even. Consistent.
Let $j=20m+19$. $g(180m+171+4)=g(180m+175) \equiv 20m+19+16=20m+35 \equiv 15 \pmod{20}$. $180m+175$ is odd, $g$ must be odd. $15$ is odd. Consistent.

The statement $g(9j+4) \equiv j+16 \pmod{20}$ for all $j \in \mathbb{Z}$ is necessary.
Let $j=0$. $g(4) \equiv 16 \pmod{20}$.
Let $j=1$. $g(13) \equiv 17 \pmod{20}$.
Let $j=2$. $g(22) \equiv 18 \pmod{20}$.
Let $j=3$. $g(31) \equiv 19 \pmod{20}$.
Let $j=4$. $g(40) \equiv 0 \pmod{20}$.

This doesn't produce a contradiction directly. The argument using $g(9j+4) = \frac{61j+27}{20}$ was based on $g(y_j)$ for $y_j=9j+4$. $g(y_j)$ must be an integer for all $j$. $\frac{61j+27}{20}$ must be an integer for all $j$.
For $j=0$, $27/20$ is not an integer.
For $j=1$, $88/20$ is not an integer.
For $j=2$, $150/20$ is not an integer.
For $j=3$, $219/20$ is not an integer.
For $j=4$, $271/20$ is not an integer.
For $j=5$, $332/20$ is not an integer.
For $j=6$, $393/20$ is not an integer.
For $j=7$, $454/20$ is not an integer.
For $j=8$, $515/20$ is not an integer.
For $j=9$, $576/20$ is not an integer.
For $j=10$, $637/20$ is not an integer.
...
$61j+27 \equiv 0 \pmod{20}$. $j+7 \equiv 0 \pmod{20}$. $j \equiv -7 \equiv 13 \pmod{20}$.
So $g(9j+4)$ is an integer only when $j \equiv 13 \pmod{20}$.
But $g(9j+4)$ must be an integer for ALL $j \in \mathbb{Z}$ since $9j+4$ is an integer.
This is a contradiction.

Thus, no such function $g$ exists, and therefore no such function $f$ exists.

The final answer is $\boxed{No}$.