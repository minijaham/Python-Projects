def convertCents(cents: int) -> list:
    quartersValue = 25
    dimesValue = 10
    nickelsValue = 5
    penniesValue = 1

    # // will return the quotient, and %= will redefine cents to the remainder
    quarters = cents // quartersValue
    cents %= quartersValue

    dimes = cents // dimesValue
    cents %= dimesValue

    nickels = cents // nickelsValue
    cents %= nickelsValue

    pennies = cents // penniesValue

    return {
        "quarter": quarters,
        "dime": dimes,
        "nickel": nickels,
        "penny": pennies
    }

cents = convertCents(int(input("Enter the number of cents you want to convert: ")))

print("Quarter Count: " + str(cents["quarter"]))
print("Dime Count: " + str(cents["dime"]))
print("Nickel Count: " + str(cents["nickel"]))
print("Penny Count: " + str(cents["penny"]))