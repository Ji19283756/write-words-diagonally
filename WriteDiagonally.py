import pyperclip


def array_to_string(array, printed_string=""):
    for thing in array:
        printed_string += thing
    return printed_string


def make_array(message, width=12, height=19, spaces=2):
    def array_to_string_and_add_spaces_and_make_all_equal_length \
                    (array, printed_string="", spaces=2, width=12):
        # VVVV makes a string with a certain amount of spaces based on the value of space
        spaces = "".join(" " for x in range(spaces))

        # VVVV  turns each string in the array into a list
        array_with_strings_to_arrays = [list(string) for string in array]

        # VVVV  adds a space to each of the letters, the amount of spaces is determined my space
        array_with_strings_to_arrays_and_spaces = \
            [[letter + spaces for letter in mini_array] for mini_array in array_with_strings_to_arrays]

        for x in array_with_strings_to_arrays_and_spaces:
            if len(x) != 0:
                while len(x) < width:
                    x += [spaces + " "]

        # VVVV  adds a \n to each mini_array if the length of the mini_array is greater than 0
        array_with_strings_to_arrays_and_spaces_and_enters = \
            [mini_array + ["\n"] for mini_array in array_with_strings_to_arrays_and_spaces if len(mini_array) > 0]

        # _______________________________________________________________________________________________________

        for x in array_with_strings_to_arrays_and_spaces_and_enters:
            for y in x:
                printed_string += y

        return printed_string

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
        message = [list(string) for string in message]
        double_array = ["" for x in range(len(message))]

        # this adds the letters from message to double_array then removes the letter spaces
        # the number of spaces removed is determined by the spaces parameter
        for mini_array in message:
            while len(mini_array) > 0:
                double_array[current] += mini_array[0]
                for x in range(spaces + 1):
                    if len(mini_array) > 0:
                        mini_array.pop(0)
            current += 1

        # VVVV the \n causes there to be an extra "" at the end, this removes that
        if len(double_array[-1]) == 0:
            double_array.pop(-1)

        return double_array

    row_count = message.count("\n")
    message_array = ["" for row in range(row_count + 1)]
    message = list(message)

    current = 0
    # VVVV makes an array where each array index is a line of the message
    for char in message:
        if char == "\n":
            current += 1
        message_array[current] += char

    # VVVV adds an extra space to the first index, because it doesnt have a \n infront of it
    # then list comp is used to remove all \n's
    message_array[0] = " " + message_array[0]
    if spaces > 0:
        message_array = [string[1:-spaces] for string in message_array]

    else:
        message_array = [string for string in message_array]
        message_array = [list(string) for string in message_array]
        for string in message_array:
            string.pop(0)
        message_array = [array_to_string(string) for string in message_array]

    # VVVV  removes the spaces that were added for visual purposes
    message_array = remove_spaces(message_array, spaces=spaces)

    # VVVV makes the each line in the message into a list full of letters
    message_array = [list(string) for string in message_array]

    # VVVV finds the array position of the last letter in the message, this is needed as the letters
    # in the correct order, this is done by seeing if consecutive array indexes are the same length
    current = -1
    if len(message_array) > 1:
        for x in range(-1, -len(message_array) - 1, -1):
            if len(message_array[x]) == len(message_array[x - 1]):
                increment = message_array.index(message_array[x])
                break


        # VVVV not exactly sure what this is but it might've been useful
    #        current=message_array[current-1]
    # VVVV shaves off the extra words until the word becomes a diagonal, This is done as when
    # we found out which indexes have the same length, we know how many times we have to shave
    # we then add it to the final message and remove it from the array, then if we can we move to the next
    # array if not, the while loop ends and then the starting array index changes
    for x in range(increment, 0, -1):
        thing = x
        while True:
            try:
                # print(str(thing)+"thing")
                # print(message_array[thing][-1]+"sdf")
                final_message += message_array[thing][-1]
                message_array[thing].pop(-1)
                thing += 1
            except:
                break

    message_len = len(message_array)
    # VVVV calculation to improve readability
    first_index_is_filled = len(message_array[0]) > 0
    # VVVV take the remaining words from message_array and then adds them to final message
    # and removes it from message_array
    mini_array = 0

    # VVVV sometimes the code messes up if this isnt in, idk what this does but it works
    try:
        if message_array[-1][-1]==" ":
            message_array[-1].pop(-1)
    except:
        pass

    #for thing in message_array:
    #    print(thing)

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
            mini_array %= (message_len)
        else:
            # if the current index position is unfilled, then it will resart at the top
            # when this happens, the length of the index changes message length is subtracted by one
            mini_array = 0
            message_len -= 1
        # VVVV calculation to improve readability
        first_index_is_filled = len(message_array[0]) > 0

    # VVVV because the words are added in backwards order, this will reverse it and turn it into a string
    final_message = reversed(final_message)
    final_message = array_to_string(final_message)

    return final_message


# OPTIONS:______________________________________________________________________________________________

message = "Hello everyone, I hope you find this code useful"

width = 5

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
