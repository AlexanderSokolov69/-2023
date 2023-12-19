import turtle as t


tom = t.Pen()
tom.pu()
tom.hideturtle()
scissors = ((24, 17), (23, 21), (44, 50), (38, 58),
            (32, 57), (25, 59), (20, 65), (20, 72),
            (23, 76), (28, 80), (33, 81), (32, 76),
            (30, 76), (26, 73), (24, 69), (26, 64),
            (32, 61), (37, 63), (40, 67), (39, 72),
            (34, 76), (32, 76), (32, 81), (37, 80),
            (40, 77), (44, 72), (44, 66), (42, 62),
            (50, 55), (56, 59), (55, 62), (54, 68),
            (55, 74), (59, 76), (62, 73), (59, 68),
            (60, 62), (62, 58), (69, 58), (74, 60),
            (77, 65), (76, 70), (72, 74), (65, 75),
            (62, 74), (60, 76), (64, 78), (72, 78),
            (78, 74), (81, 64), (78, 58), (74, 55),
            (65, 53), (60, 54), (56, 48), (71, 21),
            (71, 16), (50, 43), (24, 17))

paper = ((15, 14), (14, 83), (35, 91), (52, 80),
         (59, 79), (66, 91), (76, 90), (86, 85),
         (87, 13), (77, 22), (67, 24), (49, 14),
         (35, 25), (15, 14))
stone = ((44, 14), (56, 14), (64, 17), (71, 26),
         (76, 36), (80, 48), (82, 56), (82, 77),
         (77, 81), (67, 83), (30, 81), (23, 78),
         (17, 75), (17, 51), (22, 39), (28, 28),
         (36, 20), (44, 14))

t.register_shape('scissors', scissors)
t.register_shape('paper', paper)
t.register_shape('stone', stone)
tom.color("gray")
tom.shapesize(3, 3)
tom.right(90)
tom.shape('stone')
tom.stamp()
tom.forward(200)

t.done()