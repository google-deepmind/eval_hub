Below is one acceptable answer. In what follows we describe one way to arrive at the answer.

We wish to find a parabola that touches the horizontal line

   y = 0 at the point (α, 0)
   and the vertical line
   x = 0 at the point (0, β).

In other words, the tangent line at (α, 0) must be y = 0 and the tangent line at (0, β) must be x = 0.

Because the parabola is not given by a graph of a function of x (since one of its tangents is vertical) it is natural to describe it by a quadratic equation in x and y. One may show that any (nondegenerate) parabola may be written in the form
   
   A x² + B x y + C y² + D x + E y + K = 0
   
with the condition for being a parabola that

   B² – 4AC = 0.

Our idea is to impose the following conditions:
 
1. The point (α, 0) lies on the parabola:
  Aα² + Bα·0 + C·0² + Dα + E·0 + K = 0 ⟹ Aα² + Dα + K = 0.

2. At (α, 0) the tangent line is y = 0. (Since the normal to y = 0 is (0, 1), the gradient of the quadratic must be vertical there.) We have
  F(x,y) = A x² + B x y + C y² + D x + E y + K,
so that
  Fₓ(x,y) = 2Ax + By + D and F_y(x,y) = Bx + 2Cy + E.
At (α, 0) we must have Fₓ(α,0) = 0. That is,
  2Aα + D = 0 ⟹ D = –2Aα.
Then the condition from (1) becomes
  Aα² – 2Aα² + K = 0 ⟹ K = Aα².

3. Next, the point (0, β) lies on the parabola:
  Cβ² + Eβ + K = 0.
But K = Aα² so
  Cβ² + Eβ + Aα² = 0.

4. At (0, β) the tangent is x = 0. (The normal to x = 0 is (1, 0), so we need the x–component of the gradient to be 0 at (0,β).) That is, we require
  F_y(0,β) = B·0 + 2Cβ + E = 0 ⟹ E = –2Cβ.
Then the condition in (3) becomes
  Cβ² – 2Cβ² + Aα² = 0 ⟹ Aα² = Cβ² ⟹ C = Aα²/β².

5. Finally, the conic has to be a parabola so we require
  B² – 4AC = 0 ⟹ B² = 4AC = 4A·(Aα²/β²)= 4A²α²/β²,
so that
  B = ±(2Aα/β).

If one chooses the plus‐sign the equation factors into a perfect square (a double line) which is degenerate. Hence one must take

  B = –(2Aα/β).

Thus, putting things together we have
  D = –2Aα, E = –2Cβ = –2Aα²/β, K = Aα², C = Aα²/β², B = –(2Aα/β).

Then the general equation of the conic is

  A x² – (2Aα/β)x y + (Aα²/β²)y² – 2Aα x – (2Aα²/β)y + Aα² = 0.

Dividing through by A (≠ 0) we obtain

  x² – (2α/β)x y + (α²/β²)y² – 2α x – (2α²/β)y + α² = 0.

Notice that the first three terms form a perfect square:
  x² – (2α/β)x y + (α²/β²)y² = (x – (α/β)y)².
Thus the equation may be written as

  (x – (α/β)y)² – 2α [x + (α/β)y] + α² = 0.

A short calculation shows that by completing the square one may rewrite the above as

  (x – (α/β)y – α)² = (4α²/β) y.

This is a perfectly acceptable answer. (One may check that when y = 0 we have x = α (with y = 0 as the tangent line), and when x = 0 one finds y = β (with x = 0 as the tangent there).)

Below is the final answer in markdown with LaTeX code.

---

```latex
\[
\left(x - \frac{\alpha}{\beta}\,y - \alpha\right)^2 = \frac{4\alpha^2}{\beta}\,y.
\]
```

---

Any answer equivalent to the above is correct.