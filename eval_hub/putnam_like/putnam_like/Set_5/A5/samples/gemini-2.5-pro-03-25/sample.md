Solution:
Let $F$ be the family of all continuous functions $u:[0,1]\to\mathbb{R}$ satisfying
\[
|u(t)|^2\leq 1+6\int_0^t s^2|u(s)|\, ds,\quad \forall t\in[0,1].
\]
The functional $J:F\to\mathbb{R}$ is defined by
\[
J(u)=\int_0^1 (u^3(t)-u^2(t))\,dt.
\]
We want to prove that $J$ attains a minimum value on $F$ and find this minimum value.

Step 1: Bound the functions in $F$.
Let $u \in F$. Define $\phi(t) = 1+6\int_0^t s^2|u(s)|\, ds$. Then $\phi(t)$ is continuous, $\phi(0)=1$, and $\phi(t) \ge 1$ for all $t \in [0,1]$. The inequality is $|u(t)|^2 \leq \phi(t)$. This implies $|u(t)| \leq \sqrt{\phi(t)}$.
Since $u$ is continuous, $\phi(t)$ is continuously differentiable for $t \in (0, 1]$, and $\phi'(t) = 6t^2|u(t)|$.
Using $|u(t)| \leq \sqrt{\phi(t)}$, we get $\phi'(t) \leq 6t^2 \sqrt{\phi(t)}$.
Since $\phi(t) \ge 1 > 0$, we can divide by $\sqrt{\phi(t)}$:
\[
\frac{\phi'(t)}{2\sqrt{\phi(t)}} \leq 3t^2.
\]
The left side is the derivative of $\sqrt{\phi(t)}$. So, $(\sqrt{\phi(t)})' \leq 3t^2$.
Integrating from $0$ to $t$:
\[
\sqrt{\phi(t)} - \sqrt{\phi(0)} \leq \int_0^t 3s^2 ds = t^3.
\]
Since $\phi(0)=1$, we have $\sqrt{\phi(t)} \leq 1+t^3$.
As $|u(t)| \leq \sqrt{\phi(t)}$, we get $|u(t)| \leq 1+t^3$ for all $t \in [0,1]$.
This shows that the family $F$ is uniformly bounded: $|u(t)| \leq 1+1^3=2$ for all $u \in F$ and $t \in [0,1]$. So $\|u\|_\infty \leq 2$.

Step 2: Show the minimizer must be non-positive.
Let $u \in F$. Define $v(t) = -|u(t)|$. Since $|v(t)| = |u(t)|$, we have
\[
|v(t)|^2 = |u(t)|^2 \leq 1+6\int_0^t s^2|u(s)|\, ds = 1+6\int_0^t s^2|v(s)|\, ds.
\]
Since $u$ is continuous, $|u|$ is continuous, so $v$ is continuous. Thus $v \in F$.
Let's compare $J(u)$ and $J(v)$.
\[
J(u) - J(v) = \int_0^1 (u^3(t)-u^2(t)) dt - \int_0^1 (v(t)^3-v(t)^2) dt
\]
\[
= \int_0^1 (u^3(t)-u^2(t)) dt - \int_0^1 ((-|u(t)|)^3 - (-|u(t)|)^2) dt
\]
\[
= \int_0^1 (u^3(t)-u^2(t) + |u(t)|^3 + |u(t)|^2) dt = \int_0^1 (u(t)^3+|u(t)|^3 - (u(t)^2-|u(t)|^2)) dt.
\]
Note that $u(t)^2-|u(t)|^2 = 0$.
The integrand is $u(t)^3+|u(t)|^3$. If $u(t) \ge 0$, the integrand is $u(t)^3+u(t)^3 = 2u(t)^3 \ge 0$. If $u(t) < 0$, the integrand is $u(t)^3+(-u(t))^3 = u(t)^3-u(t)^3=0$.
So $u(t)^3+|u(t)|^3 \ge 0$ for all $t$.
Therefore, $J(u)-J(v) = \int_0^1 (u(t)^3+|u(t)|^3) dt \ge 0$.
This means $J(v) \leq J(u)$. The minimum value of $J$ must be attained for a function $u^*$ such that $u^*(t)^3 + |u^*(t)|^3 = 0$ for all $t$. This implies $u^*(t) \leq 0$ for all $t \in [0,1]$.
So we can restrict our search for the minimum to the subset $F^- = \{ u \in F : u(t) \leq 0 \text{ for all } t \in [0,1] \}$.

Step 3: Transform the problem for non-positive functions.
Let $u \in F^-$. Define $w(t) = -u(t)$. Then $w(t) \ge 0$ for all $t$. Since $u$ is continuous, $w$ is continuous.
The condition $u \in F$ becomes $w(t)^2 \leq 1+6\int_0^t s^2 w(s) ds$.
Let $F_+ = \{ w \in C([0,1]) : w(t) \ge 0, w(t)^2 \leq 1+6\int_0^t s^2 w(s) ds \}$.
Then $u \in F^- \iff w=-u \in F_+$.
The functional $J(u)$ becomes
\[
J(u) = \int_0^1 ((-w(t))^3 - (-w(t))^2) dt = \int_0^1 (-w(t)^3 - w(t)^2) dt = - \int_0^1 (w(t)^3+w(t)^2) dt.
\]
Minimizing $J(u)$ over $F^-$ is equivalent to maximizing $K(w) = \int_0^1 (w(t)^3+w(t)^2) dt$ over $F_+$.

Step 4: Find the maximizer of $K(w)$.
Let $w \in F_+$. We know $|w(t)| \leq 1+t^3$. Since $w(t) \ge 0$, we have $0 \leq w(t) \leq 1+t^3$.
Consider the function $w_1(t) = 1+t^3$. Let's check if $w_1 \in F_+$. $w_1(t) \ge 1 \ge 0$.
\[
w_1(t)^2 = (1+t^3)^2 = 1+2t^3+t^6.
\]
\[
1+6\int_0^t s^2 w_1(s) ds = 1+6\int_0^t s^2 (1+s^3) ds = 1+6\int_0^t (s^2+s^5) ds = 1+6(\frac{t^3}{3}+\frac{t^6}{6}) = 1+2t^3+t^6.
\]
So $w_1(t)^2 = 1+6\int_0^t s^2 w_1(s) ds$. The equality holds. Thus $w_1 \in F_+$.
Let $h(x) = x^3+x^2$. For $x \ge 0$, $h'(x) = 3x^2+2x \ge 0$. So $h(x)$ is non-decreasing for $x \ge 0$.
For any $w \in F_+$, we have $w(t) \leq 1+t^3 = w_1(t)$.
Since $h(x)$ is non-decreasing and $w(t), w_1(t) \ge 0$, we have $h(w(t)) \leq h(w_1(t))$.
\[
w(t)^3+w(t)^2 \leq w_1(t)^3+w_1(t)^2.
\]
Integrating from $0$ to $1$:
\[
K(w) = \int_0^1 (w(t)^3+w(t)^2) dt \leq \int_0^1 (w_1(t)^3+w_1(t)^2) dt = K(w_1).
\]
The maximum value of $K(w)$ over $F_+$ is attained at $w=w_1(t)=1+t^3$.
Since $h(x)$ is strictly increasing for $x>0$, the inequality is strict unless $w(t)=w_1(t)$ for almost every $t$. Since $w$ and $w_1$ are continuous, this implies $w(t)=w_1(t)$ for all $t$.
So $w_1(t)=1+t^3$ is the unique maximizer for $K(w)$ in $F_+$.

Step 5: Find the minimizer of $J(u)$ and the minimum value.
The minimum value of $J(u)$ over $F$ must be attained at a function $u \in F^-$.
The minimum over $F^-$ corresponds to the maximum of $K(w)$ over $F_+$.
The unique maximizer for $K(w)$ is $w_1(t)=1+t^3$.
This corresponds to the function $u_2(t) = -w_1(t) = -(1+t^3)$.
The minimum value of $J(u)$ is $J(u_2)$.
\[
J(u_2) = \int_0^1 (u_2(t)^3 - u_2(t)^2) dt = \int_0^1 ((-(1+t^3))^3 - (-(1+t^3))^2) dt
\]
\[
= \int_0^1 (-(1+t^3)^3 - (1+t^3)^2) dt.
\]
The integrand is $-(1+3t^3+3t^6+t^9) - (1+2t^3+t^6) = -t^9 - 4t^6 - 5t^3 - 2$.
\[
J(u_2) = \int_0^1 (-t^9 - 4t^6 - 5t^3 - 2) dt = \left[ -\frac{t^{10}}{10} - \frac{4t^7}{7} - \frac{5t^4}{4} - 2t \right]_0^1
\]
\[
= -\frac{1}{10} - \frac{4}{7} - \frac{5}{4} - 2.
\]
The common denominator is $140$.
\[
J(u_2) = -\frac{14}{140} - \frac{80}{140} - \frac{175}{140} - \frac{280}{140} = \frac{-14-80-175-280}{140} = \frac{-549}{140}.
\]
The minimum value is $-549/140$.

Step 6: Prove the existence of the minimum.
The argument above shows that if a minimum exists, it must be $J(u_2)$. The problem requires proving existence.
Let $m = \inf_{u \in F} J(u)$. $m \leq J(0) = 0$. $m \leq J(u_2) = -549/140$.
Let $(u_n)$ be a minimizing sequence in $F$, i.e., $u_n \in F$ and $J(u_n) \to m$.
We know $F$ is uniformly bounded, $\|u_n\|_\infty \leq 2$.
We showed that $u_n$ can be replaced by $v_n = -|u_n|$ and $J(v_n) \leq J(u_n)$. So we can assume $u_n \leq 0$. Let $w_n = -u_n \geq 0$. $w_n \in F_+$. $J(u_n) = - K(w_n)$. $K(w_n) \to -m$.
We have $0 \leq w_n(t) \leq 1+t^3$. $w_n$ is uniformly bounded.
Also, $\phi_n(t) = 1+6\int_0^t s^2 w_n(s) ds$. $w_n(t) \leq \sqrt{\phi_n(t)}$. And $\sqrt{\phi_n(t)}$ is Lipschitz continuous with constant 3: $|\sqrt{\phi_n(t_2)} - \sqrt{\phi_n(t_1)}| \leq |t_2^3-t_1^3| \leq 3|t_2-t_1|$.
This shows the family $\{\sqrt{\phi_n(t)}\}$ is uniformly bounded and equicontinuous.
By Arzela-Ascoli theorem, there is a subsequence, denoted again by $\sqrt{\phi_n}$, that converges uniformly to a continuous function $G(t)$. Thus $\phi_n(t) \to G(t)^2$ uniformly.
Since $w_n$ is uniformly bounded, by Banach-Alaoglu theorem, there is a subsequence (denoted $w_n$) converging weak-* in $L^\infty([0,1])$ to some $w \in L^\infty([0,1])$. $0 \leq w(t) \leq 1+t^3$ a.e.
$F$ is convex and closed in $C([0,1])$. As argued in thoughts, this implies $F$ is weakly closed in $L^2$. So $u \in F$.
However, standard theorems require weak lower semi-continuity of $J$. $J(u) = \int (u^3-u^2)$ is not w.l.s.c.
Instead, let's rely on the derived structure. The argument in steps 2-4 showed that $u_2(t)=-(1+t^3)$ is the unique function in $F$ that provides the value $m=-549/140$.
This uniqueness guarantees that any minimizing sequence must converge to $u_2$.
More directly, the functional $K(w) = \int_0^1 (w^3+w^2) dt$ for $w \in F_+$ has a unique maximizer $w_1(t)=1+t^3$.
The existence of a maximizer for $K$ on $F_+$ can be proven. $K$ is strictly convex for $w>0$. Need weak upper semi-continuity?
However, the argument $w(t) \leq 1+t^3$ for all $w \in F_+$ shows that $w_1(t)=1+t^3$ is the unique maximizer. The maximum is attained. Thus the minimum for $J$ is attained.

Final verification: $u_2(t) = -(1+t^3)$ is continuous. $u_2 \in F$ because equality holds $|u_2(t)|^2 = 1+6\int_0^t s^2 |u_2(s)| ds$. So $u_2$ is a candidate. Steps 2-4 prove it's the unique minimizer.

The minimum value is attained and it is $J(u_2) = -549/140$.

Final Answer: The final answer is $\boxed{-\frac{549}{140}}$