Let $x_1, x_2, x_3, x_4$ be the four roots of the equation $x^4 - 2x - 1 = 0$. We want to find the sum
\[S = \sum_{i=1}^4 \frac{2x_i^2+1}{(x_i^2-1)^2}.\]
First, let's analyze the expression in the sum. We can rewrite the term as:
\[ \frac{2x^2+1}{(x^2-1)^2} = \frac{2x^2 - 2 + 3}{(x^2-1)^2} = \frac{2(x^2-1)+3}{(x^2-1)^2} = \frac{2}{x^2-1} + \frac{3}{(x^2-1)^2}. \]
So the sum becomes
\[ S = \sum_{i=1}^4 \left(\frac{2}{x_i^2-1} + \frac{3}{(x_i^2-1)^2}\right) = 2\sum_{i=1}^4 \frac{1}{x_i^2-1} + 3\sum_{i=1}^4 \frac{1}{(x_i^2-1)^2}. \]
Let $y_i = x_i^2-1$. We need to find a polynomial whose roots are $y_i$.
From the equation $x^4 - 2x - 1 = 0$, we have $x^4 - 1 = 2x$.
This can be factored as $(x^2-1)(x^2+1) = 2x$.
Substitute $y=x^2-1$. Then $x^2 = y+1$. The equation becomes $y(y+1+1) = 2x$, which is $y(y+2) = 2x$.
Squaring both sides gives $y^2(y+2)^2 = (2x)^2 = 4x^2$.
Substitute $x^2=y+1$ into the right side: $y^2(y+2)^2 = 4(y+1)$.
Expand and rearrange the equation:
$y^2(y^2+4y+4) = 4y+4$
$y^4 + 4y^3 + 4y^2 = 4y+4$
$y^4 + 4y^3 + 4y^2 - 4y - 4 = 0$.
Let $Q(y) = y^4 + 4y^3 + 4y^2 - 4y - 4$. The roots of $Q(y)=0$ are $y_i = x_i^2-1$ for $i=1,2,3,4$.

We need to calculate $\sum_{i=1}^4 \frac{1}{y_i}$ and $\sum_{i=1}^4 \frac{1}{y_i^2}$.
For a polynomial $Q(y) = a_n y^n + a_{n-1} y^{n-1} + \dots + a_1 y + a_0$ with roots $y_1, \ldots, y_n$, Vieta's formulas give the elementary symmetric polynomials in the roots.
For $Q(y) = y^4 + 4y^3 + 4y^2 - 4y - 4$, we have $n=4$, $a_4=1, a_3=4, a_2=4, a_1=-4, a_0=-4$.
Let $e_k$ be the elementary symmetric polynomials in $y_1, y_2, y_3, y_4$.
$e_1 = \sum y_i = -a_3/a_4 = -4/1 = -4$.
$e_2 = \sum_{i<j} y_i y_j = a_2/a_4 = 4/1 = 4$.
$e_3 = \sum_{i<j<k} y_i y_j y_k = -a_1/a_4 = -(-4)/1 = 4$.
$e_4 = y_1 y_2 y_3 y_4 = a_0/a_4 = -4/1 = -4$.

The sum of the reciprocals of the roots is $\sum \frac{1}{y_i} = \frac{e_3}{e_4}$.
\[ \sum_{i=1}^4 \frac{1}{y_i} = \frac{4}{-4} = -1. \]
The sum of the squares of the reciprocals of the roots is $\sum \frac{1}{y_i^2}$. We can find this using the identity $(\sum a_i)^2 = \sum a_i^2 + 2\sum_{i<j} a_i a_j$.
Let $a_i = 1/y_i$. Then $(\sum \frac{1}{y_i})^2 = \sum \frac{1}{y_i^2} + 2\sum_{i<j} \frac{1}{y_i y_j}$.
We need to compute $\sum_{i<j} \frac{1}{y_i y_j}$. This sum is $\frac{\sum_{k<l} y_k y_l}{y_1 y_2 y_3 y_4} = \frac{e_2}{e_4}$.
\[ \sum_{i<j} \frac{1}{y_i y_j} = \frac{4}{-4} = -1. \]
Now substitute this into the identity:
\[ (-1)^2 = \sum_{i=1}^4 \frac{1}{y_i^2} + 2(-1) \]
\[ 1 = \sum_{i=1}^4 \frac{1}{y_i^2} - 2 \]
\[ \sum_{i=1}^4 \frac{1}{y_i^2} = 1 + 2 = 3. \]
So, $\sum_{i=1}^4 \frac{1}{x_i^2-1} = -1$ and $\sum_{i=1}^4 \frac{1}{(x_i^2-1)^2} = 3$.

Now we can calculate the sum $S$:
\[ S = 2\sum_{i=1}^4 \frac{1}{x_i^2-1} + 3\sum_{i=1}^4 \frac{1}{(x_i^2-1)^2} = 2(-1) + 3(3) = -2 + 9 = 7. \]
The denominators $x_i^2-1$ are non-zero because $x^2=1$ implies $x=\pm 1$, and $1^4-2(1)-1 = -2 \ne 0$, $(-1)^4-2(-1)-1 = 2 \ne 0$, so $\pm 1$ are not roots of $x^4-2x-1=0$.

The final answer is $\boxed{7}$.