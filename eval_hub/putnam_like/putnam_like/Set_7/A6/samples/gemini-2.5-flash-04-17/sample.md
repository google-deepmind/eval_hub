Let $P(x,y,z)$ be the assertion $f(xf(y+z)) + f(yf(x+z)) + f(zf(x+y)) = 2 + f(x+y+z)$.
The domain and codomain of $f$ are $(0,\infty)$, and $f$ is continuous.

First, let's check if $f(x)=1$ is a solution.
LHS: $f(x \cdot 1) + f(y \cdot 1) + f(z \cdot 1) = f(x)+f(y)+f(z) = 1+1+1=3$.
RHS: $2+f(x+y+z) = 2+1=3$.
Since $3=3$, $f(x)=1$ is a solution.

Let's investigate if there are other solutions.
The arguments $y+z, x+z, x+y$ can take any value in $(0,\infty)$ by varying $x,y,z$. Let $a=y+z, b=x+z, c=x+y$. For $x,y,z>0$, $a,b,c$ must satisfy the triangle inequalities $a+b>c, a+c>b, b+c>a$. Conversely, for any $a,b,c$ satisfying these and $a,b,c>0$, we can find $x,y,z>0$.
Also $x f(y+z)$ can take any value in $(0,\infty)$. Let $y+z=k>0$. $f(k)>0$. $xf(k)$ can take any value in $(0,\infty)$ by varying $x$. So $f$ must be defined on all $(0,\infty)$, which is given.

Let's take the limit as $x \to 0^+$ in the original equation $P(x,y,z)$. $y, z$ are fixed positive numbers.
$y+z>0$, so $f(y+z)>0$. $xf(y+z) \to 0^+$.
$x+z \to z^+$. By continuity of $f$, $f(x+z) \to f(z)$.
$x+y \to y^+$. By continuity of $f$, $f(x+y) \to f(y)$.
$x+y+z \to y+z^+$. By continuity of $f$, $f(x+y+z) \to f(y+z)$.

Let $\lim_{u \to 0^+} f(u) = M$. $M$ can be finite ($M>0$ as codomain is $(0,\infty)$) or $\infty$.
As $x \to 0^+$, $xf(y+z) \to 0^+$. $f(xf(y+z)) \to M$.
$f(yf(x+z)) \to f(yf(z))$.
$f(zf(x+y)) \to f(zf(y))$.
$f(x+y+z) \to f(y+z)$.

Taking the limit $x \to 0^+$ in $P(x,y,z)$:
$M + f(y f(z)) + f(z f(y)) = 2 + f(y+z)$ for all $y,z>0$.

If $M=\infty$: $\infty + f(y f(z)) + f(z f(y)) = 2+f(y+z)$.
LHS goes to $\infty$, RHS is finite. This is a contradiction.
So $M$ must be finite, $M>0$. $\lim_{u \to 0^+} f(u) = M$.

Now we have $M + f(y f(z)) + f(z f(y)) = 2 + f(y+z)$.
Let $y \to 0^+$ in this equation. $z$ is fixed.
$f(z)>0$, $yf(z) \to 0^+$. $f(yf(z)) \to M$.
$f(y) \to M$. $zf(y) \to zM$. $f(zf(y)) \to f(zM)$ by continuity.
$y+z \to z^+$. $f(y+z) \to f(z)$.

Taking the limit $y \to 0^+$:
$M + f(zM) + M = 2 + f(z)$ for all $z>0$.
$f(zM) + 2M = 2 + f(z)$.

Let $z=1$. $f(M) + 2M = 2 + f(1)$.
Let $z=M$. $f(M^2) + 2M = 2 + f(M)$.
$f(M^2) = 2 - 2M + f(M)$.
Also $f(M) = 2 - 2M + f(1)$.
So $f(M^2) = 2 - 2M + (2 - 2M + f(1)) = 4 - 4M + f(1)$.

Let $f(z)=c$ (constant). $c+2M = 2+c \implies 2M=2 \implies M=1$.
If $f(z)=1$ for all $z$, $1+2M=2+1 \implies 2M=2 \implies M=1$.
If $M=1$, the equation becomes $f(z) + 2 = 2 + f(z)$, which is $f(z)=f(z)$. This equation holds for any $f$ when $M=1$.
So $\lim_{u \to 0^+} f(u) = 1$.
And the equation from $x \to 0^+$ becomes $1 + f(y f(z)) + f(z f(y)) = 2 + f(y+z)$, which simplifies to
$f(y f(z)) + f(z f(y)) = 1 + f(y+z)$ for all $y,z>0$.

Let $y=1$ in $f(y f(z)) + f(z f(y)) = 1 + f(y+z)$:
$f(f(z)) + f(z f(1)) = 1 + f(1+z)$ for all $z>0$.
Let $z=1$: $f(f(1)) + f(f(1)) = 1+f(2) \implies 2f(f(1)) = 1+f(2)$.
Let $f(1)=c$. $2f(c)=1+f(2)$.

From $f(y f(z)) + f(z f(y)) = 1 + f(y+z)$, let $y=z$:
$2f(y f(y)) = 1+f(2y)$ for all $y>0$.
Let $y=1$: $2f(f(1)) = 1+f(2)$, which is $2f(c)=1+f(2)$.

Let $z=1$ in $2f(y f(y)) = 1+f(2y)$: $2f(1 f(1)) = 1+f(2)$, same equation.

From $f(f(z)) + f(cz) = 1+f(1+z)$, if $z=c$: $f(f(c)) + f(c^2) = 1+f(1+c)$.
From $2f(y f(y)) = 1+f(2y)$, let $y=c$: $2f(c f(c)) = 1+f(2c)$.

Let's show $c=f(1)=1$.
From $f(f(z)) + f(cz) = 1+f(1+z)$, consider $z$ values of the form $1/c^n$ for large $n$.
As $n \to \infty$, $1/c^n \to 0$ if $c>1$. As $n \to \infty$, $1/c^n \to \infty$ if $c<1$.
If $c=1$, $f(f(z)) + f(z) = 1+f(1+z)$.
If $f(1)=1$, then $f(f(z)) + f(z) = 1+f(1+z)$.
Let $z=1$. $f(1)+f(1)=1+f(2)$, $1+1=1+f(2) \implies f(2)=1$.
Let $z=2$. $f(f(2))+f(2)=1+f(3) \implies f(1)+1=1+f(3) \implies 1+1=1+f(3) \implies f(3)=1$.
By induction, $f(n)=1$ for all $n \in \mathbb{N}$.
$f(f(n)) + f(n) = 1+f(n+1) \implies f(1)+1 = 1+f(n+1) \implies 1+1=1+f(n+1) \implies f(n+1)=1$.

So if $f(1)=1$, then $f(n)=1$ for all $n \in \mathbb{N}$.
Substitute $z=n \in \mathbb{N}$ in $f(y f(z)) + f(z f(y)) = 1+f(y+z)$:
$f(y f(n)) + f(n f(y)) = 1+f(y+n)$.
Since $f(n)=1$ for $n \in \mathbb{N}$:
$f(y) + f(n f(y)) = 1+f(y+n)$ for all $y>0, n \in \mathbb{N}$.

Let $y=1/m$ for $m \in \mathbb{N}$.
$f(1/m) + f(n f(1/m)) = 1+f(1/m+n)$.
Let $f(x)=1$ for all $x \in \mathbb{Q}^+$.
$1 + f(n \cdot 1) = 1+f(1/m+n) \implies 1+f(n)=1+f(1/m+n) \implies 1+1=1+1$, so $f(q)=1$ for $q \in \mathbb{Q}^+$.
This holds if $f(1/m)=1$ for $m \in \mathbb{N}$.
In $f(y)+f(nf(y)) = 1+f(y+n)$, let $y=1/n$: $f(1/n)+f(n f(1/n))=1+f(1/n+n)$.
If $f(1/n)=1$, $1+f(n)=1+f(1/n+n) \implies 1+1=1+f((1+n^2)/n) \implies f((1+n^2)/n)=1$.
This shows $f(q)=1$ for $q$ of the form $(1+n^2)/n = n+1/n$. $f(2)=1, f(5/2)=1, f(10/3)=1$.

Let's prove $f(q)=1$ for all $q \in \mathbb{Q}^+$ using $f(y f(z)) + f(z f(y)) = 1+f(y+z)$ and $f(n)=1$ for $n \in \mathbb{N}$.
Let $y=p \in \mathbb{N}, z=q \in \mathbb{N}$. $f(p)+f(q)=1+f(p+q) \implies 1+1=1+1$, true.
Let $y=p \in \mathbb{N}, z=q/r \in \mathbb{Q}^+$. $f(p f(q/r)) + f(q/r f(p)) = 1+f(p+q/r)$.
$f(p f(q/r)) + f(q/r) = 1+f(p+q/r)$.
If $f(q/r)=1$: $f(p)+1=1+f(p+q/r) \implies 1+1=1+f(p+q/r) \implies f(p+q/r)=1$.
This means $f(q)=1$ for any $q \in \mathbb{Q}^+$ which is sum of an integer and a rational number. $q=p+q/r$. This is any $q \in \mathbb{Q}^+$.
Let $q \in \mathbb{Q}^+$. If $q \ge 1$, $q=n+r$ where $n \in \mathbb{N}_0$ and $r \in \mathbb{Q}^+ \cap [0,1)$. If $n \ge 1$, $f(q)=f(n+r)$. If $f(r)=1$, then $f(n+r)=1$.
So if $f(q)=1$ for $q \in \mathbb{Q}^+ \cap (0,1)$, then $f(q)=1$ for $q \in \mathbb{Q}^+ \cap [1,\infty)$.
Need to show $f(q)=1$ for $q \in \mathbb{Q}^+ \cap (0,1)$.

We know $f(1/n)=1$ for $n \in \mathbb{N}$. These are in $(0,1]$.
$f(y f(z)) + f(z f(y)) = 1+f(y+z)$. Let $y=1/m, z=1/n$ for $m,n \in \mathbb{N}$.
$f(1/m f(1/n)) + f(1/n f(1/m)) = 1+f(1/m+1/n)$.
$f(1/m \cdot 1) + f(1/n \cdot 1) = 1+f((n+m)/mn)$.
$f(1/m) + f(1/n) = 1+f((n+m)/mn)$.
$1+1=1+f((n+m)/mn) \implies f((n+m)/mn)=1$.
The set $\{(n+m)/mn : n,m \in \mathbb{N}\}$ includes $1/n+1/m$.
Any $q \in \mathbb{Q}^+$ can be written as $p/r$. We need to show $f(p/r)=1$.
Let $p/r = (n+m)/mn$. $p/r = 1/n+1/m$. For example, $1/2 = 1/3+1/6$, $1/3=1/4+1/12$, $1 = 1/2+1/2$.
Any rational $q$ in $(0,2]$ can be written as $1/n+1/m$. $1/n+1/m = (n+m)/nm$. For $q=a/b$, we need $a/b=(n+m)/nm$.

Let $q \in \mathbb{Q}^+$. $f(q)=1$.
$f(y)+f(1/y)=1+f(y+1)$ was derived from $f(y f(z)) + f(z f(y)) = 1+f(y+z)$ with $z=1$ and $f(1)=1$.
For $y=q \in \mathbb{Q}^+$, $f(q)+f(1/q)=1+f(q+1)$.
If $q \in \mathbb{Q}^+, q>1$, then $q=p/r$ with $p>r$. $q+1$ is also rational and $q+1>2$.
We have shown $f(q)=1$ for $q \in \mathbb{Q}^+, q \ge 1$.
So for $q \in \mathbb{Q}^+, q>1$, $f(q)=1$ and $f(q+1)=1$.
$1+f(1/q)=1+1 \implies f(1/q)=1$.
Since $q$ can be any rational number greater than 1, $1/q$ can be any rational number in $(0,1)$.
So $f(r)=1$ for all $r \in \mathbb{Q}^+ \cap (0,1)$.
Since $f(1)=1$, $f(q)=1$ for all $q \in \mathbb{Q}^+$.

Since $f$ is continuous and $f(x)=1$ for all $x \in \mathbb{Q}^+$, which is a dense subset of $(0,\infty)$, $f(x)=1$ for all $x \in (0,\infty)$.

Let's recap the argument flow:
1. Check $f(x)=1$ is a solution. Yes.
2. Show $\lim_{x\to 0^+} f(x)=1$. Taking $x \to 0^+$ in $P(x,y,z)$ leads to $M+f(yf(z))+f(zf(y))=2+f(y+z)$, where $M=\lim_{x\to 0^+} f(x)$. $M=\infty$ leads to a contradiction. Taking $y \to 0^+$ leads to $M+f(zM)+M=2+f(z)$, $f(zM)+2M=2+f(z)$. If $M>0$, this implies $M=1$.
3. With $\lim_{x\to 0^+} f(x)=1$, the $x\to 0^+$ equation is $f(y f(z)) + f(z f(y)) = 1 + f(y+z)$ for $y,z>0$.
4. Using this equation, let $y=n \in \mathbb{N}$. If $f(n)=1$, $f(y)+f(nf(y))=1+f(y+n)$.
5. Show $f(1)=1$. From $f(y f(z)) + f(z f(y)) = 1 + f(y+z)$, set $z=1$. $f(yf(1)) + f(f(y)) = 1+f(y+1)$. Let $f(1)=c$. $f(cy)+f(f(y))=1+f(y+1)$. Using $2f(y f(y))=1+f(2y)$ with $y=1$ gives $2f(c)=1+f(2)$.
Consider $f(n)=1$ for $n \in \mathbb{N}$ by assuming $f(1)=1$. Then $f(y)+f(nf(y))=1+f(y+n)$ for $n \in \mathbb{N}$. Consider $y=1/m$. $f(1/m)+f(nf(1/m))=1+f(n+1/m)$.
From $f(q)=1$ for $q \in \mathbb{Q}^+, q>1$ and $f(y)+f(1/y)=1+f(y+1)$, we get $f(q)+f(1/q)=1+f(q+1)$. For $q>1$, $f(q)=1, f(q+1)=1$, so $1+f(1/q)=1+1 \implies f(1/q)=1$. This shows $f(q)=1$ for $q \in \mathbb{Q}^+ \cap (0,1)$.
To start this, we need $f(q)=1$ for $q \in \mathbb{Q}^+, q>1$. $f(n)=1$ for $n \in \mathbb{N}$. Let $y=q \in \mathbb{Q}^+, q>1$. $f(q)+f(f(q))=1+f(q+1)$. If $f(q)=1$, $1+1=1+f(q+1)$, $f(q+1)=1$. This proves $f(q)=1$ for $q \in \mathbb{Q}^+, q>1$ by induction on the denominator/numerator or by proving $f(n)=1$ first and then $f(n+q)=1$ if $f(q)=1$.
$f(n)=1$ for $n \in \mathbb{N}$ is proved from $f(1)=1$ and $f(y)+f(f(y))=1+f(y+1)$ by induction.
So $f(1)=1$ is the necessary step.
$f(f(z)) + f(z) = 1+f(1+z)$ for $z>0$.
$f(n)=1$ for $n \in \mathbb{N}$. $f(1+2^k)=1$ for $k \in \mathbb{Z}$.
$1+2^k \to 1$ as $k \to -\infty$. By continuity $\lim_{k \to -\infty} f(1+2^k) = f(\lim_{k \to -\infty} (1+2^k)) = f(1)$.
$1 = f(1)$. So $f(1)=1$.
The rest follows.

The final answer is $\boxed{f(x)=1}$.