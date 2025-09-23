Let $P(x) = x^4-2x-1$. Let $x_1, x_2, x_3, x_4$ be the roots of $P(x)=0$. We want to compute the sum $S = \sum_{i=1}^4\frac{2x_i^2+1}{(x_i^2-1)^2}$.
Let $f(x) = \frac{2x^2+1}{(x^2-1)^2}$.
First, we check if $x_i^2-1=0$ for any root $x_i$. If $x_i^2=1$, then $x_i=\pm 1$.
$P(1) = 1^4 - 2(1) - 1 = 1-2-1 = -2 \neq 0$.
$P(-1) = (-1)^4 - 2(-1) - 1 = 1+2-1 = 2 \neq 0$.
So $x_i^2-1 \neq 0$ for all roots $x_i$. The terms in the sum are well-defined.

We perform a partial fraction decomposition of $f(x)$.
$f(x) = \frac{2x^2+1}{(x-1)^2(x+1)^2} = \frac{A}{x-1} + \frac{B}{(x-1)^2} + \frac{C}{x+1} + \frac{D}{(x+1)^2}$.
Since $f(x)$ is an even function ($f(-x)=f(x)$), we must have $A=-C$ and $B=D$.
We compute $B$ by multiplying by $(x-1)^2$ and setting $x=1$:
$B = \left. \frac{2x^2+1}{(x+1)^2} \right|_{x=1} = \frac{2(1)^2+1}{(1+1)^2} = \frac{3}{4}$.
So $D=3/4$.
To find $A$, we can set $x=0$:
$f(0) = \frac{2(0)^2+1}{(0^2-1)^2} = 1$.
Using the partial fraction form: $f(0) = \frac{A}{-1} + \frac{B}{(-1)^2} + \frac{C}{1} + \frac{D}{1^2} = -A+B+C+D$.
Since $C=-A$ and $B=D=3/4$, we have $1 = -A + 3/4 - A + 3/4 = -2A + 3/2$.
$2A = 3/2 - 1 = 1/2$, so $A=1/4$.
Then $C=-1/4$.
The partial fraction decomposition is:
\[f(x) = \frac{1}{4(x-1)} + \frac{3}{4(x-1)^2} - \frac{1}{4(x+1)} + \frac{3}{4(x+1)^2}.\]
We want to compute $S = \sum_{i=1}^4 f(x_i)$.
\[S = \sum_{i=1}^4 \left( \frac{1}{4(x_i-1)} + \frac{3}{4(x_i-1)^2} - \frac{1}{4(x_i+1)} + \frac{3}{4(x_i+1)^2} \right).\]
\[S = \frac{1}{4} \sum_{i=1}^4 \left( \frac{1}{x_i-1} - \frac{1}{x_i+1} \right) + \frac{3}{4} \sum_{i=1}^4 \left( \frac{1}{(x_i-1)^2} + \frac{1}{(x_i+1)^2} \right).\]

Let $y=x-1$, so $x=y+1$. The roots $y_i=x_i-1$ are the roots of the polynomial $Q(y) = P(y+1)$.
$Q(y) = (y+1)^4 - 2(y+1) - 1 = (y^4+4y^3+6y^2+4y+1) - 2y - 2 - 1 = y^4+4y^3+6y^2+2y-2$.
Let $z=x+1$, so $x=z-1$. The roots $z_i=x_i+1$ are the roots of the polynomial $R(z) = P(z-1)$.
$R(z) = (z-1)^4 - 2(z-1) - 1 = (z^4-4z^3+6z^2-4z+1) - 2z + 2 - 1 = z^4-4z^3+6z^2-6z+2$.

Let $y_1, y_2, y_3, y_4$ be the roots of $Q(y) = y^4+4y^3+6y^2+2y-2=0$. The coefficients are $a_4=1, a_3=4, a_2=6, a_1=2, a_0=-2$.
Let $z_1, z_2, z_3, z_4$ be the roots of $R(z) = z^4-4z^3+6z^2-6z+2=0$. The coefficients are $b_4=1, b_3=-4, b_2=6, b_1=-6, b_0=2$.

For a general polynomial $a_n y^n + \dots + a_1 y + a_0$ with roots $y_i$, we have the following relations based on Vieta's formulas:
$\sum \frac{1}{y_i} = \frac{-a_1}{a_0}$.
$\sum \frac{1}{y_i^2} = (\sum \frac{1}{y_i})^2 - 2 \sum_{i<j} \frac{1}{y_i y_j} = (\frac{-a_1}{a_0})^2 - 2 \frac{a_2}{a_0}$.

For $Q(y)$:
$\sum_{i=1}^4 \frac{1}{x_i-1} = \sum_{i=1}^4 \frac{1}{y_i} = \frac{-a_1}{a_0} = \frac{-2}{-2} = 1$.
$\sum_{i=1}^4 \frac{1}{(x_i-1)^2} = \sum_{i=1}^4 \frac{1}{y_i^2} = \left(\frac{-a_1}{a_0}\right)^2 - 2\frac{a_2}{a_0} = (1)^2 - 2\frac{6}{-2} = 1 - 2(-3) = 1+6 = 7$.

For $R(z)$:
$\sum_{i=1}^4 \frac{1}{x_i+1} = \sum_{i=1}^4 \frac{1}{z_i} = \frac{-b_1}{b_0} = \frac{-(-6)}{2} = 3$.
$\sum_{i=1}^4 \frac{1}{(x_i+1)^2} = \sum_{i=1}^4 \frac{1}{z_i^2} = \left(\frac{-b_1}{b_0}\right)^2 - 2\frac{b_2}{b_0} = (3)^2 - 2\frac{6}{2} = 9 - 6 = 3$.

Now substitute these values back into the expression for $S$:
$S = \frac{1}{4} \left( \sum \frac{1}{y_i} - \sum \frac{1}{z_i} \right) + \frac{3}{4} \left( \sum \frac{1}{y_i^2} + \sum \frac{1}{z_i^2} \right)$.
$S = \frac{1}{4} (1 - 3) + \frac{3}{4} (7 + 3)$.
$S = \frac{1}{4} (-2) + \frac{3}{4} (10)$.
$S = -\frac{2}{4} + \frac{30}{4} = -\frac{1}{2} + \frac{15}{2}$.
$S = \frac{14}{2} = 7$.

Final Answer: The final answer is $\boxed{7}$