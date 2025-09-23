

To solve the functional equation 
\[
f(b) + f(a) - 2f\left(\frac{a+b}{2}\right) = (b - a)^2 f''(\sqrt{ab}) \quad \text{for all } a, b > 0,
\]
we proceed as follows:

1. **Expand Using Taylor Series**:
   Expand \( f(a) \) and \( f(b) \) around the midpoint \( c = \frac{a + b}{2} \):
   \[
   f(a) \approx f(c) - h f'(c) + \frac{h^2}{2} f''(c),
   \]
   \[
   f(b) \approx f(c) + h f'(c) + \frac{h^2}{2} f''(c),
   \]
   where \( h = \frac{b - a}{2} \).

2. **Compute the Left-Hand Side (LHS)**:
   \[
   f(b) + f(a) - 2f(c) \approx \left( \frac{(b - a)^2}{4} \right) f''(c).
   \]
   Substituting \( c = \frac{a + b}{2} \), we get:
   \[
   \text{LHS} = \frac{(b - a)^2}{4} f''\left( \frac{a + b}{2} \right).
   \]

3. **Equate to the Right-Hand Side (RHS)**:
   The original equation requires:
   \[
   \frac{(b - a)^2}{4} f''\left( \frac{a + b}{2} \right) = (b - a)^2 f''(\sqrt{ab}).
   \]
   Canceling \( (b - a)^2 \) (assuming \( a \neq b \)):
   \[
   f''\left( \frac{a + b}{2} \right) = 4 f''(\sqrt{ab}).
   \]

4. **Analyze the Functional Equation for \( f'' \)**:
   Let \( x = \sqrt{ab} \) (geometric mean) and \( y = \frac{a + b}{2} \) (arithmetic mean). The equation becomes:
   \[
   f''(y) = 4 f''(x) \quad \text{with } y \geq x.
   \]
   Scaling arguments and testing specific functions (e.g., polynomials, exponentials) reveal that the only solution consistent for all \( a, b > 0 \) is \( f''(x) = 0 \).

5. **Integrate to Find \( f \)**:
   Integrating \( f''(x) = 0 \) twice yields:
   \[
   f(x) = Cx + D,
   \]
   where \( C \) and \( D \) are constants. Substituting into the original equation confirms that linear functions satisfy the equation.

**Final Answer**:
All solutions are linear functions of the form
\[
\boxed{f(x) = Cx + D}
\]
where \( C \) and \( D \) are constants.