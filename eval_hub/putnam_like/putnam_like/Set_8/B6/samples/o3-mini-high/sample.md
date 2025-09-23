```latex
\textbf{Solution:}

We wish to determine all twice differentiable functions 
\[
f:(0,+\infty)\to \mathbb{R}
\]
satisfying
\[
f(b)+f(a)-2f\!\Bigl(\frac{a+b}{2}\Bigr)=(b-a)^2\, f''\!\bigl(\sqrt{ab}\,\bigr)
\]
for all \(a,b>0\).

\medskip

\textbf{Step 1. Change of Variables.} 

Let
\[
a=x-h,\quad b=x+h,\qquad \text{with } x>h>0.
\]
Then
\[
\frac{a+b}{2}=x \quad \text{and} \quad \sqrt{ab}=\sqrt{(x-h)(x+h)}=\sqrt{x^2-h^2}.
\]
The functional equation becomes
\[
f(x+h)+f(x-h)-2f(x)=(2h)^2\, f''\!\Bigl(\sqrt{x^2-h^2}\Bigr).
\]

\medskip

\textbf{Step 2. Taylor Expansion.}

We expand \(f(x\pm h)\) about \(x\) using Taylor’s theorem:
\[
f(x\pm h)= f(x) \pm f'(x)h+\frac{f''(x)}{2}h^2 \pm \frac{f'''(x)}{6}h^3+\frac{f^{(4)}(x)}{24}h^4 + o(h^4).
\]
Adding these two expansions, we obtain:
\[
f(x+h)+f(x-h)= 2f(x)+ f''(x)h^2 + \frac{f^{(4)}(x)}{12}h^4 + o(h^4).
\]
Thus, the left-hand side of our equation is
\[
f(x+h)+f(x-h)-2f(x)= f''(x)h^2+\frac{f^{(4)}(x)}{12}h^4 + o(h^4).
\]

\medskip

\textbf{Step 3. Expansion on the Right.}

Next, expand the argument of \(f''\) in the right-hand side. Since
\[
\sqrt{x^2-h^2}= x\sqrt{1-\frac{h^2}{x^2}} = x - \frac{h^2}{2x}+O(h^4),
\]
by the differentiability of \(f''\) we have
\[
f''\!\Bigl(\sqrt{x^2-h^2}\Bigr)= f''\!\Bigl(x-\frac{h^2}{2x}+O(h^4)\Bigr)= f''(x)-\frac{h^2}{2x}\, f'''(x)+O(h^4).
\]
Multiplying by \((2h)^2=4h^2\) gives
\[
(2h)^2 f''\!\Bigl(\sqrt{x^2-h^2}\Bigr)= 4h^2 \, f''(x)-\frac{2h^4}{x}\, f'''(x)+O(h^4).
\]

\medskip

\textbf{Step 4. Equating Coefficients.}

Since the equation must hold for all small \(h>0\), we equate the coefficients of like powers of \(h\).

The coefficient of \(h^2\) in the left-hand side is \(f''(x)\), while in the right-hand side it is \(4f''(x)\). Therefore,
\[
f''(x)=4f''(x).
\]
This immediately implies
\[
3f''(x)=0\quad \Longrightarrow \quad f''(x)=0\quad \text{for all } x>0.
\]

\medskip

\textbf{Step 5. Conclusion.}

Since \(f''(x)=0\) for all \(x>0\), the function \(f\) must be linear. That is, there exist constants \(A,B\in\mathbb{R}\) such that
\[
f(x)=Ax+B.
\]
A quick verification shows that for any linear function we have
\[
f(b)+f(a)-2f\!\Bigl(\frac{a+b}{2}\Bigr)= (Ab+B)+(Aa+B)-2\Bigl(A\frac{a+b}{2}+B\Bigr)=0,
\]
and since \(f''(x)=0\), the right-hand side is also \(0\). Thus, the functional equation is satisfied.

\medskip

\boxed{\text{The general solution is } f(x)=Ax+B, \quad A,B\in\mathbb{R}.}
```