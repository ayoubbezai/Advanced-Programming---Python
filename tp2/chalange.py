

# Base dataset
data = [3, 5, 3, 7, 9, 5]
text = "Artificial Intelligence"
info = {"ML": 95, "DL": 90, "NLP": 85}

# -------------------------------
# 1️⃣ Numeric, String, and Boolean
# -------------------------------
a = 10
b = 4.5
c = 3 + 2j

print("=== Numeric, String & Boolean ===")
print(f"Sum of a and b: {a + b}")
print(f"Is a greater than b? {a > b}")
print(f"Uppercase text: {text.upper()}\n")

# -------------------------------
# 2️⃣ Sequences: Lists and Tuples
# -------------------------------
numbers = data
words = ("AI", "Machine", "Learning")

print("=== Lists & Tuples ===")
unique_sorted = sorted(set(numbers))
print(f"Unique & sorted numbers: {unique_sorted}")

joined = " ".join(words)
print(f"Joined tuple: {joined}\n")

# -------------------------------
# 3️⃣ Dictionaries
# -------------------------------
print("=== Dictionaries ===")
info["DL"] = 92  # update a value
avg_score = sum(info.values()) / len(info)
print(f"Updated dictionary: {info}")
print(f"Average AI score: {avg_score}\n")

# -------------------------------
# 4️⃣ Sets
# -------------------------------
print("=== Sets ===")
num_set = set(numbers)
print(f"Original set: {num_set}")

num_set.add(7)  # try adding duplicate
print(f"After adding duplicate 7: {num_set}")

frozen = frozenset(num_set)
print(f"Frozenset type: {type(frozen)}\n")

# -------------------------------
# 5️⃣ Binary Types
# -------------------------------
print("=== Binary Types ===")
b_data = bytes(text, "utf-8")
print(f"Bytes: {b_data}")

ba_data = bytearray(b_data)
ba_data[0] = ord("a")  # change first letter
print(f"Modified bytearray: {ba_data}\n")

# -------------------------------
# 6️⃣ NoneType
# -------------------------------
print("=== NoneType ===")
answer = None
if answer is None:
    print("No answer provided yet.")
else:
    print(f"Answer is {answer}")
