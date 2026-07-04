word="Python"
# print(word[0:3])
# print(word[3:5])
# #here in slicing starting index is included but ending index value is excluded 
# #for example in 0:3 -> 0 is taken in the output but value of 3 is excluded only value till 2 is taken

# #You can leave a side blank to go to very start / end
# print(word[:3])
# print(word[2:])

# #Here negative also work
# print(word[-4:])#last 4 will come
# print(word[:-2])#last 2 will be skipped

# #The Step
# print(word[::3])# result will have 3 skipped vallues

#python reverse string
print(word[::-1])

print(word[0:10000])#means python mai chahe jitta limit dedo error nahi ayega woh kevel utta hi dega result jitta uske pass hoga
#jaise ki yah pr 10000 tk saare values dene they magr ouput aya kevel "Python" joki only given value hai 