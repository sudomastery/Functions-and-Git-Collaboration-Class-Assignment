# function check_speed that takes a parameter speed

def check_speed(speed):
    # if speed is less than 70 print ok
    if speed <70:
        print('ok')
    else:
        # calculate demerits points for every 5 km/s above 70
        points = (speed-70)
        print (f'points:{points}')
check_speed(95)