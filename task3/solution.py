class Person(object):

    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self._siblings_observers = []
        self.successors = set()
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.father = father
        self.mother = mother
        if mother is not None:
            self._siblings_observers.append(mother.children)
            mother.successors.add(self)
        if father is not None:
            self._siblings_observers.append(father.children)
            father.successors.add(self)

    def get_brothers(self):
        brothers = set()
        for observer in self._siblings_observers:
            brothers.update(observer("M"))
        brothers.discard(self)
        return list(brothers)

    def get_sisters(self):
        sisters = set()
        for observer in self._siblings_observers:
            sisters.update(observer("F"))
        sisters.discard(self)
        return list(sisters)

    def children(self, gender="both"):
        if gender == "both":
            return list(self.successors)
        else:
            return list(filter(lambda child: child.gender == gender,
                               list(self.successors)))

    def is_direct_successor(self, other):
        return other in self.successors or self in other.successors
