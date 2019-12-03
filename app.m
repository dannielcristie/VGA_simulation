# letra a

[x,y] = meshgrid(-2:0.05:2)
z = 4-x.^2
surf(x,y,z)

#letra 3
[xx yy zz]=cylinder([3,3])
surf(xx, yy, zz.*3)
hold on
surf(xx, yy, -zz.*3)