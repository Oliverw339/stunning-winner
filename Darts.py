
points = 50
turns = 0
score_tracker = []
print('*' * 15 +
      f'Welcome to the darts game! You start with {points} points' + '*' * 15)
while True:
    score = int(input("What did you score? "))
    mult_inp = input("Did you score a Double or a Triple? ")
    DOUBLE = ['d', 'D', 'double', 'Double']
    TRIPLE = ['t', 'T', 'Triple', 'triple']
    mult = 1
    if mult_inp in DOUBLE:
        mult = 2
    if mult_inp in TRIPLE:
        mult = 3
    total = score * mult
    score_tracker.append(total)
    points -= total
    turns += 1
    print(score)
    print(mult)
    print(total)
    print(f'You scored {total} and you have {points} points remaining.')
    if points == 0:
        if mult == 2  or mult == 3:
            avg = sum(score_tracker) / turns
            print(
                f'Congradulations! YOU WIN! It took you {turns} turns with an avg score of {avg}')
            break
        elif mult != 2 or mult != 3:
            points += total
            print("You need to end on a double or triple!")
    elif points < 0:
        print('You need to finish exactly on 0!')
        points += total
        print(f'You still have {points} points remaining')
    elif points == 1:
        print('You loose!')
        break
    
