box_presents = []
with open("input2.txt") as file:
    box_presents.append(file.read())

box_presents = box_presents[0].split("\n")

surface_area = 0

for i in range(0, len(box_presents), 1):
    box_present = box_presents[i].split("x")
    surface_area += (2 * (int(box_present[0]) * int(box_present[1])) +
                     2 * (int(box_present[1]) * int(box_present[2])) +
                     2 * (int(box_present[2]) * int(box_present[0])) +
                     min((int(box_present[0]) * int(box_present[1])),
                         (int(box_present[1]) * int(box_present[2])),
                         (int(box_present[2]) * int(box_present[0]))
                         ))
print(f"Total surface area {surface_area}")
####################PART TWO##############################
total_ribbon = 0
for i in range(0, len(box_presents)):
    box_present = box_presents[i].split("x")
    total_ribbon += min(2 * (int(box_present[0]) + int(box_present[1])),
                        2 * (int(box_present[1]) + int(box_present[2])),
                        2 * (int(box_present[2]) + int(box_present[0]))) + (
                            int(box_present[0]) * int(box_present[1]) * int(box_present[2]))
print(f"Total ribbon required {total_ribbon}")
