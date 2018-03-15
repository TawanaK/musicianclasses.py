class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician):
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bop", "Boom", "Bow"])
        
    def count(self, to = 4):
        for count in range(1, to+1):
            print(count)
            
    def spontaneously_combust(self):
        print ("spontaneously combust")

class Band(Musician):
    def __init__(self):
        
        
        if members == None:
            self.members = []
        else:
            self.members = members
            
    def hire(self,person):
        members.append(person)
        
    def fire(self, person):
        for member in self.members:
            if member == person:
                self.members.remove(person)
            
    def play(self):
        for member in self.members:
            if isinstance(member, Drummer):
                member.count()
                
        for member in self.members:
            member.solo()
                
                
            