goal_list = ["Python", "HTML", "CSS"]
goal_list += ["Django", "Javascript", "Database"]

file = open("File Handling/newnote.txt", "a")

for goal in goal_list:
    file.write(f"Master {goal}\n")

file.close()