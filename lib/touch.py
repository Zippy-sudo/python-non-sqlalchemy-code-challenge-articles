class Author:
    def __init__(self, name = None):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name and isinstance(name, str):
            self._name = name

