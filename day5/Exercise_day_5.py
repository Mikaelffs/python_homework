
import os
import re
import matplotlib.pyplot as plt


class FastaParser(object):
	"""This class lets you read a fasta format file, it creates a dictionary containing the individual
	gene sequences, searchable both by the contig name and their numerical index, it also provides methods to filter
	gene sequences by (maximal) length and to plot a distribution of gene lengths"""

	def __init__(self, path):
		
		if type(path) != str: raise TypeError
		if not os.path.exists(path): raise IOError
		self.path = path
		self.count()
		self.parsed_genes()

	def count(self):
		"""This function counts the number of > characters which corresponds to the number of genes"""
		
		with open(self.path, "r") as openfile:
			
			filestr = openfile.read()
			self.count = len(re.findall(">", filestr))
			
	def __len__(self):
		"""This function returns the result of the count function as the length of the FastaParser object
		it would probably be nicer if both this and the count function returned the properties of the parsed_genes dictionary
		rather than the read file itself"""

		return self.count

	def parsed_genes(self):
		"""This function creates a dictionary from the .fasta file where the keys are tuples (sequence name, index) and the elements are the sequences 
		stored as strings"""
		
		with open(self.path, "r") as openfile:

			filestr = openfile.read()
			gene_names = re.findall(">(.*)\n", filestr)

			raw_genes = "".join(filestr.split("\n")).split(">")
			genes = [raw_genes[i+1][len(gene_names[i]):] for i in range(0,len(gene_names))]

			self.parsed_genes = {(gene_names[i],i):genes[i] for i in range(0,len(gene_names))}

	def __getitem__(self, index):
		"""This function allows indexing the FastaParser object using either integers or the gene names and indexes over the parsed_genes dicitonary"""

		if type(index) == int:
			
			if index > len(self)-1: raise IndexError

			else:

				keys = self.parsed_genes.keys()
				
				for i in range(0,len(keys)):
					if keys[i][1] == index:
						key = self.parsed_genes.keys()[i]

				return self.parsed_genes[key]

		elif type(index) == str:
			
			keys = self.parsed_genes.keys()
			key = ()

			for i in range(0,len(keys)):
				if keys[i][0] == index:
					key = self.parsed_genes.keys()[i]
				
			if key == (): raise KeyError

			return self.parsed_genes[key]

		else:
			pass

	def extract_length(self, length):
		"""This filters the gene sequences and returns a list of all sequences in the parsed_genes dictionary shorter than the integer argument length"""

		if type(length) != int: raise TypeError

		else:

			long_genes = []

			for i in range(0,len(self)):
				if len(self[i]) < length:
					long_genes.append(self[i])

			return long_genes

	def length_dist(self, path):
		"""This method produces a bar graph of the length distribution of the genes in the parsed_genes dictionary and saves it as a .pdf file at the
		location specified in the argument path"""

		length_list = [len(self[i]) for i in range(0,len(self))]

		plt.hist(length_list)
		plt.title("Gene length distribution")
		plt.xlabel("Length")
		plt.ylabel("Frequency")
		
		plt.savefig(path)
		







