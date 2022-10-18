import time
from termcolor import colored

print(colored("********** Welcome to the WPM calculator **********", "blue"))
print(colored("""DIRECTIONS: 
There are 3 levels in this typing game, complete all of them, and check your score, and the time it took you to type the sentence.""", 'green'))
print()
print(colored("Press 1 to start the game", 'red'))

if input() == "1":
    score = 0
    print("Level 1")
    print("Type the sentence below")
    print("The quick brown fox jumps over the lazy dog")
    start = time.time()
    sentence = input()
    end = time.time()
    if sentence == "The quick brown fox jumps over the lazy dog":
        score = score + 1
        print("Correct")
        print("Time: ", end - start)
        print("Level 2")
        print("Type the sentence below")
        print("")
        print("Pack my box with five dozen")
        start = time.time()
        sentence = input()
        end = time.time()
        if sentence == "Pack my box with five dozen":
            score = score + 1
            print("Correct")
            print("Time: ", end - start)
            print("Level 3")
            print("Type the sentence below")
            print("")
            print("How vexingly quick daft zebras jump")
            start = time.time()
            sentence = input()
            end = time.time()
            if sentence == "How vexingly quick daft zebras jump":
                score = score + 1
                print("Correct")
                print("Time: ", end - start)
                print("Your score is: ", score)
                print("Your WPM is: ", score / (end - start) * 60)
            else:
                print("Incorrect")
else:
    print("Invalid input")
