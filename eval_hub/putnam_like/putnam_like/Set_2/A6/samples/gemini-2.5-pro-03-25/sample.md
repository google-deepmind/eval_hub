Let $P(x,y)$ be the assertion $\frac{f(x)+f(y)}{f(xy)}=\frac{1}{f(x+y)}-2xy$.
The domain and codomain of $f$ are $\mathbb{R}^+$, and $f$ is continuous.

First, let's test some values.
$P(1,1) \implies \frac{f(1)+f(1)}{f(1)} = \frac{1}{f(2)} - 2(1)(1)$.
$\frac{2f(1)}{f(1)} = \frac{1}{f(2)} - 2$.
$2 = \frac{1}{f(2)} - 2$.
$4 = \frac{1}{f(2)}$, so $f(2) = 1/4$.

Let $c = f(1)$. Since $f(x)>0$ for all $x$, $c>0$.
$P(x,1) \implies \frac{f(x)+f(1)}{f(x)} = \frac{1}{f(x+1)} - 2x$.
$1 + \frac{c}{f(x)} = \frac{1}{f(x+1)} - 2x$.
$P(1,x) \implies \frac{f(1)+f(x)}{f(x)} = \frac{1}{f(1+x)} - 2x$. This is the same equation.

Let's use the relation $1 + \frac{c}{f(x)} = \frac{1}{f(x+1)} - 2x$ to find values of $f$ at integers.
For $x=1$: $1 + \frac{c}{f(1)} = \frac{1}{f(2)} - 2(1)$. $1 + \frac{c}{c} = \frac{1}{1/4} - 2$. $1+1 = 4-2$. $2=2$. This is consistent but doesn't determine $c$.
For $x=2$: $1 + \frac{c}{f(2)} = \frac{1}{f(3)} - 2(2)$. $1 + \frac{c}{1/4} = \frac{1}{f(3)} - 4$. $1+4c = \frac{1}{f(3)} - 4$.
$\frac{1}{f(3)} = 5+4c$, so $f(3) = \frac{1}{5+4c}$.
For $x=3$: $1 + \frac{c}{f(3)} = \frac{1}{f(4)} - 2(3)$. $1 + c(5+4c) = \frac{1}{f(4)} - 6$.
$\frac{1}{f(4)} = 1+5c+4c^2+6 = 4c^2+5c+7$.
$f(4) = \frac{1}{4c^2+5c+7}$.

Now let's use $P(x,x)$.
$P(2,2) \implies \frac{f(2)+f(2)}{f(2 \cdot 2)} = \frac{1}{f(2+2)} - 2(2)(2)$.
$\frac{2f(2)}{f(4)} = \frac{1}{f(4)} - 8$.
$\frac{2(1/4)}{f(4)} = \frac{1}{f(4)} - 8$.
$\frac{1/2}{f(4)} = \frac{1}{f(4)} - 8$.
Multiply by $f(4)$: $1/2 = 1 - 8f(4)$.
$8f(4) = 1 - 1/2 = 1/2$.
$f(4) = \frac{1}{16}$.

We have two expressions for $f(4)$:
$f(4) = \frac{1}{16}$ and $f(4) = \frac{1}{4c^2+5c+7}$.
Equating the denominators: $16 = 4c^2+5c+7$.
$4c^2+5c+7-16 = 0$.
$4c^2+5c-9 = 0$.
This is a quadratic equation in $c$. The roots are given by the quadratic formula:
$c = \frac{-5 \pm \sqrt{5^2 - 4(4)(-9)}}{2(4)} = \frac{-5 \pm \sqrt{25 + 144}}{8} = \frac{-5 \pm \sqrt{169}}{8} = \frac{-5 \pm 13}{8}$.
The possible values for $c$ are $c_1 = \frac{-5+13}{8} = \frac{8}{8} = 1$ and $c_2 = \frac{-5-13}{8} = \frac{-18}{8} = -9/4$.
Since $f: \mathbb{R}^+ \to \mathbb{R}^+$, we must have $c=f(1)>0$.
Therefore, $c=1$. So $f(1)=1$.

Now we know $f(1)=1$. Let's substitute $c=1$ into the expressions for $f(2), f(3), f(4)$.
$f(1)=1 = 1/1^2$.
$f(2)=1/4 = 1/2^2$.
$f(3)=1/(5+4c) = 1/(5+4(1)) = 1/9 = 1/3^2$.
$f(4)=1/16 = 1/4^2$.
This suggests that $f(n)=1/n^2$ for all $n \in \mathbb{N}$. Let's prove this by induction using the relation $1 + \frac{1}{f(x)} = \frac{1}{f(x+1)} - 2x$ (since $c=1$).
Rearranging gives $f(x+1) = \frac{1}{1 + 1/f(x) + 2x} = \frac{f(x)}{f(x)+1+2xf(x)}$.
Base case $n=1$: $f(1)=1=1/1^2$.
Inductive step: Assume $f(k)=1/k^2$ for some $k \in \mathbb{N}$.
$f(k+1) = \frac{f(k)}{f(k)+1+2kf(k)} = \frac{1/k^2}{1/k^2+1+2k(1/k^2)} = \frac{1/k^2}{1/k^2+1+2/k} = \frac{1/k^2}{(1+k^2+2k)/k^2} = \frac{1/k^2}{(k+1)^2/k^2} = \frac{1}{(k+1)^2}$.
Thus, by induction, $f(n)=1/n^2$ for all $n \in \mathbb{N}$.

Let's define $g(x) = 1/f(x)$. Since $f(x)>0$, $g(x)>0$. Since $f$ is continuous, $g$ is continuous.
The original equation can be rewritten in terms of $g$.
$\frac{1/g(x)+1/g(y)}{1/g(xy)} = g(x+y) - 2xy$.
$\frac{(g(x)+g(y))/(g(x)g(y))}{1/g(xy)} = g(x+y) - 2xy$.
$\frac{g(x)+g(y)}{g(x)g(y)} g(xy) = g(x+y) - 2xy$.

We found $f(n)=1/n^2$ for $n \in \mathbb{N}$. This means $g(n)=1/f(n)=n^2$ for $n \in \mathbb{N}$. In particular, $g(1)=1^2=1$.
The relation $f(x+1) = \frac{f(x)}{f(x)+1+2xf(x)}$ translates to $g$.
$1/g(x+1) = \frac{1/g(x)}{1/g(x)+1+2x/g(x)} = \frac{1/g(x)}{(1+g(x)+2x)/g(x)} = \frac{1}{g(x)+2x+1}$.
So $g(x+1) = g(x)+2x+1$.

Let $G(x) = g(x)-x^2$. Since $g$ is continuous, $G$ is continuous.
We want to show $G(x)=0$ for all $x \in \mathbb{R}^+$.
$G(x+1)+(x+1)^2 = g(x+1) = g(x)+2x+1 = G(x)+x^2+2x+1$.
$G(x+1)+x^2+2x+1 = G(x)+x^2+2x+1$.
$G(x+1)=G(x)$. This means $G$ is periodic with period 1.
For $n \in \mathbb{N}$, $G(n)=g(n)-n^2=n^2-n^2=0$.
Since $G(x+1)=G(x)$ and $G(1)=0$, it follows that $G(n)=0$ for all $n \in \mathbb{N}$.

Now let's use the main equation for $g$: $\frac{g(x)+g(y)}{g(x)g(y)} g(xy) = g(x+y) - 2xy$.
Let $y=n \in \mathbb{N}$. $g(n)=n^2$.
$\frac{g(x)+n^2}{g(x)n^2} g(xn) = g(x+n) - 2xn$.
We know $g(x+1)=g(x)+2x+1$. By induction, we can show $g(x+n) = g(x)+2nx+n^2$.
Base case $n=1$: $g(x+1)=g(x)+2x+1$. True.
Assume $g(x+k)=g(x)+2kx+k^2$. Then $g(x+k+1)=g((x+k)+1)=g(x+k)+2(x+k)+1 = (g(x)+2kx+k^2)+2x+2k+1 = g(x)+2(k+1)x+(k+1)^2$. This completes the induction.
So, $\frac{g(x)+n^2}{g(x)n^2} g(xn) = (g(x)+2nx+n^2) - 2xn = g(x)+n^2$.
Since $g(x)>0$ and $n^2>0$, $g(x)+n^2>0$. We can divide by $g(x)+n^2$.
$\frac{g(xn)}{g(x)n^2} = 1$.
$g(xn) = g(x)n^2$.

Let's express this in terms of $G(x)=g(x)-x^2$.
$G(xn)+(xn)^2 = (G(x)+x^2)n^2 = G(x)n^2 + (xn)^2$.
$G(xn) = G(x)n^2$ for all $x \in \mathbb{R}^+$ and $n \in \mathbb{N}$.

Now let $x=p/q$ be a positive rational number, where $p, q \in \mathbb{N}$.
Using the property $G(xn)=G(x)n^2$, let $x=p/q$ and $n=q$.
$G(q \cdot p/q) = G(p/q)q^2$.
$G(p) = G(p/q)q^2$.
Since $p \in \mathbb{N}$, we know $G(p)=0$.
So $0 = G(p/q)q^2$.
Since $q \in \mathbb{N}$, $q \ge 1$, so $q^2 \ge 1$. Thus $q^2 \neq 0$.
Therefore, $G(p/q)=0$.
This shows that $G(x)=0$ for all $x \in \mathbb{Q}^+$.
So $g(x)=x^2$ for all $x \in \mathbb{Q}^+$.

Finally, we use the continuity of $g$.
Let $x \in \mathbb{R}^+$. Since $\mathbb{Q}^+$ is dense in $\mathbb{R}^+$, there exists a sequence $(q_k)_{k=1}^\infty$ of positive rational numbers such that $\lim_{k \to \infty} q_k = x$.
Since $g$ is continuous, $g(x) = g(\lim_{k \to \infty} q_k) = \lim_{k \to \infty} g(q_k)$.
Since $q_k \in \mathbb{Q}^+$, $g(q_k) = q_k^2$.
So $g(x) = \lim_{k \to \infty} q_k^2$.
Since the function $t \mapsto t^2$ is continuous, $\lim_{k \to \infty} q_k^2 = (\lim_{k \to \infty} q_k)^2 = x^2$.
Thus, $g(x)=x^2$ for all $x \in \mathbb{R}^+$.

Since $g(x)=1/f(x)$, we have $f(x)=1/g(x)=1/x^2$.
Let's check if $f(x)=1/x^2$ satisfies all conditions.
$f: \mathbb{R}^+ \to \mathbb{R}^+$. If $x>0$, $x^2>0$, so $1/x^2>0$. This holds.
$f(x)=1/x^2$ is continuous on $\mathbb{R}^+$. This holds.
Let's check the original equation:
LHS: $\frac{f(x)+f(y)}{f(xy)} = \frac{1/x^2+1/y^2}{1/(xy)^2} = \frac{(y^2+x^2)/(x^2y^2)}{1/(x^2y^2)} = x^2+y^2$.
RHS: $\frac{1}{f(x+y)} - 2xy = \frac{1}{1/(x+y)^2} - 2xy = (x+y)^2 - 2xy = (x^2+2xy+y^2)-2xy = x^2+y^2$.
Since LHS=RHS, the function $f(x)=1/x^2$ is indeed a solution.
Based on the derivation, this is the unique solution.

Final Answer: The final answer is $\boxed{f(x)=1/x^2}$