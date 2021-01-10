from time import sleep
from win10toast import ToastNotifier
toaster = ToastNotifier()
print("**********   WELCOME TO PYTHON DATA STRUCTURE IMPLEMENTATION   ********** ")
print("*********************    STACKS AND QUEUES   ***************************")
print("\n")


# Data Structure as Python list
STACKS = []
QUEUES = []


class Stacks():
    '''Class for stack implementation'''

    def push(self, element):
        print("Pushing element......")
        sleep(1)
        STACKS.append(element)
        print(f"{element} added into STACK")
        toaster.show_toast(
            "STACKS",
            f"{element} added",
            duration=4
        )

    def pop(self):
        if len(STACKS) == 0:
            print("STACK is empty. Hence cannot further delete")
        else:
            print("Deleting element.......")
            deleted = STACKS.pop()
            print(f"Deleted element is {deleted}")
            toaster.show_toast(
                "STACKS",
                f"{deleted} deleted",
                duration=4
            )

    def display(self):
        if len(STACKS) == 0:
            print("STACK is empty")
        else:
            print("Displaying from top to bottom")
            sleep(1)
            for i in range(len(STACKS)-1, -1, -1):
                sleep(0.5)
                print(STACKS[i])

    def top(self):
        if len(STACKS) == 0:
            print("STACK is empty")
        else:
            topElement = STACKS[-1]
            print(f"Top element is {topElement}")
            toaster.show_toast(
                "STACKS",
                f"{topElement} is on the top",
                duration=4
            )

    def size(self):
        print(f"Size of STACK is {len(STACKS)}")
        toaster.show_toast(
            "STACKS",
            f"{len(STACKS)} is the lenght of Stack",
            duration=4
        )


class Queue():
    ''' Class for queue implementation '''

    def push(self, element):
        print("Pushing element......")
        sleep(1)
        QUEUES.append(element)
        print(f"{element} added into QUEUES")
        toaster.show_toast(
            "QUEUE",
            f"{element} Added",
            duration=4
        )

    def pop(self):
        if len(STACKS) == 0:
            print("QUEUE is empty. Hence cannot further delete")
        else:
            print("Deleting element.......")
            sleep(1)
            deleted = STACKS.pop(0)
            print(f"Deleted element is {deleted}")
            toaster.show_toast(
                "QUEUES",
                f"{deleted} Deleted",
                duration=4
            )

    def display(self):
        if len(QUEUES) == 0:
            print("QUEUE is empty")
        else:
            sleep(1)
            for i in range(0, len(QUEUES)):
                sleep(0.5)
                print(QUEUES[i])

    def top(self):
        if len(QUEUES) == 0:
            print("QUEUE is empty")
        else:
            topElement = QUEUES[-1]
            print(f"Top element is {topElement}")
            toaster.show_toast(
                "QUEUE",
                f"{topElement} is top element",
                duration=4
            )

    def firstElement(self):
        if len(QUEUES) == 0:
            print("QUEUE is empty")
        else:
            firstElement = QUEUES[0]
            print(f"First element is {firstElement}")
            toaster.show_toast(
                "QUEUES",
                f"{firstElement} is first element",
                duration=4
            )

    def size(self):
        print(f"Size of STACK is {len(QUEUES)}")
        toaster.show_toast(
            "QUEUES",
            f"{len(QUEUES)} is the size",
            duration=4
        )


class MenuFunctions():
    ''' Class for all menus box used in this program '''

    def stackMenu(self):
        print("Enter 1 : Push in STACK")
        print("Enter 2 : POP in STACK")
        print("Enter 3 : Display STACK")
        print("Enter 4 : Get Top element of STACK")
        print("Enter 5 : Get Size of STACK")
        print("Any digit to exit")

    def queueMenu(self):
        print("Enter 1 : Push in QUEUE")
        print("Enter 2 : POP in QUEUE")
        print("Enter 3 : Display QUEUE")
        print("Enter 4 : Get Top element of QUEUE")
        print("Enter 5 : Get first element")
        print("Enter 6 : Get Size of QUEUE")
        print("Any digit to exit")

    def mainMenu(self):
        print("Enter 1 : STACKS")
        print("Enter 2 : QUEUES")
        print("Any key to exit")


def stack():
    '''Stack driver function'''

    toaster.show_toast(
        "STACKS",
        "Stack Data Structure selected",
        duration=4
    )
    menuObject = MenuFunctions()
    while True:
        menuObject.stackMenu()
        try:
            choice = int(input("Your choice : "))
            obj = Stacks()
            if choice == 1:
                element = input("Enter element to be pushed : ")
                print(f"Pushing {element} in STACK")
                sleep(1)
                obj.push(element=element)

            elif choice == 2:
                obj.pop()
            elif choice == 3:
                obj.display()
            elif choice == 4:
                obj.top()
            elif choice == 5:
                obj.size()
            else:
                toaster.show_toast(
                    "Python",
                    "Exiting.....",
                    duration=4
                )
                break

        except:
            print("Something went wrong")
            toaster.show_toast(
                "Error",
                "Something went wrong",
                duration=4
            )


def queue():
    '''Queue driver function'''

    toaster.show_toast(
        "QUEUES",
        "Queue Data Structure selected",
        duration=4
    )
    menuObject = MenuFunctions()
    while True:
        menuObject.queueMenu()
        try:
            choice = int(input("Your choice : "))
            obj = Queue()
            if choice == 1:
                element = input("Enter element to be pushed : ")
                print(f"Pushing {element} in QUEUE")
                sleep(1)
                obj.push(element=element)

            elif choice == 2:
                obj.pop()
            elif choice == 3:
                obj.display()
            elif choice == 4:
                obj.top()
            elif choice == 5:
                obj.firstElement()
            elif choice == 6:
                obj.size()
            else:
                toaster.show_toast(
                    "Python",
                    "Exiting.....",
                    duration=4
                )
                break
        except:
            print("Something went wrong")
            toaster.show_toast(
                "Error",
                "Something went wrong",
                duration=4
            )


''' Driver function All execution of the code starts from here '''
if __name__ == "__main__":
    menuObject = MenuFunctions()
    menuObject.mainMenu()
    try:
        choice = int(input("Your choice : "))
    except:
        print("Something went wrong :-(")
        print("Try again")
        exit(0)

    if choice == 1:
        stack()
    elif choice == 2:
        queue()
    else:
        print("Exiting......")
        sleep(1)
        print("Thank you for using my software ..........")
        toaster.show_toast(
            "Python",
            "Thank you for using me",
            duration=4
        )
        exit(0)

# Clearing stacks and queue data
STACKS.clear()
QUEUES.clear()