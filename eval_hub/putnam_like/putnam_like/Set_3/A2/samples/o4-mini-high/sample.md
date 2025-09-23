```markdown
**Solution.**  
Let 
\[
f(x)=\frac1{x^k+1}, 
\qquad
p_n(x)=(x^k+1)^{\,n+1}\,f^{(n)}(x),
\]
so in the statement $p(x)=p_n(x)$.  We will show by induction on $n$ that

1.  \(p_n(x)\in\Bbb Z[x]\),  
2.  for \(n\ge1\) the polynomial \(p_n(x)\) is divisible by \(k\) in \(\Bbb Z[x]\).

Since \(p_n(x)\in\Bbb Z[x]\), in particular \(p_n(k-1)\in\Bbb Z\).  And since for \(n\ge1\) we have \(k\!\mid\,p_n(x)\) as a polynomial, it follows that \(k\mid p_n(k-1)\).  This completes the proof once we establish the two claims.

---

### 1. The basic recurrence

Start from the identity
\[
(x^k+1)\,f(x)=1.
\]
Differentiate \(n\) times.  On the left we use Leibniz’s rule:
\[
\frac{d^n}{dx^n}\bigl[(x^k+1)f(x)\bigr]
=\sum_{j=0}^n\binom nj\frac{d^j}{dx^j}(x^k+1)\;\;f^{(n-j)}(x)
=0.
\]
Now
\[
\frac{d^j}{dx^j}(x^k+1)
=(k)_j\,x^{k-j}, 
\quad
\text{where }(k)_j=k(k-1)\cdots(k-j+1),
\]
and by definition
\[
f^{(n-j)}(x)
=\frac{p_{n-j}(x)}{(x^k+1)^{\,n-j+1}}.
\]
Hence
\[
0
=\sum_{j=0}^n\binom nj\,(k)_j\,x^{k-j}\,
\frac{p_{n-j}(x)}{(x^k+1)^{\,n-j+1}}
=\frac1{(x^k+1)^{\,n+1}}
\sum_{j=0}^n\binom nj\,(k)_j\,x^{k-j}\,(x^k+1)^j\,p_{n-j}(x).
\]
Isolating the top–order term \(j=0\) shows equivalently
\[
p_n'(x)\,(x^k+1)\;-\;(n+1)\,k\,x^{k-1}\,p_n(x)
\;=\;p_{n+1}(x).
\]
In other words we have the recurrence
\[
\boxed{
 p_0(x)=1,
 \quad
 p_{n+1}(x)
 =(x^k+1)\,p_n'(x)\;-\;(n+1)\,k\,x^{k-1}\,p_n(x).
}
\]

---

### 2. Induction in \(\Bbb Z[x]\)

**Base case \(n=0\).**  We have \(p_0(x)=1\in\Bbb Z[x]\).  

**Induction step.**  Suppose \(p_n(x)\in\Bbb Z[x]\).  Then
- \(p_n'(x)\in\Bbb Z[x]\) as well,
- \((x^k+1)p_n'(x)\in\Bbb Z[x]\),
- \((n+1)\,k\,x^{k-1}\,p_n(x)\in\Bbb Z[x]\).

Therefore 
\[
p_{n+1}(x)
=(x^k+1)p_n'(x)\;-\;(n+1)\,k\,x^{k-1}\,p_n(x)
\;\in\;\Bbb Z[x].
\]
Thus \(p_n(x)\in\Bbb Z[x]\) for all \(n\).

---

### 3. Divisibility by \(k\)

For \(n=1\) the recurrence gives
\[
p_1(x)
=(x^k+1)p_0'(x)-1\cdot k\,x^{k-1}p_0(x)
=-k\,x^{\,k-1},
\]
which is clearly divisible by \(k\) in \(\Bbb Z[x]\).  Now assume for some \(n\ge1\) that
\[
k\;\bigm|\;p_n(x)\quad\text{in }\Bbb Z[x].
\]
Then
- \(p_n'(x)\) is also divisible by \(k\) (since differentiating preserves the factor \(k\)),
- hence \((x^k+1)p_n'(x)\) is divisible by \(k\),
- and \((n+1)\,k\,x^{k-1}p_n(x)\) is divisible by \(k\) (in fact by \(k^2\)).

Subtracting shows
\[
p_{n+1}(x)
=(x^k+1)p_n'(x)\;-\;(n+1)\,k\,x^{k-1}\,p_n(x)
\]
is divisible by \(k\) in \(\Bbb Z[x]\).  By induction, for every \(n\ge1\),  
\[
k\;\bigm|\;p_n(x)\quad\text{in }\Bbb Z[x].
\]

---

### 4. Conclusion

- Since \(p_n(x)\in\Bbb Z[x]\), we have \(p_n(k-1)\in\Bbb Z\).  
- Since for \(n\ge1\) the polynomial \(p_n(x)\) carries a factor \(k\), it follows
  \(\,k\mid p_n(k-1)\).

Hence, for all positive integers \(k,n\), the number
\[
p(k-1)=p_n(k-1)
\]
is an integer and is divisible by \(k\), as required.  □  
```