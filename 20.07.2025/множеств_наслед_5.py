class Parent1:
    def say(self):
        print("Hello from Parent1")

class Parent2:
    def sleep(self):
        print("Zzzz")

    def say(self):
        print("Hello from Parent2")


class Child(Parent1, Parent2):
    pass

c = Child()

c.say()
c.sleep()
