We are asked if there exists a function $f:\mathbb{Z}\to\mathbb{Z}$ such that
 \[
 9f(x)-10f(f(x))=2x \quad\text{(1)}
 \]
 \[
 f(2x)=2f(x) \quad\text{(2)}
 \]
 for all $x\in\mathbb{Z}$.

First, let's deduce some properties of $f$.
From (2), setting $x=0$, we get $f(2 \cdot 0) = 2f(0)$, which simplifies to $f(0)=2f(0)$. This implies $f(0)=0$.
Let's check if $f(0)=0$ is consistent with (1). Setting $x=0$ in (1), we get $9f(0) - 10f(f(0)) = 2(0)$, which is $9(0) - 10f(0) = 0$, so $0-10(0)=0$. This is true.

From (2), we can show by induction that $f(2^k x) = 2^k f(x)$ for any non-negative integer $k$.
For $k=0$, $f(2^0 x) = f(x) = 2^0 f(x)$.
Assume $f(2^k x) = 2^k f(x)$ for some $k \ge 0$. Then $f(2^{k+1} x) = f(2(2^k x)) = 2f(2^k x) = 2(2^k f(x)) = 2^{k+1} f(x)$.
This completes the induction.

Let $x=1$ in the property $f(2^k x) = 2^k f(x)$. We get $f(2^k) = 2^k f(1)$. Let $c=f(1)$. Since $f: \mathbb{Z} \to \mathbb{Z}$, $c$ must be an integer.
Then $f(2^k) = c 2^k$ for all $k \ge 0$.

Now let's use equation (1). Set $x=1$:
$9f(1) - 10f(f(1)) = 2(1)$.
$9c - 10f(c) = 2$.
Since $c \in \mathbb{Z}$ and $f(c) \in \mathbb{Z}$, this equation tells us something about $c$.
$9c - 2 = 10f(c)$. This means $9c-2$ must be divisible by 10.
$9c-2 \equiv 0 \pmod{10}$.
Since $9 \equiv -1 \pmod{10}$, we have $-c - 2 \equiv 0 \pmod{10}$, which is $-c \equiv 2 \pmod{10}$.
Multiplying by $-1$, we get $c \equiv -2 \pmod{10}$, or $c \equiv 8 \pmod{10}$.
So, $f(1)$ must be an integer ending in 8.
Also, from $9c-10f(c)=2$, we have $f(c) = \frac{9c-2}{10}$. Since $c \equiv 8 \pmod{10}$, $c=10k+8$ for some integer $k$.
$f(c) = f(10k+8) = \frac{9(10k+8)-2}{10} = \frac{90k+72-2}{10} = \frac{90k+70}{10} = 9k+7$.

Since $c = 10k+8 = 2(5k+4)$, $c$ is always an even integer.
Using property (2), $f(c) = f(2(5k+4)) = 2f(5k+4)$.
So we have $2f(5k+4) = 9k+7$.
The left side is an even integer. Thus, $9k+7$ must be an even integer.
$9k+7 \equiv 0 \pmod 2$.
$k+1 \equiv 0 \pmod 2$.
This implies $k$ must be an odd integer. Let $k=2j+1$ for some integer $j$.

Now we express $c$ and $f(c)$ in terms of $j$.
$c = 10k+8 = 10(2j+1)+8 = 20j+10+8 = 20j+18$.
$f(c) = 9k+7 = 9(2j+1)+7 = 18j+9+7 = 18j+16$.
Let $m = 5k+4 = 5(2j+1)+4 = 10j+5+4 = 10j+9$. Note that $m$ is always odd.
We have $2f(m) = f(c)$, so $2f(10j+9) = 18j+16$.
Dividing by 2, we get $f(10j+9) = 9j+8$.

Now let's use equation (1) with $x=m=10j+9$.
$9f(m) - 10f(f(m)) = 2m$.
$9f(10j+9) - 10f(f(10j+9)) = 2(10j+9)$.
Substitute the expression for $f(10j+9)$:
$9(9j+8) - 10f(9j+8) = 20j+18$.
$81j + 72 - 10f(9j+8) = 20j+18$.
$81j + 72 - 20j - 18 = 10f(9j+8)$.
$61j + 54 = 10f(9j+8)$.
$f(9j+8) = \frac{61j+54}{10}$.

Since $f$ must map integers to integers, $f(9j+8)$ must be an integer for all integers $j$.
This means that $61j+54$ must be divisible by 10 for all $j \in \mathbb{Z}$.
Let's check the condition $61j+54 \equiv 0 \pmod{10}$.
$61j+54 \equiv 1j + 4 \pmod{10}$.
So we require $j+4 \equiv 0 \pmod{10}$ for all $j \in \mathbb{Z}$.
This implies $j \equiv -4 \equiv 6 \pmod{10}$.
This condition is not true for all integers $j$. For example, if we take $j=0$, then $j \not\equiv 6 \pmod{10}$.
For $j=0$, $f(9(0)+8) = f(8) = \frac{61(0)+54}{10} = \frac{54}{10} = 5.4$.
This is not an integer.
However, the problem requires $f(x)$ to be an integer for all $x \in \mathbb{Z}$. We have found that $f(8)$ must be $5.4$ for the equations to hold, which contradicts the requirement that $f$ maps integers to integers.

Therefore, no such function $f:\mathbb{Z}\to\mathbb{Z}$ exists.

Final Answer: The final answer is $\boxed{No}$