# Solution

I'll solve this by expressing the exponential function as a power series and then integrating term by term.

First, recall that:
$$e^{\sin x} = \sum_{n=0}^{\infty} \frac{(\sin x)^n}{n!}$$

This allows us to write:
$$\int_0^{\pi/2} e^{\sin x}\ dx = \sum_{n=0}^{\infty} \frac{1}{n!}\int_0^{\pi/2} (\sin x)^n\ dx$$

I'll evaluate these integrals by separating them into even and odd powers of sine.

## Step 1: Establish formulas for the integrals of sine powers.

For even powers of sine, we have:
$$\int_0^{\pi/2} \sin^{2k} x\ dx = \frac{(2k-1)!!}{(2k)!!}\cdot \frac{\pi}{2}$$

For odd powers of sine, we have:
$$\int_0^{\pi/2} \sin^{2k+1} x\ dx = \frac{(2k)!!}{(2k+1)!!}$$

## Step 2: Split the sum into even and odd parts.

$$\int_0^{\pi/2} e^{\sin x}\ dx = \sum_{k=0}^{\infty} \frac{1}{(2k)!}\int_0^{\pi/2} \sin^{2k} x\ dx + \sum_{k=0}^{\infty} \frac{1}{(2k+1)!}\int_0^{\pi/2} \sin^{2k+1} x\ dx$$

## Step 3: Substitute the formulas for the integrals.

For the even powers:
$$\sum_{k=0}^{\infty} \frac{1}{(2k)!}\int_0^{\pi/2} \sin^{2k} x\ dx = \sum_{k=0}^{\infty} \frac{1}{(2k)!} \cdot \frac{(2k-1)!!}{(2k)!!} \cdot \frac{\pi}{2}$$

For $k=0$, we have $\sin^0 x = 1$, so $\int_0^{\pi/2} \sin^0 x\ dx = \frac{\pi}{2}$. Using the convention that $(-1)!! = 1$ (as implied by the problem), the formula gives $\frac{(-1)!!}{(0)!!} \cdot \frac{\pi}{2} = \frac{\pi}{2}$, which matches.

So we can write:
$$\sum_{k=0}^{\infty} \frac{1}{(2k)!} \cdot \frac{(2k-1)!!}{(2k)!!} \cdot \frac{\pi}{2} = \frac{\pi}{2} \left(1 + \sum_{k=1}^{\infty} \frac{(2k-1)!!}{(2k)!(2k)!!}\right)$$

For the odd powers:
$$\sum_{k=0}^{\infty} \frac{1}{(2k+1)!}\int_0^{\pi/2} \sin^{2k+1} x\ dx = \sum_{k=0}^{\infty} \frac{1}{(2k+1)!} \cdot \frac{(2k)!!}{(2k+1)!!} = \sum_{k=0}^{\infty} \frac{(2k)!!}{(2k+1)!(2k+1)!!}$$

## Step 4: Combine the results.

$$\int_0^{\pi/2} e^{\sin x}\ dx = \frac{\pi}{2}\left(1 + \sum_{k=1}^{\infty} \frac{(2k-1)!!}{(2k)!(2k)!!}\right) + \sum_{k=0}^{\infty} \frac{(2k)!!}{(2k+1)!(2k+1)!!}$$

This completes the proof of the given identity.