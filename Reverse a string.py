#Input a word or sentence
string = input("please enter your own string")

string2 = ('')
#loop  for printing in reverse
for i in string:
    string2 = i + string2

print("\nThe orignal string =",string)
print("The reversed String =",string2)