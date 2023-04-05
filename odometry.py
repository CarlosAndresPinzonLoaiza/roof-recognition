import math

def kinematic(wl,wr): #kinematic model of the differential drive
    r = 10
    vl = wl*r
    vr = wr*r
    v = (vl+vr)/2
    d = 10
    w = (vr-vl)/d
    return v,w

def odometry1(v,w,xi,yi,thetai,dt): #Euler odometry
    xf = xi+v*dt*cos(thetai)
    yf = yi+v*dt*sin(thetai)
    thetaf = thetai+w*dt
    return xf,yf,thetaf

def odometry2(v,w,xi,yi,thetai,dt): # Rungekutta odometry
    xf = xi+v*dt*cos(thetai+(w*dt)/2)
    yf = yi+v*dt*sin(thetai+(w*dt)/2)
    thetaf = thetai+w*dt
    return xf,yf,thetaf

def odometry(left_wheel_ticks, right_wheel_ticks, ticks_per_revolution, wheel_radius, wheelbase, slip_factor):
    # Convert ticks to radians
    left_wheel_radians = left_wheel_ticks / ticks_per_revolution * 2 * math.pi
    right_wheel_radians = right_wheel_ticks / ticks_per_revolution * 2 * math.pi
    
    # Calculate the average wheel displacement
    displacement = (wheel_radius * left_wheel_radians + wheel_radius * right_wheel_radians) / 2
    
    # Calculate the robot's heading change
    heading_change = (wheel_radius * right_wheel_radians - wheel_radius * left_wheel_radians) / wheelbase
    
    # Calculate the amount of slippage
    slippage = slip_factor * (right_wheel_radians - left_wheel_radians) / 2
    
    # Calculate the new position and heading of the robot
    x = displacement * math.cos(heading_change / 2)
    y = displacement * math.sin(heading_change / 2)
    heading = heading_change + slippage
    
    return (x, y, heading)