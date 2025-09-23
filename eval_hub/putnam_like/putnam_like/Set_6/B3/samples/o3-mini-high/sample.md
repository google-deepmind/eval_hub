```markdown
We are given a function 
\[
f:\mathbb{R}\to\mathbb{R}
\]
with a continuous derivative, and the inequality
\[
|f'(x)|\leq |f(x)-f(0)|
\]
for all \( x\in\mathbb{R} \). Our goal is to show that \( f \) is constant; that is, \( f(x) = f(0) \) for every \( x \).

### Step 1. Define an Auxiliary Function

Define the function
\[
g(x) = f(x) - f(0).
\]
Notice that \( g(0)=0 \), and \( g \) inherits continuous differentiability from \( f \). The given inequality becomes
\[
|g'(x)|\leq |g(x)|.
\]

### Step 2. Consider the Squared Function

A common method is to examine the square of \( g(x) \). Define
\[
G(x) = [g(x)]^2 = [f(x)-f(0)]^2.
\]
Since \( G(0) = 0 \) and \( G(x) \geq 0 \) for all \( x \), we differentiate \( G \) with respect to \( x \). Using the chain rule, we obtain
\[
G'(x) = 2 g(x) g'(x).
\]
Taking absolute values on both sides gives
\[
|G'(x)| = 2 |g(x)|\,|g'(x)|.
\]

### Step 3. Apply the Given Inequality

Using the inequality \( |g'(x)|\leq |g(x)| \), we have
\[
|G'(x)| \leq 2 |g(x)|^2 = 2 G(x).
\]
This differential inequality, along with the fact that \( G(0)=0 \), will force \( G(x) \) to be identically zero.

### Step 4. Conclude the Proof via Gronwall's Inequality

One way to see this is to apply Gronwall's inequality. For a function \( H(x) \) satisfying
\[
H'(x) \leq C \, H(x) \quad \text{with} \quad H(0)=0,
\]
Gronwall's lemma implies that \( H(x)=0 \) for all \( x \). In our case, since
\[
|G'(x)|\le 2G(x) \quad \text{and} \quad G(0)=0,
\]
it follows that \( G(x)=0 \) for all \( x \). 

### Step 5. Final Conclusion

Since
\[
G(x) = [g(x)]^2 = 0 \quad \text{for all } x,
\]
we deduce that \( g(x)=0 \) for all \( x \). Recalling that \( g(x)=f(x)-f(0) \), we conclude that
\[
f(x) = f(0) \quad \text{for all } x.
\]
Thus, the function \( f \) is constant.
```