```markdown
**Solution.**  
We shall show that \(f\equiv0\). Suppose, for contradiction, that there is a point \(x_0\in\mathbb{R}^2\) with \(f(x_0)\neq0\). By continuity of \(f\), there exists \(\delta>0\) such that
\[
\bigl|f(x)-f(x_0)\bigr|<\tfrac12\,\bigl|f(x_0)\bigr|
\quad\Longrightarrow\quad
\bigl|f(x)\bigr|\ge\tfrac12\,\bigl|f(x_0)\bigr|
>0
\quad\text{for all }x\in B(x_0,\delta).
\]
Thus on the little ball \(B(x_0,\delta)\), the function \(f\) has a fixed nonzero sign.  Now fix the given radius \(r>0\).  Choose a center \(a\in\mathbb{R}^2\) with
\[
\lvert a - x_0\rvert \;\le\; r - \delta,
\]
so that
\[
B(x_0,\delta)\;\subset\;B(a,r).
\]
Then
\[
\int_{B(a,r)} f(x)\,dx
\;\ge\;
\int_{B(x_0,\delta)} f(x)\,dx
\;>\;
\frac12\,\bigl|f(x_0)\bigr|\;\bigl|B(x_0,\delta)\bigr|
\;=\;
\frac12\,|f(x_0)|\;\pi\,\delta^2
\;>\;0,
\]
which contradicts the hypothesis that every ball of radius \(r\) has integral zero.  Hence no such \(x_0\) exists, and we conclude
\[
f(x)\;=\;0\quad\text{for all }x\in\mathbb{R}^2.
\]
```