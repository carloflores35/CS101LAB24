#Some of the functions have variables revolving around Star Wars Sith, so bare with me
#The function Darth Tyrannus, represents the Count. Counting how many words there are. 
def word_count(text):
    darthwordtyrannus = text.split()
    print(darthwordtyrannus)
    print("Word Count:", len(darthwordtyrannus))
    print()
#The function Darth Sidious, represents the long word. Comparing the length of each element to the other
def find_longest_word(text):
    darthwordsidious = text.split()
    max = len(darthwordsidious[0])
    bulk = darthwordsidious[0]
    for i in darthwordsidious:
        if(len(i) > max):
            max = len(i)
            bulk = i
    print("Longest Word:", bulk)
    print()
#The function Darth Maul, represents the Count of the substring. Counting how many occurences using the count() method. 
def count_substring(text, substring):
    darthwordmaul = text.split()
    count = darthwordmaul.count(substring)
    print(f"Count of Substring '{substring}': {count}")
    print()
#The function Darth Vader, involves removing and appending. For if a word is not in a list that starts empty, add it 
def extract_unique_words(text):
    darthwordvader = text.split()
    unique_words = []
    for word in darthwordvader:
        if word not in unique_words:
            unique_words.append(word)
    print("Unique Words:", unique_words)
    print()
#The function that controls everything. Using a while loop, until the user is done.
def main():
    name = "carlo"
    print(len(name))
    print("Welcome to the Text Processing Program!\n")
    analytext = input("Enter some text: ")
    print("Original Text:\n",analytext,'\n')
    print("Text Analysis Options:\n1. Word Count\n2. Longest Word\n3. Count of Substring\n4. Unique Words\n5. Exit")
    choice = 0
    while choice != 5:
        choice = int(input("Enter the number from the analysis options (1-5):"))
        print()
        if choice == 1:
            word_count(analytext)
            print("Text Analysis Options:\n1. Word Count\n2. Longest Word\n3. Count of Substring\n4. Unique Words\n5. Exit")
        elif choice == 2:
            find_longest_word(analytext)
            print("Text Analysis Options:\n1. Word Count\n2. Longest Word\n3. Count of Substring\n4. Unique Words\n5. Exit")
        elif choice == 3:
            substringinput = input("Enter a substring to count: ")
            count_substring(analytext, substringinput)
            print("Text Analysis Options:\n1. Word Count\n2. Longest Word\n3. Count of Substring\n4. Unique Words\n5. Exit")
        elif choice == 4:
            extract_unique_words(analytext)
            print("Text Analysis Options:\n1. Word Count\n2. Longest Word\n3. Count of Substring\n4. Unique Words\n5. Exit")
        else:
            print("Thank you for using the Text Processing Program!")
            break


main()
