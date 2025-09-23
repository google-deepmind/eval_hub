Here is a detailed, step-by-step solution to the problem.

### 1. Understanding the Problem

We are given a second-order nonlinear ordinary differential equation (ODE) for a function $u(x)$:
$$ ( u' )^2 (1+u^2) = 1 - u'' u \quad (*)$$
with the initial condition $u(0)=0$. We are also told that $u$ is a $\mathcal{C}^1$ function, meaning $u$ and its first derivative $u'$ are continuous. The presence of $u''$ in the equation implies that $u$ must be twice differentiable. We want to prove that for all $x>0$, the inequality $|u(x)| < \sqrt{2x}$ holds.

This inequality is equivalent to $u(x)^2 < 2x$ for $x>0$. This suggests that analyzing the evolution of $u(x)^2$ might be a fruitful approach.

### 2. Transforming the Differential Equation

Let's define a new function $v(x) = u(x)^2$. We will derive a differential equation for $v(x)$.
First, we find the first and second derivatives of $v(x)$ with respect to $x$:
- **First derivative:** Using the chain rule,
  $$ v'(x) = \frac{d}{dx} (u(x)^2) = 2u(x)u'(x) $$
- **Second derivative:** Using the product rule and chain rule,
  $$ v''(x) = \frac{d}{dx} (2u(x)u'(x)) = 2(u'(x))^2 + 2u(x)u''(x) $$

Now, let's rearrange the original ODE $(*)$ to isolate the term $u u''$:
$$ u u'' = 1 - (u')^2(1+u^2) = 1 - (u')^2 - u^2(u')^2 $$
Substitute this expression for $u u''$ into our equation for $v''(x)$:
$$ v''(x) = 2(u')^2 + 2 \left( 1 - (u')^2 - u^2(u')^2 \right) $$
$$ v''(x) = 2(u')^2 + 2 - 2(u')^2 - 2u^2(u')^2 $$
$$ v''(x) = 2 - 2u^2(u')^2 $$
We can express the term $u^2(u')^2$ in terms of $v'(x)$. From the expression for $v'$, we have $v'(x) = 2u(x)u'(x)$. Squaring both sides gives:
$$ (v'(x))^2 = (2u(x)u'(x))^2 = 4u^2(x)(u'(x))^2 $$
Therefore, $u^2(u')^2 = \frac{(v'(x))^2}{4}$.
Substituting this back into the equation for $v''(x)$:
$$ v''(x) = 2 - 2 \left( \frac{(v'(x))^2}{4} \right) $$
$$ v''(x) = 2 - \frac{(v'(x))^2}{2} \quad (**) $$
This is a much simpler ODE for the function $v(x)$.

### 3. Finding the Initial Conditions for $v(x)$

We use the given initial condition $u(0)=0$ to find the initial conditions for $v(x)$ and $v'(x)$:
- $v(0) = u(0)^2 = 0^2 = 0$.
- $v'(0) = 2u(0)u'(0) = 2 \cdot 0 \cdot u'(0) = 0$.

So we have a second-order initial value problem for $v(x)$:
$$ v'' = 2 - \frac{(v')^2}{2}, \quad v(0)=0, \quad v'(0)=0 $$

### 4. Solving the ODE for $v(x)$

The ODE for $v(x)$ is autonomous (it does not explicitly depend on $x$). We can reduce its order by letting $w(x) = v'(x)$. Then $w'(x) = v''(x)$. The ODE becomes a first-order equation in $w(x)$:
$$ w' = 2 - \frac{w^2}{2} $$
with the initial condition $w(0) = v'(0) = 0$.

This is a separable differential equation:
$$ \frac{dw}{dx} = \frac{4-w^2}{2} $$
$$ \frac{dw}{4-w^2} = \frac{1}{2} dx $$
We can integrate both sides. The left side is integrated using partial fraction decomposition:
$$ \frac{1}{4-w^2} = \frac{1}{(2-w)(2+w)} = \frac{A}{2-w} + \frac{B}{2+w} $$
Solving for $A$ and $B$ gives $A=1/4$ and $B=1/4$. So,
$$ \int \left( \frac{1/4}{2-w} + \frac{1/4}{2+w} \right) dw = \int \frac{1}{2} dx $$
$$ \frac{1}{4} \left( -\ln|2-w| + \ln|2+w| \right) = \frac{x}{2} + C_1 $$
$$ \frac{1}{4} \ln\left|\frac{2+w}{2-w}\right| = \frac{x}{2} + C_1 $$
$$ \ln\left|\frac{2+w}{2-w}\right| = 2x + 4C_1 $$
$$ \left|\frac{2+w}{2-w}\right| = e^{2x + 4C_1} = C e^{2x}, \quad \text{where } C = e^{4C_1} $$
Now, we use the initial condition $w(0)=0$:
$$ \left|\frac{2+0}{2-0}\right| = C e^{0} \implies |1| = C \implies C=1 $$
So the equation for $w(x)$ is:
$$ \left|\frac{2+w}{2-w}\right| = e^{2x} $$
For $x>0$, we need to determine the sign of the expression inside the absolute value. We start with $w(0)=0$. The derivative is $w' = (4-w^2)/2$. At $x=0$, $w'(0) = (4-0^2)/2 = 2 > 0$. This means $w(x)$ is increasing for $x$ near 0. As long as $|w(x)| < 2$, $w'(x)$ remains positive, so $w(x)$ will continue to increase. It will approach the stable equilibrium point $w=2$ as $x \to \infty$. Thus, for $x>0$, we have $0 \le w(x) < 2$.
This implies that both $2+w$ and $2-w$ are positive, so we can drop the absolute value:
$$ \frac{2+w}{2-w} = e^{2x} $$
Now we solve for $w(x)$:
$$ 2+w = e^{2x}(2-w) = 2e^{2x} - w e^{2x} $$
$$ w + w e^{2x} = 2e^{2x} - 2 $$
$$ w(1+e^{2x}) = 2(e^{2x} - 1) $$
$$ w(x) = 2 \frac{e^{2x}-1}{e^{2x}+1} $$
This expression is equivalent to the hyperbolic tangent function. By dividing the numerator and denominator by $e^x$:
$$ w(x) = 2 \frac{e^x - e^{-x}}{e^x + e^{-x}} = 2 \tanh(x) $$
Since $w(x) = v'(x)$, we have $v'(x) = 2 \tanh(x)$. To find $v(x)$, we integrate $v'(x)$:
$$ v(x) = \int 2 \tanh(x) dx = 2 \ln(\cosh(x)) + C_2 $$
Using the initial condition $v(0)=0$:
$$ v(0) = 2 \ln(\cosh(0)) + C_2 = 2 \ln(1) + C_2 = 0 + C_2 $$
So, $C_2=0$. The solution for $v(x)$ is:
$$ v(x) = 2 \ln(\cosh(x)) $$

### 5. Proving the Final Inequality

We have found that $u(x)^2 = v(x) = 2 \ln(\cosh(x))$. The inequality we want to prove is $|u(x)| < \sqrt{2x}$ for $x>0$. As we noted earlier, this is equivalent to proving:
$$ u(x)^2 < 2x $$
Substituting our expression for $u(x)^2$:
$$ 2 \ln(\cosh(x)) < 2x $$
$$ \ln(\cosh(x)) < x $$
Since the exponential function $f(t)=e^t$ is strictly increasing, we can exponentiate both sides without changing the inequality's direction:
$$ e^{\ln(\cosh(x))} < e^x $$
$$ \cosh(x) < e^x $$
Now we use the definition of the hyperbolic cosine, $\cosh(x) = \frac{e^x + e^{-x}}{2}$:
$$ \frac{e^x + e^{-x}}{2} < e^x $$
Multiplying both sides by 2 (which is positive):
$$ e^x + e^{-x} < 2e^x $$
Subtracting $e^x$ from both sides:
$$ e^{-x} < e^x $$
Since the natural logarithm function $f(t)=\ln(t)$ is strictly increasing for $t>0$, we can take the logarithm of both sides:
$$ \ln(e^{-x}) < \ln(e^x) $$
$$ -x < x $$
$$ 0 < 2x $$
$$ 0 < x $$
This final inequality, $x>0$, is precisely the condition given in the problem. All the steps in this final derivation are reversible for $x>0$. Therefore, the inequality $\cosh(x) < e^x$ is true for all $x>0$, which in turn implies that $u(x)^2 < 2x$ for all $x>0$.

### Conclusion

Taking the square root of both sides of $u(x)^2 < 2x$ gives:
$$ \sqrt{u(x)^2} < \sqrt{2x} $$
$$ |u(x)| < \sqrt{2x} $$
This holds for all $x>0$, which is what we needed to show.