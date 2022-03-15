list = ['A', 'E', 'I', 'O', 'U']

user_word = input("Input a word: ")
user_word = user_word.upper()

for letter in user_word:

    if letter in list:
        continue
    print(letter)B