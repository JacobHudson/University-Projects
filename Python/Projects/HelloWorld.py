# def RemoveDuplicateWords(s):
#     return set(s.split())

# print(RemoveDuplicateWords("Hello World Hello World"))

######

# import random

# sizes = ["tiny", "minuscule", "puny", "undersized", "microscopic", "scanty", "meagre", "diminutive", "paltry", "insignificant"]
# quantities = ["insufficient", "scarce", "sparse", "limited", "deficient", "inadequate", "paltry", "negligible", "depleted", "lacking", "diminished", "minimal", "short", "restricted"]
# qualities = ["arrogant", "callous", "deceitful", "greedy", "hostile", "lazy", "obnoxious", "rude", "selfish", "vindictive"]
# ages = ["decrepit", "senile", "doddering", "over-the-hill", "ancient", "geriatric", "past-it", "old-fashioned", "fossilized", "wizened"]
# shapes = ["bulky", "clunky", "crooked", "lopsided", "misshapen", "stubby", "twisted", "warped", "awkward", "bent"]
# colors = ["dull", "drab", "muddy", "bleak", "harsh", "washed-out", "garish", "brash", "loud", "somber"]

# def GenerateInsults(noun):
#     return f"You {random.choice(sizes)} {random.choice(quantities)} {random.choice(qualities)} {noun}! You're as {random.choice(ages)} as a {random.choice(shapes)} {random.choice(colors)}!"

# print(GenerateInsults(input("Enter a noun: ")))

######

class Shape:
    def beats(self, other):
        raise NotImplementedError("This method should be overridden by subclasses")

class Rock(Shape):
    def beats(self, other):
        return isinstance(other, Scissors)

class Paper(Shape):
    def beats(self, other):
        return isinstance(other, Rock)

class Scissors(Shape):
    def beats(self, other):
        return isinstance(other, Paper)

class ComputerPlayer:
    def ChooseShape(self):
        import random
        return random.choice([Rock(), Paper(), Scissors()])

comp = ComputerPlayer()
while True:
    comp_shape = comp.ChooseShape()

    user_shape = input("Rock, Paper, Scissors? ")
    if user_shape == "Rock":
        user_shape = Rock()
    elif user_shape == "Paper":
        user_shape = Paper()
    elif user_shape == "Scissors":
        user_shape = Scissors()
    else:
        print("Invalid input")
        continue

    print(f"Computer chose {comp_shape.__class__.__name__}")
    if user_shape.beats(comp_shape):
        print("You win!")
    else:
        print("You lose!")
