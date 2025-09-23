Here is a detailed step-by-step solution to the problem.

The given functional equation is for a continuous function $f: \mathbb{R}^+ \to \mathbb{R}^+$:
$$ \frac{f(x)+f(y)}{f(xy)}=\frac{1}{f(x+y)}-2xy \quad (*)$$

### Step 1: Guess a solution
Let's test some simple forms for $f(x)$. The structure of the equation involves sums ($x+y$) and products ($xy$). Let's try a function of the form $f(x) = cx^n$. Given that $f(x) > 0$ for $x>0$, we need $c>0$. The presence of the $2xy$ term suggests a relationship with squares. Let's try $f(x) = 1/x^2$. This function maps $\mathbb{R}^+ \to \mathbb{R}^+$ and is continuous.

Let's substitute $f(x)=1/x^2$ into the equation $(*)$:
*   **Left-hand side (LHS):**
    $$ \frac{f(x)+f(y)}{f(xy)} = \frac{1/x^2+1/y^2}{1/(xy)^2} = \frac{(y^2+x^2)/(x^2y^2)}{1/(x^2y^2)} = x^2+y^2 $$
*   **Right-hand side (RHS):**
    $$ \frac{1}{f(x+y)}-2xy = \frac{1}{1/(x+y)^2} - 2xy = (x+y)^2 - 2xy = (x^2+2xy+y^2)-2xy = x^2+y^2 $$
Since LHS = RHS, the function $f(x)=1/x^2$ is indeed a solution.

### Step 2: Prove that this is the only solution
To prove uniqueness, we will analyze the properties of any function $f$ that satisfies the given conditions.

Let's rearrange the equation $(*)$:
$$ \frac{f(x)+f(y)}{f(xy)}+2xy = \frac{1}{f(x+y)} $$
Let's define a new function $g(x) = 1/f(x)$. Since $f: \mathbb{R}^+ \to \mathbb{R}^+$ is continuous, $g: \mathbb{R}^+ \to \mathbb{R}^+$ is also continuous. Substituting $f(x) = 1/g(x)$ into the rearranged equation:
$$ \frac{1/g(x)+1/g(y)}{1/g(xy)} + 2xy = g(x+y) $$
$$ \frac{(g(x)+g(y))/(g(x)g(y))}{1/g(xy)} + 2xy = g(x+y) $$
$$ \frac{(g(x)+g(y))g(xy)}{g(x)g(y)} + 2xy = g(x+y) \quad (**) $$
This equation for $g$ seems more complex than the original one. Let's return to the original equation and derive some specific relations.

### Step 3: Derive relations for $f(x)$
Let's make specific substitutions for $x$ and $y$ in $(*)$.

1.  **Set $x=y$:**
    $$ \frac{2f(x)}{f(x^2)} = \frac{1}{f(2x)} - 2x^2 \quad (1) $$

2.  **Set $x=1$:** Let $C=f(1)$. Since $f(1) \in \mathbb{R}^+$, $C>0$.
    $$ \frac{f(1)+f(y)}{f(y)} = \frac{1}{f(1+y)} - 2y $$
    $$ \frac{C}{f(y)} + 1 = \frac{1}{f(1+y)} - 2y $$
    $$ \frac{C}{f(y)} + 1 + 2y = \frac{1}{f(1+y)} \quad (2) $$

### Step 4: Use the derived relations to find $f(1)$
Let's use the function $g(x)=1/f(x)$ to simplify these two relations.
From (1):
$$ \frac{2/g(x)}{1/g(x^2)} = g(2x) - 2x^2 \implies \frac{2g(x^2)}{g(x)} = g(2x) - 2x^2 \quad (1')$$
From (2):
$$ Cg(y) + 1 + 2y = g(y+1) \quad (2') $$
Here $C=f(1)=1/g(1)$. So $g(1)=1/C$.

Let's use these relations to find the values of $g$ at integer points.
*   From $(1')$, let $x=1$:
    $$ \frac{2g(1)}{g(1)} = g(2)-2(1)^2 \implies 2 = g(2)-2 \implies g(2)=4 $$
*   From $(2')$, let $y=1$:
    $$ Cg(1) + 1 + 2(1) = g(2) \implies C(1/C) + 3 = g(2) \implies 1+3=4=g(2) $$
    This is consistent, but doesn't determine $C$. Let's compute $g(4)$ in two ways.

*   **First way (using (2')):**
    -   Set $y=2$ in $(2')$: $g(3) = Cg(2)+1+2(2) = C(4)+5 = 4C+5$.
    -   Set $y=3$ in $(2')$: $g(4) = Cg(3)+1+2(3) = C(4C+5)+7 = 4C^2+5C+7$.

*   **Second way (using (1')):**
    -   Set $x=2$ in $(1')$:
        $$ \frac{2g(2^2)}{g(2)} = g(2 \cdot 2) - 2(2^2) \implies \frac{2g(4)}{4} = g(4)-8 $$
        $$ \frac{g(4)}{2} = g(4)-8 \implies g(4) = 2g(4) - 16 \implies g(4) = 16 $$

*   **Equating the results for $g(4)$:**
    $$ 4C^2+5C+7 = 16 $$
    $$ 4C^2+5C-9 = 0 $$
    This is a quadratic equation for $C$. We solve it using the quadratic formula:
    $$ C = \frac{-5 \pm \sqrt{5^2 - 4(4)(-9)}}{2(4)} = \frac{-5 \pm \sqrt{25+144}}{8} = \frac{-5 \pm \sqrt{169}}{8} = \frac{-5 \pm 13}{8} $$
    The two possible values for $C$ are $C_1 = \frac{-5+13}{8}=1$ and $C_2 = \frac{-5-13}{8}=-\frac{18}{8}=-\frac{9}{4}$.
    Since $f: \mathbb{R}^+ \to \mathbb{R}^+$, we must have $f(1)=C>0$. Therefore, we must have $C=1$.

### Step 5: Determine the form of $g(x)$
Now we know $f(1)=1$, which implies $g(1)=1$. The relation $(2')$ becomes:
$$ g(y) + 1 + 2y = g(y+1) $$
Let's define a new function $k(x) = g(x) - x^2$ for $x \in \mathbb{R}^+$. Since $g$ and $x \mapsto x^2$ are continuous, $k$ is continuous.
Let's rewrite the relation for $g$ in terms of $k$:
$$ (y^2+k(y)) + 1 + 2y = (y+1)^2 + k(y+1) $$
$$ y^2+k(y) + 1 + 2y = y^2+2y+1 + k(y+1) $$
$$ k(y) = k(y+1) $$
This shows that $k(x)$ is a periodic function with period 1 for all $x \in \mathbb{R}^+$.

We can show by induction that $g(n)=n^2$ for all positive integers $n$.
Base case: $g(1)=1=1^2$.
Inductive step: Assume $g(n)=n^2$. Then $g(n+1)=g(n)+1+2n = n^2+2n+1=(n+1)^2$.
So, $g(n)=n^2$ for all $n \in \mathbb{N}, n\ge 1$.
This implies $k(n) = g(n)-n^2 = n^2-n^2=0$ for all $n \in \mathbb{N}, n\ge 1$.

Now, let's use the other relation $(1')$: $2g(x^2)/g(x) = g(2x)-2x^2$.
Substitute $g(x)=x^2+k(x)$:
$$ \frac{2((x^2)^2+k(x^2))}{x^2+k(x)} = (2x)^2+k(2x)-2x^2 $$
$$ \frac{2x^4+2k(x^2)}{x^2+k(x)} = 2x^2+k(2x) $$
$$ 2x^4+2k(x^2) = (x^2+k(x))(2x^2+k(2x)) $$
$$ 2x^4+2k(x^2) = 2x^4 + 2x^2k(x) + x^2k(2x) + k(x)k(2x) $$
$$ 2k(x^2) = 2x^2k(x) + x^2k(2x) + k(x)k(2x) \quad (3) $$

### Step 6: Prove that $k(x) = 0$ for all $x$
We have a continuous, 1-periodic function $k(x)$ on $\mathbb{R}^+$, which is zero at all positive integers. We need to show it's zero everywhere.
Since $k$ is continuous and 1-periodic, it is bounded on $\mathbb{R}^+$. Let $M = \sup_{x \in \mathbb{R}^+} |k(x)|$.

Divide equation (3) by $x^2$:
$$ \frac{2k(x^2)}{x^2} = 2k(x) + k(2x) + \frac{k(x)k(2x)}{x^2} $$
Let's take the limit as $x \to \infty$:
$$ \lim_{x\to\infty} \frac{2k(x^2)}{x^2} = \lim_{x\to\infty} \left( 2k(x) + k(2x) + \frac{k(x)k(2x)}{x^2} \right) $$
The terms involving $1/x^2$ go to zero because $k$ is bounded:
$|\frac{2k(x^2)}{x^2}| \le \frac{2M}{x^2} \to 0$ as $x \to \infty$.
$|\frac{k(x)k(2x)}{x^2}| \le \frac{M^2}{x^2} \to 0$ as $x \to \infty$.
So, we are left with:
$$ \lim_{x\to\infty} (2k(x) + k(2x)) = 0 $$
Let $M_{max} = \sup_{x\in\mathbb{R}^+} k(x)$ and $M_{min} = \inf_{x\in\mathbb{R}^+} k(x)$. Since $k$ is a continuous periodic function, these suprema and infima are attained.
There exists a sequence $(x_n)$ such that $x_n \to \infty$ and $k(x_n) \to M_{max}$. For example, if $M_{max}$ is attained at $x_0 \in [1,2)$, we can choose $x_n = x_0+n$.
For this sequence, $\lim_{n\to\infty} k(x_n) = M_{max}$.
The sequence $2x_n = 2x_0+2n$ also goes to infinity. As $k$ is 1-periodic, $k(2x_n)=k(2x_0+2n)=k(2x_0)$.
So, for this sequence, the limit becomes:
$$ \lim_{n\to\infty} (2k(x_n) + k(2x_n)) = 2M_{max} + k(2x_0) = 0 $$
Since $k(2x_0) \le M_{max}$, we have $2M_{max} + M_{max} \ge 0$, which means $3M_{max} \ge 0$.
More importantly, since $k(2x_0) \ge M_{min}$, we have $2M_{max} + M_{min} \le 2M_{max} + k(2x_0) = 0$. So, $2M_{max} + M_{min} \le 0$.

Similarly, there exists a sequence $(y_n)$ such that $y_n \to \infty$ and $k(y_n) \to M_{min}$. Let $y_0$ be a point in $[1,2)$ where $k$ attains its minimum, and set $y_n = y_0+n$.
Then $\lim_{n\to\infty} k(y_n) = M_{min}$ and $\lim_{n\to\infty} k(2y_n) = k(2y_0)$.
The limit condition gives:
$$ \lim_{n\to\infty} (2k(y_n) + k(2y_n)) = 2M_{min} + k(2y_0) = 0 $$
Since $k(2y_0) \le M_{max}$, we have $2M_{min} + M_{max} \ge 2M_{min} + k(2y_0) = 0$. So, $2M_{min} + M_{max} \ge 0$.

We have a system of two inequalities:
1) $2M_{max} + M_{min} \le 0$
2) $M_{max} + 2M_{min} \ge 0$

From (1), $M_{min} \le -2M_{max}$. Substituting this into (2):
$M_{max} + 2(-2M_{max}) \ge 0 \implies M_{max} - 4M_{max} \ge 0 \implies -3M_{max} \ge 0 \implies M_{max} \le 0$.

From (2), $M_{max} \ge -2M_{min}$. Substituting this into (1):
$2(-2M_{min}) + M_{min} \le 0 \implies -4M_{min} + M_{min} \le 0 \implies -3M_{min} \le 0 \implies M_{min} \ge 0$.

So we have $M_{max} \le 0$ and $M_{min} \ge 0$. By definition, $M_{min} \le k(x) \le M_{max}$ for all $x$. This forces $M_{min}=M_{max}=0$.
Thus, $k(x)=0$ for all $x \in \mathbb{R}^+$.

### Step 7: Final Conclusion
Since $k(x)=0$ for all $x \in \mathbb{R}^+$, we have $g(x) - x^2 = 0$, which means $g(x)=x^2$.
As $f(x)=1/g(x)$, the unique solution is $f(x)=1/x^2$.

This function meets all the requirements of the problem:
-   Domain and Codomain: $f: \mathbb{R}^+ \to \mathbb{R}^+$, since for $x>0$, $x^2>0$ and $1/x^2>0$.
-   Continuity: $f(x)=1/x^2$ is continuous on $\mathbb{R}^+$.
-   Functional Equation: We verified in Step 1 that it satisfies the equation.

Therefore, the only continuous function satisfying the given conditions is $f(x) = 1/x^2$.