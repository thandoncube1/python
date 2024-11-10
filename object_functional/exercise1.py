def list_of_common_words():
    result = dict()

    words = str(input("Enter a list of words seperated by commas: ")).lower()

    collection = words.split(", ")
    for word in collection:
        first_letter = word[0].strip()
        if first_letter not in result:
            result[first_letter] = []
        if word not in result[first_letter]:
            result[first_letter].append(word)

    return result


list_of_words = list_of_common_words()

def main():
    choice = str(input("Enter a letter you want: ")).lower()
    for word in list_of_words:
        if choice in list_of_words[word]:
            print(word)


main()

