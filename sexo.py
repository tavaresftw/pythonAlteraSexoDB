arquivo = open("sexo_teste.txt","r")
arquivo2 = open("nomes_ibge.txt","r")
arq = open("novo-arquivo.txt", "w")


for linha in arquivo:
	txt = linha.split()
	for linha2 in arquivo2:
		txt2 = linha2.split(",")
		if txt2[0] == txt[0]:
			linha += txt2[2]
			arq = open("novo-arquivo.txt","a+")
			arq.write(linha)
			arq.write("\n")
	arquivo2.seek(0)
input()

arq.close()
arquivo.close()
arquivo2.close()