#find area of circle, area of triangle and area of rectangle

  #r is radius of circle
  # l and h are the one side and hight of triangle
  # s and t is two sides of rectangle
r,l,h,s,t=map(int,input("enter radius of circle,   side of triangle & hight of triangle  and, and two sides of rectangle" ).split())


area_cir=3.14*r*r
area_tri=0.5*l*h
area_rect=2*(s+t)
print(3.14*r*r)
print(area_tri)
print(area_rect)
