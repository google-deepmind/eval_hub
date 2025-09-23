Making calculations it is clear that:
$$f(x+1)-f(x)=\frac{1}{2} \left(\log_{10}(x+1)-\log_{10}(x) \right)$$
\noindent so for a positive integer $n$ we have:
\begin{eqnarray*}
f(n)\\=f(n)-f(n-1)+f(n-1)-f(n-2)+\cdots+f(2)-f(1)+f(1) \\
= \frac{1}{2} \left( \log_{10}(n)-\log_{10}(n-1)+\log_{10}(n-1)- \log_{10}(n-2)\right) \\
+\cdots +\frac{1}{2} \left(\log_{10}(2)-\log_{10}(1)\right)+f(1)
\end{eqnarray*}
\noindent so $f(n)=\frac{1}{2} \log_{10}(n)+f(1)$ and we have that:
$$f(10^{2024})-f(10^{1516})=\frac{1}{2} \left(2024-1516 \right)+f(1)-f(1)=254$$ 
\noindent and we are done.