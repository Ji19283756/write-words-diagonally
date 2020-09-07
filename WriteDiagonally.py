import pyperclip


def array_to_string(array, printed_string=""):
    for thing in array:
        printed_string += thing
    return printed_string


def make_array(message, width=12, height=19, spaces=2):
    def array_to_string_and_add_spaces_and_make_all_equal_length(array, printed_string="", spaces=2, width=12):
        # VVVV makes a string with a certain amount of spaces based on the value of space
        spaces = "".join(" " for x in range(spaces))

        # VVVV  turns each string in the array into a list
        array_with_strings_to_arrays = [list(string) for string in array if len(string)>0]

        # VVVV  adds a space to each of the letters, the amount of spaces is determined my space
        array_with_strings_to_arrays_and_spaces = \
            [[letter + spaces for letter in mini_array] for mini_array in array_with_strings_to_arrays]

        for line in array_with_strings_to_arrays_and_spaces:
            while len(line) < width:
                line += [spaces + " "]
            line+=["\n"]

        # _______________________________________________________________________________________________________

        for line in array_with_strings_to_arrays_and_spaces:
            for letter in line:
                printed_string += letter

        return printed_string

    if height<0 or width<0 or spaces<0:
        print("Nah")
        return

    message = list(message)
    return_array = ["" for x in range(height)]
    increment = 0

    # vvv while the last array index is not filled and words in the message sill havent been added
    while len(return_array[height - 1]) < width and len(message) > 0:
        current = increment  # the current array index

        # vvv whiel the index is bigger than -1, the current index isnt bigger than the width, and theres
        # still letters to add
        while current >= 0 and len(return_array[current]) < width and len(message) > 0:
            return_array[current] += message[0]
            message.pop(0)
            current -= 1  # everytime a letter is added, the index gets lower to move to the one below
        increment += increment < (height - 1)  # insures that the array index isnt more than the length of

    return_array = \
        array_to_string_and_add_spaces_and_make_all_equal_length(return_array, spaces=spaces, width=width)
    return return_array


def revert_message(message, spaces=2, final_message="", increment=0):
    def remove_spaces(message, spaces, current=0):
        double_array = [[] for x in range(len(message))]

        # this adds the letters from message to double_array then removes the letter spaces
        # the number of spaces removed is determined by the spaces parameter
        for mini_array in message:
            while len(mini_array) > 0:
                double_array[current] += [mini_array[0]]
                for x in range(spaces + 1):
                    if len(mini_array) > 0:
                        mini_array.pop(0)
            current += 1

        return double_array

    if message==None or spaces<0:
        print("Please but a number of spaces that is acceptable")
        return

    message=message.split("\n")
    message_array=[list(line) for line in message if len(line)!=0]

    # VVVV  removes the spaces that were added for visual purposes
    message_array = remove_spaces(message_array, spaces=spaces)

    # VVVV finds the array position of the last letter in the message, this is needed as the letters
    # in the correct order, this is done by seeing if consecutive array indexes are the same length
    current = -1
    if len(message_array) > 1:
        for x in range(-1, -len(message_array) - 1, -1):
            if len(message_array[x]) == len(message_array[x - 1]):
                increment = message_array.index(message_array[x])
                break

    # VVVV shaves off the extra words until the word becomes a diagonal, This is done as when
    # we found out which indexes have the same length, we know how many times we have to shave
    # we then add it to the final message and remove it from the array, then if we can we move to the next
    # array if not, the while loop ends and then the starting array index changes
    for x in range(increment, 0, -1):
        thing = x
        while True:
            try:
                final_message += message_array[thing][-1]
                message_array[thing].pop(-1)
                thing += 1
            except:
                break

    mini_array = 0

    # VVVV calculation to improve readability
    first_index_is_filled = len(message_array[0]) > 0

    # VVVV take the remaining words from message_array and then adds them to final message
    # and removes it from message_array

    while first_index_is_filled:

        # VVVV calculation to improve readability
        the_current_line_length_is_greater_than_zero = len(message_array[mini_array]) > 0

        if the_current_line_length_is_greater_than_zero:

            # VVVV first this will get the last letter of the message and add it to final message
            # it will then remove it from the array and move on to the next array index
            final_message += message_array[mini_array][-1]
            message_array[mini_array].pop(-1)
            mini_array += 1

            # VVVV insures that increment is never longer than the message, as to not go to an index that
            # doesn't exist
            mini_array %= (len(message_array))
        else:

            # if the current index position is unfilled, then it will resart at index position 0
            mini_array = 0

        # VVVV calculation to improve readability
        first_index_is_filled = len(message_array[0]) > 0

    # VVVV because the words are added in backwards order, this will reverse it and turn it into a string
    final_message=final_message[::-1].strip()

    return final_message


# OPTIONS:______________________________________________________________________________________________

message = "somebody once told me the world was going to roll me i aint the sharpest tool in the shed"

width = 12

height = 19

spaces = 2

copy_to_clipboard = False

# ______________________________________________________________________________________________________

diagonal_message = make_array(message, width=width, height=height, spaces=spaces)

print(diagonal_message)

undiagonaled_message = revert_message(diagonal_message, spaces=spaces)

print(undiagonaled_message)

if copy_to_clipboard:
    pyperclip.copy(diagonal_message)
