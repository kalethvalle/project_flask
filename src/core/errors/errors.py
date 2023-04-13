class InvalidEntity(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class EntityNotFound(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

