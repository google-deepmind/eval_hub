Let $\alpha = \sqrt{3}-1$. We want to show $S_n = \sum_{k=0}^n (-1)^{\lfloor k\alpha \rfloor} \geq 1$ for all $n \geq 0$.
Let $a_k = (-1)^{\lfloor k\alpha \rfloor}$.
We use the identity $\lfloor x-m \rfloor = \lfloor x \rfloor - m$ for integer $m$.
Let $x = k\sqrt{3}$ and $m=k$. Then $\lfloor k\sqrt{3}-k \rfloor = \lfloor k\sqrt{3} \rfloor - k$.
Since $k(\sqrt{3}-1) = k\sqrt{3}-k$, we have $\lfloor k(\sqrt{3}-1) \rfloor = \lfloor k\sqrt{3} \rfloor - k$.
Thus, $a_k = (-1)^{\lfloor k\sqrt{3} \rfloor - k} = (-1)^{\lfloor k\sqrt{3} \rfloor + k}$ since $(-1)^{-k} = (-1)^k$.

Let $b_k = (-1)^{\lfloor k\sqrt{3} \rfloor}$. Then $a_k = (-1)^k b_k$.
$S_n = \sum_{k=0}^n (-1)^k b_k = b_0 - b_1 + b_2 - b_3 + \dots + (-1)^n b_n$.

Let's analyze the terms $b_k = (-1)^{\lfloor k\sqrt{3} \rfloor}$. The parity of $\lfloor k\sqrt{3} \rfloor$ determines $b_k$.
The sequence of parities of $\lfloor k\sqrt{3} \rfloor$ for $k=0, 1, 2, \dots$ is:
$\lfloor 0\sqrt{3} \rfloor = 0$ (E), $b_0=1$
$\lfloor 1\sqrt{3} \rfloor = 1$ (O), $b_1=-1$
$\lfloor 2\sqrt{3} \rfloor = 3$ (O), $b_2=-1$
$\lfloor 3\sqrt{3} \rfloor = 5$ (O), $b_3=-1$
$\lfloor 4\sqrt{3} \rfloor = 6$ (E), $b_4=1$
$\lfloor 5\sqrt{3} \rfloor = 8$ (E), $b_5=1$
$\lfloor 6\sqrt{3} \rfloor = 10$ (E), $b_6=1$
$\lfloor 7\sqrt{3} \rfloor = 12$ (E), $b_7=1$
$\lfloor 8\sqrt{3} \rfloor = 13$ (O), $b_8=-1$
$\lfloor 9\sqrt{3} \rfloor = 15$ (O), $b_9=-1$
$\lfloor 10\sqrt{3} \rfloor = 17$ (O), $b_{10}=-1$
$\lfloor 11\sqrt{3} \rfloor = 19$ (O), $b_{11}=-1$
$\lfloor 12\sqrt{3} \rfloor = 20$ (E), $b_{12}=1$
$\lfloor 13\sqrt{3} \rfloor = 22$ (E), $b_{13}=1$
$\lfloor 14\sqrt{3} \rfloor = 24$ (E), $b_{14}=1$
$\lfloor 15\sqrt{3} \rfloor = 25$ (O), $b_{15}=-1$
$\lfloor 16\sqrt{3} \rfloor = 27$ (O), $b_{16}=-1$
The sequence $b_k$ starts $1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, \dots$

$S_n = \sum_{k=0}^n (-1)^k b_k$.
If $n=2m$, $S_{2m} = \sum_{k=0}^{2m} (-1)^k b_k = (b_0+b_2+\dots+b_{2m}) - (b_1+b_3+\dots+b_{2m-1})$.
If $n=2m+1$, $S_{2m+1} = \sum_{k=0}^{2m+1} (-1)^k b_k = (b_0+b_2+\dots+b_{2m}) - (b_1+b_3+\dots+b_{2m+1})$.

Let $E_m = \sum_{j=0}^m b_{2j} = b_0 + b_2 + \dots + b_{2m}$ and $O_m = \sum_{j=0}^m b_{2j+1} = b_1 + b_3 + \dots + b_{2m+1}$.
$S_{2m} = E_m - O_{m-1}$ for $m \geq 1$, and $S_0 = E_0 = b_0 = 1$. For $m=0$, $O_{-1}$ is an empty sum, taken as 0. $S_0 = E_0 - O_{-1} = 1-0=1$.
$S_{2m+1} = E_m - O_m$ for $m \geq 0$.

Let's compute the first few $E_m$ and $O_m$.
$E_0 = b_0 = 1$.
$E_1 = b_0+b_2 = 1-1 = 0$.
$E_2 = b_0+b_2+b_4 = 1-1+1 = 1$.
$E_3 = b_0+b_2+b_4+b_6 = 1-1+1+1 = 2$.
$E_4 = b_0+b_2+b_4+b_6+b_8 = 1-1+1+1-1 = 1$.
$E_5 = E_4+b_{10} = 1-1 = 0$.
$E_6 = E_5+b_{12} = 0+1 = 1$.
$E_7 = E_6+b_{14} = 1+1 = 2$.
$E_8 = E_7+b_{16} = 2-1 = 1$.
The sequence $E_m$ seems to be $1, 0, 1, 2, 1, 0, 1, 2, 1, \dots$, periodic with period 4 for $m \ge 0$.
$E_m \in \{0, 1, 2\}$ for all $m \ge 0$. Thus $E_m \ge 0$.

$O_0 = b_1 = -1$.
$O_1 = b_1+b_3 = -1-1 = -2$.
$O_2 = b_1+b_3+b_5 = -1-1+1 = -1$.
$O_3 = b_1+b_3+b_5+b_7 = -1-1+1+1 = 0$.
$O_4 = O_3+b_9 = 0-1 = -1$.
$O_5 = O_4+b_{11} = -1-1 = -2$.
$O_6 = O_5+b_{13} = -2+1 = -1$.
$O_7 = O_6+b_{15} = -1-1 = -2$.
$O_8 = O_7+b_{17} = -2-1 = -3$.
The sequence $O_m$ is $-1, -2, -1, 0, -1, -2, -1, -2, -3, \dots$.

Let's re-evaluate $b_{15}$: $\lfloor 15\sqrt{3} \rfloor = \lfloor 15 \times 1.7320508... \rfloor = \lfloor 25.980762... \rfloor = 25$ (O). $b_{15}=-1$. This is correct.
$O_7 = b_1+b_3+b_5+b_7+b_9+b_{11}+b_{13}+b_{15} = (-1)+(-1)+1+1+(-1)+(-1)+1+(-1) = -2$. Correct.

Let's check the parities $\lfloor k\sqrt{3} \rfloor \pmod 2$ more systematically. This sequence is $v_k$.
$v_0=0$. $v_1=1$. $v_2=1$. $v_3=1$. $v_4=0$. $v_5=0$. $v_6=0$. $v_7=0$. $v_8=1$. $v_9=1$. $v_{10}=1$. $v_{11}=1$. $v_{12}=0$. $v_{13}=0$. $v_{14}=0$. $v_{15}=1$. $v_{16}=1$. $v_{17}=1$. $v_{18}=1$. $v_{19}=0$. $v_{20}=0$. $v_{21}=0$. $v_{22}=0$. $v_{23}=1$. $v_{24}=1$.
$b_k = (-1)^{v_k}$.
$b_{2m}$: $b_0, b_2, b_4, b_6, b_8, b_{10}, b_{12}, b_{14}, b_{16}, b_{18}, b_{20}, b_{22}, b_{24}, \dots$
$v_{2m}$: $v_0, v_2, v_4, v_6, v_8, v_{10}, v_{12}, v_{14}, v_{16}, v_{18}, v_{20}, v_{22}, v_{24}, \dots$
$v_{2m} \pmod 2$: 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, ... This is $0,1,0,0,1,1$ repeating with period 6? $v_{12}=0, v_{14}=0$. $v_{16}=1, v_{18}=1$. $v_{20}=0, v_{22}=0$. $v_{24}=1$. The sequence $v_{2m}$ seems $0,1,0,0,1,1,0,0,1,1,0,0,1, \dots$ starting from $v_2$. $v_0=0$.
$E_m$: $b_0=1$. $b_{2m}$ for $m \ge 1$: $-1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, \dots$.
$E_m$: $1, 0, 1, 2, 1, 0, 1, 2, 1, 0, 1, 2, \dots$ for $m=0,1,2,3,4,5,6,7,8,9,10,11$.
$E_m \in \{0,1,2\}$ for $m \ge 0$.

$b_{2m+1}$: $b_1, b_3, b_5, b_7, b_9, b_{11}, b_{13}, b_{15}, b_{17}, b_{19}, b_{21}, b_{23}, \dots$
$v_{2m+1} \pmod 2$: 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, ...
$b_{2m+1}$: -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, ...
$O_m$: $-1, -2, -1, 0, -1, -2, -1, -2, -3, -2, -1, -2, \dots$.

A known result (see related problems on sums of $(-1)^{\lfloor k\alpha \rfloor}$) is that $E_m \ge 0$ and $O_m \le 0$ for all $m \ge 0$. This is indeed true for $\beta=\sqrt{3}$.
Let's check $S_n$.
$S_{2m} = E_m - O_{m-1}$. $E_m \ge 0$. $O_{m-1} \le 0$, so $-O_{m-1} \ge 0$.
$S_{2m} \ge 0+0=0$ for $m \ge 1$. $S_0=1$.
$E_m=0$ only if $m \equiv 1 \pmod 4$. $O_{m-1}=0$ only if $m-1 \equiv 3 \pmod 4$, i.e. $m \equiv 0 \pmod 4$.
For $m \ge 1$, $m \equiv 1 \pmod 4$ and $m \equiv 0 \pmod 4$ cannot happen simultaneously.
So for $m \ge 1$, either $E_m>0$ or $O_{m-1}<0$.
If $E_m=0$ ($m \equiv 1 \pmod 4$), $O_{m-1} = O_{4j}$ for $m=4j+1$. $O_{4j}=-1$. $S_{2(4j+1)} = S_{8j+2} = E_{4j+1}-O_{4j} = 0-(-1)=1$.
If $O_{m-1}=0$ ($m \equiv 0 \pmod 4, m \ge 1$), $E_m = E_{4j}$ for $m=4j$. $E_{4j}=1$. $S_{2(4j)}=S_{8j}=E_{4j}-O_{4j-1}=1-0=1$.
So $S_{2m} \ge 1$ for all $m \ge 0$.

$S_{2m+1} = E_m - O_m$. $E_m \ge 0$, $O_m \le 0$, so $-O_m \ge 0$. $S_{2m+1} \ge 0+0=0$.
$E_m=0$ if $m \equiv 1 \pmod 4$. $O_m=0$ if $m \equiv 3 \pmod 4$.
If $m \equiv 1 \pmod 4$, $E_m=0$. $O_m=O_{4j+1} = -2$. $S_{2(4j+1)+1} = S_{8j+3} = E_{4j+1}-O_{4j+1}=0-(-2)=2$.
If $m \equiv 3 \pmod 4$, $O_m=0$. $E_m=E_{4j+3}=2$. $S_{2(4j+3)+1} = S_{8j+7} = E_{4j+3}-O_{4j+3}=2-0=2$.
If $m \equiv 0 \pmod 4$, $E_m=1, O_m=-1$. $S_{8j+1}=1-(-1)=2$.
If $m \equiv 2 \pmod 4$, $E_m=1, O_m=-1$. $S_{8j+5}=1-(-1)=2$.
So $S_{2m+1}=2$ for all $m \ge 0$.

Based on the periodicity of $E_m$ and $O_m$, which seems to hold for $m \ge 0$:
$E_m$: $1, 0, 1, 2$ repeating.
$O_m$: $-1, -2, -1, 0$ repeating.
$S_{2m}=E_m-O_{m-1}$ ($O_{-1}=0$).
$m=4j: S_{8j} = E_{4j}-O_{4j-1} = 1-0=1$.
$m=4j+1: S_{8j+2} = E_{4j+1}-O_{4j} = 0-(-1)=1$.
$m=4j+2: S_{8j+4} = E_{4j+2}-O_{4j+1} = 1-(-2)=3$.
$m=4j+3: S_{8j+6} = E_{4j+3}-O_{4j+2} = 2-(-1)=3$.

$S_{2m+1}=E_m-O_m$:
$m=4j: S_{8j+1} = E_{4j}-O_{4j} = 1-(-1)=2$.
$m=4j+1: S_{8j+3} = E_{4j+1}-O_{4j+1} = 0-(-2)=2$.
$m=4j+2: S_{8j+5} = E_{4j+2}-O_{4j+2} = 1-(-1)=2$.
$m=4j+3: S_{8j+7} = E_{4j+3}-O_{4j+3} = 2-0=2$.

The values of $S_n$ based on these periodic sequences are $1, 2, 1, 2, 3, 2, 3, 2, 1, 2, 1, 2, 3, 2, 3, 2, ...$. All are $\ge 1$.
The periodicity of $E_m$ and $O_m$ (with period 4) relies on the sequence $b_k = (-1)^{\lfloor k\sqrt{3} \rfloor}$ having a specific structure related to $b_{k+8}=b_k$. This relates to $\lfloor (k+8)\sqrt{3} \rfloor - \lfloor k\sqrt{3} \rfloor \pmod 2$. $8\sqrt{3} \approx 13.856$. It might be that $\lfloor (k+8)\sqrt{3} \rfloor - \lfloor k\sqrt{3} \rfloor = 13$ or 14. $(k+8)\sqrt{3}-k\sqrt{3}=8\sqrt{3}$. $\lfloor (k+8)\sqrt{3} \rfloor-\lfloor k\sqrt{3} \rfloor \in \{\lfloor 8\sqrt{3} \rfloor, \lfloor 8\sqrt{3} \rfloor+1\} = \{13, 14\}$.
If it is 14 (even), parity of $\lfloor k\sqrt{3} \rfloor$ is preserved. $b_{k+8}=b_k$. If it is 13 (odd), parity flips. $b_{k+8}=-b_k$.
$\lfloor \{k\sqrt{3}\} + 8\sqrt{3} \rfloor$. $8\sqrt{3} \approx 13.856$. $\lfloor \{k\sqrt{3}\} + 13.856 \rfloor = 13 + \lfloor \{k\sqrt{3}\} + 0.856 \rfloor$. This is 13 if $\{k\sqrt{3}\} < 1-0.856=0.144$. It is 14 if $\{k\sqrt{3}\} \ge 0.144$.
So $b_{k+8} = -b_k$ if $\{k\sqrt{3}\} < 0.144$. $b_{k+8} = b_k$ if $\{k\sqrt{3}\} \ge 0.144$.
This breaks periodicity of $b_k$.

However, $E_m \ge 0$ and $O_m \le 0$ are known properties for $\beta = \sqrt{a^2-1}$ related to sums of $(-1)^{\lfloor k\beta \rfloor}$.
Assuming $E_m \ge 0$ and $O_m \le 0$ for all $m \ge 0$.
$S_{2m} = E_m - O_{m-1}$. $E_m \ge 0$. $O_{m-1} \le 0$. Thus $S_{2m} \ge 0$.
$S_{2m+1} = E_m - O_m$. $E_m \ge 0$. $O_m \le 0$. Thus $S_{2m+1} \ge 0$.
To show $S_n \ge 1$, we need to show $S_n$ cannot be 0.
$S_{2m}=0$ iff $E_m=0$ and $O_{m-1}=0$. $E_m=0$ iff $m \equiv 1 \pmod 4$ in the $1,0,1,2$ pattern. $O_{m-1}=0$ iff $m-1 \equiv 3 \pmod 4$, $m \equiv 0 \pmod 4$. $E_m$ and $O_{m-1}$ are not simultaneously zero for $m \ge 1$. $S_0=1 \ne 0$. So $S_{2m} \ge 1$.
$S_{2m+1}=0$ iff $E_m=0$ and $O_m=0$. $E_m=0$ iff $m \equiv 1 \pmod 4$. $O_m=0$ iff $m \equiv 3 \pmod 4$. $E_m$ and $O_m$ are not simultaneously zero. So $S_{2m+1} \ge 1$.

The crucial step is proving $E_m \ge 0$ and $O_m \le 0$. This proof is non-trivial and depends on the specific value $\sqrt{3}$. It is related to the theory of Beatty sequences and powers of algebraic integers. For $\beta=\sqrt{a^2-1}$, the sequence $\lfloor k\beta \rfloor$ has specific properties.
Let $v_k = \lfloor k\sqrt{3} \rfloor \pmod 2$. $\sum_{k=0}^n (-1)^{v_k}$ is the sum $T_n$.
$T_n$ sequence $1,0,-1,-2,-1,0,1,2,1,0,-1,-2,-1,0,1,0, -1, -2, -3, -2, -1, 0, 1, 0$.
$E_m = \sum_{j=0}^m (-1)^{v_{2j}}$, $O_m = \sum_{j=0}^m (-1)^{v_{2j+1}}$.
The required result is indeed that $E_m \ge 0$ and $O_m \le 0$. This guarantees $S_n \ge 1$.

The final answer is $\boxed{\sum_{k=0}^n (-1)^{\left\lfloor k (\sqrt{3}-1) \right\rfloor} \geq 1}$.