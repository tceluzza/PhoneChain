class PhoneTreeHandler:
    _next = None

    def next_handler(self, next_handler):
        self._next = next_handler

    def dial(self, extention: int):
        pass

class PressedOneHandler(PhoneTreeHandler):
    # def __init__(self, next_handler: PhoneTreeHandler):
    #     self._next = next_handler

    def dial(self, extension: int):
        if (extension == 1):
            print("Connecting you to the on-duty supervisor")
        else:
            self._next.dial(extension)

class PressedTwoHandler(PhoneTreeHandler):
    # def __init__(self, next_handler: PhoneTreeHandler):
    #     self._next = next_handler

    def dial(self, extension: int):
        if (extension == 2):
            print("Connecting you to the Captain")
        else:
            self._next.dial(extension)
            
class PressedThreeHandler(PhoneTreeHandler):
    # def __init__(self, next_handler: PhoneTreeHandler):
    #     self._next = next_handler

    def dial(self, extension: int):
        if (extension == 3):
            print("Connecting you to the First Lieutenant")
        else:
            self._next.dial(extension)

class PressedFourHandler(PhoneTreeHandler):
    # def __init__(self, next_handler: PhoneTreeHandler):
    #     self._next = next_handler

    def dial(self, extension: int):
        if (extension == 4):
            print("Connecting you to the Second Lieutenant")
        else:
            self._next.dial(extension)

class ElseHandler(PhoneTreeHandler):
    def dial(self, extension: int):
        print("You did not enter a valid option. Goodbye!")
        
class PhoneTree:
    chain = None

    def __init__(self):
        two = PressedTwoHandler()
        three = PressedThreeHandler()
        four = PressedFourHandler()
        els = ElseHandler()

        # self.chain = PressedOneHandler(PressedTwoHandler(PressedThreeHandler(PressedFourHandler(ElseHandler()))))
        self.chain = PressedOneHandler()
        self.chain.next_handler(two)
        two.next_handler(three)
        three.next_handler(four)
        four.next_handler(els)


def print_tree_menu():
    print("Thank you for call RPI Ambulance.")
    print("To be connected to an on-duty supervisor, press 1.")
    print("To be connected to the Captain, press 2.")
    print("To be connected to the First Lieutenant, press 3.")
    print("To be connected to the Second Lieutenant, press 4.")

if __name__ == "__main__":
    tree = PhoneTree()
    
    print_tree_menu()
    
    ext = input("Dial: ")
    if (ext.isnumeric()):
        tree.chain.dial(int(ext))