#### 1(a).A program that calculates the volumes and surface rea of a spherical cap
###The code will first give the variable "P" the pi value which is 3.142
###The user will then be prompted to input values of of the radius of the sphere(r)and height of the cap(h)
###A value for the volume of the spherical cap is to be computed using the formular: (1/3)*P*(h**2)*(3*r-h)
###The surface area of the spherical cap is to be computed using the formula: 2*P*r*h
###The code will print out the calculated volume and surface

#assign value of P
P=3.142 #value of P is pi
#ask user to input the radius of the sphere 
r=int(input("Enter the radius of the sphere in centimeters: "))
#ask user to input the height of the cap
h=int(input("Enter the height of the cap in centimeters: "))

#calculating the volume of the spherical cap
Vol=(1/3)*P*(h**2)*(3*(r-h))

#calculating the surface area of the spherical cap
S_A=2*P*r*h

#print the value of the volume and the surfface area
print(f"The spherical cap has a volume of {Vol} centimeters cubed and a surface area of {S_A} centimeters squared")
####End of the program 

####1(b). A program that calculates the area of a regular polygon 
###The code should ask the user to enter the number of sides, the length of a side and the apothem
###The code should calculate the perimeter of the polygon using the formula:n*s
###The code then  calculate the area of the polygon using the formula:(1/2)*perimeter*a
###The code should then print out the calculted area and the perimeter

#Ask the user to input the number of sides
n=int(input("Give the number of sides of the polygon: "))
#Ask the user to input the length of a side 
s=int(input("Enter the length of sides of the polygon: "))
#Ask the user to input the apothem
a=int(input("Enter the apothem: "))

#Calculate the perimeter of the polygon
Perimeter=n*s
#Calculate the area of the area
Area=(1/2)*(Perimeter*a)
#Print the calculated area of the polygon
print(f"The area of the polygon is {Area}")
####End of the program



