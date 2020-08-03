import random


class Numeron:
    def __init__(self):
        self.answer = random.randrange(1, 10, 1)
        self.times_tried = 0
        self.limit_of_try = 3

    def set_number(self):
        self.answer = random.randrange(1, 10, 1)

    def reset_data(self):
        self.set_number()
        self.times_tried = 0

    def start(self):
        player = input("Tell us your name: ")
        print("Hi "+player+", welcome to the game")
        print("It's a game of guessing a number from 1 to 10. You can try up to 3 times. Let's begin")
        while self.times_tried < self.limit_of_try:
            while True:
                num = input("Enter a number from 1 to 10: ")
                try:
                    int(num)
                    break
                except ValueError:
                    print("Input number!!!")
            if int(num) == self.answer:
                print("Correct! You won!")
                break
            else:
                self.times_tried += 1
                if self.limit_of_try-self.times_tried == 0:
                    print("Wrong... GamerOver... The number was "+str(self.answer))
                else:
                    print("Wrong, you have "+str(self.limit_of_try-self.times_tried)+" times left")
        result = input("Do you want to play again? y/n: ")
        if result == 'y':
            self.reset_data()
            self.start()
        else:
            print("bye")


game = Numeron()
answer = input("Do you wanna have fun with us? y/n: ")
if answer == 'y':
    game.start()
else:
    print("Perras putas")
