from typing import Tuple


class FastPhone(object):
    """
    Fastphone Implementaion using Trie Algorithm
    
    """

    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1
        self.mincounter = 3
        self.maxcounter = 10
        self.person = ""
        self.inputdigit = ""


def add_number(root, number: str, person: str):
    """
    Adding a super speed dialing number using the trie structure
    """
    node = root
    counter = 0
    worldlength = len(number)

    # Check specifications and handling edge cases
    try:
        # Accept phonenumbers, digits only
        if (int(number) <= 0):
            print("Invalid Number! Please check the number : ", number, person)
            return False
        # Accept phonenumbers, variable length from 3 <= digits <=10
        if (worldlength < root.mincounter) or (worldlength > root.maxcounter):
            print("Invalid Range! Please check the number : ", number, person)
            return False
    except:
        # Accept phonenumbers, positive integres only
        print("Invalid Number! Please check the number : ", number, person)
        return False

    # Add phone numbers using Trie algorithm
    for char in number:
        if counter < root.mincounter:
            found_in_child = False
            # Search for the character in the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found it, increase the counter by 1 to keep track that another
                    # word has it as well
                    child.counter += 1
                    counter += 1
                    # And point the node to the child that contains this char
                    node = child
                    found_in_child = True
                    break
            # We did not find it so add a new chlid
            if not found_in_child:
                new_node = FastPhone(char)
                node.children.append(new_node)
                # And then point node to the new child
                node = new_node
        else:
            print("Invalid Number! Trying to add unreachable number", number, person)
            return False
    # Adding the contact name
    node.person = person
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True


def dial(root, prefix: str) -> Tuple[bool, int]:
    """
    Check and return the name associated with the supre speed dial number
    """
    node = root
    root.inputdigit = root.inputdigit + prefix
    inputprefix = root.inputdigit
    if len(inputprefix) >= root.mincounter:
        # If the root node has no children, then return False.
        # Because it means we are trying to search in an empty trie
        if not root.children:
            return False, 0

        for char in inputprefix:

            char_not_found = True
            # Search through all the children of the present `node`
            for child in node.children:
                if child.char == char:
                    # We found the char existing in the child.
                    char_not_found = False
                    # Assign node as the child containing the char and break
                    node = child
                    break

            # Return False anyway when we did not find a char.
            if char_not_found:
                return "Number does not exist"
        # Well, we are here means we have found the number prefix.
        if not char_not_found:
            while child.word_finished == False:
                for child in node.children:
                    if child.word_finished:
                        root.inputdigit = ""
                        return child.person
                node = child
            root.inputdigit = ""
            return child.person
    else:
        return "None"
