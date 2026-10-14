def average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0
    return total / count
print(average([70, 75, 80, 85, 90]))

def check_status(temp):
    
    if temp < 80:   
        return "normal"
    elif temp >= 80 and temp < 90:
        return "high"
    else:
        return "warning"
temperatures = [70, 75, 80, 85, 90]
for temp in temperatures:
    print(check_status(temp))