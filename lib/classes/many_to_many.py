class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not hasattr(self, "title") and isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError

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
            raise ValueError

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in Article.all if article.author == self})
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len([article for article in Article.all if article.author == self]) > 0:
            return list({article.magazine.category for article in Article.all if article.author == self})

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and  2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError

    def articles(self):
        return [article for article in Article.all if article.magazine == self] 

    def contributors(self):
        return list({article.author for article in Article.all if article.magazine == self})
    
    def article_titles(self):
        if len([article for article in Article.all if article.magazine == self]) > 0:
            return [article.title for article in Article.all if article.magazine == self]

    def contributing_authors(self):
        a = {article.author for article in Article.all if article.magazine == self}
        b = [article.author for article in Article.all if article.magazine == self]
        c = []
        for element in a:
            if isinstance(element, Author) and b.count(element) > 2:
                c.append(element)

        if len(c) > 0 :
            return c
        
    @classmethod
    def top_publisher(self):

        a = []

        if len(Article.all) > 0:
            for element in Magazine.all:
                a.append(len([article for article in Article.all if article.magazine == element]))
        else:
            return None

        return Magazine.all[a.index(max(a))]