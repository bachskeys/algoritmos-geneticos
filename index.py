import random
from deap import base
from deap import creator
from deap import tools
toolbox = base.Toolbox()


#todo esto es para crear un cromosoma con las caracteristicas requeridas para despues utilizar
#las funciones del toolbox mutar y cruzar de forma sensilla.
creator.create("FitnessMax",base.Fitness,weights=(1.0,))
creator.create("Individual",list,fitness=creator.FitnessMax)
toolbox.register('attr_bool',random.randint,0,1)


toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_bool, 5)



#restriccion donde x4+x5 <= 1 o ser penalizado
def restriccion2(individual):
    x1, x2, x3, x4, x5 = [individual[i] for i in (0,1,2,3,4)]
    suma = x5+x4
    print(individual)
    print(suma)
    if suma <= 1:
        return True,
    else:
        return False,

#primer restricion donde x1+x2+x3+x4+x4 = 3 para aprobar la restriccion o ser penalizado
def restriccion1(individual):
    suma = sum(individual)
    print(individual)
    print(suma)
    if suma < 3:
        return True,
    else:
        return False,
#una vez que definimos todad las restricciones llamamos esta fucion que se le pasara al toolbox como parametro
#este hara su trabajo evolucionando los cromosomas y implementando dicha funcion para calcular los valores de aptitudes
# de los nuevos miebros de la poblacion
def aptitudIndividuo(individual):
    x1, x2, x3, x4, x5 = [individual[i] for i in (0,1,2,3,4)]
    validaRestriccion1 = restriccion1(individual)
    validaRestriccion2 = restriccion2(individual)
    print('evaluando restriciones 1',validaRestriccion1," 2 ",validaRestriccion2)
    apitud = 2*x1+2.4*x2+3*x3+4*x4+4.4*x5
    print('evaluando la aptitud del individuo sin restriccion', apitud)
    return 1,

    
print('buscando al individuo',aptitudIndividuo(toolbox.individual()))





