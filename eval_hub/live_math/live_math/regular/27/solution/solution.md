We can take $x = 20$, $y = z = 5$. We will prove that $20$ is the largest possible value. In fact, we will prove that if $x > 20$ and $x + y + z =30$, then $xyz < 500$.


 Assume that $x = 20 + 2t$. Then $y + z = 10 - 2t$. By the arithmetic-geometric mean inequality we know that $yz$ will have the maximal value when $y = z = 5-t$. Therefore we need to prove that $(20+2t)(5-t)^2 < 500$ for $t\in (0,5)$. We have
$$(20+2t)(5-t)^2 = 2(10+t)(25-10t+t^2) = 50\cdot(10+t) - 2(10+t)(10t-t^2)$$
$$= 50\cdot(10+t) - 2t\cdot(100-t^2) = 2t^3 - 150t + 500.$$


Now notice that $2t^3 - 150t = t(2t^2 - 150)$. As $t>0$, we have $t>0$, but from $t<5$ we have $2t^2 - 150 < -100 < 0$. Hence $xyz < 500$.