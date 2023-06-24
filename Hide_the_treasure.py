row1 = ["📦", "📦", "📦"]
row2 = ["📦", "📦", "📦"]
row3 = ["📦", "📦", "📦"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")
hori = (int(position[0]) - 1)
Vert = (int(position[1]) - 1)
# print(hori)
# print(Vert)
map[hori][Vert] = "x"
# print(map)
print(f"{row1}\n{row2}\n{row3}")
