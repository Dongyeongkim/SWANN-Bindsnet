import random as rd

### - IMPLEMENT NEAT ALGORITHM TO THIS - ###

def Crossover(gene1,gene2):
    A_Gene1 = []; A_Gene2 = []
    C_Gene1 = gene1; C_Gene2 = gene2
    # Crossovering Process
    for i in range(len(C_Gene1)):
        if(i>len(C_Gene2)-1):
            A_Gene1.append(C_Gene1)
        else:
            S_Genotype = rd.randint(0, 1)
            if(S_Genotype==0):
                A_Gene1.append(C_Gene1[i])
            else:
                A_Gene1.append(C_Gene2[i])
     
    for j in range(len(C_Gene2)):
        if(j>len(C_Gene1)-1):
            A_Gene2.append(C_Gene2)
        else:
            S_Genotype = rd.randint(0, 1)
            if(S_Genotype==0):
                A_Gene2.append(C_Gene1[j])
            else:
                A_Gene2.append(C_Gene2[j])
    
    return A_Gene1,A_Gene2


def Generate_Gene_Base(Neuron_a,Num):
    Neuron_Num = Neuron_a # Neuron Amount
    Neuron_Type = rd.choice('~!@#$')
    while True:
        Source_Neuron = str(rd.randint(1,Neuron_Num))
        Target_Neuron = str(rd.randint(1,Neuron_Num))
        if(Source_Neuron!=Target_Neuron):
            break
        else:
            pass
    Connection = rd.choice('01')
    if(Connection=='0'):
        Connection = 'T'
    else:
        Connection = 'F'

    Gene_Base = Num + '>' + Source_Neuron + Neuron_Type + Target_Neuron + Connection;print(Gene_Base)
    return Gene_Base


def Mutate(Gene,accr):

    Mutated_Gene = []
    for i in range(len(Gene)):
        random_PER = rd.random()
        if(1-accr>random_PER):
            Mutated_Gene.append(Gene[i])
        else:
            Gene_Slave =Gene[i].split('>'); Gene_Slave = Gene_Slave[1]; Gene_Node = Gene_Slave[0]
            for j in range(len(Gene_Slave)):
                if(Gene_Slave[j].isdecimal()==False):
                    Gene_Slave = Gene_Slave.split(Gene_Slave[j])
                    Source_Neuron = int(Gene_Slave[0])
                    Gene_Slave = Gene_Slave[1]
                    for k in range(len(Gene_Slave)):
                        if(Gene_Slave[k].isdecimal()==False):
                            Gene_Slave = Gene_Slave.split(Gene_Slave[j])
                            Target_Neuron = Gene_Slave[0]
                        else:
                            pass

                else:
                    pass
                
            Neuron_Type = rd.choice('~!@#$')
            Connection = rd.choice('01')
            if(Connection=='0'):
                Connection = 'T'
            else:
                Connection = 'F'
            Mutated_Gene.append(Gene_Node + '>' + Source_Neuron + Neuron_Type + Target_Neuron + Connection)
        
    random_factor = rd.random()
    while(0.7-accr>random_factor):
        random_factor = rd.random()
        Mutated_Gene.append(Generate_Gene_Base(10000,len(Mutated_Gene)+1))
    
    return Mutated_Gene


def Calc_Fitness(accr_set):
    Sum=sum(accr_set)
    fitness_set = []
    for i in range(len(accr_set)):
        fitness_set.append(accr_set[i]/Sum)
    return fitness_set
