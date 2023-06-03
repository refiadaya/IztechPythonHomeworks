"""

CHARACTER PALETTE
You can copy the necessary characters for drawing cards from here.

Horizontal lines:  │

Vertical lines:  ─

Corners of a card:  ┐  ┌  ┘  └

Intersections of two cards:

    if card1_height == card2_height:  ┬  ┴

    if card1_height < card2_height:  ┤

    if card1_height > card2_height:  ├

"""

print("This program will draw two cards next to each other.")
print("─" * 20)

print("Texts must not be empty.")
card1_text = input("Text of first card: ")
card2_text = input("Text of second card: ")
print("─" * 20)

##############################
# INSERT YOUR CODE HERE
# Assign proper values to card1_min_width and card2_min_width here.
# They are length of the corresponding text + 2.
# For example, if card1_text contains 5 characters, then card1_min_width must be 7.
card1_min_width = len(card1_text) + 2
card2_min_width = len(card2_text) + 2
# DO NOT EDIT THE CODE UNDER THIS LINE.
##############################

print("Width of first card must be at least " + str(card1_min_width) + ".")
card1_width = int(input("Width of first card: "))
print("Width of second card must be at least " + str(card2_min_width) + ".")
card2_width = int(input("Width of second card: "))
print("─" * 20)

print("Heights must be odd and at least 3.")
card1_height = int(input("Height of first card: "))
card2_height = int(input("Height of second card: "))
print("─" * 20)


##############################
# INSERT YOUR CODE HERE
# Assign the proper value to is_invalid.
# Check if there is at least one problem in the inputs.
# I added two conditions, add more to the line below.
is_invalid = len(card1_text) == 0 or len(card2_text) == 0 or card1_width < card1_min_width or card2_width < card2_min_width or card1_height < 3 or card2_height < 3 or card1_height%2 == 0 or card2_height%2 == 0
# DO NOT EDIT THE CODE UNDER THIS LINE.
##############################

if is_invalid:
    print("ERROR: Invalid inputs.")

else:

    if card1_height == card2_height:

        ##############################
        # INSERT YOUR CODE HERE
        # Case 1
        # You can add as many new lines as you need.
        borderh= "│"
        borderv= "─"
        vertical= card1_height-3
        upper= vertical//2
        lower= vertical-upper

        horizontal1= card1_width - 2 - len(card1_text)
        left1= horizontal1//2
        right1= horizontal1 - left1

        horizontal2= card2_width - 2 - len(card2_text)
        left2= horizontal2//2
        right2= horizontal2 - left2

        top_line= "┌" + (card1_width-2)*borderv + "┬" + (card2_width-2)*borderv + "┐" + "\n"
        upper_lines= (borderh + " "*(card1_width-2) + borderh + " "*(card2_width-2) + borderh + "\n")*upper
        center_line= borderh + " "*left1 + card1_text + " "*right1 + borderh + " "*left2 + card2_text + " "*right2 + borderh + "\n"
        lower_lines= (borderh + " "*(card1_width-2) + borderh + " "*(card2_width-2) + borderh + "\n")*lower
        bottom_line= "└" + (card1_width-2)*borderv + "┴" + (card2_width-2)*borderv + "┘" + "\n"
        print(top_line + upper_lines + center_line + lower_lines + bottom_line)

        pass


        # DO NOT EDIT THE CODE UNDER THIS LINE.
        ##############################


    elif card1_height > card2_height:

        ##############################
        # INSERT YOUR CODE HERE
        # Case 2
        # You can add as many new lines as you need.
        pass



        # DO NOT EDIT THE CODE UNDER THIS LINE.
        ##############################


    else:

        ##############################
        # INSERT YOUR CODE HERE
        # Case 3
        # You can add as many new lines as you need.
        pass



        # DO NOT EDIT THE CODE UNDER THIS LINE.
        ##############################
