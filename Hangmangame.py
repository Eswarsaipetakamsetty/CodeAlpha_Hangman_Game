import random
def hangman(chances):
    if chances==5:
        x='''-----|
             |    |
             |   ( )
             |   /|\
             |   / \
             |        '''
    elif chances==4:
        x = '''-----|
               |    |
               |   ( )
               |   /|\
               |   / 
               |        '''
    elif chances==3:
        x = '''-----|
               |    |
               |   ( )
               |   /|\
               |   
               |        '''
    elif chances==2:
        x = '''-----|
               |    |
               |   ( )
               |   /|
               |   
               |        '''
    elif chances==1:
        x = '''-----|
               |    |
               |   ( )
               |    |
               |   
               |        '''
    elif chances==0:
        x = '''-----|
               |    |
               |   ( )
               |   
               |   
               |        '''
    return x

name = input("What is your name? ")
print("Good Luck ! ", name)
words = ['Python','Java','Numpy','Pandas','Kotlin','Django','Tensorflow','Programming']
word = random.choice(words)
print("----------This Quiz is about different Programming languages----------")
print("Guess the characters")
guesses = ''
turns = 5
while turns > 0:
    failed = 0
    for char in word.lower():
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
    print()
    guess = input("guess a character:")
    guesses += guess
    if guess not in word.lower():
        turns -= 1
        print("Wrong")
        print(hangman(turns))
        print("You have", + turns, 'more guesses')
        if turns == 0:
            print("You Loose")