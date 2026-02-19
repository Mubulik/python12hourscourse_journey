# 2D List = Liste faite de liste

fruits =    ["fraise", "framboise", "noix de coco", "pêche"]
legumes =   ["concombre", "courgette", "carottes", "haricots", "pumpkin"]
viandes =   ["boeuf", "poulet", "porc", "veau"]

courses = [fruits, legumes, viandes]

print(courses[2][2])


# Parcours de la liste 2D fait maison avant de voir la solution simplifiée
# for x in range(len(courses)):
#     for y in range(len(courses[x])):
#         print(courses[x][y], end=", ")
#     print()

for type in courses:
    for item in type:
        print(item, end=", ")
    print()