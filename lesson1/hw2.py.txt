import math   
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# discriminant
d = b**2-4*a*c 

if d < 0:

    print ('No solutions')

elif d == 0:
    print ('No solutions')
    #only two solutions under the statement of task
    #x1 = -b / (2*a)
    #print ('There's one solution, x = ',x1)

else: # if d > 0

    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print ('x1 = ',x1,'x2 = ',x2)