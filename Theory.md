**Theoretical questions:**

1. Linear transformation is sort of operation defined on vector space **V** which maps every vector of space **V** to a vector from space **W**. 
In a way that preserves operations of vector **addition** and **scalar multiplication** of vectors.

Interestingly enough linear transformation keeps straight lines straight; 

F(u+v) = F(u) + F(v);

F(c*v) = c * F(v);        c = const;

F(0v) = 0F(v) = 0 * w;

2. Linear transformation is widely used in fields of GameDev, vector graphics, etc.
3. The matrix of linear transformation, which is when applied to a vector from vector space **V** gives the corresponding vector from the space **W**, 
essentially contains the transformed basis vectors of the space **V** accordingly to a specific linear operator *F*. 
4. The matrix of rotation can be depicted like this  

[cos(x), -sin(x)]

[sin(x), cos(x)]

**-counter clockwise** rotation; if the other *sin(x)* is negative it will give us the **clockwise** rotation;

**Good to know:**
- det of rotation matrix = +-1
- A^t * A = I; 
- A^-1 = A^t (they are orthogonal)
5. The order of applying the transformation matters as the matrix product **is not commutative:**

Let *A*, *B* - square matrices, *v* - vector of space **V**, THEN

*A * B * v != B * A * v*

6. The linear transformation can be represented as an equation:

*A * v = w*; where A - transformation matrix, *v* - vector of space *V*, w is the vector of space *W*

If we know two components out of three => we can find the reverse transformation as it all comes to solving an equation, in general 
case the reverse transformation is performed by applying *A^(-1)*


7.
- If |det(A)| > 1: the object(volume of the object) scales up
- If |det(A)| < 1: the object(volume of the object) scales down
- If |det(A)| = 1: the volume stays the same 