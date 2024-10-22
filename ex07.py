# 7 QUESTÃO Dois torcedores de times pernambucanos estabeleceram um código secreto para se comunicarem sem que outras pessoas entendam.

lista1_secreta = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

l_secreta_a = [19, 1, 14, 20, 9, 14, 8, 1, 0, 6, 15, 1, 4, 5, 0, 19, 5, 18, 9, 5]
l_secreta_b = [22, 1, 9, 0, 19, 21, 2, 9, 18, 0, 14, 9, 14, 7, 21, 5, 13]

m_secreta_a = ''.join([lista1_secreta[num] if num != 0 else ' ' for num in l_secreta_a])
m_secreta_b = ''.join([lista1_secreta[num] if num != 0 else ' ' for num in l_secreta_b])


print(m_secreta_a)
print(m_secreta_b)