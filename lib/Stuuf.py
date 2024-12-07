import ipdb
class Author:
    def __init__(self, name = None):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not hasattr(self, "_name") and isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            print("Hmmm")

ipdb.set_trace()
