```markdown
We use the fact that the characteristic (and hence minimal) polynomial of \(M\) is
\[
\chi_M(\lambda)=(\lambda-1)^3=0
\quad\Longrightarrow\quad
(M-I)^3=0.
\]
Set \(N=M-I\); then \(N^3=0\) and \(M=I+N\).  For any integer \(m\ge3\),
\[
M^m=(I+N)^m
=\sum_{k=0}^m\binom m k N^k
=\sum_{k=0}^2\binom m k N^k
\;=\;
I+\;m\,N\;+\;\frac{m(m-1)}2\,N^2.
\]
Now substitute back \(N=M-I\):

\[
\begin{aligned}
M^m
&=I
+\,m\,(M-I)
+\frac{m(m-1)}2\,(M-I)^2\\
&=I+mM-mI+\frac{m(m-1)}2\bigl(M^2-2M+I\bigr)\\
&=\frac{m(m-1)}2\,M^2
\;+\;\bigl(m-\,m(m-1)\bigr)\,M
\;+\;\Bigl(1-m+\tfrac{m(m-1)}2\Bigr)\,I.
\end{aligned}
\]
Collecting coefficients gives
\[
M^m \;=\; a_m\,M^2 \;+\; b_m\,M \;+\; c_m\,I_3,
\]
where
\[
a_m=\binom m2=\frac{m(m-1)}2,
\quad
b_m=-\,m(m-2)=2m-m^2,
\quad
c_m=\frac{(m-1)(m-2)}2.
\]
```

**Answer.**  
For all integers \(m\ge3\),
\[
\boxed{
a_m=\frac{m(m-1)}2,\quad
b_m=-m(m-2),\quad
c_m=\frac{(m-1)(m-2)}2,
}
\]
so that
\[
M^m
=\frac{m(m-1)}2\,M^2
-m(m-2)\,M
+\frac{(m-1)(m-2)}2\,I_3.
\]
