from core import models


def criar_registros():
    numero = int(input('Digite a quantidade de registros: '))

    for n in range(numero):
        d = models.Department()
        d.name = 'Departamento_{}'.format(n)
        d.save()

    for d in models.Department.objects.all():
        print('Id: {}'.format(d.id))
        print('Nome: {}'.format(d.name))
        print('Criado em: {}'.format(d.created_at))


def ler_arquivo():
    with open('/Users/ozzy/crud_funcionario/core/departamentos.txt') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            d = models.Department()
            d.name = linha.replace('\n', '')
            d.save()

    print(models.Department.objects.all())