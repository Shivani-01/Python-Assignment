import random
class Coin:
    def __init__(self):
        self.up='Head'
    def toss(self):
        if random.randint(0,1):
            self.up='Tails'
    def get_side(self):
        return self.up
def main():
    a=Coin()
    print(a.up)
    print("Coin tossed")
    a.toss()
    print(a.up)

main()

