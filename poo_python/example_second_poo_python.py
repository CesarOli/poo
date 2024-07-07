class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eating(self):
        print(f'{self} está se alimentando')

    def speaking(self):
        pass


class Wolf(Animal):
    def eating(self):
        return f'{self.name} hungryyy!'

    def speaking(self):
        return f'{self.name} AUUUU!'


class Snake(Animal):
    def eating(self):
        return f'{self.name} hungryyyy'

    def speaking(self):
        return f'{self.name} Ssssiiii!'
    

wolf = Wolf('O Mal', 1)
snake = Snake('A Celest', 1)

print(wolf.speaking())
print(snake.speaking())

print(wolf.eating())
print(snake.eating())

