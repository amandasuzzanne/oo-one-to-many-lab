class Owner:
    def __init__(self, name) -> None:
        self.name = name
        pass

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception(f"{pet} is not a Pet")
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    
    pass

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all =[]
    def __init__(self, name, pet_type, owner=None) -> None:
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception(f"{pet_type} is not a valid pet type")
        self.name = name
        self.owner = owner
        self.all.append(self)
      