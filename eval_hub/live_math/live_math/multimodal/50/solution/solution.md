The rosette is constructed from six identical patterns arranged symmetrically around a central point A. This means the angle corresponding to one pattern is $360^{\circ} / 6 = 60^{\circ}$. Each pattern is also symmetric, so we can analyze the geometry in a $30^{\circ}$ wedge, as shown in the pattern diagram on the right.

Let $R$ be the radius of the larger circle and $r$ be the radius of the smaller one. Let C be the center of the large circle and E be the center of the small circle. Let A be the vertex of the cone-like shape. From the diagram, A, E, B, C are collinear, where B is the tangency point of the two circles.

Consider the large right triangle with vertices A, C, and the tangency point D. We have $\angle CAD = 30^{\circ}$ and $\angle ADC = 90^{\circ}$. The side $DC = R$. Using trigonometry, $\sin(30^{\circ}) = DC/AC = R/AC$, which gives $AC = R / \sin(30^{\circ}) = 2R$.

Similarly, for the small right triangle with vertices A, E, and its tangency point F on the line AD, we have $\angle FAE = 30^{\circ}$ and $\angle AFE = 90^{\circ}$. The side $EF = r$. This gives $AE = r / \sin(30^{\circ}) = 2r$.

The distance $AB$ can be expressed in two ways:
1. $AB = AC - BC = 2R - R = R$
2. $AB = AE + EB = 2r + r = 3r$
Equating these gives $R = 3r$.

From the diagram, the radius of the small circle is given as $r = 1/2$. Therefore, $R = 3(1/2) = 3/2$.
We also find the distances from A: $AE = 2r = 1$ and $AC = 2R = 3$.

Now we calculate the areas of the relevant shapes for one of the 12 identical pieces that make up the total shaded area.

- The large triangle ADC has base $AD = \sqrt{AC^2 - DC^2} = \sqrt{3^2 - (3/2)^2} = \sqrt{9 - 9/4} = \sqrt{27/4} = \frac{3\sqrt{3}}{2}$. Its area is $\text{Area}(\triangle ADC) = \frac{1}{2} \cdot AD \cdot DC = \frac{1}{2} \cdot \frac{3\sqrt{3}}{2} \cdot \frac{3}{2} = \frac{9\sqrt{3}}{8}$.

- The small triangle AEF has base $AF = \sqrt{AE^2 - EF^2} = \sqrt{1^2 - (1/2)^2} = \sqrt{3/4} = \frac{\sqrt{3}}{2}$. Its area is $\text{Area}(\triangle AEF) = \frac{1}{2} \cdot AF \cdot EF = \frac{1}{2} \cdot \frac{\sqrt{3}}{2} \cdot \frac{1}{2} = \frac{\sqrt{3}}{8}$.

The total shaded area is composed of 12 identical pieces. The area of one piece is calculated by subtracting the unshaded areas from the area of the large triangle ADC.

- In $\triangle ADC$, $\angle ACD = 180^{\circ} - 90^{\circ} - 30^{\circ} = 60^{\circ}$. The area of the circular sector defined by $\angle BCD$ (which is the same as $\angle ACD$) is $\text{Area}(\text{sector } BCD) = \frac{60}{360} \pi R^2 = \frac{1}{6} \pi \left(\frac{3}{2}\right)^2 = \frac{9\pi}{24} = \frac{3\pi}{8}$.

- In $\triangle AEF$, $\angle AEF = 180^{\circ} - 90^{\circ} - 30^{\circ} = 60^{\circ}$. Since A, E, B are collinear, $\angle BEF = 180^{\circ} - 60^{\circ} = 120^{\circ}$. The area of the circular sector defined by $\angle BEF$ is $\text{Area}(\text{sector } BEF) = \frac{120}{360} \pi r^2 = \frac{1}{3} \pi \left(\frac{1}{2}\right)^2 = \frac{\pi}{12}$.

Following the provided solution's method, the shaded area of one piece is given by the expression:

$$ \text{Area}_{\text{piece}} = \text{Area}(\triangle ADC) - \text{Area}(\triangle AEF) - \text{Area}(\text{sector } BEF) - \text{Area}(\text{sector } BCD) $$

$$ \text{Area}_{\text{piece}} = \frac{9\sqrt{3}}{8} - \frac{\sqrt{3}}{8} - \frac{\pi}{12} - \frac{3\pi}{8} $$

$$ \text{Area}_{\text{piece}} = \frac{8\sqrt{3}}{8} - \left(\frac{2\pi}{24} + \frac{9\pi}{24}\right) = \sqrt{3} - \frac{11\pi}{24} $$

Since there are 12 such identical pieces making up the total shaded area of the rosette:

$$ \text{Total Shaded Area} = 12 \times \left(\sqrt{3} - \frac{11\pi}{24}\right) = 12\sqrt{3} - \frac{11\pi}{2} $$

Now, we compute the numerical value:

$$ 12\sqrt{3} - \frac{11\pi}{2} \approx 12(1.7320508) - \frac{11(3.1415926)}{2} \approx 20.78461 - 17.27876 = 3.50585 $$

The problem asks to multiply the result by $10^5$ and take the floor:

$$ \left\lfloor 3.50585 \times 10^5 \right\rfloor = \left\lfloor 350585 \right\rfloor = 350585 $$