def check_speed(speed):
    # Speed limit
    limit = 70
    
    if speed <= limit:
        print("Ok")
    else:
        # Calculating points
        points = (speed - limit) // 5
        if points > 12:
            print("License suspended")
        else:
            print(f"Points: {points}")

# test
check_speed(80)   # Output: Points: 2
check_speed(60)   # Output: Ok
check_speed(135)  # Output: License suspended
