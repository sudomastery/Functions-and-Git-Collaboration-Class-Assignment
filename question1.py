def speed_detector(speed):
    # Set the maximum allowed speed
    speed_limit = 70
    
    # Initialize demerit points
    demerit_points = 0

    # Check if the speed is within the limit
    if speed <= speed_limit:
        return "Ok"  # No action needed, driver is within the limit
    else:
        # Calculate demerit points: 1 point for every 5 km/h above the speed limit
        demerit_points = (speed - speed_limit) // 5
        
        # Check if demerit points exceed 12
        if demerit_points > 12:
            return "License suspended"  # Too many points, license is suspended
        else:
            # Return the number of demerit points
            return f"Points: {demerit_points}"


# Example tests
print(speed_detector(80))   # Expected output: "Points: 2"
print(speed_detector(135))  # Expected output: "License suspended"