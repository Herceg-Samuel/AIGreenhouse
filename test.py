num = range(11, 21)
for x in num:
    print(x)

#

# Example usage of the alert system
print("\nTesting alert system:")
# Test case 1: Normal conditions
print("\nTest 1 - Normal conditions:")
check_alerts(30, 0.5, 800, 0.4, 900)  # Should not trigger alert

# Test case 2: Multiple alerts (first occurrence)
print("\nTest 2 - Multiple alerts (first time):")
check_alerts(37, 0.2, 1300, 0.2, 1200)  # Should trigger alert

# Test case 3: Multiple alerts again (second consecutive occurrence)
print("\nTest 3 - Multiple alerts (second consecutive time):")
check_alerts(38, 0.2, 1400, 0.2, 1300)  # Should trigger critical risk flag

# Test case 4: Return to normal
print("\nTest 4 - Return to normal conditions:")
check_alerts(30, 0.5, 800, 0.4, 900)  # Should reset consecutive count

# shading control test

#testing watering
watering(0.3, 60, 0)
watering(0.4, 50, 0)
watering(0.5, 40, 0)
watering(0.6, 30, 0)
watering(0.8, 20, 0)


import random

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print("Original list:", my_list)

random.shuffle(my_list)

print("Shuffled list:", my_list)

print("Looping through the shuffled list:")
for fruit in my_list:
    print(fruit)