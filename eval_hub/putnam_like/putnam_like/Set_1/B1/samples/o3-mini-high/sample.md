```latex
\textbf{Solution:}

We wish to solve
\[
6^{x^2} + 5^{x^2} - 10^{x^2} = 1
\]
for all real numbers \( x \).

\smallskip

\textbf{Step 1. Substitute:} 

Since \( x^2 \ge 0 \) for all \( x \in \mathbb{R} \), let
\[
y = x^2 \quad \text{with } y \ge 0.
\]
Then the equation becomes
\[
6^y + 5^y - 10^y = 1.
\]

\smallskip

\textbf{Step 2. Check obvious values:}

\textit{Case 1:} \( y = 0 \)  
We have
\[
6^0 + 5^0 - 10^0 = 1 + 1 - 1 = 1.
\]
Thus, \( y = 0 \) is a solution which corresponds to
\[
x^2 = 0 \quad \Longrightarrow \quad x = 0.
\]

\smallskip

\textit{Case 2:} \( y = 1 \)  
We calculate
\[
6^1 + 5^1 - 10^1 = 6 + 5 - 10 = 1.
\]
Thus, \( y = 1 \) is also a solution, and it corresponds to
\[
x^2 = 1 \quad \Longrightarrow \quad x = \pm 1.
\]

\smallskip

\textbf{Step 3. Show there are no other solutions:}

Define the function
\[
f(y) = 6^y + 5^y - 10^y.
\]
We need to solve
\[
f(y) = 1 \quad \text{for } y \ge 0.
\]

Notice that:
\[
f(0) = 6^0 + 5^0 - 10^0 = 1 + 1 - 1 = 1
\]
and
\[
f(1) = 6^1 + 5^1 - 10^1 = 6 + 5 - 10 = 1.
\]

Evaluating at an intermediate point, say \( y = 0.5 \):
\[
f(0.5) \approx \sqrt{6} + \sqrt{5} - \sqrt{10} \approx 2.45 + 2.24 - 3.16 \approx 1.53,
\]
which shows that \( f(y) \) exceeds 1 for some \( y \) in the interval \((0,1)\). However, for \( y > 1 \), the term \( 10^y \) grows more rapidly than \( 6^y \) and \( 5^y \), causing \( f(y) \) to drop below 1. Hence, the equation
\[
6^y + 5^y - 10^y = 1
\]
is satisfied only at \( y = 0 \) and \( y = 1 \).

\smallskip

\textbf{Conclusion:}

Recalling the substitution \( y = x^2 \), we have the solutions:
\[
x^2 = 0 \quad \Longrightarrow \quad x = 0,
\]
\[
x^2 = 1 \quad \Longrightarrow \quad x = -1 \quad \text{or} \quad x = 1.
\]
Therefore, the complete solution set is
\[
\boxed{x = -1,\quad 0,\quad \text{or} \quad 1.}
\]
```