from random import shuffle
print('Welcome to the Magical Quiz of Disney!')
print("Let's see how well you know Disney movies :)")
print('Good Luck and May the Odds Be Ever in your Favor!')

with open("TriviaQuestions.txt") as a:
    lines = a.readlines()

shuffle(lines)
right = 0
wrong = []

numberQuest = int(input("Are you up for answering 100 questions about Disney movies? If so type 100 and if not how many questions would you like to answer?"))

for l in lines[:numberQuest]:
    question, rightAns = l.strip().split("\t")
    answer = raw_input(question + ' ')
    if answer.lower() == rightAns.lower():
        print('Correct, you are so awesome!')
        right += 1
    else:
        print('Ha Ha Ha you got it wrong Chump!: the answer is %s.' % rightAns)
        wrong.append(question)

print('You got %d right! Woohoo!' % (right))

if(wrong):
    print('You got the following wrong:')
    for w in wrong:
        print(w)

print "Thanks for playing Beautiful Person!"
print "Hope you have a nice day!"
