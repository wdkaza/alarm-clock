import time
seconds = 10
time_passed = 0

while time_passed < seconds:
    time.sleep(1)
    time_passed += 1

    time_left = seconds - time_passed
    minutes_left = time_left // 60
    seconds_left = time_left % 60
    print(f"{minutes_left:02d}:{seconds_left:02d}")