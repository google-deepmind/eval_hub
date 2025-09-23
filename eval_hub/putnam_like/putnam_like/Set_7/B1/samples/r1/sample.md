

To show that \( g(x) = \int_{x}^{x+1} f(y) \, dy \) is Lebesgue integrable and that \( \int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(x) \, dx \), proceed as follows:

### Step 1: Show \( g \) is Lebesgue Integrable
By the triangle inequality for integrals:
\[
|g(x)| \leq \int_{x}^{x+1} |f(y)| \, dy.
\]
Integrate both sides over \( \mathbb{R} \):
\[
\int_{-\infty}^\infty |g(x)| \, dx \leq \int_{-\infty}^\infty \left( \int_{x}^{x+1} |f(y)| \, dy \right) dx.
\]
Apply **Tonelli's Theorem** to switch the order of integration (justified as \( |f| \geq 0 \)):
\[
\int_{-\infty}^\infty |g(x)| \, dx \leq \int_{-\infty}^\infty |f(y)| \left( \int_{y-1}^{y} dx \right) dy = \int_{-\infty}^\infty |f(y)| \, dy.
\]
Since \( f \) is Lebesgue integrable, \( \int |f| < \infty \), so \( \int |g| < \infty \). Thus, \( g \) is Lebesgue integrable.

### Step 2: Compute \( \int_{-\infty}^\infty g(x) \, dx \)
Use **Fubini's Theorem** (justified as \( g \) is integrable):
\[
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty \left( \int_{x}^{x+1} f(y) \, dy \right) dx = \int_{-\infty}^\infty f(y) \left( \int_{y-1}^{y} dx \right) dy.
\]
The inner integral over \( x \) evaluates to 1:
\[
\int_{y-1}^{y} dx = 1 \quad \text{for all } y.
\]
Thus:
\[
\int_{-\infty}^\infty g(x) \, dx = \int_{-\infty}^\infty f(y) \, dy.
\]
This completes the proof.