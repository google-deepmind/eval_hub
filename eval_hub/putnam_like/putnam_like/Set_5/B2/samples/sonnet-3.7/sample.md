# Solution

The problem involves $n \times n$ invertible matrices $A$ and $B$ that satisfy the conditions $A+B=I$ and $A^4+B^4=I$. We need to compute $\det(AB)$.

## Step 1: Find constraints on eigenvalues of matrices $A$ and $B$.

From $A+B=I$, we get $B=I-A$. For any eigenvalue $\lambda$ of $A$ with corresponding eigenvector $v$, we have:
$$Av = \lambda v$$

This means:
$$Bv = (I-A)v = v - \lambda v = (1-\lambda)v$$

So if $\lambda$ is an eigenvalue of $A$, then $\mu = 1-\lambda$ is an eigenvalue of $B$ with the same eigenvector.

## Step 2: Use the condition $A^4+B^4=I$.

Substituting $B=I-A$ into $A^4+B^4=I$:
$$A^4+(I-A)^4=I$$

Expanding $(I-A)^4$:
$$(I-A)^4 = I-4A+6A^2-4A^3+A^4$$

Therefore:
$$A^4+I-4A+6A^2-4A^3+A^4=I$$
$$2A^4-4A^3+6A^2-4A=0$$
$$A(2A^3-4A^2+6A-4I)=0$$

Since $A$ is invertible, we have:
$$2A^3-4A^2+6A-4I=0$$
$$A^3-2A^2+3A-2I=0$$

## Step 3: Find the eigenvalues of $A$.

If $\lambda$ is an eigenvalue of $A$, then applying the above equation to its eigenvector gives:
$$\lambda^3-2\lambda^2+3\lambda-2=0$$

Factoring this cubic equation:
$$(\lambda-1)(\lambda^2-\lambda+2)=0$$

This gives us $\lambda=1$ or $\lambda^2-\lambda+2=0$. Using the quadratic formula:
$$\lambda = \frac{1 \pm \sqrt{1-4 \cdot 1 \cdot 2}}{2} = \frac{1 \pm \sqrt{-7}}{2} = \frac{1 \pm i\sqrt{7}}{2}$$

So the possible eigenvalues of $A$ are:
- $\lambda_1 = 1$
- $\lambda_2 = \frac{1 + i\sqrt{7}}{2}$
- $\lambda_3 = \frac{1 - i\sqrt{7}}{2}$

## Step 4: Consider the invertibility constraints.

Since $B$ is invertible, none of its eigenvalues can be zero. If $\lambda$ is an eigenvalue of $A$, the corresponding eigenvalue of $B$ is $\mu = 1-\lambda$. 

If $\lambda = 1$, then $\mu = 0$, which contradicts the invertibility of $B$.

Therefore, the eigenvalues of $A$ must only be $\frac{1 + i\sqrt{7}}{2}$ and $\frac{1 - i\sqrt{7}}{2}$.

## Step 5: Compute $\det(AB)$.

The determinant of a matrix equals the product of its eigenvalues. Let's say $A$ has $r$ eigenvalues equal to $\frac{1 + i\sqrt{7}}{2}$ and $s$ eigenvalues equal to $\frac{1 - i\sqrt{7}}{2}$, where $r+s=n$.

$$\det(A) = \left(\frac{1 + i\sqrt{7}}{2}\right)^r \cdot \left(\frac{1 - i\sqrt{7}}{2}\right)^s$$

The corresponding eigenvalues of $B$ are $\frac{1 - i\sqrt{7}}{2}$ (corresponding to $\lambda = \frac{1 + i\sqrt{7}}{2}$) and $\frac{1 + i\sqrt{7}}{2}$ (corresponding to $\lambda = \frac{1 - i\sqrt{7}}{2}$). Therefore:

$$\det(B) = \left(\frac{1 - i\sqrt{7}}{2}\right)^r \cdot \left(\frac{1 + i\sqrt{7}}{2}\right)^s$$

Now, for $\det(AB)$:
$$\det(AB) = \det(A) \cdot \det(B)$$
$$= \left(\frac{1 + i\sqrt{7}}{2}\right)^r \cdot \left(\frac{1 - i\sqrt{7}}{2}\right)^s \cdot \left(\frac{1 - i\sqrt{7}}{2}\right)^r \cdot \left(\frac{1 + i\sqrt{7}}{2}\right)^s$$
$$= \left(\frac{1 + i\sqrt{7}}{2}\right)^{r+s} \cdot \left(\frac{1 - i\sqrt{7}}{2}\right)^{r+s}$$
$$= \left[\left(\frac{1 + i\sqrt{7}}{2}\right) \cdot \left(\frac{1 - i\sqrt{7}}{2}\right)\right]^{r+s}$$
$$= \left[\frac{(1+i\sqrt{7})(1-i\sqrt{7})}{4}\right]^{r+s}$$
$$= \left[\frac{1+7}{4}\right]^{r+s}$$
$$= \left[\frac{8}{4}\right]^{r+s}$$
$$= 2^{r+s}$$
$$= 2^n$$

Therefore, $\det(AB) = 2^n$.