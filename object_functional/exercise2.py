collections = dict()

words = ["fire", "apple", "double", "cat", "elephant", "bubble", "fish", "air", "dog", "beach", "front", "early", "door", "bird", "cave", "flag", "awesome", "begin", "date", "control", "ember", "flat", "cloud", "force", "dragon", "banana", "cute", "finish", "eagle", "about", "dance", "bird", "alone", "feed", "cruel", "energy", "dust", "anchor", "flower", "deep", "card", "avoid", "feather", "bare", "cause", "dark", "face", "echo", "brave", "focus"]

for word in words:
    first_letter = word[0].strip().lower()
    if first_letter not in collections:
        collections[first_letter] = list()
    if first_letter not in collections[first_letter]:
        collections[first_letter].append(word)


# print(collections)
sorted_collection = dict()
# Sort the collection manually
unsorted = { 'a': '', 'f': 'F', 'c': 'c', 'b': 'B', 'd': 'DD', 'e': 'ef'}

keys = list(unsorted.keys())

for i in range(len(keys)):
    for j in range(len(keys) - 1):
        if keys[j] > keys[j + 1]:
            keys[j], keys[j + 1] = keys[j + 1], keys[j]


print("Sorted Keys: ", keys)
for letter in keys:
    if letter in unsorted:
        sorted_collection[letter] = unsorted[letter]


print(sorted_collection)
