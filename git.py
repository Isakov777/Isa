def say(word):
    def inner():
        word()
    return inner

@say
def hi():
    print("hi you")
hi()