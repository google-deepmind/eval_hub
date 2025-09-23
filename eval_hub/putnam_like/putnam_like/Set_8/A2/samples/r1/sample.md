

To find the equation of the parabola tangent to the lines \( y = 0 \) and \( x = 0 \) at points \( (\alpha, 0) \) and \( (0, \beta) \), we derive the following solution:

### Equation of the Parabola
The equation of the parabola is given by:

\[
\left( \frac{x}{\alpha} - \frac{y}{\beta} \right)^2 = 2 \left( \frac{x}{\alpha} + \frac{y}{\beta} \right) - 1
\]

### Verification of Conditions
1. **Passes through \((\alpha, 0)\):**
   Substituting \( x = \alpha \), \( y = 0 \):
   \[
   \left( \frac{\alpha}{\alpha} - 0 \right)^2 = 2 \left( \frac{\alpha}{\alpha} + 0 \right) - 1 \implies 1 = 2(1) - 1 \implies 1 = 1
   \]
   
2. **Passes through \((0, \beta)\):**
   Substituting \( x = 0 \), \( y = \beta \):
   \[
   \left( 0 - \frac{\beta}{\beta} \right)^2 = 2 \left( 0 + \frac{\beta}{\beta} \right) - 1 \implies 1 = 2(1) - 1 \implies 1 = 1
   \]

3. **Horizontal tangent at \((\alpha, 0)\):**
   Differentiate implicitly and solve for \( \frac{dy}{dx} \):
   \[
   2 \left( \frac{x}{\alpha} - \frac{y}{\beta} \right) \left( \frac{1}{\alpha} - \frac{dy/dx}{\beta} \right) = 2 \left( \frac{1}{\alpha} + \frac{dy/dx}{\beta} \right)
   \]
   At \((\alpha, 0)\), solving gives \( \frac{dy}{dx} = 0 \), confirming a horizontal tangent.

4. **Vertical tangent at \((0, \beta)\):**
   Differentiate implicitly with respect to \( y \) and solve for \( \frac{dx}{dy} \):
   \[
   2 \left( \frac{x}{\alpha} - \frac{y}{\beta} \right) \left( \frac{dx/dy}{\alpha} - \frac{1}{\beta} \right) = 2 \left( \frac{dx/dy}{\alpha} + \frac{1}{\beta} \right)
   \]
   At \((0, \beta)\), solving gives \( \frac{dx}{dy} = 0 \), implying \( \frac{dy}{dx} \) is undefined (vertical tangent).

### Final Answer
The equation of the parabola is:

```markdown
\[
\boxed{\left( \frac{x}{\alpha} - \frac{y}{\beta} \right)^2 = 2 \left( \frac{x}{\alpha} + \frac{y}{\beta} \right) - 1}
\]
```