# Assignment Goals:
#    If the car’s speed is less than 70 -> print "Ok".
#    If the car’s speed is 70 or more:
#       a. For every 5 km more than 70, give 1 demerit point and then print number of demerit points "Points: X".
#           e.g. 80 - 70 = 10 >>> 10/5 = 2 Demerit Points 
#       b. If the points are more than 12, print "License Suspended".

def speed_detector(speed):
   
    speed_limit = 70
    
    demerit_points = 0

    # If the speed is within the limit:

    if speed <= speed_limit:
        return "Ok"  
    else:
        # Calculate demerit points: 1 point for every 5 km/h above the speed limit

        demerit_points = (speed - speed_limit) // 5
        
        # If demerit points exceed 12

        if demerit_points > 12:
            return "License suspended" 
        else:
            # Return the number of demerit points
            return f"Points: {demerit_points}"


# Example tests
print(speed_detector(80))   # Expected output: "Points: 2"
print(speed_detector(135))  # Expected output: "License suspended"
