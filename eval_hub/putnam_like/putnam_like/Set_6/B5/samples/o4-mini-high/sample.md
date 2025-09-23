Here is a short proof by “peeling‐off’’ finitely many large terms and then using that each remaining sum‐set is a null–sequence.  

```markdown
**Solution.**  
Let \((r_n)\) be a positive null–sequence and fix any nonempty open interval \((a,b)\).  We shall exhibit a nonempty subinterval of \((a,b)\) which contains no sums of the form
\[
r_{i_1}+r_{i_2}+\cdots+r_{i_{2025}},
\]
with all \(i_j\) distinct.

---

1.  Since \(r_n\to0\), choose \(N\) so large that
\[
r_n<\frac{b-a}{2026}
\quad
\text{for all }n\ge N.
\]
2.  **Split the 2025‐term sums into two kinds.**  
   (i) Those all of whose indices lie in \(\{1,2,\dots,N-1\}\).  There are only finitely many such sums.  
   (ii) Those which use at least one index \(\ge N\).  

   Let  
   \[
   F_1
   =\bigl\{
     r_{i_1}+\cdots+r_{i_{2025}}
     : 1\le i_1<\cdots<i_{2025}<N
     \bigr\},
   \]
   a finite set.  Remove these finitely many points from \((a,b)\); since \((a,b)\) is open and \(F_1\) is finite, the result is still a nonempty open interval, say
   \[
     I=(a',b')\;\subset\;(a,b),
   \]
   containing no “all‐small‐index’’ sums.

3.  Any remaining sum in \(I\) must be of kind (ii).  Write such a sum as
   \[
     S
     =r_{i_1}+\cdots+r_{i_{2024}}+r_m,
     \quad
     1\le i_1<\cdots<i_{2024}<N\le m.
   \]
   Let
   \[
     F_2
     =\bigl\{
       r_{i_1}+\cdots+r_{i_{2024}}
       :1\le i_1<\cdots<i_{2024}<N
     \bigr\},
   \]
   which is again finite.  Then
   \[
     S\;=\;s + r_m,
     \quad
     s\in F_2,\;m\ge N.
   \]

4.  For each fixed \(s\in F_2\), the set
   \[
     \{\,s + r_m:\;m\ge N\}
   \]
   is a null–sequence converging to \(s\).  In particular it has empty interior.  Since \(F_2\) is finite, the **union**
   \[
     U \;=\;\bigcup_{s\in F_2}\{\,s+r_m:\;m\ge N\}
   \]
   is still a countable union of nowhere‐dense sets, hence has empty interior in \(\R\).

5.  Now \(I\setminus U\) is open (being the complement of a closed–in‐\(I\) nowhere‐dense set) and nonempty.  Pick any nonempty open subinterval
   \[
     (c,d)\;\subset\;I\setminus U.
   \]
   By construction \((c,d)\) contains none of the finite “all‐small‐index’’ sums from \(F_1\), nor any of the “one‐large‐index’’ sums in \(U\).  Hence \((c,d)\) contains no sum of 2025 distinct \(r_n\) at all, as required.  

∎
```

**Remark.**  Equivalently one can note that the set of all 2025‐term sums is
\[
  S_{2025}\;=\;\bigcup_{1\le k\le N-1}\Bigl(S_{2024}+\{r_k\}\Bigr)
        \;\cup\;\bigl\{ \text{finitely many “large‐index’’ sums}\bigr\},
\]
each translate \(S_{2024}+r_k\) has empty interior (by induction or Baire’s theorem), so \(S_{2025}\) has empty interior, and any nonempty open interval contains a gap.