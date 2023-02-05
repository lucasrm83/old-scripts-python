
arq = open("arquivos.txt","r")

alunos = []
linhas = arq.read().splitlines()
for linha in linhas:
    aluno = linha.split(";")
    nome = aluno[0]
    endereco = aluno[1]
    telefone = aluno[2]
    alunos.append([nome,endereco,telefone])
arq.close()

for aluno in alunos:
    print("Nome: %s" % aluno[0])
    print("Endereço: %s" % aluno[1])
    print("Telefone: %s" % aluno[2])
