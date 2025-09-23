Let $q \in (0,1)$ be a rational number and $q = \frac{a}{b}$ where $a, b$ are integers and $\gcd(a,b)=1$.
Since $q \in (0,1)$, we have $0 < a/b < 1$. We can assume $b > 0$. Then $a$ must be positive as well, so $a > 0$.
The condition $a/b < 1$ implies $a < b$. Since $a,b$ are integers, $a \ge 1$ and $b \ge a+1 \ge 2$.

We want to show $\left|q-\frac{1}{\sqrt{3}}\right| > \frac{1}{9b^2}$.
Substitute $q = \frac{a}{b}$:
\[
\left|\frac{a}{b}-\frac{1}{\sqrt{3}}\right| = \left|\frac{a\sqrt{3}-b}{b\sqrt{3}}\right| = \frac{|a\sqrt{3}-b|}{b\sqrt{3}}.
\]
We need to find a lower bound for $|a\sqrt{3}-b|$.
Consider the expression $a\sqrt{3}-b$. Since $a$ and $b$ are integers and $\sqrt{3}$ is irrational, $a\sqrt{3}-b=0$ if and only if $a=b=0$. However, $a,b$ are positive integers, so $a\sqrt{3}-b \ne 0$.
We can write
\[
|a\sqrt{3}-b| = \frac{|(a\sqrt{3}-b)(a\sqrt{3}+b)|}{|a\sqrt{3}+b|} = \frac{|(a\sqrt{3})^2 - b^2|}{a\sqrt{3}+b} = \frac{|3a^2-b^2|}{a\sqrt{3}+b}.
\]
Since $a$ and $b$ are integers, $3a^2-b^2$ is an integer.
Since $a\sqrt{3}-b \ne 0$, we have $3a^2-b^2 \ne 0$.
Thus, $3a^2-b^2$ is a non-zero integer. This implies $|3a^2-b^2| \ge 1$.
Therefore, we have a lower bound for $|a\sqrt{3}-b|$:
\[
|a\sqrt{3}-b| \ge \frac{1}{a\sqrt{3}+b}.
\]
Now substitute this back into the expression for $\left|q-\frac{1}{\sqrt{3}}\right|$:
\[
\left|q-\frac{1}{\sqrt{3}}\right| = \frac{|a\sqrt{3}-b|}{b\sqrt{3}} \ge \frac{1}{(a\sqrt{3}+b)b\sqrt{3}}.
\]
To prove the original inequality, we need to show that
\[
\frac{1}{(a\sqrt{3}+b)b\sqrt{3}} > \frac{1}{9b^2}.
\]
Since $b>0$ and $a>0$, both denominators are positive. We can cross-multiply:
\[
9b^2 > (a\sqrt{3}+b)b\sqrt{3}.
\]
Since $b>0$, we can divide both sides by $b$:
\[
9b > (a\sqrt{3}+b)\sqrt{3} = 3a + b\sqrt{3}.
\]
Rearranging the inequality to isolate $b/a$:
\[
9b - b\sqrt{3} > 3a
\]
\[
b(9-\sqrt{3}) > 3a.
\]
Since $a>0$ and $9-\sqrt{3} = 9-1.732... > 0$, we can divide by $3a$:
\[
\frac{b}{a} > \frac{3}{9-\sqrt{3}}.
\]
Let's simplify the right-hand side:
\[
\frac{3}{9-\sqrt{3}} = \frac{3(9+\sqrt{3})}{(9-\sqrt{3})(9+\sqrt{3})} = \frac{3(9+\sqrt{3})}{9^2 - (\sqrt{3})^2} = \frac{27+3\sqrt{3}}{81-3} = \frac{27+3\sqrt{3}}{78} = \frac{9+\sqrt{3}}{26}.
\]
So the inequality we need to prove is equivalent to
\[
\frac{b}{a} > \frac{9+\sqrt{3}}{26}.
\]
We know that $q = a/b \in (0,1)$, which means $0 < a/b < 1$. Since $a$ and $b$ are positive integers, this implies $a \ge 1$ and $b \ge a+1$.
Therefore, $b/a \ge (a+1)/a = 1 + 1/a$.
Since $a \ge 1$, $1/a \ge 0$, so $b/a \ge 1 + 1/a > 1$.
Thus, $b/a > 1$.

Now let's evaluate the value $\frac{9+\sqrt{3}}{26}$.
$\sqrt{3} \approx 1.732$.
$\frac{9+\sqrt{3}}{26} \approx \frac{9+1.732}{26} = \frac{10.732}{26} \approx 0.4128$.
The inequality $b/a > \frac{9+\sqrt{3}}{26}$ is true if $1 \ge \frac{9+\sqrt{3}}{26}$, because we know $b/a > 1$.
Let's check if $1 \ge \frac{9+\sqrt{3}}{26}$:
$26 \ge 9+\sqrt{3}$
$17 \ge \sqrt{3}$.
Squaring both sides (both are positive):
$17^2 \ge (\sqrt{3})^2$
$289 \ge 3$.
This is true. Thus, $1 \ge \frac{9+\sqrt{3}}{26}$.

Since $b/a > 1$ and $1 \ge \frac{9+\sqrt{3}}{26}$, it implies $b/a > \frac{9+\sqrt{3}}{26}$.
Furthermore, $b/a$ is rational and $\frac{9+\sqrt{3}}{26}$ is irrational, so $b/a \ne \frac{9+\sqrt{3}}{26}$.
Thus the inequality $b/a > \frac{9+\sqrt{3}}{26}$ is strict.
This implies that the inequality $\frac{1}{(a\sqrt{3}+b)b\sqrt{3}} > \frac{1}{9b^2}$ is strict.

We have $\left|q-\frac{1}{\sqrt{3}}\right| \ge \frac{1}{(a\sqrt{3}+b)b\sqrt{3}}$.
Since $\frac{1}{(a\sqrt{3}+b)b\sqrt{3}} > \frac{1}{9b^2}$, we can conclude that
\[
\left|q-\frac{1}{\sqrt{3}}\right| > \frac{1}{9b^2}.
\]

The final answer is $\boxed{\left|q-\frac{1}{\sqrt{3}}\right| > \frac{1}{9b^2}}$.