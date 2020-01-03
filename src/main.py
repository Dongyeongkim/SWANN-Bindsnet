import SNN
import NEAT
import Genetic
import ribosome
import random as rd


Generation_num = 100#int(input("Input the number of testing generations"))

for i in range(Generation_num):
    gene_list = Genetic.Read_Gene()

    gene_score_list = []
    selected_gene = []
    descendants_gene = []
    descendant_mutated = []
    score_list = []
    network_list = ribosome.Translate_Into_Networks(4, [1,4], 2, -1)
    score_list = SNN.return_score(network_list,i)
    gene_score_list.append(score_list)
    selected_gene: list = NEAT.calc_and_select_gene(gene_score_list, gene_list)
    gene_num: int = len(gene_list)/2
    for k in range(gene_num):
        cross1 = rd.choice(selected_gene)
        cross2 = rd.choice(selected_gene)
        Agene1,Agene2 = NEAT.Crossover(cross1, cross2)
        gene_list.remove(cross1)
        gene_list.remove(cross2)
        descendants_gene.append(Agene1)
        descendants_gene.append(Agene2)
    for idx_gene,gene in enumerate(descendants_gene):
        descendant_mutated.append(NEAT.Mutate(gene,score_list[idx_gene],1000000))
    Genetic.Write_Gene(descendants_gene)








