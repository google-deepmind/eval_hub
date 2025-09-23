This step is worth 1 point.
If one of the sum $(a_i+b_i+c_i)$ is zero then both side of the inequality equal $0$.

This step is worth 1 point.
Now assume that right hand side is non-zero and divide both side by it. We are going to prove
$$
\left(\prod_{i=1}^n \frac{a_i}{a_i+b_i+c_i}\right)^\frac 1n+
\left(\prod_{i=1}^n \frac{b_i}{a_i+b_i+c_i}\right)^\frac 1n+
\left(\prod_{i=1}^n \frac{c_i}{a_i+b_i+c_i}\right)^\frac 1n \leq 1
$$

This step is worth 7 points.
Applying AM-GM inequality to the first summand 
$$
\left(\prod_{i=1}^n \frac{a_i}{a_i+b_i+c_i}\right)^\frac 1n \leq
\frac 1n \sum \frac{a_i}{a_i+b_i+c_i}.
$$
Similar inequalities we can write for the second and the third summand.

This step is worth 1 point.
Adding three inequalities we get the desired result directly.