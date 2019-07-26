import mouse
import keyboard
import time

delete = input("Do you want to empty the Output.txt file? (y/n) ")
running = True

if delete.lower() == "y":
    text_file.truncate(0)
    print("\nOutput.txt has been emptied.\n")
else:
    print("\nOutput.txt has not been emptied.\n")

with open("Output.txt", "a") as file:
    while running:
        position = mouse.get_position()
        if mouse.is_pressed(button="left"):
            file.write(str(position) + ("\n"))
            print("You have saved the coord: " + (str(position)))
            time.sleep(1)
        if keyboard.is_pressed("space"):
            running = False
            file.close()
