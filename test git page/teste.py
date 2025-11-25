from vpython import *
import math

scene.title = "Mapa 3D com Áreas de Calor"
scene.background = color.black

chao = box(pos=vector(0,-0.5,0), size=vector(20,0.1,20), color=color.green)

# Função semelhante ao numpy.linspace
def linspace(a, b, n):
    step = (b - a) / (n - 1)
    return [a + step * i for i in range(n)]

def area_de_calor(x_centro, y_centro, intensidade, raio, resolucao=20, transparencia=0.5):
    for x in linspace(x_centro - raio*2, x_centro + raio*2, resolucao):
        for y in linspace(y_centro - raio*2, y_centro + raio*2, resolucao):

            T = intensidade * math.exp(-((x - x_centro)**2 + (y - y_centro)**2) / (2 * raio**2))

            cor = vector(T/intensidade, 0, 1 - T/intensidade)

            pos = vector(x, T * 3, y)

            sphere(pos=pos, radius=0.2, color=cor, opacity=transparencia, emissive=True)

# Criar áreas de calor
area_de_calor(0, 0, intensidade=1.0, raio=2.5)
area_de_calor(-5, 3, intensidade=0.8, raio=2)
area_de_calor(4, -4, intensidade=1.2, raio=3)

while True:
    rate(30)
