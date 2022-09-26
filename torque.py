import math

banner = '''

88888888888                                         888 
    888                                             888 
    888                                             888 
    888   .d88b.  888d888 .d88888 888  888  .d88b.  888 
    888  d88""88b 888P"  d88" 888 888  888 d8P  Y8b 888 
    888  888  888 888    888  888 888  888 88888888 Y8P 
    888  Y88..88P 888    Y88b 888 Y88b 888 Y8b.      "  
    888   "Y88P"  888     "Y88888  "Y88888  "Y8888  888 
                              888                       
                              888                       
                              888                       '''

a = {}
print("\nWelcome to the torque finder\n")
print(banner)
n = 1 
while True:
    
    force = float(input("\nenter the magnitude of force in N: "))
    angle = math.radians(float(input("\nThe angle with the X axis in degrees ")))
    x,y  = input("\nenter the cordinates x,y ").split(',')

    x_comp = force*math.cos(angle)
    y_comp = force*math.sin(angle)

    force = [int(x), int(y),x_comp,y_comp]
    a[str(n)] = force 
    print
    if input("\nEnter 'y' to add another or 'q' to quit ") == 'y':
        n += 1
        continue
    else:
        break

center_x, center_y =  input("\nEnter the coordinates of the center x,y ").split(',')

torque = 0 

for force in a.values():
    force_torque = (force[0] - float(center_x))*force[3] + (force[1] - float(center_y))*force[2]
    torque += force_torque

print("\nResulatnt torque is " +str(torque) )

