Let $A$ be an $n \times n$ matrix with entries $a_{ij} \in \{0, 1\}$. $n$ is an even integer.
Let $J_n$ be the $n \times n$ matrix with ones in each odd column and zeros in each even column.
$J_n = (j_{ij})$ where $j_{ij} = 1$ if $j$ is odd, and $j_{ij} = 0$ if $j$ is even.
$J_n = \begin{pmatrix}
1 & 0 & 1 & 0 & \dots & 1 & 0 \\
1 & 0 & 1 & 0 & \dots & 1 & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
1 & 0 & 1 & 0 & \dots & 1 & 0
\end{pmatrix}$.
The equation is $A^2 = J_n$. Let $A = (a_{ij})$. The $(i,j)$-th entry of $A^2$ is $\sum_{k=1}^n a_{ik} a_{kj}$.
So, $\sum_{k=1}^n a_{ik} a_{kj} = 1$ if $j$ is odd, and $\sum_{k=1}^n a_{ik} a_{kj} = 0$ if $j$ is even.
Since $a_{ij} \in \{0, 1\}$, the sum $\sum_{k=1}^n a_{ik} a_{kj}$ is the number of indices $k$ such that $a_{ik}=1$ and $a_{kj}=1$.

For any $j$ that is even, $\sum_{k=1}^n a_{ik} a_{kj} = 0$ for all $i=1, \dots, n$.
This means that for a fixed even $j$, for every $i$ and $k$, $a_{ik}a_{kj}=0$.
If there exists a $k_0$ such that $a_{k_0, j}=1$, then $a_{ik_0}=0$ for all $i=1, \dots, n$.
This implies that if an even column $j$ of $A$ contains a $1$ (say $a_{k_0, j}=1$), then the $k_0$-th row of $A$ must be a zero row ($a_{k_0,m}=0$ for all $m$). However, if $a_{k_0, j}=1$ is true, then $a_{k_0, j}=0$ must also be true if row $k_0$ is a zero row. This is a contradiction unless $a_{k_0, j}=0$.
So, for any even column $j$, $a_{kj}=0$ for all $k=1, \dots, n$.
All even columns of $A$ must be zero columns. Let $A_j$ denote the $j$-th column of $A$.
$A_j = \mathbf{0}$ for $j \in \{2, 4, \dots, n\}$.
$A$ has the form $(A_1, \mathbf{0}, A_3, \mathbf{0}, \dots, A_{n-1}, \mathbf{0})$.

Let $j$ be an odd column index, $j \in \{1, 3, \dots, n-1\}$.
$\sum_{k=1}^n a_{ik} a_{kj} = 1$ for all $i=1, \dots, n$.
Since $a_{k, 2m}=0$ for all $k, m$, $k$ must be odd for $a_{k, \text{even}}$ to be non-zero. No, $a_{k, even}=0$.
$a_{k, 2m}=0$ for all $k, m$.
The summation for $(A^2)_{ij}$ becomes $\sum_{k \text{ odd}} a_{ik} a_{kj} + \sum_{k \text{ even}} a_{ik} a_{kj}$.
Since $a_{i, 2m}=0$ for all $i, m$, the terms $a_{i, 2m}$ are zero. Oh, this applies to the first index.
$(A^2)_{ij} = \sum_{k=1}^n a_{ik} a_{kj}$. We know $a_{k, 2m}=0$ for all $k, m$.
If $j$ is even, $(A^2)_{ij} = \sum_k a_{ik} \cdot 0 = 0$, which is correct.
If $j$ is odd, $(A^2)_{ij} = \sum_k a_{ik} a_{kj} = 1$. For a fixed pair $(i,j)$ with $j$ odd, there is exactly one $k$ such that $a_{ik}=1$ and $a_{kj}=1$.

Let $R_i$ be the $i$-th row of $A$. $R_i A$ is the $i$-th row of $A^2$.
The $i$-th row of $J_n$ is $(1, 0, 1, 0, \dots, 1, 0)$. Let this row vector be $\mathbf{w}^T$.
$R_i A = \mathbf{w}^T$ for all $i=1, \dots, n$.
Let $A = (a_{ij})$. $R_i = (a_{i1}, a_{i2}, \dots, a_{in})$.
$a_{i, 2m}=0$ for all $i, m$. $R_i = (a_{i1}, 0, a_{i3}, 0, \dots, a_{i,n-1}, 0)$.
$R_i A = (a_{i1}, 0, a_{i3}, 0, \dots, a_{i,n-1}, 0) A = \mathbf{w}^T = (1, 0, 1, 0, \dots, 1, 0)$.

Let $A_{odd}$ be the $n \times n/2$ matrix containing the odd columns of $A$. $A_{odd} = (a_{i, 2l-1})$.
Let $R_{i,odd} = (a_{i1}, a_{i3}, \dots, a_{i,n-1})$. This is a $1 \times n/2$ vector.
The rows of $A$ are $(R_{1,odd} | \mathbf{0}_{1 \times n/2}), \dots, (R_{n,odd} | \mathbf{0}_{1 \times n/2})$.
Let $A = \begin{pmatrix} R_{1,odd} & \mathbf{0} \\ \vdots & \vdots \\ R_{n,odd} & \mathbf{0} \end{pmatrix}$. Let $R_{i,odd}$ be $r_i$. $A = \begin{pmatrix} r_1 \\ \vdots \\ r_n \end{pmatrix} (I_{n/2} | 0)$ No this is not $A$.
$A = \begin{pmatrix} \mathbf{c}_1 & \mathbf{0} & \mathbf{c}_3 & \mathbf{0} & \dots \end{pmatrix}$. $A_{odd} = (\mathbf{c}_1, \mathbf{c}_3, \dots)$.
The $i$-th row of $A$ is $r_i = (a_{i1}, 0, a_{i3}, 0, \dots, a_{i,n-1}, 0)$.
$(A^2)_{ij} = \sum_k a_{ik} a_{kj}$. $j$ is odd: $\sum_{l=1}^{n/2} a_{i, 2l-1} a_{2l-1, j} = 1$. $j$ is even: 0.
Let $B = (a_{i, 2l-1})$ be $n \times n/2$. Let $C = (a_{2l-1, 2m-1})$ be $n/2 \times n/2$.
The condition $(A^2)_{ij}=1$ for $j=2m-1$ is $\sum_{l=1}^{n/2} b_{il} c_{lm} = 1$ for all $i=1..n, m=1..n/2$.
This is $BC = J'$, where $J'$ is the $n \times n/2$ matrix of all ones.

$B$ and $C$ have entries in $\{0,1\}$. $(BC)_{im} = \sum_l b_{il} c_{lm} = 1$.
For each pair $(i,m)$, there must be exactly one $l$ such that $b_{il}=1$ and $c_{lm}=1$.

Consider the rows of $B$. Let $R_i$ be the $i$-th row of $B$. $R_i C = (1, 1, \dots, 1)$.
$R_i$ is $1 \times n/2$. If $R_i$ is a zero vector, $R_i C = \mathbf{0} \ne (1, \dots, 1)$. So $R_i$ must have at least one 1.
Suppose $R_i$ has only one 1, at column $l_i$. $R_i = e_{l_i}^T$. Then $e_{l_i}^T C = C_{l_i, \cdot}$ (row $l_i$ of $C$) must be $(1, \dots, 1)$.
If this holds for all $i$, then for each $i \in \{1, \dots, n\}$, there is $l_i \in \{1, \dots, n/2\}$ such that $R_i=e_{l_i}^T$, and the $l_i$-th row of $C$ is $\mathbf{1}_{n/2}^T$.

If $C$ contains a zero row, say row $l_0$, then $\sum_m c_{l_0, m}=0$. $C_{l_0, \cdot} = \mathbf{0}$.
If any $R_i = e_{l_0}^T$, then $R_i C = \mathbf{0} \ne \mathbf{1}_{n/2}^T$. So $R_i \ne e_{l_0}^T$ for all $i$. Column $l_0$ of $B$ is $\mathbf{0}$.

If all rows of $C$ are $\mathbf{1}_{n/2}^T$, then $C = \mathbf{1}_{n/2} \mathbf{1}_{n/2}^T$. All entries of $C$ are 1.
In this case, $\sum_l b_{il} c_{lm} = \sum_l b_{il} = 1$. The row sums of $B$ must be 1.
Each row of $B$ is $e_{l_i}^T$. $b_{i,l_i}=1$, others 0.
$A_{odd} = B$. $a_{i, 2l-1} = b_{il}$. Row $i$ of $A$ is $(b_{i1}, 0, b_{i2}, 0, \dots)$.
Row sum of $A$ is $\sum_l b_{il} = 1$.
So $A$ is a $\{0,1\}$ matrix with row sums equal to 1.
This implies $a_{ij}=1$ for exactly one $j$ for each $i$. Let this be $j=\sigma(i)$.
So $a_{ij} = \delta_{j, \sigma(i)}$.
Since $a_{i, 2m}=0$, $\sigma(i)$ must be odd for all $i=1, \dots, n$.
$\sigma: \{1, \dots, n\} \to \{1, 3, \dots, n-1\}$.
$A^2 = (d_{ij})$ where $d_{ij} = \sum_k a_{ik} a_{kj} = \sum_k \delta_{k, \sigma(i)} \delta_{j, \sigma(k)} = \delta_{j, \sigma(\sigma(i))}$.
$A^2=J_n$ means $d_{ij} = j_{ij}$.
$\delta_{j, \sigma(\sigma(i))} = 1$ if $j$ is odd, 0 if $j$ is even.
This means $j = \sigma(\sigma(i))$ if and only if $j$ is odd.
The set of values $\{\sigma(\sigma(i)) \mid i=1, \dots, n\}$ must be exactly $\{1, 3, \dots, n-1\}$.
Let $O = \{1, 3, \dots, n-1\}$. $|\text{Im}(\sigma \circ \sigma)| = n/2$.
We know $\text{Im}(\sigma) \subseteq O$. $|\text{Im}(\sigma)| \le n/2$.
Also $|\text{Im}(\sigma \circ \sigma)| \le |\text{Im}(\sigma)|$.
So $n/2 \le |\text{Im}(\sigma)| \le n/2$. This means $|\text{Im}(\sigma)| = n/2$.
$\text{Im}(\sigma) = O$. $\sigma: \{1, \dots, n\} \to O$ is surjective.
For any $o \in O$, there are $n/(n/2)=2$ indices $i$ such that $\sigma(i)=o$.

$\sigma(\sigma(i))$ is always in $\sigma(O)$. Since $\text{Im}(\sigma)=O$, $\sigma(O)$ is $\sigma$ restricted to $O$. $\sigma|_O: O \to O$.
$\text{Im}(\sigma \circ \sigma) = \sigma(\text{Im}(\sigma)) = \sigma(O)$.
We require $\sigma(O)=O$. So $\sigma|_O: O \to O$ must be surjective. Since $O$ is finite, $\sigma|_O$ is a permutation of $O$.
Let $\sigma_O = \sigma|_O$. $\sigma_O: \{1,3,\dots,n-1\} \to \{1,3,\dots,n-1\}$ is a permutation.

$j = \sigma(\sigma(i))$ iff $j \in O$.
If $i \in O$, $\sigma(i) \in O$, so $\sigma(\sigma(i)) = \sigma_O(\sigma(i)) \in O$. This is consistent.
If $i \notin O$, $i$ is even. $\sigma(i) \in O$. $\sigma(\sigma(i)) \in O$. This is consistent.
$j=\sigma(\sigma(i))$. This gives $\{1,3,...,n-1\}$ as range.

The matrix $A$ has $a_{ij}=\delta_{j, \sigma(i)}$.
$A^2 = (d_{ij})$ with $d_{ij} = \delta_{j, \sigma(\sigma(i))}$.
$J_n = (j_{ij})$ with $j_{ij}=1$ if $j$ is odd, 0 if $j$ is even.
$d_{ij} = j_{ij}$ requires $\sigma(\sigma(i))=j$ for all $i$ when $j$ is odd, and $\sigma(\sigma(i))=j$ must be impossible when $j$ is even.
The second part is guaranteed as $\sigma(\sigma(i)) \in O$.
The first part requires that for each $j \in O$, there is some $i$ such that $\sigma(\sigma(i))=j$. This is $\text{Im}(\sigma \circ \sigma)=O$. This was shown to be equivalent to $\text{Im}(\sigma)=O$ and $\sigma|_O$ is a permutation.

So $A$ is a matrix with row sums 1, $a_{i, 2m}=0$ for all $i,m$. $A$ must have form $a_{ij}=\delta_{j, \sigma(i)}$ where $\sigma: \{1,\dots,n\} \to O$ is surjective and $\sigma|_O: O \to O$ is a permutation.
$A_{OO} = (a_{ij})_{i,j \in O}$. $a_{ij} = \delta_{j, \sigma(i)}$. Since $i \in O \implies \sigma(i) \in O$, this submatrix is a permutation matrix. Let it be $P_O$.
$A_{EO} = (a_{ij})_{i \in E, j \in O}$. $a_{ij}=\delta_{j, \sigma(i)}$. $i \in E \implies \sigma(i) \in O$. This submatrix specifies $\sigma$ on $E$. $\sigma|_E: E \to O$ is a function.
Since $\sigma$ maps $\{1..n\}$ to $O$, $\sigma(O)=O, \sigma(E)=O$.
$|O|=n/2, |E|=n/2$. Since $\sigma|_O$ is a permutation, $\sigma|_O: O \to O$ is bijective.
Since $\sigma: \{1..n\} \to O$ is surjective, and $\sigma|_O$ is a bijection, $\sigma|_E$ must be a bijection from $E$ to $O$.
Let $\sigma(i) = \pi_O(i)$ for $i \in O$, $\pi_O$ is perm of $O$. Let $\sigma(i) = \pi_E(i)$ for $i \in E$, $\pi_E: E \to O$ is a bijection.

$A$ can be written in block form regarding $O$ and $E$ indices.
$A = \begin{pmatrix} A_{OO} & A_{OE} \\ A_{EO} & A_{EE} \end{pmatrix}$. $A_{OO}$ is $n/2 \times n/2$, etc.
$a_{ij}=0$ for $j \in E$. $A_{OE}=0, A_{EE}=0$.
$a_{ij}=1$ iff $j=\sigma(i)$.
$i \in O \implies \sigma(i) \in O$. $a_{ij}=\delta_{j, \pi_O(i)}$ for $i,j \in O$. $A_{OO}$ is perm matrix $P_O$.
$i \in E \implies \sigma(i) \in O$. $a_{ij}=\delta_{j, \pi_E(i)}$ for $i \in E, j \in O$. $A_{EO}$ matrix for $\pi_E$.
$A = \begin{pmatrix} P_O & 0 \\ P_E & 0 \end{pmatrix}$ after rearranging rows/cols to group $O, E$. Let $O=\{1,..,n/2\}, E=\{n/2+1,..,n\}$.
$A^2 = \begin{pmatrix} P_O & 0 \\ P_E & 0 \end{pmatrix} \begin{pmatrix} P_O & 0 \\ P_E & 0 \end{pmatrix} = \begin{pmatrix} P_O^2 & 0 \\ P_E P_O & 0 \end{pmatrix}$.
This must be $J_n$ in this block form.
$J_n = \begin{pmatrix} J_{OO} & J_{OE} \\ J_{EO} & J_{EE} \end{pmatrix}$. $j_{ij}=1$ if $j$ odd (first $n/2$ columns), 0 if $j$ even (last $n/2$ columns).
$J_{OO}$ is $n/2 \times n/2$ matrix of all 1s. $J_{OE}=0$. $J_{EO}$ is $n/2 \times n/2$ matrix of all 1s. $J_{EE}=0$.
$J_n = \begin{pmatrix} \mathbf{1}_{n/2 \times n/2} & 0 \\ \mathbf{1}_{n/2 \times n/2} & 0 \end{pmatrix}$.

So we need $P_O^2 = \mathbf{1}_{n/2 \times n/2}$ and $P_E P_O = \mathbf{1}_{n/2 \times n/2}$.
$P_O$ is a permutation matrix. Its entries are 0 or 1. $P_O^2$ has entries 0 or 1.
$P_O^2 = \mathbf{1}_{n/2 \times n/2}$ means all entries of $P_O^2$ are 1.
$P_O^2$ entry $(i,j)$ is 1 iff $i \to \sigma(i) \to \sigma(\sigma(i))=j$. Number of paths of length 2 is 1 for all $i,j$.
If $P_O$ is perm matrix, $P_O^2=I$ if $P_O=P_O^{-1}$. If $P_O^2=\mathbf{1}$, $P_O$ must be $\mathbf{1}_{n/2 \times n/2}$.
$P_O$ is a permutation matrix of size $n/2 \times n/2$. If $n/2 > 1$, $P_O$ cannot be $\mathbf{1}_{n/2 \times n/2}$.
$P_O = \mathbf{1}_{n/2 \times n/2}$ only if $n/2=1$, which means $n=2$.
If $n=2$, $n/2=1$. $P_O$ is $1 \times 1$. $P_O=(1)$. $P_O^2=(1)$. $\mathbf{1}_{1 \times 1}=(1)$. $n=2$ works.

If $n>2$, $n/2>1$, $P_O$ cannot be $\mathbf{1}_{n/2 \times n/2}$. $P_O^2$ has only 0 and 1. For $P_O^2$ to be $\mathbf{1}_{n/2 \times n/2}$, it must be $\mathbf{1}$ matrix.
This can only happen if $n/2=1$.

Thus, such a matrix $A$ exists only if $n=2$.

Final check for $n=2$:
$J_2 = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$. $n$ is even.
We need $A$ with entries in $\{0,1\}$ s.t. $A^2=J_2$.
$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$. $a,b,c,d \in \{0,1\}$.
$A^2 = \begin{pmatrix} a^2+bc & b(a+d) \\ c(a+d) & d^2+bc \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$.
$a+bc=1$ ($a^2=a$ as $a \in \{0,1\}$).
$b(a+d)=0$.
$c(a+d)=1$. $c=1, a+d=1$.
$d+bc=0$.
$a+d=1$ means $(a,d)$ is $(1,0)$ or $(0,1)$.
If $(a,d)=(1,0)$: $c=1$. $a+bc=1+1\cdot b=1 \implies b=0$. $d+bc=0+1\cdot 0=0$. This solution $(a,b,c,d)=(1,0,1,0)$ works. $A=\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$.
If $(a,d)=(0,1)$: $c=1$. $a+bc=0+b\cdot 1=1 \implies b=1$. $b(a+d)=1(0+1)=1 \ne 0$. No solution here.
So only $A=\begin{pmatrix} 1 & 0 \\ 1 & 0 \end{pmatrix}$ is possible for $n=2$. Entries are in $\{0,1\}$.

The condition holds only for $n=2$.

The final answer is $\boxed{n=2}$.