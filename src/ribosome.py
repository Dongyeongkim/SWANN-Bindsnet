import os
import src.Genetic as Genetic
import bindsnet.network as network

path = "gene/"
file_list = os.listdir(path)
gene_list = [file for file in file_list if file.endswith(".txt")]
if(len(gene_list)==0):
    import src.startup

Gene_List = Genetic.Read_Gene()
network = network.Network()


