import os
import random as rd
import NEAT

def Generate_Gene_Pool(G_num,Neuron_Num):
    Gene_Pool = []
    for _ in range(G_num):
        tNoRN = rd.randint(int(Neuron_Num/10),Neuron_Num) #The Number of Random Neurons
        tNoRC = rd.randint(1,tNoRN*(tNoRN-1)+2) #The Number of Random Connection
        Gene = [] 
        for _ in range(tNoRC):
            Gene.append(NEAT.Generate_Gene_Base(tNoRN))
        Gene_Pool.append(Gene)

    return Gene_Pool

def Write_Gene(Gene_Pool):
    for i in range(len(Gene_Pool)):
        f = open('gene/'+str(i)+'.txt','w')
        for j in range(len(Gene_Pool[i])):
            if(j==0):
                f.write(Gene_Pool[i][j])
            else:
                f.write('/'+Gene_Pool[i][j])
        f.close()

def Read_Gene():
    Gene_Pool = []
    path = "gene/"
    file_list = os.listdir(path)
    gene_list = [file for file in file_list if file.endswith(".txt")]
    for i in gene_list:
        f = open('gene/'+str(i),'r')
        gene=f.read()
        f.close()
        GeneBase_List = gene.split('/')
        Gene_Pool.append(GeneBase_List)
    
    return Gene_Pool









