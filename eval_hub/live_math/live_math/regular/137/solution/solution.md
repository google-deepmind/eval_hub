Notice that:
$$P(A=k)= \left\{ \begin{array}{lcc} 1/15 & if & k=3,4,10,11 \\ \\ 2/15 & if & k=5,6,8,9 \\ \\ 3/15 & if & k= 7 \end{array} \right.$$
\noindent and $P(B > A)=P(A=3) \cdot P(B > 3)+ P(A=4) \cdot P(B > 4) +\cdots+P(A=11) \cdot P(B  > 11)$. It is also clear that:
$$P(B=k)=(n-k)/n$$
\noindent so:
\begin{eqnarray*}
P(B >A)=\frac{1}{15} \left( \frac{n-3}{n}+\frac{n-4}{n}+\frac{n-10}{n}+\frac{n-11}{n}\right) \\ +\frac{2}{15} \left( \frac{n-5}{n}+\frac{n-6}{n}+\frac{n-8}{n}+\frac{n-9}{n}\right)+\frac{3}{15} \frac{n-7}{n} \\=1-\frac{7}{n}
\end{eqnarray*}
\noindent so $1-7/n=10/17$  implies that $n=17$ and we are done.