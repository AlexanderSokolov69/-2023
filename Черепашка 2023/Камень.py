import turtle as t


tom = t.Pen()
fig = ((70, 0), (65, -55), (45, -80), (-90, -80),
       (-90, 0), (-80, 50), (-55, 80), (-30, 90),
       (12, 90), (45, 75), (65, 45))
t.register_shape('romb', fig)

# tom.shapesize(14, 14)

tom.shape('romb')
tom.left(90)
tom.stamp()




t.done()
