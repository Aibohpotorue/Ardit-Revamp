date = input("Enter today's Date: ")
mood = input("Rate your mood today on a scale of 1-10: ")
thoughts = input("Let your thoughts flow:\n")

with open(f"files/journal/{date}.txt", "w") as file:
    file.write(mood + "\n")
    file.write(thoughts)