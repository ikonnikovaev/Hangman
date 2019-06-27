import random
import string 

def play():
    words = ["python", "java", "kotlin", "javascript"]
    remaining_attempts = 8

    target = random.choice(words)
    hint = ["-"] * (len(target))
    used_letters = []

    while (remaining_attempts > 0):
        print()
        opened = ''.join(hint)
        print(opened)
        if (opened == target):
            print("You guessed the word " + target + "!")
            print("You survived!")
            break
    
        user_input = input("Input a letter: ").strip()
        if (len(user_input) != 1):
            print("You should print a single letter")
            continue
    
        ch = user_input[0]
        if not (ch in string.ascii_lowercase):
            print("It is not an ASCII lowercase letter")
            continue    

        if (ch in used_letters):
            print("You already typed this letter")
            continue        
    
        found = False
        used_letters.append(ch)

        for i in range(0, len(target)):        
            if (target[i] == ch):
                found = True
                if (hint[i] == "-"):
                    hint[i] = ch
                            
        if (not found):
            print("No such letter in the word")
            remaining_attempts -= 1    
        
        if (remaining_attempts == 0):
            print("You are hanged!")



print("H A N G M A N")
action = input('Type "play" to play the game, "exit" to quit: ').strip()
while not (action in ['play', 'exit']):
    action = input('Type "play" to play the game, "exit" to quit: ').strip()
if (action == 'play'):
    play()


    
        

'''
print("Thanks for playing!")
print("We'll see how well you did in the next stage")'''


'''hint = target[:3] + ("-" * (len(target) - 3))
if (input("Guess the word " + hint + ":").strip() == target):
    print("You survived!")
else:
    print("You are hanged!")'''

