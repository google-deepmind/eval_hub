```markdown
**Solution.**

1.  Define the continuous function \(p\colon[0,1]\to\R\) by the equality
   \[
     p(t)^2 \;=\; 1 \;+\;6\int_0^t s^2\,p(s)\,ds,\qquad p(0)=1.
   \]
   Differentiating both sides gives
   \[
     2\,p(t)\,p'(t)
     \;=\;
     6\,t^2\,p(t)
     \quad\Longrightarrow\quad
     p'(t)=3\,t^2,
     \quad p(0)=1,
   \]
   hence
   \[
     p(t)=1+\int_0^t 3s^2\,ds
     \;=\;
     1+t^3.
   \]
   A direct check shows that indeed
   \(\;p(t)^2=1+6\int_0^t s^2\,p(s)\,ds\).

2.  If \(u\in F\) then by hypothesis
   \[
     |u(t)|^2\;\le\;1+6\int_0^t s^2\,|u(s)|\,ds
     \;\le\;
     1+6\int_0^t s^2\,p(s)\,ds
     \;=\;p(t)^2,
   \]
   so
   \[
     |u(t)|\;\le\;p(t)=1+t^3\quad\forall\,t\in[0,1].
   \]

3.  Set
   \[
     f(x)=x^3-x^2.
   \]
   One checks
   \[
     f'(x)=3x^2-2x=x(3x-2),
   \]
   so \(f\) is strictly increasing on \((-\infty,0]\), then decreasing on \([0,\tfrac23]\),
   then increasing on \([\tfrac23,\infty)\).  In particular, on the symmetric interval
   \(\bigl[-p(t),\,p(t)\bigr]\) the minimum of \(f\) is attained at
   \(\;x=-p(t)\).  Hence for each \(t\),
   \[
     f\bigl(u(t)\bigr)\;\ge\;f\bigl(-p(t)\bigr)
     \;=\;-\,\bigl(p(t)^3+p(t)^2\bigr).
   \]
   Integrating over \([0,1]\) gives
   \[
     J(u)
     \;=\;
     \int_0^1\bigl(u(t)^3-u(t)^2\bigr)\,dt
     \;\ge\;
     -\int_0^1\!\bigl((1+t^3)^3+(1+t^3)^2\bigr)\,dt.
   \]
   A straightforward computation shows
   \[
     \int_0^1(1+t^3)^3\,dt
     =\int_0^1\bigl(1+3t^3+3t^6+t^9\bigr)\,dt
     =1+\tfrac34+\tfrac{3}{7}+\tfrac{1}{10},
   \]
   \[
     \int_0^1(1+t^3)^2\,dt
     =\int_0^1\bigl(1+2t^3+t^6\bigr)\,dt
     =1+\tfrac12+\tfrac{1}{7},
   \]
   so altogether
   \[
     J(u)\;\ge\;
     -\Bigl(
       \bigl(1+\tfrac34+\tfrac{3}{7}+\tfrac{1}{10}\bigr)
       +
       \bigl(1+\tfrac12+\tfrac{1}{7}\bigr)
     \Bigr)
     =-\frac{549}{140}.
   \]

4.  Finally, the function
   \[
     u^*(t) \;=\; -\,p(t)\;=\;-\,\bigl(1+t^3\bigr)
   \]
   belongs to \(F\) (it saturates the defining inequality) and achieves
   equality in the above estimate.  Hence
   \[
     \min_{u\in F}J(u)
     \;=\;
     J\bigl(u^*\bigr)
     \;=\;
     -\frac{549}{140}.
   \]

**Answer.**  
\(J\) attains its minimum on \(F\) at
\[
   u^*(t)=-1-t^3,
\]
and
\[
   \min_{u\in F}J(u)
   =-\frac{549}{140}.
\]
```