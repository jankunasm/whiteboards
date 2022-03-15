# Electric Company
# Create a function that given a list which represents street lights given as a parameter(l_street), determine if an outage has occurred. A street with a total number of "F" greater than or equal to 2 returns "Outage", anything below returns "Power"
# Example Input: [ T, F, F, F ]
# Example Output: "Outage"

def street_lights(l_street):
    emptylist = []
    for i in l_street:
        if i == "F":
            emptylist.append(i)
    if len(emptylist) >= 2:
        return("Outage")
    else:
        return("Power")

print(street_lights([ "T", "F", "F", "F"]))