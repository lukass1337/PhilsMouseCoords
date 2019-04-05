import mouse
import keyboard
import time

running = True
text_file = open("Output.txt", "a")
delete = input("Do you want to empty the Output.txt file? (y/n) ")

if delete == "y":
    text_file.truncate(0)
    print("\nOutput.txt has been emptied.\n")
else:
    print("\nOutput.txt has not been emptied.\n")

while running:
    position = mouse.get_position()
    if mouse.is_pressed(button="left"):
        text_file.write(str(position) + ("\n"))
        print("You have saved the coord: " + (str(position)))
        time.sleep(1)
    if keyboard.is_pressed("space"):
        running = False
        text_file.close()