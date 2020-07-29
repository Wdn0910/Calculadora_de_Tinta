from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

#largura: float = float(input('Qual a largura do cômodo? '))
#profundidade: float = float(input('Qual a profundidade do cômodo? '))

comodo = Comodo(
    input('Qual a largura do cômodo? '),
    input('Qual a profundidade do cômodo? '))

print('A area das paredes é:', calc.calcular_area_paredes(
    comodo
))

#calc.area_teto: float = largura * profundidade
print('A area do teto é:', calc.calcular_area_teto(
    comodo
))

print('A litragem de tinta necessária é:', calc.calcular_litragem_necessaria())