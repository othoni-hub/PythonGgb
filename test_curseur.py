"""
Intersect a line and a parabola

Create a parabola which can be adjusted using a slider, and find its
intersection with a fixed line.
"""

coeff_a = Slider(1, 5, increment = 0.1)
coeff_b = Slider(1, 5, increment = 0.1)
coeff_c = Slider(-2,2, increment = 0.1)
coeff_c.value = -1
parabola = Parabola(coeff_a, coeff_b, coeff_c)
line = Line(1, 0)

print(Intersect(parabola, line,2))
    

