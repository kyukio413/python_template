def hello(name: str, age: int) -> str:
    result1: str = "My name is " + name + ".\n"
    result2: int = "I am " + str(age) + " years old."
    return result1 + result2


result: int = 10
result = hello(name="Otao", age=23)
print(result)
