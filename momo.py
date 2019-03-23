from creature import Human, Animal, Oni


class Party:
    member = []

    def __init__(self, master, target, kibi):
        self.target = Oni(target)
        master = Human(master)
        master.IsMaster = True
        self.member.append(master)
        self.kibi = kibi

    def addmember(self, animals):
        for animal in animals:
            self.member.append(Animal(animal))
            self.kibi += -1


p = Party(master='momotaro', target='oni', kibi=7)
p.addmember(['inu', 'saru', 'kiji', ])
print(p.kibi)  # 4

# print('target:' + p.target.typename)
#
# cnt = 1
# member = ''
# for s in p.member:
#     member = s.gettype()
#     if hasattr(s, 'IsBoss'):
#         if getattr(s, 'IsBoss'):
#             member += ' [*]'
#             boss = s.gettype()
#
#     print('member' + str(cnt) + ':' + member)
#     cnt += 1
#
# print('kibidango remained:' + str(p.kibi))  # 4
