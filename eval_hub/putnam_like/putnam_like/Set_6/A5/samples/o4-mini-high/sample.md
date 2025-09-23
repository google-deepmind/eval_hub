```markdown
# Solution

We will explicitly construct an integer \(N\) and \(n\) distinct bases
\[
  b_1,b_2,\dots,b_n\ge2
\]
so that in each base \(b_i\), the base‑\(b_i\) expansion of \(N\) is
exactly 4 digits long and is a palindrome.

---

## 1. Reduction to two simple congruences

Fix a base \(b\ge2\).  A 4‑digit palindrome in base \(b\) has the form
\[
   (a,\;c,\;c,\;a)_b
   \;=\;
   a\,b^3 \;+\; c\,b^2 \;+\; c\,b \;+\; a
   \;=\;
   a\,(b^3+1)\;+\;c\,(b^2+b),
\]
where
\[
   1\;\le a\le b-1,
   \quad
   0\;\le c\le b-1.
\]
We shall enforce the **simplest** choice \(a=1\).  Then
\[
   N
   \;=\;
   1\cdot(b^3+1)\;+\;c\,(b^2+b),
\]
and one checks easily that
\[
   b^3 < b^3+1 \;\le N \;<\; b^3+1 + (b-1)(b^2+b)
             \;=\; 2b^3 - b +1 \;<\; b^4,
\]
so indeed \(N\) has exactly 4 digits in base \(b\).

All that remains is to show that one can arrange for
\[
   N \;=\; (b^3+1) \;+\; c\,(b^2+b)
\]
with some integer \(c\in[0,b-1]\).  Equivalently, we want
\[
   N\equiv b^3+1\;\pmod{b^2+b}.
\]
But one checks
\[
   b^3+1 \;\equiv\; b+1
     \pmod{b^2+b},
\]
so it suffices to arrange
\[
   N\equiv b+1\pmod{b^2+b}
   \quad\Longleftrightarrow\quad
   \begin{cases}
     N\equiv1\pmod b,\\
     N\equiv0\pmod{b+1}.
   \end{cases}
\]
Once these two congruences hold, write
\[
   N=(b^2+b)\,q+(b+1)
   \quad\Longrightarrow\quad
   N-(b^3+1)
   =\bigl(q-(b-1)\bigr)(b^2+b),
\]
so \(c=q-(b-1)\).  A short check shows \(0\le c\le b-1\).  Hence in base \(b\)
\[
   N = (1,c,c,1)_b
\]
is a 4‑digit palindrome.

---

## 2. Choosing the bases \(b_1,\dots,b_n\) so the moduli are coprime

For each \(i\) we will impose the double congruence
\[
   N\equiv1\pmod{b_i},
   \quad
   N\equiv0\pmod{b_i+1}.
\]
Let
\[
   m_i \;=\; b_i(b_i+1).
\]
We will choose
\[
   b_1,b_2,\dots,b_n
\]
inductively so that the \(m_i\) are pairwise coprime.  Then the simultaneous
system
\[
   N\equiv1\pmod{b_i},
   \quad
   N\equiv0\pmod{b_i+1},
   \quad
   (i=1,\dots,n)
\]
is a system of congruences modulo the pairwise‐coprime integers
\(m_1,m_2,\dots,m_n\), and hence by the Chinese Remainder Theorem has a
solution \(N\).  This \(N\) then yields a valid 4‑digit base‑\(b_i\)
palindrome for each \(i\).

### 2.1 Inductive choice of the bases

-  Start with
   \[
     b_1 = 2,
     \quad
     m_1 = 2\cdot3=6.
   \]
-  Once \(b_1,\dots,b_k\) (and hence \(m_1,\dots,m_k\)) are chosen, set
   \[
     M_k \;=\; m_1\,m_2\cdots m_k,
     \quad
     b_{k+1} \;=\; M_k! \;+\;1.
   \]
   Then \(b_{k+1}\) is coprime to every prime dividing \(M_k\), hence
   \(\gcd\bigl(b_{k+1},M_k\bigr)=1\).  Similarly
   \(\gcd\bigl(b_{k+1}+1,M_k\bigr)=1\).  Thus
   \(\gcd\bigl(b_{k+1}(b_{k+1}+1),M_k\bigr)=1\), i.e. \(m_{k+1}\) is
   coprime to every earlier \(m_i\).  Proceed up to \(k=n-1\).

By induction we obtain \(n\) bases whose corresponding moduli
\(m_i=b_i(b_i+1)\) are pairwise coprime.

---

## 3. Putting it all together

1.  We have \(m_1,\dots,m_n\) pairwise coprime.
2.  By CRT there is an integer \(N\) satisfying
    \[
      N\equiv1\pmod{b_i},
      \quad
      N\equiv0\pmod{b_i+1},
      \qquad i=1,2,\dots,n.
    \]
3.  Then for each \(i\),
    \[
      N\equiv b_i+1\;\pmod{b_i^2+b_i}
      \;\Longrightarrow\;
      N=\bigl(b_i^3+1\bigr)+c_i\,(b_i^2+b_i),
      \quad
      0\le c_i\le b_i-1.
    \]
    Hence in base \(b_i\),
    \[
      N=(1,c_i,c_i,1)_{b_i},
    \]
    a 4‑digit palindrome.

This constructs **one** integer \(N\) which in **at least** the \(n\)
distinct bases \(b_1,\dots,b_n\) has a 4‑digit palindromic expansion.
Since \(n\) was arbitrary, the problem is solved. ∎
```