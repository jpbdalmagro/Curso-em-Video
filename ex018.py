import math
ang = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {}° tem o seno de {:.2f}, o cosseno de {:.2f}. e a tangente de {:.2f}'.format(ang,sen,cos,tan))
