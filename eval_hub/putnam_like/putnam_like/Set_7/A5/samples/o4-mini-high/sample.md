Here is a counter‐example showing that in general one cannot conclude \(a_k\to0\) from the hypothesis.  We will build

1.  an increasing sequence \(m_k\to\infty\),  
2.  an infinite subset \(F\subset\Bbb N\),  
3.  a “cut‐off’’ \(K(\gamma)\in\Bbb N\) for each \(\gamma>1\),  

so that if we set
\[
A \;=\;\bigcup_{\gamma>1}\;\bigl\{\lfloor\gamma^{m_k}\rfloor:\;k\ge K(\gamma)\bigr\}
\]
and then define
\[
a_n=\begin{cases}
0,&n\in A,\\
1,&n\in F\;(\subset\Bbb N\setminus A)\!,
\end{cases}
\]
then:

–  For each fixed \(\gamma>1\), by construction \(a_{\lfloor\gamma^{m_k}\rfloor}=0\) for all \(k\ge K(\gamma)\), hence 
\[
a_{\lfloor\gamma^{m_k}\rfloor}\;\longrightarrow\;0\quad(k\to\infty).
\]
–  But \(F\) is infinite and on \(F\) we have \(a_n\equiv1\), so \(\limsup_{n\to\infty}|a_n|=1\neq0\).  Thus \(a_n\not\to0\).

---

**The concrete choice.**  Take
\[
m_k \;=\;2^k,
\]
and let
\[
F \;=\;\bigcup_{j\ge1}\bigl\{\,2^j+1,\,2^j+2,\;\dots,\;2^j+2^{\,j-1}\bigr\}.
\]
Then \(F\) is clearly infinite, and consists of the “first half’’ of each dyadic block
\(\{2^j+1,\dots,2^{j+1}\}\).  

Now fix any \(\gamma>1\).  Since \(\gamma^{2^k}\) grows doubly‐exponentially in \(k\), for large \(k\) one has
\[
\gamma^{2^k}\;>\;2^k+2^{\,k-1}\,,
\]
hence for all sufficiently large \(k\),
\(\lfloor\gamma^{2^k}\rfloor\notin F\).  Therefore
\[
\bigl\{\,k:\lfloor\gamma^{m_k}\rfloor\in F\bigr\}
\]
is a finite set; define
\[
K(\gamma)
=
1+\max\bigl\{\,k:\lfloor\gamma^{2^k}\rfloor\in F\bigr\},
\]
so that for every \(k\ge K(\gamma)\) we have \(\lfloor\gamma^{m_k}\rfloor\notin F\).  We then set
\[
A
=
\bigcup_{\gamma>1}\bigl\{\lfloor\gamma^{m_k}\rfloor : k\ge K(\gamma)\bigr\},
\]
and finally
\[
a_n = \begin{cases}
0,&n\in A,\\
1,&n\in F.
\end{cases}
\]

1.  By construction, whenever \(k\ge K(\gamma)\) one has 
\(\lfloor\gamma^{m_k}\rfloor\in A\), so \(a_{\lfloor\gamma^{m_k}\rfloor}=0\).  
   Thus indeed
   \(\,a_{\lfloor\gamma^{m_k}\rfloor}\to0\) for every \(\gamma>1\).

2.  On the other hand \(F\subset\Bbb N\setminus A\) is infinite, and \(a_n=1\) for \(n\in F\), so \(a_n\not\to0\).

This completes the counter‐example.  In particular the answer to the original question is:

**No**, one cannot deduce \(a_k\to0\) from the condition that for every \(\gamma>1\), \(a_{\lfloor\gamma^{m_k}\rfloor}\to0\).