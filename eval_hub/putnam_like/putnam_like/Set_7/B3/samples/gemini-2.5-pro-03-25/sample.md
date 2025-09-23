Let $f : (0,1) \rightarrow \mathbb{R}$ be a function of class $\mathcal{C}^\infty$.
The condition is that for every integer $n \geq 0$, the function $g_n(x) = \frac{f(x)}{x^n}$ is increasing on $(0,1)$.
Since $f$ is $\mathcal{C}^\infty$, $g_n$ is $\mathcal{C}^\infty$ on $(0,1)$.
The condition that $g_n(x)$ is increasing is equivalent to $g_n'(x) \geq 0$ for all $x \in (0,1)$.
Let's compute the derivative of $g_n(x)$:
$$ g_n'(x) = \frac{f'(x)x^n - f(x)nx^{n-1}}{(x^n)^2} = \frac{x f'(x) - n f(x)}{x^{n+1}} $$
Since $x \in (0,1)$, $x^{n+1} > 0$. Thus, the condition $g_n'(x) \geq 0$ is equivalent to
$$ x f'(x) - n f(x) \geq 0 $$
This must hold for all integers $n \geq 0$ and for all $x \in (0,1)$.

Let's fix $x \in (0,1)$. Let $A = x f'(x)$ and $B = f(x)$. The condition is $A \geq n B$ for all $n = 0, 1, 2, \dots$.
Consider the case $B > 0$. Then $f(x) > 0$. The sequence $\{nB\}_{n \geq 0}$ is $0, B, 2B, 3B, \dots$. As $n \to \infty$, $nB \to \infty$.
The condition $A \geq n B$ must hold for all $n$. But $A = x f'(x)$ is a fixed real number. If $B > 0$, we can always find an integer $n$ large enough such that $nB > A$. For example, choose any integer $n > A/B$. This leads to a contradiction.
Therefore, we must have $B \leq 0$. This means $f(x) \leq 0$ for all $x \in (0,1)$.

Now consider the case $B = 0$. Then $f(x) = 0$. The condition $A \geq n B$ becomes $A \geq n \cdot 0 = 0$. So $A = x f'(x) \geq 0$. Since $x > 0$, this implies $f'(x) \geq 0$.
Consider the case $B < 0$. Then $f(x) < 0$. The condition is $A \geq n B$ for all $n \geq 0$. The sequence $\{nB\}_{n \geq 0}$ is $0, B, 2B, 3B, \dots$. Since $B < 0$, this sequence is $0, B, 2B, 3B, \dots$ where $B < 0$. This sequence is decreasing towards $-\infty$. The supremum of the set $\{n B \mid n \geq 0\}$ is $0$ (achieved at $n=0$).
The condition $A \geq n B$ for all $n \geq 0$ implies that $A$ must be greater than or equal to the supremum of $\{n B \mid n \geq 0\}$. Thus, $A \geq 0$.
So we must have $A = x f'(x) \geq 0$. Since $x > 0$, this implies $f'(x) \geq 0$.

In summary, the given conditions imply that $f(x) \leq 0$ and $f'(x) \geq 0$ for all $x \in (0,1)$.

The question asks if it is true that $f^{(k)}(x) \geq 0$ for every $k \geq 0$ and all $x \in (0,1)$.
The condition $k=0$ corresponds to $f^{(0)}(x) = f(x)$. So the question asks if $f(x) \geq 0$ for all $x \in (0,1)$.
We have deduced from the premises that $f(x) \leq 0$ for all $x \in (0,1)$.
If the statement $f^{(k)}(x) \geq 0$ for all $k \geq 0$ were true, then $f(x) \geq 0$ must hold.
Combining $f(x) \leq 0$ and $f(x) \geq 0$, we must have $f(x) = 0$ for all $x \in (0,1)$.
If $f(x) = 0$ for all $x \in (0,1)$, then $f$ is $\mathcal{C}^\infty$.
$g_n(x) = 0/x^n = 0$. $g_n'(x)=0$, so $g_n(x)$ is increasing for all $n \geq 0$.
The derivatives are $f^{(k)}(x) = 0$ for all $k \geq 0$. So $f^{(k)}(x) \geq 0$ holds.
Thus, the statement is true for the zero function $f(x)=0$.

However, the question asks if the statement is true for *any* such function $f$. This means: Does the condition imply that $f^{(k)}(x) \geq 0$ must hold for all $k$?
This is equivalent to asking: Is $f(x)=0$ the only function satisfying the conditions? If there exists a non-zero function satisfying the conditions, and this function does not satisfy $f^{(k)}(x) \geq 0$ for all $k$, then the answer is NO.

Let's test the function $f(x) = c$ for some constant $c$.
For $f$ to be $\mathcal{C}^\infty$, this is fine.
We need $f(x) \leq 0$, so $c \leq 0$.
We need $f'(x) \geq 0$. $f'(x)=0$, which satisfies this condition.
We need $x f'(x) - n f(x) \geq 0$ for all $n \geq 0$.
$x(0) - n c \geq 0$, which means $-nc \geq 0$.
If $c=0$, $f(x)=0$, which works.
If $c < 0$, then $-c > 0$. So we need $n \geq 0$. This condition holds for all $n \geq 0$.
So any constant negative function $f(x)=c$ with $c<0$ satisfies the hypotheses. For example, let's take $f(x)=-1$.

Let $f(x) = -1$.
$f$ is $\mathcal{C}^\infty$.
$g_n(x) = \frac{-1}{x^n} = -x^{-n}$.
$g_n'(x) = -(-n)x^{-n-1} = n x^{-n-1}$.
For $n=0$, $g_0(x) = -1$, $g_0'(x) = 0$. This is $\geq 0$. So $g_0$ is increasing.
For $n \geq 1$, $n > 0$. Since $x \in (0,1)$, $x^{-n-1} > 0$. So $g_n'(x) = n x^{-n-1} > 0$. So $g_n$ is increasing.
Thus, $f(x)=-1$ satisfies all the hypotheses.

Now, let's check the conclusion for $f(x)=-1$.
We need $f^{(k)}(x) \geq 0$ for all $k \geq 0$.
For $k=0$: $f^{(0)}(x) = f(x) = -1$. Is $-1 \geq 0$? No, this is false.
For $k \geq 1$: $f'(x)=0$, $f''(x)=0$, etc. $f^{(k)}(x)=0$. So $f^{(k)}(x) \geq 0$ is true for $k \geq 1$.
However, since the condition fails for $k=0$, the statement is false.

The statement "$f^{(n)}(x) \geq 0$ for every $n \geq 0$ and all $x \in (0,1)$" is not true for $f(x)=-1$, which satisfies the hypotheses.

Final Conclusion: The statement is false.

Counterexample: $f(x)=-1$.
This function is $\mathcal{C}^\infty$ on $(0,1)$.
For $n \geq 0$, $g_n(x) = \frac{f(x)}{x^n} = -x^{-n}$.
$g_n'(x) = n x^{-n-1}$. For $x \in (0,1)$, $x^{-n-1} > 0$.
If $n=0$, $g_0'(x)=0$. If $n>0$, $g_n'(x) > 0$.
In all cases $g_n'(x) \geq 0$, so $g_n(x)$ is increasing on $(0,1)$ for all $n \geq 0$.
Thus $f(x)=-1$ satisfies the hypotheses.
However, $f^{(0)}(x) = f(x) = -1$, which is not non-negative.
Therefore, the statement is false.

Another counterexample: $f(x)=x-1$.
$f$ is $\mathcal{C}^\infty$. $f(x) = x-1$. $f'(x)=1$.
$g_n(x) = \frac{x-1}{x^n} = x^{1-n} - x^{-n}$.
$g_n'(x) = (1-n)x^{-n} - (-n)x^{-n-1} = (1-n)x^{-n} + n x^{-n-1} = x^{-n-1}((1-n)x + n)$.
We need $(1-n)x + n \geq 0$ for $x \in (0,1)$ and $n \geq 0$.
If $n=0$, $x \geq 0$. True.
If $n=1$, $1 \geq 0$. True.
If $n \geq 2$, $n \geq (n-1)x$. $x \leq \frac{n}{n-1} = 1 + \frac{1}{n-1}$. Since $x \in (0,1)$ and $1 + \frac{1}{n-1} \geq 1+1 = 2$ (for $n=2$), this holds true for all $n \geq 2$.
So $f(x)=x-1$ satisfies the hypotheses.
However, $f^{(0)}(x) = f(x) = x-1$. For $x \in (0,1)$, $f(x) \in (-1,0)$, so $f(x) < 0$.
The statement fails for $k=0$.

Final Answer: The final answer is $\boxed{No}$