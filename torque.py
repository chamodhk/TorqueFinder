import math

a = {}
print("Welcome to the torque finder")
n = 1 
while True:
    
    force = int(input("enter the magnitude of force in N: "))
    angle = math.radians(float(input("The angle with the X axis in degrees ")))
    x,y  = input("enter the cordinates x,y").split(',')

    x_comp = force*math.cos(angle)
    y_comp = force*math.sin(angle)

    force = [int(x), int(y),x_comp,y_comp]
    a[str(n)] = force 
    print
    if input("Enter 'y' to add another or 'q' to quit ") == 'y':
        n += 1
        continue
    else:
        break

print(a)
center_x, center_y =  input("Enter the coordinates of the center x,y ").split(',')

torque = 0 

for force in a.values():
    force_torque = (force[0] - int(center_x))*force[3] + (force[1] - int(center_y))*force[2]
    torque += force_torque

print(torque) 

