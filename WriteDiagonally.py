import pyperclip


def make_array(message, width=12, height=19, spaces=2):
    def array_to_string_add_spaces_make_all_equal_length\
                    (array, spaces=2, width=12):
        #print(f"{width} + {spaces}")
        # VVVV  turns each line of the array to a list and adds spaces based on spaces
        #array_with_spaces = [[letter+space_of_len(spaces) for letter in line]
        #     for line in array if len(line)!=0]
        # consistant_array_with_spaces= ["".join(line)+space_of_len((width-len(line))*(spaces+1))
        #    for line in array_with_spaces]

        # VVVV  turns each line of the array to a list and adds spaces based on spaces
        array_with_spaces = ["".join(letter + " " * spaces for letter in line)
                             for line in array if len(line)!=0]

        # VVVV turns the message into a consistant width
        consistant_array_with_spaces = [line + " " * (width*(spaces + 1) - len(line))
                            for line in array_with_spaces]

        printed_string="".join(line+"\n" for line in consistant_array_with_spaces)

        return printed_string

    if height < 0 or width < 0 or spaces < 0 or message == None:
        print("Nah")
        return

    message = list(message)
    return_array = ["" for x in range(height)]
    increment = 0
    message_increment=0
    # vvv while the last array index is not filled and words in the message
    # still haven't been added
    while len(return_array[height - 1]) < width and message_increment<len(message):
        current = increment  # the current array index

        # VVVV while the index is bigger than -1, the current index isn't bigger
        # than the width, and there still letters to add
        while current >= 0 and len(return_array[current]) < width and \
                message_increment<len(message) :
            return_array[current] += message[message_increment]
            message_increment+=1
            # everytime a letter is added, the index gets lower to move to the one below
            current -= 1
            # insures that the array index isn't more than the length of

        increment += increment < (height - 1)
    return_array = array_to_string_add_spaces_make_all_equal_length(return_array, spaces=spaces, width=width)
    return return_array


def revert_message(message, spaces=2, final_message="", increment=0):
    if message is None or spaces < 0:
        print("Please but a number of spaces that is acceptable")
        return

    message = message.split("\n")
    # all spaces that were added for visual purposes are removed
    # iterates through ever mini_array within message, then it makes a double array
    # that has every letter in miniarray, with the increment based on spaces amount
    message_array = [[mini_array[x] for x in range(0,len(mini_array),spaces+1)]
                      for mini_array in message if len(mini_array)!=0]

    # VVVV shaves off the extra words until the word becomes a diagonal
    for x in range(len(message), 0, -1):
        thing = x
        while True:
            try:
                final_message += message_array[thing][-1]
                message_array[thing].pop(-1)
                thing += 1
            except IndexError:
                break

    # VVVV calculation to improve readability
    first_index_is_filled = len(message_array[0]) > 0
    mini_array = 0

    # print(message_array)
    # VVVV take the remaining words from message_array and then adds them to final message
    # and removes it from message_array
    increment=0
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

            # if the current index position is unfilled, then it will restart at index position 0
            mini_array = 0

        # VVVV calculation to improve readability
        first_index_is_filled = len(message_array[0]) > 0

    # VVVV because the words are added in backwards order, this will reverse it and turn it into a string
    final_message = final_message[::-1].strip()

    return final_message


# OPTIONS:______________________________________________________________________________________________

message = "I hope you find this code useful"
width = 12

height = 19

spaces = 2

copy_to_clipboard = True

# ______________________________________________________________________________________________________

diagonal_message = make_array(message, width=width, height=height, spaces=spaces)

print(diagonal_message)

undiagonaled_message = revert_message(diagonal_message, spaces=spaces)

print(undiagonaled_message)

if copy_to_clipboard:
    pyperclip.copy(diagonal_message)
