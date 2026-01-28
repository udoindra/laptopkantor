import os
import keyboard
import time

width, height = 20, 10
x, y = width // 2, height // 2
symbol = "@"
score = 0

while True:
    os.system("cls")
    for row in range(height):
        line = ""
        for col in range(width):
            if row == 0 or row == height-1 or col == 0 or col == width-1:
                line += "#"  # border
            elif row == y and col == x:
                line += symbol
            else:
                line += " "
        print(line)

    # Show instructions and score
    print(f"\nUse arrow keys to move. Press Q or Esc to quit.")
    print(f"Score: {score}")

    moved = False  # track if a move happened

    # Movement
    if keyboard.is_pressed("up"):
        y = max(1, y - 1)
        moved = True
    elif keyboard.is_pressed("down"):
        y = min(height - 2, y + 1)
        moved = True
    elif keyboard.is_pressed("left"):
        x = max(1, x - 1)
        moved = True
    elif keyboard.is_pressed("right"):
        x = min(width - 2, x + 1)
        moved = True

    # Exit key
    elif keyboard.is_pressed("q") or keyboard.is_pressed("esc"):
        print("Exiting game...")
        break

    # Increase score only if moved
    if moved:
        score += 1

    time.sleep(0.1)