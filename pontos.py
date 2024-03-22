import math
ponto1x = int(input("Digite a coordenada x do primeiro ponto:"))
ponto1y = int(input("Digite a coordenada y do primeiro ponto:"))
ponto2x = int(input("Digite a coordenada x do primeiro ponto:"))
ponto2y = int(input("Digite a coordenada y do segundo ponto:"))

distancia = math.sqrt((ponto1x - ponto2x)**2 + (ponto1y - ponto2y)**2)
if distancia >= 10:
    print("longe")
else:
    print("perto")