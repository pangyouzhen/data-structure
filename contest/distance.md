本质是个数学问题

$x_{0},x_{1},x_{2},...x_{n}$ 按照升序排列

$S_{i} = \sum\limits_{j=0}{\vert x_{i} - x_{j}\vert}$

$S_{i+1} = \sum\limits_{j=0}{\vert x_{i+1} - x_{j}\vert}$

所以$S_{i+1} - S_{i}$ 展开
前i-1项：$x_{i+1} - x_{0} + x_{i+1} - x_{1} + x_{i+1} - x_{2} +... -(x_{i} - x_{0} + x_{i} - x_{1} + x_{i} - x_{2} + ...)=i(x_{i+1} - x_{i})$

第i,i+1项: $x_{i+1} - x_{i+1} + x_{i+1} - x_{i} -(x_{i} - x_{i} + x_{i+1} - x_{i}) = 0$

后i+2项: $x_{i+2} - x_{i+1} + x_{i+3} - x_{i+1} + x_{i+4} - x_{i+1} +... -(x_{i+2} - x_{i} + x_{i+3} - x_{i} + x_{i+4} - x_{i} + ...) = (n - (i+2) + 1)(x_{i} - x_{i+1}) = (i+1-n)(x_{i+1}-x_{i})$

所以 $S_{i+1} - S_{i} = (i+i+1-n)(x_{i+1}-x_{i})=(2i+1-n)(x_{i+1}-x_{i})$

 比如有0,2,4,5,6,8,的数列n=5
 S0 = 25
 i=0时, $S1 - S0 = (1-5)(2-0) = -8$ 所以S1= 17
 i=1时，$S2 - S1 = (3-5)(4-2) = -4$ 所以S2= 13
 i=2时，$S3 - S2 = (5-5)(5-4) = 0$  所以S3 = 13
 