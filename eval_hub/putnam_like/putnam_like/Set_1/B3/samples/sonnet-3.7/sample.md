# Solution

To show that $\Psi$ is convex on $[p,q]$, I'll use the second derivative test: a twice-differentiable function is convex if its second derivative is non-negative.

Let's define $I(s) = \int_{\mathbb{R}^n} |f(x)|^s \, dx$, so that $\Psi(s) = \ln(I(s))$.

## First Derivative

Using the chain rule:
$$\Psi'(s) = \frac{I'(s)}{I(s)}$$

To find $I'(s)$, I'll differentiate under the integral sign:
$$I'(s) = \frac{d}{ds} \int_{\mathbb{R}^n} |f(x)|^s \, dx = \int_{\mathbb{R}^n} \frac{\partial}{\partial s}|f(x)|^s \, dx = \int_{\mathbb{R}^n} |f(x)|^s \ln|f(x)| \, dx$$

Therefore:
$$\Psi'(s) = \frac{\int_{\mathbb{R}^n} |f(x)|^s \ln|f(x)| \, dx}{\int_{\mathbb{R}^n} |f(x)|^s \, dx}$$

## Second Derivative

Using the quotient rule:
$$\Psi''(s) = \frac{I''(s)I(s) - I'(s)^2}{I(s)^2}$$

I need to find $I''(s)$:
$$I''(s) = \frac{d}{ds}\int_{\mathbb{R}^n} |f(x)|^s \ln|f(x)| \, dx = \int_{\mathbb{R}^n} \frac{\partial}{\partial s}(|f(x)|^s \ln|f(x)|) \, dx$$

Using the product rule:
$$\frac{\partial}{\partial s}(|f(x)|^s \ln|f(x)|) = \ln|f(x)| \cdot \frac{\partial}{\partial s}|f(x)|^s + |f(x)|^s \cdot \frac{\partial}{\partial s}\ln|f(x)|$$

Since $\ln|f(x)|$ doesn't depend on $s$, the second term is zero. Therefore:
$$\frac{\partial}{\partial s}(|f(x)|^s \ln|f(x)|) = \ln|f(x)| \cdot |f(x)|^s \ln|f(x)| = |f(x)|^s \ln^2|f(x)|$$

This gives:
$$I''(s) = \int_{\mathbb{R}^n} |f(x)|^s \ln^2|f(x)| \, dx$$

Substituting into the formula for $\Psi''(s)$:
$$\Psi''(s) = \frac{\int_{\mathbb{R}^n} |f(x)|^s \ln^2|f(x)| \, dx \cdot \int_{\mathbb{R}^n} |f(x)|^s \, dx - \left(\int_{\mathbb{R}^n} |f(x)|^s \ln|f(x)| \, dx\right)^2}{\left(\int_{\mathbb{R}^n} |f(x)|^s \, dx\right)^2}$$

## Probabilistic Interpretation

Define a probability measure on $\mathbb{R}^n$ by:
$$d\mu_s(x) = \frac{|f(x)|^s \, dx}{\int_{\mathbb{R}^n} |f(x)|^s \, dx}$$

Then $\Psi''(s)$ can be rewritten as:
$$\Psi''(s) = \int_{\mathbb{R}^n} \ln^2|f(x)| \, d\mu_s(x) - \left(\int_{\mathbb{R}^n} \ln|f(x)| \, d\mu_s(x)\right)^2$$

This is precisely the variance of the random variable $\ln|f(X)|$ when $X$ has distribution $\mu_s$:
$$\Psi''(s) = \text{Var}_{\mu_s}(\ln|f|) = \mathbb{E}_{\mu_s}[\ln^2|f|] - \mathbb{E}_{\mu_s}[\ln|f|]^2$$

Since variance is always non-negative, we have $\Psi''(s) \geq 0$ for all $s \in [p,q]$.

Therefore, $\Psi$ is convex on $[p,q]$.