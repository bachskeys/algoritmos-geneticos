import random
from deap import base
from deap import creator
from deap import tools
from deap import algorithms
import numpy
import matplotlib.pyplot as plt
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
    return True if x5+x4 <= 1 else False

#primer restricion donde x1+x2+x3+x4+x4 = 3 para aprobar la restriccion o ser penalizado
def restriccion1(individual):
    suma = sum(individual)
    return True if suma == 3 else False

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




def algoritmo(poblacion,cbxpb,mutpb,ngen):
    #se define el tamaño que tendra la poblacion inicial
    N= int(poblacion)
    pop = toolbox.population(n=N)
    print('poblacion inicial',pop)
    #se definen aqui las constants de probabilidad de cruze tambien la de mutacion
    #CBXP {probabilidade de cruza}
    #MUTPB {probabilidad de mutacion}
    #NGEN {numero de generaciones despues de la poblacion inicial}
    CBXPB = float(cbxpbbueb)
    MUTPB = float(mutpb)
    NGEN =  int(ngen)
    hof = tools.HallOfFame(1)
    # en este objeto asignamois 4 arreglos de numpy
    # estos arreglos los registramos a las funciones genericas de stadisticas para que el algoritmo las pueble
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register('avg',numpy.mean)
    stats.register('sdt',numpy.std)
    stats.register('min',numpy.min)
    stats.register('max',numpy.max)
    #inicializamos el algoritmo pasando nuestra poblacion la clase hall of fame y nuetras constantes del problema
    pop,logbook = algorithms.eaSimple(pop, toolbox,cxpb=CBXPB,mutpb=MUTPB,ngen=NGEN,stats=stats,halloffame=hof)

    return pop, logbook, hof

def main(poblacion,CBXPB,MUTPB,NGEN):
    pops,log,hof = algoritmo(poblacion,CBXPB,MUTPB,NGEN)
    gen, avg,min_, max_ = log.select('gen','avg','min','max')
    plt.plot(gen,avg, label="average")
    plt.plot(gen,min_,label="minimum")
    plt.plot(gen,max_,label="maximum")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")   
    plt.legend(loc="lower right")
    plt.show()
    print('el individuo con mas optimo para esta funcion es', hof)

#registra el tipo de cruza seleccionado
def mateType(type,toolbox):
    print(type)
    if(type == "1"):
        toolbox.register("mate",tools.cxOnePoint)
    elif(type == "2"):
         toolbox.register("mate",tools.cxTwoPoint)
    elif(type == "3"):
         toolbox.register("mate",tools.cxUniform,indpb=0.7)



if __name__ == "__main__":
        population = input("Ingrese el tamanio de la poblacion  :")     
        print("por favor seleccione el tipo de cruza")  
        cruza = input('[1] - cruza 1 punto [2] - cruza 2 puntos [3] - cruza uniforme    :') 
        probabilidadCX = input("por favor ingrese la probabilidad de cruza [0.1-0.99] :")
        probabilidadMX = input("por favor ingrese la probabilidad de mutacion [0.1-0.99] :")
        ngen = input("intruduzca el numero de generaciones a generar   :")
        mateType(cruza,toolbox)
        toolbox.register('evaluate',aptitudIndividuo)
        toolbox.register("mutate",tools.mutFlipBit,indpb=0.50)
        toolbox.register("select",tools.selTournament,tournsize=2)
        main(population,probabilidadCX,probabilidadMX,ngen)
    

 














