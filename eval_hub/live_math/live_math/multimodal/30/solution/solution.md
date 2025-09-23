The coordinates of the vertices of the square based pyramid are given as $A(0,0,0)$, $B(4,0,0)$, $C(4,4,0)$, $D(0,4,0)$, and the apex $E(2,2,3)$.

Let $M$, $N$, and $P$ be the midpoints of the edges $AE$, $DE$, and $BC$ respectively.
- The coordinates of $M$ are $\left(\frac{0+2}{2}, \frac{0+2}{2}, \frac{0+3}{2}\right) = (1, 1, 1.5)$.
- The coordinates of $N$ are $\left(\frac{0+2}{2}, \frac{4+2}{2}, \frac{0+3}{2}\right) = (1, 3, 1.5)$.
- The coordinates of $P$ are $\left(\frac{4+4}{2}, \frac{0+4}{2}, \frac{0+0}{2}\right) = (4, 2, 0)$.

The solution follows a constructive approach by calculating the volume of a prism and subtracting the volumes of two pyramids.

Let $M'$ be the orthogonal projection of $M$ onto the plane $y=0$ (the xz-plane), and $N'$ be the orthogonal projection of $N$ onto the plane $y=4$.
- The coordinates of $M'$ are $(1, 0, 1.5)$.
- The coordinates of $N'$ are $(1, 4, 1.5)$.

The volume of the final object is given by the volume of the prism $ABM'DCN'$ ($V_1$) minus the volumes of two pyramids, $ABMM'$ ($V_2$) and $NPCN'D$ ($V_3$).

1.  **Volume of the prism $V_1 = \text{Volume}(ABM'DCN')$:**
    The prism has a base $ABM'$ in the plane $y=0$ and a congruent top $DCN'$ in the plane $y=4$. The height of the prism is $h_1 = 4-0 = 4$.
    The base is a triangle with vertices $A(0,0,0)$, $B(4,0,0)$, and $M'(1,0,1.5)$. In the xz-plane, the vertices are (0,0), (4,0), and (1,1.5).
    The area of the base is $\text{Area}(ABM') = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 4 \times 1.5 = 3$.
    The volume of the prism is $V_1 = \text{Area}(ABM') \times h_1 = 3 \times 4 = 12$.

2.  **Volume of the pyramid $V_2 = \text{Volume}(ABMM')$:**
    This pyramid has base $ABM'$ and apex $M(1,1,1.5)$. The base area is 3.
    The height of the pyramid $h_2$ is the perpendicular distance from $M$ to the plane of the base ($y=0$), which is the y-coordinate of $M$. So, $h_2 = 1$.
    The volume is $V_2 = \frac{1}{3} \times \text{Area}(ABM') \times h_2 = \frac{1}{3} \times 3 \times 1 = 1$.

3.  **Volume of the pyramid $V_3 = \text{Volume}(NPCN'D)$:**
    This pyramid has apex $D(0,4,0)$ and base, the quadrilateral $NPCN'$.
    The vertices of the base are $N(1,3,1.5)$, $P(4,2,0)$, $C(4,4,0)$, and $N'(1,4,1.5)$. These points lie on the plane $x+2z=4$.
    The base quadrilateral $NPCN'$ is a trapezoid, as $\vec{N'N} = (0, -1, 0)$ is parallel to $\vec{CP} = (0,-2,0)$. Lengths of parallel sides are $|\vec{N'N}| = 1$ and $|\vec{CP}|=2$.
    The height of the trapezoid is the perpendicular distance between the lines containing these segments, which is $\sqrt{(4-1)^2 + (0-1.5)^2} = \sqrt{9+2.25} = \sqrt{11.25} = \frac{\sqrt{45}}{2}$.
    The area of the trapezoid is $\text{Area}(NPCN') = \frac{1}{2}(1+2) \frac{\sqrt{45}}{2} = \frac{3\sqrt{45}}{4}$.
    The height of the pyramid $h_3$ is the distance from the apex $D(0,4,0)$ to the plane of the base $x+2z-4=0$.
    $h_3 = \frac{|1(0) + 0(4) + 2(0) - 4|}{\sqrt{1^2+0^2+2^2}} = \frac{|-4|}{\sqrt{5}} = \frac{4}{\sqrt{5}}$.
    The volume is $V_3 = \frac{1}{3} \times \text{Area}(NPCN') \times h_3 = \frac{1}{3} \times \frac{3\sqrt{45}}{4} \times \frac{4}{\sqrt{5}} = \frac{\sqrt{45}}{\sqrt{5}} = \sqrt{9} = 3$.

4.  **Final Volume:**
    The total volume of the remaining object is $V = V_1 - V_2 - V_3 = 12 - 1 - 3 = 8$.