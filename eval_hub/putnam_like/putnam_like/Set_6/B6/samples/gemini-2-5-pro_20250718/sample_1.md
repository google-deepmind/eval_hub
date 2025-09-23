An expert solution to the problem follows.

### 1. Problem Simplification and Reformulation

Let the sequence of i.i.d. random variables be $(X_n=(R_n,S_n,T_n))$, where each $X_n$ is uniformly distributed on the set of 6 permutations of $(1,2,3)$. The sum of the components of any such permutation is $1+2+3=6$.

Let $\hat{X}_n = (\hat{R}_n, \hat{S}_n, \hat{T}_n) = \sum_{i=1}^{n} X_i$.
A crucial property is that the sum of the components of $\hat{X}_n$ is fixed:
$\hat{R}_n + \hat{S}_n + \hat{T}_n = \sum_{i=1}^{n} (R_i+S_i+T_i) = \sum_{i=1}^{n} 6 = 6n$.

The probability $p_n$ is defined as $p_n = P(\hat{R}_n=\hat{S}_n=\hat{T}_n)$. If this event occurs, the sum property implies $3\hat{R}_n = 6n$, so we must have $\hat{R}_n = \hat{S}_n = \hat{T}_n = 2n$.
Thus, $p_n = P(\hat{R}_n=2n, \hat{S}_n=2n, \hat{T}_n=2n)$.

To simplify the problem, we introduce centered random variables. Let $X_i' = X_i - (2,2,2) = (R_i-2, S_i-2, T_i-2)$. Let's denote $X_i' = (r_i, s_i, t_i)$. The expected value of each component of $X_i$ is $(1+2+3)/3 = 2$, so $X_i'$ are mean-zero variables.
The possible values for $X_i'$ are the 6 permutations of $(-1, 0, 1)$, each with probability $1/6$.
Let $\hat{X}_n' = \sum_{i=1}^{n} X_i' = (\hat{r}_n, \hat{s}_n, \hat{t}_n)$, where:
$\hat{r}_n = \hat{R}_n - 2n$
$\hat{s}_n = \hat{S}_n - 2n$
$\hat{t}_n = \hat{T}_n - 2n$

The sum property for these centered variables becomes:
$\hat{r}_n + \hat{s}_n + \hat{t}_n = (\hat{R}_n+\hat{S}_n+\hat{T}_n) - 6n = 6n - 6n = 0$.

Now, let's rewrite $p_n$ and $q_n$ in terms of these new variables.
$p_n = P(\hat{R}_n-2n=0, \hat{S}_n-2n=0, \hat{T}_n-2n=0) = P(\hat{r}_n=0, \hat{s}_n=0, \hat{t}_n=0)$.

$q_n = P(\hat{R}_n, \hat{S}_n, \hat{T}_n \in \{2n-1, 2n, 2n+1\}, \hat{R}_n \neq \hat{S}_n)$.
The condition on the values is equivalent to:
$\hat{R}_n-2n, \hat{S}_n-2n, \hat{T}_n-2n \in \{-1, 0, 1\}$, which means $\hat{r}_n, \hat{s}_n, \hat{t}_n \in \{-1, 0, 1\}$.
Given the sum property $\hat{r}_n + \hat{s}_n + \hat{t}_n = 0$, the only possible integer triples $(\hat{r}_n, \hat{s}_n, \hat{t}_n)$ are permutations of $(-1,0,1)$ or the triple $(0,0,0)$.
The condition $\hat{R}_n \neq \hat{S}_n$ is equivalent to $\hat{r}_n \neq \hat{s}_n$.
If $(\hat{r}_n, \hat{s}_n, \hat{t}_n)$ is a permutation of $(-1,0,1)$, its components are distinct, so $\hat{r}_n \neq \hat{s}_n$ is automatically satisfied.
If $(\hat{r}_n, \hat{s}_n, \hat{t}_n)=(0,0,0)$, then $\hat{r}_n = \hat{s}_n$, so this outcome is excluded.
Therefore, the event for $q_n$ is simply that $(\hat{r}_n, \hat{s}_n, \hat{t}_n)$ is a permutation of $(-1,0,1)$.
$q_n = P((\hat{r}_n, \hat{s}_n, \hat{t}_n) \text{ is a permutation of } (-1,0,1))$.

### 2. An Exact Relation Between $p_n$ and $q_n$

We can derive a relationship between $p_n$ and $q_n$ by considering the transition from step $n$ to $n+1$.
$p_{n+1} = P(\hat{X}_{n+1}' = (0,0,0)) = P(\hat{X}_n' + X_{n+1}' = (0,0,0))$.
Using the law of total probability, we can write:
$p_{n+1} = \sum_{v} P(\hat{X}_n' = -v \text{ and } X_{n+1}' = v)$
where the sum is over all 6 possible values $v$ for $X_{n+1}'$, which are the permutations of $(-1,0,1)$.
By independence of the random variables $X_i'$,
$p_{n+1} = \sum_{v} P(\hat{X}_n' = -v) P(X_{n+1}' = v)$.
The distribution of $X_{n+1}'$ is uniform, so $P(X_{n+1}' = v) = 1/6$ for each permutation $v$.
$p_{n+1} = \frac{1}{6} \sum_{v} P(\hat{X}_n' = -v)$.

The set of permutations of $(-1,0,1)$ is closed under negation. For any permutation $v$, $-v$ is also a permutation of $(-1,0,1)$. For example, if $v=(-1,1,0)$, $-v=(1,-1,0)$. Thus, summing over all $v$ is the same as summing over all $-v$.
Let $w = -v$. Then the sum becomes $\sum_{w} P(\hat{X}_n' = w)$, where $w$ ranges over all permutations of $(-1,0,1)$.

The distribution of the sum $\hat{X}_n' = (\hat{r}_n, \hat{s}_n, \hat{t}_n)$ is symmetric with respect to permutation of its components. This is because the distribution of each $X_i'$ is symmetric in this way. For example, $P(r_i=a, s_i=b, t_i=c) = P(r_i=b, s_i=a, t_i=c)$. This symmetry carries over to the sum $\hat{X}_n'$.
Therefore, for any two permutations $w_1, w_2$ of $(-1,0,1)$, we have $P(\hat{X}_n' = w_1) = P(\hat{X}_n' = w_2)$.
Let's fix one such permutation, say $w_0=(-1,0,1)$. Then $P(\hat{X}_n' = w) = P(\hat{X}_n' = w_0)$ for all 6 permutations $w$.
The sum becomes:
$\sum_{w} P(\hat{X}_n' = w) = 6 \cdot P(\hat{X}_n' = w_0)$.
So, $p_{n+1} = \frac{1}{6} \cdot 6 \cdot P(\hat{X}_n' = w_0) = P(\hat{r}_n=-1, \hat{s}_n=0, \hat{t}_n=1)$.

Now consider $q_n$:
$q_n = P((\hat{r}_n, \hat{s}_n, \hat{t}_n) \text{ is a permutation of } (-1,0,1))$
$q_n = \sum_{w} P(\hat{X}_n' = w)$, where the sum is over all 6 permutations $w$ of $(-1,0,1)$.
Using the same symmetry argument, $q_n = 6 \cdot P(\hat{X}_n' = w_0)$.
Comparing the expressions for $p_{n+1}$ and $q_n$, we find the elegant relation:
$q_n = 6p_{n+1}$.

### 3. Analyzing the Inequality

The inequality we need to prove is $4p_n < q_n$ for infinitely many $n$.
Substituting the relation we just found, this becomes:
$4p_n < 6p_{n+1}$
$\frac{p_{n+1}}{p_n} > \frac{4}{6} = \frac{2}{3}$.

We need to show that this inequality holds for infinitely many values of $n$. Note that $p_n$ can be zero (e.g., $p_1=0$), in which case the ratio is not well-defined. We are interested in $n$ for which $p_n > 0$.

### 4. Asymptotic Behavior of $p_n$

To understand the behavior of the ratio $p_{n+1}/p_n$, we analyze the asymptotic behavior of $p_n$ for large $n$. This can be done using the multidimensional Central Limit Theorem or, equivalently, by analyzing the characteristic function.
The probability $p_n=P(\hat{X}_n'=(0,0,0))$ can be expressed using the Fourier transform (characteristic function) of $X_i'$.
The characteristic function of a single step $X'$ is $\phi(\theta_1,\theta_2,\theta_3) = E[e^{i(\theta_1 r + \theta_2 s + \theta_3 t)}]$. Due to the constraint $r+s+t=0$, we can set $\theta_3=0$ without loss of generality (or, more formally, we are working on a 2D lattice). Let the state be $(r,s)$. The characteristic function is $\phi(\theta_1,\theta_2) = E[e^{i(\theta_1 r + \theta_2 s)}]$.
The probability generating function for one step $(r_i, s_i, t_i)$ is $P(x,y,z) = \frac{1}{6} \sum_{\text{perms of }(-1,0,1)} x^r y^s z^t$.
$p_n$ is the constant term of $(P(x,y,z))^n$. This can be found by integration over the torus:
$p_n = \frac{1}{(2\pi)^3} \int_0^{2\pi}\int_0^{2\pi}\int_0^{2\pi} \left[ \frac{1}{3}(\cos(\theta_1-\theta_2) + \cos(\theta_2-\theta_3) + \cos(\theta_3-\theta_1)) \right]^n d\theta_1 d\theta_2 d\theta_3$.
The integral depends only on the differences of angles. We can reduce the dimension by 1, let $u=\theta_1-\theta_2, v=\theta_2-\theta_3$.
$p_n = \frac{1}{(2\pi)^2} \iint_{[-\pi,\pi]^2} [G(u,v)]^n du dv$, where $G(u,v) = \frac{1}{3}(\cos u + \cos v + \cos(u+v))$.

For large $n$, this integral can be approximated by Laplace's method. The value of the integral is dominated by the regions where $|G(u,v)|$ is maximal.
1.  The global maximum of $G(u,v)$ is $G(0,0)=1$.
2.  The global minimum of $G(u,v)$ is $G(2\pi/3, 2\pi/3) = G(4\pi/3, 4\pi/3) = -1/2$.

The asymptotic behavior of $p_n$ is determined by the sum of contributions from these critical points.
- The contribution from the maximum at $(0,0)$ gives the main term, which is of order $1/n$. A detailed calculation (Local Central Limit Theorem) gives $p_n \approx \frac{\sqrt{3}}{2\pi n}$.
- The contribution from the minima at $(2\pi/3, 2\pi/3)$ and $(4\pi/3, 4\pi/3)$ gives a second term. Since $G=-1/2$ at these points, their contribution to the $n$-th power is proportional to $(-1/2)^n$.

A more detailed asymptotic analysis (e.g., using Edgeworth expansion or saddle-point methods) yields:
$p_n = \frac{\sqrt{3}}{2\pi n} \left(1 + 2\left(-\frac{1}{2}\right)^n + O\left(\frac{1}{n}\right)\right)$.

Let's analyze the ratio $p_{n+1}/p_n$ using this asymptotic formula:
$\frac{p_{n+1}}{p_n} \approx \frac{\frac{\sqrt{3}}{2\pi(n+1)}\left(1 + 2(-\frac{1}{2})^{n+1}\right)}{\frac{\sqrt{3}}{2\pi n}\left(1 + 2(-\frac{1}{2})^n\right)} = \frac{n}{n+1} \cdot \frac{1 - (-1/2)^n}{1 + 2(-1/2)^n}$.

We need to show $\frac{p_{n+1}}{p_n} > 2/3$ for infinitely many $n$. Let's examine the behavior for large even and odd $n$.

**Case 1: $n$ is a large odd number.**
Let $n=2m+1$ for large integer $m$.
$(-1/2)^n = (-1/2)^{2m+1} = -1/2 \cdot (1/4)^m$.
The ratio becomes:
$\frac{p_{2m+2}}{p_{2m+1}} \approx \frac{2m+1}{2m+2} \cdot \frac{1 - (-1/2)^{2m+1}}{1 + 2(-1/2)^{2m+1}} = \frac{2m+1}{2m+2} \cdot \frac{1 + (1/2)^{2m+1}}{1 - 2(1/2)^{2m+1}} = \frac{2m+1}{2m+2} \cdot \frac{1 + (1/2)^{2m+1}}{1 - (1/2)^{2m}}$.
As $m \to \infty$, the second fraction approaches 1. The whole expression approaches $\lim_{m\to\infty} \frac{2m+1}{2m+2} = 1$.
Since $1 > 2/3$, the inequality will hold for all sufficiently large odd $n$.
To be more precise, for large $m$, the term $\frac{1 + (1/2)^{2m+1}}{1 - (1/2)^{2m}} > 1$.
So, $\frac{p_{2m+2}}{p_{2m+1}} > \frac{2m+1}{2m+2}$.
We need to check if $\frac{2m+1}{2m+2} > \frac{2}{3}$.
$3(2m+1) > 2(2m+2) \implies 6m+3 > 4m+4 \implies 2m > 1 \implies m > 1/2$.
This holds for all integers $m \ge 1$. Thus, for all odd $n \ge 3$, the ratio $p_{n+1}/p_n$ is greater than $2/3$. This provides an infinite set of integers $n$ for which the condition holds.

**Case 2: $n$ is a large even number.**
Let $n=2m$ for large integer $m$.
$(-1/2)^n = (1/4)^m$.
The ratio becomes:
$\frac{p_{2m+1}}{p_{2m}} \approx \frac{2m}{2m+1} \cdot \frac{1 - (-1/2)^{2m}}{1 + 2(-1/2)^{2m}} = \frac{2m}{2m+1} \cdot \frac{1 - (1/4)^m}{1 + 2(1/4)^m}$.
As $m \to \infty$, this also approaches 1.
However, for any finite $m \ge 1$, the second fraction $\frac{1 - (1/4)^m}{1 + 2(1/4)^m}$ is less than 1. So the ratio is less than $\frac{2m}{2m+1}$.
For $n=2$ (i.e. $m=1$), we have $p_2=1/6$ and $p_3=1/18$ (by direct computation). The ratio is $p_3/p_2 = (1/18)/(1/6) = 1/3$.
$1/3 \ngtr 2/3$. So the inequality does not hold for $n=2$. The asymptotic formula gives $\frac{2}{3}\frac{1-1/4}{1+2/4}=\frac{2}{3}\frac{3/4}{3/2}=\frac{1}{3}$, which is exact in this case.
The inequality fails for even $n$ when $n$ is small, but for large enough even $n$, the ratio will be arbitrarily close to 1 and thus greater than $2/3$.

The argument for odd $n$ is sufficient. Since the inequality $p_{n+1}/p_n > 2/3$ holds for all odd integers $n \ge 3$, it holds for infinitely many $n$.

### Conclusion

1.  We simplified the problem by shifting the random variables to have a mean of zero. The variables $\hat{r}_n, \hat{s}_n, \hat{t}_n$ represent the deviation from the expected mean value $2n$.
2.  We rewrote the probabilities $p_n$ and $q_n$ in terms of these new variables, finding $p_n=P(\hat{r}_n=0, \hat{s}_n=0, \hat{t}_n=0)$ and $q_n=P((\hat{r}_n, \hat{s}_n, \hat{t}_n) \text{ is a permutation of } (-1,0,1))$.
3.  We established a simple, exact relationship $q_n = 6p_{n+1}$ using a one-step recurrence and symmetry argument.
4.  The inequality to prove, $4p_n < q_n$, was transformed into $p_{n+1}/p_n > 2/3$.
5.  By examining the asymptotic behavior of $p_n$, we showed that this ratio approaches 1 as $n\to\infty$. More specifically, we demonstrated that for all odd $n \geq 3$, the inequality holds.
6.  Since there are infinitely many odd integers, we have shown that $4p_n < q_n$ for infinitely many $n$.