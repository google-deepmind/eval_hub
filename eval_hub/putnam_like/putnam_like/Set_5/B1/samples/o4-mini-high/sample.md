```markdown
**Solution.**

Set
\[
P \;=\;\prod_{i=1}^n\bigl(a_i+b_i+c_i\bigr).
\]
For each \(i\) define
\[
x_i=\frac{a_i}{a_i+b_i+c_i},\quad
y_i=\frac{b_i}{a_i+b_i+c_i},\quad
z_i=\frac{c_i}{a_i+b_i+c_i}.
\]
Then \(x_i+y_i+z_i=1\) and
\[
\prod_{i=1}^n a_i
=\prod_{i=1}^n\bigl((a_i+b_i+c_i)\,x_i\bigr)
=P\;\prod_{i=1}^n x_i,
\]
and similarly
\(\prod b_i=P\prod y_i\), \(\prod c_i=P\prod z_i\).  Hence
\[
\Bigl(\prod_{i=1}^n a_i\Bigr)^{\!1/n}
+\Bigl(\prod_{i=1}^n b_i\Bigr)^{\!1/n}
+\Bigl(\prod_{i=1}^n c_i\Bigr)^{\!1/n}
=
P^{1/n}\Bigl((x_1\cdots x_n)^{1/n}+(y_1\cdots y_n)^{1/n}+(z_1\cdots z_n)^{1/n}\Bigr).
\]
By the AM–GM inequality,
\[
(x_1\cdots x_n)^{1/n}\le\frac{x_1+\cdots+x_n}{n},\quad
(y_1\cdots y_n)^{1/n}\le\frac{y_1+\cdots+y_n}{n},\quad
(z_1\cdots z_n)^{1/n}\le\frac{z_1+\cdots+z_n}{n}.
\]
Since \(\sum_i(x_i+y_i+z_i)=n\), adding these three bounds gives
\[
(x_1\cdots x_n)^{1/n}+(y_1\cdots y_n)^{1/n}+(z_1\cdots z_n)^{1/n}
\;\le\;
\frac{\sum_i(x_i+y_i+z_i)}n
\;=\;1.
\]
Therefore
\[
\Bigl(\prod a_i\Bigr)^{1/n}+\Bigl(\prod b_i\Bigr)^{1/n}+\Bigl(\prod c_i\Bigr)^{1/n}
\;\le\;P^{1/n}
\;=\;\Bigl(\prod_{i=1}^n (a_i+b_i+c_i)\Bigr)^{1/n},
\]
as claimed.  
```

**Remark.**  
The key idea is the normalization
\(\,x_i=a_i/(a_i+b_i+c_i)\), etc., which forces
\(x_i+y_i+z_i=1\).  After pulling out the common factor
\(\prod_i(a_i+b_i+c_i)\), one applies AM–GM to each of the three families
\(\{x_i\}\), \(\{y_i\}\), \(\{z_i\}\).