import random
from deap import base
from deap import creator
from deap import tools
from deap import algorithms
import numpy
toolbox = base.Toolbox()


#todo esto es para crear un cromosoma con las caracteristicas requeridas para despues utilizar
#las funciones del toolbox mutar y cruzar de forma sensilla.
creator.create("FitnessMin",base.Fitness,weights=(-1.0,))
creator.create("Individual",list,fitness=creator.FitnessMin)
toolbox.register('attr_bool',random.randint,0,1)


toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_bool, 5)
toolbox.register('population',tools.initRepeat, list, toolbox.individual)



#restriccion donde x4+x5 <= 1 o ser penalizado
def restriccion2(individual):
    x1, x2, x3, x4, x5 = [individual[i] for i in (0,1,2,3,4)]
    suma = x5+x4
    if suma <= 1:
        return True
    else:
        return False

#primer restricion donde x1+x2+x3+x4+x4 = 3 para aprobar la restriccion o ser penalizado
def restriccion1(individual):
    suma = sum(individual)
    if suma == 3:
        return True
    else:
        return False
#una vez que definimos todad las restricciones llamamos esta fucion que se le pasara al toolbox como parametro
#este hara su trabajo evolucionando los cromosomas y implementando dicha funcion para calcular los valores de aptitudes
# de los nuevos miebros de la poblacion
def aptitudIndividuo(individual):
    x1, x2, x3, x4, x5 = [individual[i] for i in (0,1,2,3,4)]

    validaRestriccion1 = restriccion1(individual)
    validaRestriccion2 = restriccion2(individual)
    aptitud = 2*x1+2.4*x2+3*x3+4*x4+4.4*x5
    aptitud = aptitud if aptitud != 0 else 100000.0 
    aptitud = aptitud if validaRestriccion1 else 10000.0
    aptitud = aptitud if validaRestriccion2 else aptitud+8.0
  
    return aptitud,

    
toolbox.register('evaluate',aptitudIndividuo)
toolbox.register("mate",tools.cxTwoPoint)
toolbox.register("mutate",tools.mutFlipBit,indpb=0.50)
toolbox.register("select",tools.selTournament,tournsize=2)


def main():
    pop = toolbox.population(n=2)
    print('poblacion inicial',pop)
    CBXPB,MUTPB,NGEN = 0.5,0.2,15
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register('avg',numpy.mean)
    stats.register('std',numpy.std)
    stats.register('min',numpy.min)
    stats.register('max',numpy.max)

    algorithms.eaSimple(pop, toolbox,cxpb=CBXPB,mutpb=MUTPB,ngen=NGEN,stats=stats,halloffame=hof)

    return pop, stats, hof

if __name__ == "__main__":
    pops,stats,hof = main()
    print('looking at stats', stats)
    print('el mejor individuo de acuerdo a la funcion',hof)
   













