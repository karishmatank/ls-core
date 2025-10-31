import math

# Q1
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
    
    def __str__(self):
        return f"{self.color.title()} {self.year} {self.model}"
    
    def __repr__(self):
        return f"Car({repr(self.model)}, {self.year}, {repr(self.color)})"
    
vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)
print(repr(vwbuzz))


# Q2
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)
    
    # __iadd__ omitted as we don't need for this exercise

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        
        return (self.x * other.x) + (self.y * other.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        x = repr(self.x)
        y = repr(self.y)
        return f"Vector({x}, {y})"

v1 = Vector(5, 12)
v2 = Vector(13, -4)
print(v1 + v2) # Vector(18, 8)

# New
print(v1 - v2) # Vector(-8, 16)
print(v1 * v2) # 17
print(abs(v1))

# Q3
class Candidate:
    def __init__(self, full_name):
        self.full_name = full_name
        self.votes = 0
    
    def __iadd__(self, count):
        if not isinstance(count, int):
            return NotImplemented
        
        self.votes += count
        return self

class Election:
    def __init__(self, candidates):
        self.candidates = candidates

    def _print_votes(self):
        for candidate in self.candidates:
            print(f"{candidate.full_name}: {candidate.votes} votes")

    def _get_winner(self):
        winner = None
        for candidate in self.candidates:
            if not winner or candidate.votes > winner.votes:
                winner = candidate
        return winner

    def results(self):
        self._print_votes()
        winner = self._get_winner()
        total_votes = sum([candidate.votes for candidate in self.candidates])
        pct_votes = winner.votes / total_votes
        print(f"{winner.full_name} won: {pct_votes:.1%} of votes")


mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()