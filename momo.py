from creature import Human, Animal, Oni


class Team:
    member = []
    kibi = 0

    def __init__(self, target, boss, kibi):
        self.target = Oni(target)
        boss = Human(boss)
        boss.IsBoss = True
        self.member.append(boss)
        self.kibi = kibi

    def addmember(self, animals):
        for animal in animals:
            self.member.append(Animal(animal))
            self.kibi += -1


team = Team(target='oni', boss='momotaro', kibi=7)
team.addmember(['inu', 'saru', 'kiji', ])
print('target:' + team.target.typename)

cnt = 0
member = ''
for s in team.member:
    cnt += 1
    member = s.gettype()
    if hasattr(s, 'IsBoss'):
        if getattr(s, 'IsBoss'):
            member += ' [*]'
            boss = s.gettype()

    print('member' + str(cnt) + ':' + member)

print('kibidango remained:' + str(team.kibi))  # 4
