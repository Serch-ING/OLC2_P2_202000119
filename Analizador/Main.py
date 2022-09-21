import Gramatica as g

f = open("./entrada.txt", "r")
input = f.read()

instrucciones = g.parse(input)

print("\nImprimeinedo arboles")
if instrucciones is not None:
    for x in instrucciones:
        print(x)
