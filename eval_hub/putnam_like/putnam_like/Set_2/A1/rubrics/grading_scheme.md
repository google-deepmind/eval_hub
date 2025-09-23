Solution step (2 points)

$$
\det(A)\neq 0 \text{ and }\det(B)\neq 0,
$$
$$
\det(-A)=(-1)^{2n+1}\det(A) =-\det(A),
$$
$$
\det(-B)=(-1)^{2n+1}\det(B) =-\det(B).
$$
Hence there exist two numbers $\alpha,\beta\in \{-1,1\}$ such that
$$
\det(\alpha A)>0\text{ and }\det(\beta B)<0.
$$

Solution step (6 points)

Define a function $f: [0,1]\to \mathbb{R}$ by
$$
f(t)=\det(t\alpha A+(1-t)\beta B) \text{ for }t\in [0,1].
$$
The above function admits the following properties:

* $f(0)=\det(\beta B)<0$,
* $f(1)=\det(\alpha A)>0$,
* $f$ is continuous on $[0,1]$.

Solution step (2 points)

By the intermediate value theorem, there exists a real number $c_0\in (0,1)$ such that $f(c_0)=0$. Finally, it suffices to set
$$
a:=c_0\cdot\alpha\text{ and } b:=(1-c_0)\beta,
$$
since then we have
$$
\det(aA+bB)=f(c_0)=0.
$$