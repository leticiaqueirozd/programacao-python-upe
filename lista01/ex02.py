#2 QUESTÃO. Dada a string ‘This is spartaaaaaaa’ como seria possível modificar as três palavras (‘This’, ‘is’, ‘spartaaaaaaa’) por qualquer outra palavra nessa string? Isso é possível? Justifique.

a = 'This is spartaaaaaaa'
words = a.split()
print(words)

change = input('Digite a palavra que quer substituir: ') #tem que digitar exatamente como está na string
anotherWord = input('Digite a nova palavra: ')

if change in a:
    newWord = a.replace(change, anotherWord)
    print(newWord)


# Bom, a partir do meu exemplo é possível perceber que eu não fiz uma alteração direta na string original,
# pois não existe essa possibilidade levando em consideração como o python funciona, uma vez que strings são
# consideradas imutáveis. Contudo, através de outras strings e estruturas condicionais eu pude realizar a
# proposta da atividade, mostando que é possível utilizar uma lógica para muitas situações adversas.