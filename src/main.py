import SNN
import NEAT
import Genetic
import ribosome
import random as rd

Generation_Num = int(input("Input Generation Number"))
gene_list = []
for i in range(Generation_Num):
    gene_list = Genetic.Read_Gene()
    if(len(gene_list) == 0):
        import startup
    gene_score_list = []
    selected_gene = []
    descendants_gene = []
    descendant_mutated = []
    score_list = []
    network_list = ribosome.Translate_Into_Networks(4, [1,4], 2, -1)
    score_list = SNN.return_score(network_list,i)
    gene_score_list.append(score_list)
    selected_gene: list = NEAT.calc_and_select_gene(gene_score_list, gene_list)
    gene_num: int = int(len(gene_list)/2)
    for k in range(gene_num):
        cross1 = rd.choice(selected_gene)
        cross2 = rd.choice(selected_gene)
        print(cross1,cross2)
        Agene1,Agene2 = NEAT.Crossover(cross1, cross2)
        descendants_gene.append(Agene1)
        descendants_gene.append(Agene2)
    for idx_gene,gene in enumerate(descendants_gene):
        descendant_mutated.append(NEAT.Mutate(gene,score_list[idx_gene],1000000))
    Genetic.Write_Gene(descendants_gene)
        








