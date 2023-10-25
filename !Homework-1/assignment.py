# -*- coding: utf-8 -*-

#Start of Question 1

tendered = 50.00
cost = 14.36
remainingValue = tendered - cost

hundredBills = 0
fiftyBills = 0
twentyBills = 0
tenBills = 0
fiveBills = 0
oneBills = 0

quarters = 0
dimes = 0
nickles = 0
pennies = 0

# check for $100 bills
if remainingValue > 0.00 and (remainingValue // 100.00) > 0.00:
    hundredBills = int(remainingValue // 100.00)
    remainingValue = remainingValue % 100.00

# check for $50 bills
if remainingValue > 0.00 and (remainingValue // 50.00) > 0:
    fiftyBills = int(remainingValue // 50.00)
    remainingValue = remainingValue % 50.00

# check for $20 bills
if remainingValue > 0.00 and (remainingValue // 20.00) > 0:
    twentyBills = int(remainingValue // 20.00)
    remainingValue = remainingValue % 20.00

# check for $10 bills
if remainingValue > 0.00 and (remainingValue // 10.00) > 0:
    tenBills = int(remainingValue // 10.00)
    remainingValue = remainingValue % 10.00

# check for $5 bills
if remainingValue > 0.00 and (remainingValue // 5.00) > 0:
    fiveBills = int(remainingValue // 5.00)
    remainingValue = remainingValue % 5.00

# check for $1 bills
if remainingValue > 0.00 and (remainingValue // 1.00) > 0:
    oneBills = int(remainingValue // 1.00)
    remainingValue = remainingValue % 1.00

# check for quarters
if remainingValue > 0.00 and (remainingValue // 0.25) > 0:
    quarters = int(remainingValue // 0.25)
    remainingValue = remainingValue % 0.25

# check for dimes
if remainingValue > 0.00 and (remainingValue // 0.10) > 0:
    dimes = int(remainingValue // 0.10)
    remainingValue = remainingValue % 0.10

# check for nickles
if remainingValue > 0.00 and (remainingValue // 0.05) > 0:
    nickles = int(remainingValue // 0.05)
    remainingValue = remainingValue % 0.05

remainingValue += 0.0001
round(remainingValue, 2)

# check for pennies
if remainingValue > 0.00 and (remainingValue // 0.01) > 0:
    pennies = int(remainingValue // 0.01)
    remainingValue = remainingValue % 0.01

print("Total Cost: $", cost)
print("Paid: $", tendered)
print("Change: $", round(tendered-cost, 2))
print(" ")
print("$100 bills: ", hundredBills)
print("$50 bills: ", fiftyBills)
print("$20 bills: ", twentyBills)
print("$10 bills: ", tenBills)
print("$5 bills: ", fiveBills)
print("$1 bills: ", oneBills)
print("Quarters: ", quarters)
print("Dimes: ", dimes)
print("Nickles: ", nickles)
print("Pennies: ", pennies)
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")






#Start of question 2
providedValue = -60.9
providedMeasurement = "C"
newValue = 0.0
newMeasurement = "K"

# F to C
if providedMeasurement == "F" and newMeasurement == "C":
    newValue = (5.0/9.0) * (providedValue - 32)

# C to F
elif providedMeasurement == "C" and newMeasurement == "F":
    newValue = (9.0/5.0) * (providedValue + 32)

# K to C
elif providedMeasurement == "K" and newMeasurement == "C":
    newValue = providedValue - 273

# C to K
elif providedMeasurement == "C" and newMeasurement == "K":
    newValue = providedValue + 273

# F to K
elif providedMeasurement == "F" and newMeasurement == "K":
    newValue = ( (5.0/9.0) * (providedValue - 32) ) + 273

# K to F
elif providedMeasurement == "K" and newMeasurement == "F":
    newValue = ( (9.0/5.0) * (providedValue -273) ) + 32

else:
    print("ERROR: Did not calculate. Must have not registered the correct units.")

print("Original Value: ", providedValue, " ", providedMeasurement)
print("Converted to: ", newMeasurement)
print("New Value: ", newValue, newMeasurement)