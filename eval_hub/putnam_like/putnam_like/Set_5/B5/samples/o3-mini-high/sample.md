```markdown
We wish to determine the number of zeros of
\[
P(z)= z^8 - 5z^3+10,
\]
inside the set
\[
A=\{z\in\mathbb{C}:\tfrac{\pi}{2}\leq\arg z\leq\pi\}.
\]
Since \(P(z)\) is a polynomial of degree 8, it has exactly 8 zeros (counted with multiplicity) in \(\mathbb{C}\). Our goal is to count how many of these lie in the sector \(A\).

### Step 1. Applying Rouché’s Theorem

Write
\[
P(z)= z^8 + \bigl(-5z^3+10\bigr).
\]
Define
\[
f(z)=z^8 \quad \text{and} \quad g(z)=-5z^3+10.
\]
We shall show that on a suitable contour the term \(z^8\) dominates the perturbation \(-5z^3+10\).

Choose a large radius \(R>0\) and consider the arc of the circle
\[
\Gamma_R=\{z=Re^{i\theta}:\theta\in [\tfrac{\pi}{2},\pi]\}.
\]
On this arc, we have
\[
|f(z)|=|z^8|=R^8,
\]
and
\[
|g(z)|\leq 5R^3+10.
\]
For \(R\) sufficiently large, the inequality 
\[
R^8 > 5R^3+10
\]
holds. Therefore, by Rouché’s theorem the functions \(f(z)=z^8\) and
\[
P(z)=z^8+(-5z^3+10)
\]
have the same number of zeros inside the closed contour formed by \(\Gamma_R\) together with the two rays along \(\arg z=\frac{\pi}{2}\) and \(\arg z=\pi\) (and a small circular arc near the origin if needed).

### Step 2. Counting the Zeros of \(z^8\) in the Sector

The function \(f(z)=z^8\) has a zero of multiplicity 8 at \(z=0\). Although all “zeros” coincide at the origin, when counting their distribution according to angle (i.e. via the argument principle) the zero “splits” evenly among all directions. In any sector of angular width \(\Delta\theta\) (with the vertex at the origin) the number of zeros (counted with multiplicity) is
\[
n = 8\cdot \frac{\Delta\theta}{2\pi}.
\]

For the sector
\[
A=\{z:\tfrac{\pi}{2}\leq\arg z\leq\pi\},
\]
the angular width is
\[
\Delta\theta = \pi-\tfrac{\pi}{2} = \tfrac{\pi}{2}.
\]
Thus, the number of zeros of \(z^8\) in \(A\) is
\[
n = 8\cdot \frac{\pi/2}{2\pi} = 8\cdot \frac{1}{4} = 2.
\]

### Step 3. Conclusion

By Rouché’s theorem, since \(z^8\) and \(P(z)\) have the same number of zeros in the region bounded by the modified contour (which eventually covers the whole unbounded sector \(A\)), it follows that
\[
P(z)=z^8-5z^3+10
\]
also has exactly \(\boxed{2}\) zeros in the set \(A\).

**Answer:** The polynomial \(P(z)\) has 2 zeros in the set \(A\).
```