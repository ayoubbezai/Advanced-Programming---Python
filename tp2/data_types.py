def printType(object : any):
    print(type(object))
a = 3
b = 3.5
c = 3 + 3j
print ("Part 1. Numeric, String, and Boolean Basics : ")
printType(a)
printType(b)
printType(c)
d = a > b 
printType(d)

name = "Ayoub"
ai_tool = "ChatGPT"
print(name + " " + ai_tool)

print ("Part 2. Numeric, String, and Boolean Basics : ")

numbers = [1, 2, 3, 4, 5]
words = ("AI", "ML", "NLP")
print(numbers, type(numbers))
print(words, type(words))

num = list(range(10))

print(num , type(num))

ai_dict = {
    "ML": "Machine Learning",
    "DL": "Deep Learn",
    "NLP": "Natural Language Processing"
}
print(ai_dict["DL"])

ai_dict["DL"] = 'Deep Learning'

print(ai_dict)

print(num)

num_set = set(num)

print(num_set)

num_set.add(4)
print(num_set)
print('dublicated is ignored')

num_fronzen = frozenset(num_set)

print(num_fronzen)
printType(num_fronzen)

b1 = bytes("Artificial Intelligence", "utf-8")
print(b1)
b2 = bytearray(b"Artificial Intelligence")
b2[0] = 97  # changes 'A' to 'a' (ASCII)
print(b2)

answer = None
print(type(answer))

if answer is None:
    print("No answer")