# map_step: multiplica cada elemento del array por 2.
# reduce_step: combina todos los valores en un único resultado (en este caso, su suma).
# Resultado: Si data = [5,2,7,3,10], tras map → [10,4,14,6,20] y reduce → 10+4+14+6+20 = 54.

from functools import reduce

# MAP step: ejemplo sencillo que duplica cada elemento
def map_step(values):
    return [v * 2 for v in values]

# REDUCE step: sumar todos los elementos mapeados
def reduce_step(mapped_values):
    return reduce(lambda x, y: x + y, mapped_values, 0)

if __name__ == "__main__":
    data = [5, 2, 7, 3, 10]

    # MAP
    mapped = map_step(data)
    print("Map result:", mapped)

    # REDUCE
    result = reduce_step(mapped)
    print("Map-Reduce final result:", result)
