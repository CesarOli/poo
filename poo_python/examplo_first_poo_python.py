class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Wolf(Animal):
    def speak(self):
        return f'{self.name} AUUUU!'
    

class Snake(Animal):
    def speak(self):
        return f'{self.name} Ssssiiii!'
    

wolf = Wolf('O Mal!!')
snake = Snake('A Celeste')

print(wolf.speak())
print(snake.speak())

