class PhoneTreeHandler:
    # an interface to be implemented by each concrete handler
    
    _next = None

    def set_next_handler(self, next_handler):
        self._next = next_handler

    def dial(self, extention: int):
        pass

# Now, we implement each of the concrete handlers for the chain
class PressedOneHandler(PhoneTreeHandler):
    def dial(self, extension: int):
        if (extension == 1):
            print("Connecting you to the on-duty supervisor")
        else:
            self._next.dial(extension)

class PressedTwoHandler(PhoneTreeHandler):
    def dial(self, extension: int):
        if (extension == 2):
            print("Connecting you to the Captain")
        else:
            self._next.dial(extension)
            
class PressedThreeHandler(PhoneTreeHandler):
    def dial(self, extension: int):
        if (extension == 3):
            print("Connecting you to the First Lieutenant")
        else:
            self._next.dial(extension)

class PressedFourHandler(PhoneTreeHandler):
    def dial(self, extension: int):
        if (extension == 4):
            print("Connecting you to the Second Lieutenant")
        else:
            self._next.dial(extension)

class ElseHandler(PhoneTreeHandler):
    def dial(self, extension: int):
        print("You did not enter a valid option. Goodbye!")
        
class PhoneTree:
    # the Chain of Responsibility is essentially a linked list
    # for this implementation. Each concrete handler points to
    # another concrete handler as the next link in the chain.
    # The chain itself points to the first link in the chain,
    # the first step in the 
    responsibility_chain = None

    def __init__(self):
        # initialize all of the concrete handlers
        one_handler = PressedOneHandler()
        two_handler = PressedTwoHandler()
        three_handler = PressedThreeHandler()
        four_handler = PressedFourHandler()
        other_handler = ElseHandler()
        
        # create the links (building the chain)
        one_handler.set_next_handler(two_handler)
        two_handler.set_next_handler(three_handler)
        three_handler.set_next_handler(four_handler)
        four_handler.set_next_handler(other_handler)
        
        self.responsibility_chain = PressedOneHandler()

### DEMONSTRATION CODE ###

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