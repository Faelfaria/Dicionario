students = {
    'João': {
        'idade':18,
        'cidade': 'São Paulo',
        'notas': [7.5, 8.0, 9.0]
    },
    'Maria': {
        'idade': 20,
        'cidade': 'Rio de Janeiro',
        'notas': [6.5, 7.0, 8.5]
    },
    'Pedro': {
        'idade':19,
        'cidade': 'Belo Horizonte',
        'notas':[8.0, 8.5, 9.5]
    }
}
#Imprimir a idade de joão
print('A idade de João é:' + str(students['João']['idade']))
#Adicionar uma nota para Maria
students['Maria']['notas'].append(9.0)
#Imprimir todas as informações dos alunos
for students, info in students.items():
    print(students + ':')
    print('Idade: ' + str(info['idade']))
    print('Cidade: ' + info['cidade'])
    print('Notas:' + str(info['notas']))
    print('Média:' + str(sum(info['notas']) / len(info['notas'])))
    print()