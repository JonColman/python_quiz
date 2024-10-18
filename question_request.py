CATEGORY_NUMBERS = {'general knowledge': 9,
                    'entertainment: books': 10,
                    'entertainment: film': 11,
                    'entertainment: music': 12,
                    'entertainment: musicals & theatre': 13,
                    'entertainment: television': 14,
                    'entertainment: video games': 15,
                    'entertainment: board games': 16,
                    'science & nature': 17,
                    'science: computers': 18,
                    'science: mathematics': 19,
                    'mythology': 20,
                    'sports': 21,
                    'geography': 22,
                    'history': 23,
                    'art': 25,
                    'politics': 24,
                    'celebrities': 26,
                    'animals': 27,
                    'vehicles': 28,
                    'entertainment: comics': 29,
                    'science: gadgets': 30,
                    'entertainment: japanese anime & manga': 31,
                    'entertainment: cartoons & animations': 32,
}

class BaseRequest:
    def __str__(self):
        return f"https://opentdb.com/api.php?"

class AttributeRequest:
    def __init__(self, base, attribute, value):
        self.base = base
        self.attribute = attribute
        self.value = value

    def __str__(self):
        return f"{str(self.base)}&{self.attribute}={self.value}"

#Decorator Class
class SizeRequest(AttributeRequest):
    def __init__(self, base, size):
        super().__init__(base, 'amount', size)

#Decorator Class
class DifficultyRequest(AttributeRequest):
    def __init__(self, base, difficulty):
        super().__init__(base, 'difficulty', difficulty)

#Decorator Class
class TypeRequest(AttributeRequest):
    def __init__(self, base, type):
        super().__init__(base, 'type', type)

#Decorator Class
class CategoryRequest(AttributeRequest):
    def __init__(self, base, category: int):
        super().__init__(base, 'category', category)

    def __init__(self, base, category: str):
        super().__init__(base, 'category', CATEGORY_NUMBERS[category])