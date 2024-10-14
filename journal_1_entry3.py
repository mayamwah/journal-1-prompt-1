#defining my name
"""
name = "Maya"
#defining fav movie
movie = "avatar"
#defining fav food
food = "birria tacos"
#write my sentence with my defining characteristics using fstring
sentence = f"My name is {name}. My favorite movie is {movie}. I love to eat {food}."
#This function will print sentence
print(sentence)

x = 2.3
y = 5.7
#code will print the sum of two floating point numbers
print(x + y)
print(type(x + y))

z = 5
t = 2
#code will the difference between two integers
print(z - t)
print(type(z - t))

#code will find the product of a floating point number and an integer
print(x * z)
print(type(x * z))"""


#code will define the function f(x) equal to x**3 + 8
def f(x):
    return x**3 + 8
#define a main function where x=9
def main():
    x = 9
    result = f(x)
    print(result)
#add a command for if result is bigger than 27
    if result > 27:
        print("YAY!")
        
if __name__=="__main__":
    main()

    
#declare a class
"""
class dog:
    def __init__(self, arms, legs, eyes, has_tail, is_furry):
        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.has_tail = has_tail
        self.is_furry = is_furry
        
    def describe(self):
        print(f"animal characterstics:")
        print(f" arm length = {self.arms} meters")
        print(f" leg length = {self.legs} meters")
        print(f" number of eyes = {self.eyes}")
        print(f" Has a tail: {'Yes' if self.has_tail else 'No'}")
        print(f" Is it furry: {'Yes' if self.is_furry else 'No'}")
              
if __name__ == "__main__":
        my_dog = dog(4, 4, 2, True, True)
              
        my_dog.describe()"""



