cosmic_clonal <- read.table("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/clonal_runs/clonal_cosmic_hits_filtered.txt", fill = TRUE, row.names = NULL , sep = "\t", header = FALSE) 
cosmic_clonal_misense <- read.table("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/clonal_runs/clonal_cosmic_hits_missense.txt", fill = TRUE, row.names = NULL , sep = "\t", header = FALSE) 
cosmic_clonal_silent <- read.table("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/clonal_runs/clonal_cosmic_hits_silent.txt", fill = TRUE, row.names = NULL , sep = "\t", header = FALSE) 
cosmic_clonal_nonsense <- read.table("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/clonal_runs/clonal_cosmic_hits_nonsense.txt", fill = TRUE, row.names = NULL , sep = "\t", header = FALSE) 

cosmic_subclonal <- read.table("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/subclonal_runs/subclonal_cosmic_hits_filtered.txt", fill = TRUE, header = FALSE, sep = "\t", row.names = NULL)
cosmic_subclonal_missense <- read.table("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/subclonal_runs/subclonal_cosmic_hits_missense.txt", fill = TRUE, row.names = NULL , sep = "\t", header = FALSE) 
cosmic_subclonal_silent <- read.table("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/subclonal_runs/subclonal_cosmic_hits_silent.txt", fill = TRUE, row.names = NULL , sep = "\t", header = FALSE) 
cosmic_subclonal_nonsense <- read.table("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/subclonal_runs/subclonal_cosmic_hits_nonsense.txt", fill = TRUE, row.names = NULL , sep = "\t", header = FALSE) 



occurences_clonal<- table(cosmic_clonal["V1"])
occurences_clonal_m<- table(cosmic_clonal_misense["V1"])
occurences_clonal_s<- table(cosmic_clonal_silent["V1"])
occurences_clonal_n<- table(cosmic_clonal_nonsense["V1"])
oc_df_clonal <- as.data.frame(occurences_clonal)
colnames(oc_df_clonal) <- c("Gene_name", "Mutation_count")
colnames(oc_df_clonal_m) <- c("Gene_name", "Mutation_count")
colnames(oc_df_clonal_n) <- c("Gene_name", "Mutation_count")
colnames(oc_df_clonal_s) <- c("Gene_name", "Mutation_count")

write.table(oc_df_clonal, file='/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/clonal_gene_counts.tsv', quote=FALSE, sep='\t', row.names = FALSE)
write.table(oc_df_clonal_m, file='/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/clonal_gene_counts_missense.tsv', quote=FALSE, sep='\t', row.names = FALSE)
write.table(oc_df_clonal_n, file='/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/clonal_gene_counts_nonsense.tsv', quote=FALSE, sep='\t', row.names = FALSE)
write.table(oc_df_clonal_s, file='/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/clonal_gene_counts_silent.tsv', quote=FALSE, sep='\t', row.names = FALSE)




oc_df_clonal_m <- as.data.frame(occurences_clonal_m)
oc_df_clonal_s <- as.data.frame(occurences_clonal_s)
oc_df_clonal_n <- as.data.frame(occurences_clonal_n)


occurences_subclonal<- table(cosmic_subclonal["V1"])
occurences_subclonal_m<- table(cosmic_subclonal_missense["V1"])
occurences_subclonal_s<- table(cosmic_subclonal_silent["V1"])
occurences_subclonal_n<- table(cosmic_subclonal_nonsense["V1"])
oc_df_subclonal <- as.data.frame(occurences_subclonal)
colnames(oc_df_subclonal) <- c("Gene_name", "Mutation_count")
colnames(oc_df_subclonal_m) <- c("Gene_name", "Mutation_count")
colnames(oc_df_subclonal_n) <- c("Gene_name", "Mutation_count")
colnames(oc_df_subclonal_s) <- c("Gene_name", "Mutation_count")

write.table(oc_df_subclonal, file='/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/subclonal_gene_counts.tsv', quote=FALSE, sep='\t', row.names = FALSE)
write.table(oc_df_subclonal_m, file='/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/subclonal_gene_counts_missense.tsv', quote=FALSE, sep='\t', row.names = FALSE)
write.table(oc_df_subclonal_n, file='/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/subclonal_gene_counts_nonsense.tsv', quote=FALSE, sep='\t', row.names = FALSE)
write.table(oc_df_subclonal_s, file='/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/subclonal_gene_counts_silent.tsv', quote=FALSE, sep='\t', row.names = FALSE)
write.table(oc_df_clonal$Gene_name, file= '/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/clonal_gene_list.txt', quote = FALSE, sep="\t", row.names = FALSE)


oc_df_subclonal_m <- as.data.frame(occurences_subclonal_m)
oc_df_subclonal_s <- as.data.frame(occurences_subclonal_s)
oc_df_subclonal_n <- as.data.frame(occurences_subclonal_n)

uniq_subclonal <- as.vector(oc_df_subclonal$Gene_name[!(oc_df_subclonal$Gene_name %in% oc_df_clonal$Gene_name)])
uniq_clonal <- as.vector(oc_df_clonal$Gene_name[!(oc_df_clonal$Gene_name %in% oc_df_subclonal$Gene_name)])
length(uniq_clonal)
length(uniq_subclonal)
uniq_clonal <- as.data.frame(uniq_clonal)

x <- uniq_clonal
y <- uniq_subclonal
n <- max(length(x), length(y))
length(x) <- n                      
length(y) <- n
uniq_genes <- as.data.frame(cbind(x,y))
colnames(uniq_genes) <- c("Clonal", "Subclonal")
write.table(uniq_genes, file='/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/uniq_genes.tsv', quote=FALSE, sep='\t', row.names = FALSE)
write.table(uniq_clonal, file = '/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/uniq_genes_clonal.txt', quote = FALSE, sep = "\t" , row.names = FALSE)

common_clonal_subclonal <- intersect(oc_df_clonal$Gene_name, oc_df_subclonal$Gene_name)
length(common_clonal_subclonal)
library(dplyr)
top_n(oc_df_clonal, 20, oc_df_clonal$Freq)
top_n(oc_df_subclonal, 20, oc_df_subclonal$Freq)

top_n(oc_df_clonal_m, 10, oc_df_clonal_m$Freq)
top_n(oc_df_clonal_s, 10, oc_df_clonal_s$Freq)
top_n(oc_df_clonal_n, 10, oc_df_clonal_n$Freq)


top_n(oc_df_subclonal_m, 10, oc_df_subclonal_m$Freq)
top_n(oc_df_subclonal_s, 10, oc_df_subclonal_s$Freq)
top_n(oc_df_subclonal_n, 10, oc_df_subclonal_n$Freq)





if (!requireNamespace("BiocManager", quietly = TRUE))
  install.packages("BiocManager")

BiocManager::install("biomaRt")
library(biomaRt)
clonal_list <- uniq_subclonal
human <- useMart("ensembl", dataset="hsapiens_gene_ensembl")
gene_coords2=getBM(attributes=c("hgnc_symbol", "start_position","end_position"), filters="hgnc_symbol", values=clonal_list, mart=human, uniqueRows=T)
gene_coords2$size=gene_coords2$end_position - gene_coords2$start_position
write.table(gene_coords2, file = '/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/subclonal_gene_lengths.txt', quote = FALSE, sep = "\t" , row.names = FALSE)



dups <- as.data.frame(table(gene_coords2$hgnc_symbol))


listEnsembl(mart = human,host = "www.ensembl.org", version = NULL,
            GRCh = 37, mirror = NULL, verbose = FALSE)


read_file <- read.table("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/subclonal_gene_lengths_normalized_dups.tsv",fill = TRUE, row.names = NULL , sep = "\t", header = T)
freq <- as.vector(as.numeric(read_file$Normalized_Count))
hist(freq, breaks = 10000, xlim = range(0,0.05))
max(freq)
thing <- as.data.frame(table(read_file$Gene))





library(dplyr)
test <- distinct(read_file, read_file$Gene, read_file$Normalized_Count , .keep_all= TRUE)



subclonal_gene_len_normalized <- read.table("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/cosmic_hits/subclonal_uniq_gene_lengths_normalized.tsv", fill = TRUE , header = TRUE) 
subclonal_gene_len_normalized <- as.data.frame(subclonal_gene_len_normalized, stringsAsFactors=FALSE)
hist(subclonal_gene_len_normalized$Gene_Length_Normalized, breaks = 1000)
print(uniq_subclonal)
uniq_subclonal <- as.vector(uniq_subclonal)

uniq_subclonal_2 <- subclonal_gene_len_normalized[uniq_subclonal, ]

uniq_subclonal_2 <- subset(subclonal_gene_len_normalized, subclonal_gene_len_normalized$Gene_Name %in% uniq_subclonal)


uniq_subclonal_2 <- as.vector(subclonal_gene_len_normalized$Gene_Name[!(subclonal_gene_len_normalized$Gene_Name %in% oc_df_clonal$Gene_name)])

hist(uniq_subclonal_2$Gene_Length_Normalized, breaks = 500, xlim = range(0, 0.010))





