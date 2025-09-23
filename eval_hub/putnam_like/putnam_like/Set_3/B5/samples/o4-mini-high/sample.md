```markdown
**Solution.**

Let 
\[
f(x)=x^4-2x-1
\]
and denote its roots by \(x_1,x_2,x_3,x_4\). We wish to compute the sum
\[
S=\sum_{i=1}^4\frac{2x_i^2+1}{(x_i^2-1)^2}.
\]

1. **Partial‐fraction decomposition.**

   Observe that
   \[
   \frac{2x^2+1}{(x^2-1)^2}
   =\frac{A}{(x-1)^2}+\frac{B}{(x+1)^2}+\frac{C}{x-1}+\frac{D}{x+1}.
   \]
   Clearing denominators and matching coefficients one finds
   \[
   A=B=\tfrac34,\quad
   C=\tfrac14,\quad
   D=-\tfrac14.
   \]
   Hence
   \[
   \frac{2x^2+1}{(x^2-1)^2}
   =\frac{3/4}{(x-1)^2}+\frac{3/4}{(x+1)^2}
    +\frac{1/4}{x-1}-\frac{1/4}{x+1}\,.
   \]
   It follows that
   \[
   S
   =\sum_{i=1}^4\frac{2x_i^2+1}{(x_i^2-1)^2}
   =\frac34\sum_{i=1}^4\frac1{(x_i-1)^2}
    +\frac34\sum_{i=1}^4\frac1{(x_i+1)^2}
    +\frac14\sum_{i=1}^4\frac1{x_i-1}
    -\frac14\sum_{i=1}^4\frac1{x_i+1}.
   \]

2. **Using Vieta–derivative identities.**

   For a monic polynomial \(f(x)=\prod_{i=1}^4(x-x_i)\), one has
   \[
   \sum_{i=1}^4\frac1{x_i-a}
    =-\frac{f'(a)}{f(a)},
   \qquad
   \sum_{i=1}^4\frac1{(x_i-a)^2}
    =\frac{f'(a)^2-f''(a)\,f(a)}{f(a)^2}.
   \]
   We compute
   \[
     f(1)=1-2-1=-2,\quad f'(x)=4x^3-2\ \Longrightarrow\ f'(1)=2,
     \quad f''(x)=12x^2\ \Longrightarrow\ f''(1)=12,
   \]
   \[
     f(-1)=1+2-1=2,\quad f'(-1)=-6,\quad f''(-1)=12.
   \]
   Hence
   \[
   \sum_{i=1}^4\frac1{x_i-1}
    =-\,\frac{f'(1)}{f(1)}=-\frac{2}{-2}=1,
   \quad
   \sum_{i=1}^4\frac1{x_i+1}
    =-\,\frac{f'(-1)}{f(-1)}=-\frac{-6}{2}=3,
   \]
   \[
   \sum_{i=1}^4\frac1{(x_i-1)^2}
    =\frac{2^2-12\cdot(-2)}{(-2)^2}
    =\frac{4+24}{4}=7,
   \quad
   \sum_{i=1}^4\frac1{(x_i+1)^2}
    =\frac{(-6)^2-12\cdot2}{2^2}
    =\frac{36-24}{4}=3.
   \]

3. **Assembling the result.**

   Substitute these into the expression for \(S\):
   \[
   S
   =\frac34\cdot7+\frac34\cdot3+\frac14\cdot1-\frac14\cdot3
   =\frac{21+9+1-3}{4}
   =\frac{28}{4}
   =7.
   \]
   
Therefore, the desired sum is
\[
\boxed{7}.
\]
```