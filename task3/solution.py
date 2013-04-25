class Person(object):

    def __init__(self, name, birth_year, gender, father=None, mother=None):
        self.__siblings_observers = []
        self.successors = []
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.father = father
        self.mother = mother
        if mother is not None:
            self.__siblings_observers.append(mother.children)
            mother.successors.append(self)
        if father is not None:
            self.__siblings_observers.append(father.children)
            father.successors.append(self)

    def get_brothers(self):
        return self.__get_my_siblings("M")

    def get_sisters(self):
        return self.__get_my_siblings("F")

    def __get_my_siblings(self, gender):
        siblings = set()
        for observer in self.__siblings_observers:
            siblings.update(observer(gender))
        siblings.discard(self)
        return list(siblings)

    def children(self, gender="both"):
        if gender == "both":
            return self.successors
        else:
            return [child for child in self.successors if child.gender == gender]

    def is_direct_successor(self, other):
        return other in self.successors or self in other.successors
