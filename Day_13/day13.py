#Project Helix Gene Database
#Author: J Pearlson Job
print("==============================================")
print("      PROJECT HELIX GENE DATABASE ")
print("==============================================")
gene=("TP53","Human",17)
print(gene[0])
print(gene[1])
print(gene[2])
gene_list=["TP53","BRCA1","EGFR","TP53","MYC","BRCA1"]
print(gene_list)
new_gene=input("Emter a gene name:").upper()
unique_genes=set(gene_list)
unique_genes.add(new_gene)
print("Unique Genes:")
for gene in unique_genes:
    print(gene)
print("Total genes:",len(gene_list))
print("Unique genes:",len(unique_genes))
