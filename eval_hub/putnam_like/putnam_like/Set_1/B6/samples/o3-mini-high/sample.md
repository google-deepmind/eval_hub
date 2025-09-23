```markdown
We will show that if
\[
x_{n+1}=\beta x_n+\lfloor\alpha x_n\rfloor,\quad n\ge0,
\]
with
- \(x_0\in\mathbb{N}\),
- \(\beta\in\mathbb{N}\),
- \(\alpha\in(0,\infty)\setminus\mathbb{Q}\) with \(\alpha^2\in\mathbb{N}\),
- and \(\beta-\alpha\in(0,1)\),
then the limit
\[
L=\lim_{n\to\infty}\frac{x_n}{(\alpha+\beta)^n}
\]
satisfies
\[
L=\frac{x_0}{2}+\frac{1}{2\alpha}\lfloor\alpha x_0\rfloor.
\]

Below are the details.

1. **Rewriting the Recurrence**

   Notice that since
   \[
   \lfloor \alpha x_n\rfloor = \alpha x_n -\{\alpha x_n\},
   \]
   the recurrence may be written as
   \[
   x_{n+1}=\beta x_n+\alpha x_n-\{\alpha x_n\}=(\alpha+\beta)x_n-\{\alpha x_n\}.
   \]
   For convenience, set
   \[
   r_n=\{\alpha x_n\}.
   \]
   Then
   \[
   x_{n+1}=(\alpha+\beta)x_n-r_n.
   \]

2. **Finding a Recurrence for the Fractional Parts**

   We next compute the fractional part of \(\alpha x_{n+1}\). We have
   \[
   \alpha x_{n+1}=\alpha\bigl[(\alpha+\beta)x_n-r_n\bigr]
   =\alpha(\alpha+\beta)x_n-\alpha r_n.
   \]
   Write
   \[
   \alpha(\alpha+\beta)x_n = \alpha^2 x_n+\alpha\beta x_n.
   \]
   Because \(\alpha^2\in\mathbb{N}\) and \(x_n\in\mathbb{N}\), the product
   \[
   I_n=\alpha^2 x_n
   \]
   is an integer. Also,
   \[
   \alpha x_n = \lfloor\alpha x_n\rfloor+r_n.
   \]
   Hence,
   \[
   \alpha\beta x_n=\beta\lfloor\alpha x_n\rfloor+\beta r_n.
   \]
   Thus we may write
   \[
   \alpha x_{n+1}= \underbrace{\Bigl(I_n+\beta\lfloor\alpha x_n\rfloor\Bigr)}_{\in\mathbb{N}}+(\beta-\alpha)r_n.
   \]
   This shows that the fractional part of \(\alpha x_{n+1}\) is
   \[
   r_{n+1}=\{\alpha x_{n+1}\}=\{(\beta-\alpha)r_n\}.
   \]
   But since \(\beta-\alpha\in(0,1)\) and \(r_n\in[0,1)\), one has
   \[
   0\le (\beta-\alpha)r_n<1,
   \]
   so the fractional part is just
   \[
   r_{n+1}=(\beta-\alpha)r_n.
   \]
   Iterating this and recalling that
   \[
   r_0 =\{\alpha x_0\},
   \]
   we obtain
   \[
   r_n=(\beta-\alpha)^n\,\{\alpha x_0\}\quad\text{for all }n\ge0.
   \]

3. **Solving for \(x_n\)**

   Now write the recurrence
   \[
   x_{n+1}=(\alpha+\beta)x_n-r_n
   \]
   in its “variation‐of‐constants” form:
   \[
   x_n=(\alpha+\beta)^n x_0-\sum_{j=0}^{n-1}(\alpha+\beta)^{n-1-j}\,r_j.
   \]
   Dividing by \((\alpha+\beta)^n\) gives
   \[
   \frac{x_n}{(\alpha+\beta)^n} = x_0 - \sum_{j=0}^{n-1}\frac{r_j}{(\alpha+\beta)^{j+1}}.
   \]
   Since \(r_j=(\beta-\alpha)^j\,\{\alpha x_0\}\), we have
   \[
   \frac{x_n}{(\alpha+\beta)^n} = x_0 - \frac{\{\alpha x_0\}}{\alpha+\beta} \sum_{j=0}^{n-1}\left(\frac{\beta-\alpha}{\alpha+\beta}\right)^j.
   \]

4. **Taking the Limit**

   The infinite geometric series
   \[
   \sum_{j=0}^{\infty}\left(\frac{\beta-\alpha}{\alpha+\beta}\right)^j
   \]
   converges because
   \[
   \left|\frac{\beta-\alpha}{\alpha+\beta}\right| <1.
   \]
   Its sum is
   \[
   \sum_{j=0}^{\infty}\left(\frac{\beta-\alpha}{\alpha+\beta}\right)^j=\frac{1}{1-\frac{\beta-\alpha}{\alpha+\beta}} 
   =\frac{\alpha+\beta}{(\alpha+\beta)-(\beta-\alpha)}
   =\frac{\alpha+\beta}{2\alpha}.
   \]
   Hence,
   \[
   \lim_{n\to\infty}\frac{x_n}{(\alpha+\beta)^n}
   = x_0 - \frac{\{\alpha x_0\}}{\alpha+\beta}\cdot\frac{\alpha+\beta}{2\alpha}
   = x_0 -\frac{\{\alpha x_0\}}{2\alpha}.
   \]
   Finally, using
   \[
   \{\alpha x_0\}=\alpha x_0-\lfloor\alpha x_0\rfloor,
   \]
   we have
   \[
   x_0-\frac{\{\alpha x_0\}}{2\alpha}
   = x_0-\frac{\alpha x_0-\lfloor\alpha x_0\rfloor}{2\alpha}
   = \frac{2\alpha x_0-\alpha x_0+\lfloor\alpha x_0\rfloor}{2\alpha}
   =\frac{x_0}{2}+\frac{\lfloor\alpha x_0\rfloor}{2\alpha}.
   \]

Thus, the final answer is
\[
\boxed{\lim_{n\to\infty}\frac{x_n}{(\alpha+\beta)^n}
=\frac{x_0}{2}+\frac{1}{2\alpha}\lfloor\alpha x_0\rfloor.}
\]
```