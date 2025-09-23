```markdown
**Solution.**  
We show that \(f''\equiv0\) by a Taylor–expansion argument.  Fix \(a>0\) and set \(b=a+h\).  Then for small \(h\),

\[
\begin{aligned}
f(a+h)&=f(a)+h\,f'(a)+\tfrac{h^2}{2}f''(a)+\tfrac{h^3}{6}f'''(a)+O(h^4),\\
f\!\Bigl(a+\tfrac h2\Bigr)
&=f(a)+\tfrac h2\,f'(a)+\tfrac{h^2}{8}f''(a)+\tfrac{h^3}{48}f'''(a)+O(h^4).
\end{aligned}
\]
Hence
\[
f(a+h)+f(a)-2\,f\!\Bigl(a+\tfrac h2\Bigr)
=\frac{h^2}{4}\,f''(a)+\frac{h^3}{24}\,f'''(a)+O(h^4).
\]
On the other hand
\[
(b-a)^2\,f''\bigl(\sqrt{a(a+h)}\bigr)
=h^2\Bigl(f''(a)+\tfrac h2\,f'''(a)\Bigr)+O(h^4)
=h^2\,f''(a)+\tfrac{h^3}{2}\,f'''(a)+O(h^4).
\]
Equating the coefficients of \(h^2\) in the given identity
\[
f(a+h)+f(a)-2\,f\Bigl(a+\tfrac h2\Bigr)
=(b-a)^2\,f''\bigl(\sqrt{a(a+h)}\bigr)
\]
yields
\[
\frac{1}{4}\,f''(a)=f''(a)\,,\qquad\forall\,a>0
\quad\Longrightarrow\quad f''(a)=0\,. 
\]
Hence \(f\) is affine,
\[
f(x)=A\,x+B,\qquad A,B\in\Bbb R.
\]
One easily checks these do satisfy the original equation, since \(f''\equiv0\).  

**Answer.**  
\[
\boxed{\,f(x)=A x+B\,,\quad A,B\in\Bbb R\,.}
\]
```