class Pet:
    def __init__(self, species, name):
        self._species = species
        self._name = name
    
    @property
    def info(self):
        return f"a {self._species} named {self._name}"
    
class Owner:
    def __init__(self, name):
        self._name = name
        self._pets = []
    
    @property
    def name(self):
        return self._name
    
    def adopt(self, pet):
        self._pets.append(pet)
        
    def print_pets(self):
        for pet in self._pets:
            print(pet.info)
        
    def number_of_pets(self):
        return len(self._pets)

class Shelter:
    def __init__(self):
        self._adopters = set()
    
    def adopt(self, owner, pet):
        self._adopters.add(owner)
        owner.adopt(pet)
    
    def print_adoptions(self):
        for adopter in self._adopters:
            print(f"{adopter.name} has adopted the following pets:")
            adopter.print_pets()
            print()

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")


# Further exploration:
class Pet:
    def __init__(self, species, name):
        self._species = species
        self._name = name
    
    @property
    def info(self):
        return f"a {self._species} named {self._name}"
    
class Owner:
    def __init__(self, name):
        self._name = name
        self._pets = []
    
    @property
    def name(self):
        return self._name
    
    def adopt(self, pet):
        self._pets.append(pet)
        
    def print_pets(self):
        for pet in self._pets:
            print(pet.info)
        
    def number_of_pets(self):
        return len(self._pets)

class Shelter:
    def __init__(self, pets):
        self._unadopted_pets = pets
        self._adopters = set()
    
    def adopt(self, owner, pet):
        self._adopters.add(owner)
        owner.adopt(pet)
        self._unadopted_pets.remove(pet)
    
    def print_adoptions(self):
        for adopter in self._adopters:
            print(f"{adopter.name} has adopted the following pets:")
            adopter.print_pets()
            print()
    
    def print_unadopted_pets(self):
        print(f"The shelter has the following unadopted pets:")
        for pet in self._unadopted_pets:
            print(pet.info)
        print()
    
    def number_of_unadopted_pets(self):
        return len(self._unadopted_pets)

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')
asta = Pet('dog', 'Asta')
laddie = Pet('dog', 'Laddie')
fluffy = Pet('cat', 'Fluffy')
kat = Pet('cat', 'Kat')
ben = Pet('cat', 'Ben')
chatterbox = Pet('parakeet', 'Chatterbox')
bluebell = Pet('parakeet', 'Bluebell')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter([
    cocoa,
    cheddar,
    darwin,
    kennedy,
    sweetie,
    molly,
    chester,
    asta,
    laddie,
    fluffy,
    kat,
    ben,
    chatterbox,
    bluebell
])

shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
shelter.print_unadopted_pets()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
print(f"The Animal shelter has {shelter.number_of_unadopted_pets()} unadopted pets.")
                