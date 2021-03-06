# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kaz = Character("Kaedehara Kazuha")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene background liyue

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show kazuhastill: 
        xalign 0.8
        yalign 0.5
        zoom 0.5
        

    # These display lines of dialogue.

    kaz "Solitary cloud"

    kaz "Shadow in the setting sun"

    kaz "Stirs the drifters's heart."

    # This ends the game.

    return
