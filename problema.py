#Autor: Matheus Mota Santos
#Componente Curricular: EXA854 MI-Algoritmo
#Concluido em: 02/12/2021
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

from funcoes import Cadastro,escrever_arquivo,buscar_alteas,obter_dados, coleta_dados, transforma,mostra_modalidade,relatório,atuliza_dicionario
from time import sleep
#Recebe os dados do arquivo json
dicionario_atleta = obter_dados()

if __name__ == '__main__':
    todas_modalidades =[
    'atletismo','badminton','basquetebol em cadeira de rodas','bocha','canoagem','ciclismo de estrada','ciclismo de pista','esgrima em cadeira de rodas','futebol de 5','goalball', 'hipismo','judô','levantamento de peso','natação','remo','rugby em cadeira de rodas','taekwondo','tênis de mesa','tênis em cadeira de rodas','tiro','tiro com arco','triatlo','voleibol sentado',]

    while True:
        #Converte os dados dos Atletas em objetos da classe Cadastro
        lista_atletas = transforma(dicionario_atleta)
        #Caso Não tenha atletas cadastrados, será mostrada ao usuário apenas a opção de cadastar atleta e sair
        if not lista_atletas:
            menu = int(input('[1] Cadastrar atleta\n[2] Sair\n->'))
            # Verifica se as opções está entre o que é esperado
            if 1<= menu <= 2:
                if (menu == 1):
                    #Coleta od dados do atleta, e retorna o objeto da classe cadastro
                    atleta = coleta_dados(dicionario_atleta,lista_atletas)
                    atuliza_dicionario(atleta, dicionario_atleta)
                else:
                    break
            #Caso o usário digite um opção que não foi esperada
            else:
                print('Opção inválida!')
                continue
        #Caso já exista atletas cadastrado, outras opções serão exibidas
        else:
            menu = int(input('[1] Cadastrar atleta\n[2] Editar Cadastro\n[3] Excluir modalidade\n[4] Exibir relatório\n[5] Sair\n->'))
            if menu < 1 or menu > 5:
                print('Opção inválida')
                continue
            else:
                #Caso o usário digite 1, é será oferecido um formulário para cadastro
                if (menu == 1):
                    atleta = coleta_dados(dicionario_atleta,lista_atletas)
                    atuliza_dicionario(atleta, dicionario_atleta)

                #Caso o usuário digite 2, será direcionado para opções de edição de cadstro
                elif (menu == 2):
                    #Usa o nome do usário para fazer uma busaca nos dados
                    inf_nome = input('Digite seu nome: ').title()
                    #Retorna a posição onde o usuário está na lista
                    indice = buscar_alteas(lista_atletas, inf_nome)
                    #Caso retorne -1, o usuário ainda não foi cadastrado
                    if (indice == -1) :
                        print(f'O usuário {inf_nome} ainda não foi cadastrado!')
                    else:
                        indice = buscar_alteas(lista_atletas, inf_nome)
                        #Mostra todas informações do usário
                        sleep(0.1)
                        print(lista_atletas[indice])
                        while True:
                            #Exibe um menu para edição do cadastro, para alterar o nome,sexo, situação em relação ao covid-19, tipo de parilisia,modalidades cadastradas, cada medalha de determinada modalidadde ou sair.
                            print('O que deseja Editar?')
                            edicao = int(input('[1] Nome\n[2] Idade\n[3] Sexo\n[4] Situação Covid-19\n[5] Tipo de paralisia\n[6] Modalidades Cadastradas\n[7] Medalha de uma modalidade\n[8] Sair\n->'))

                            #Caso digite um, é mostrada a opção para mudar de nome
                            if (edicao == 1):
                                #É preciso que o usário digite o novo nome
                                while True:
                                    novo_nome = input('Digite o novo nome: ').title().strip()
                                    print()
                                    #Verifica se o usuário digitou um nome
                                    if novo_nome == '' or novo_nome.isnumeric():
                                        print('Por favor, digite um nome!\n')
                                        continue
                                    else:
                                        #Usa um metódo da classe para alterar o nome
                                        lista_atletas[indice].altera_nome(novo_nome)
                                        #Mostra o cadastro atualizado ao usário
                                        sleep(0.1)
                                        print(lista_atletas[indice])
                                        #Remove o usário do dicionário, já que a chave do cadastro era o nome
                                        del dicionario_atleta[inf_nome]
                                        #Faz a atualização dos dados
                                        atuliza_dicionario(lista_atletas[indice], dicionario_atleta)
                                        print()
                                        break
                            #Caso o usário digite 2, é mostrado d opção de editar a idade
                            elif (edicao == 2):
                                while True:
                                    nova_idade = input('Digite a nova idade: ')
                                    print()
                                    if nova_idade.isnumeric():
                                        #Usa o metódo para alterar a idade
                                        lista_atletas[indice].alterar_idade(int(nova_idade))
                                        #Mostra o cadastro atualizado
                                        sleep(0.1)

                                        print(lista_atletas[indice])
                                        #Faz a atualização dos dados
                                        atuliza_dicionario(lista_atletas[indice], dicionario_atleta)
                                        print()
                                        break
                                    else:
                                        print('Entrada inválida!\n')
                                        continue

                            #Caso o usário digite 3, é mostrado a opção de editar o sexo
                            elif (edicao == 3):
                                #Usa o metódo atlerar_sexo da calsse cadastro para fazer a atualização do sexo
                                lista_atletas[indice].alterar_sexo()
                                #Mostra o cadastro alterado
                                sleep(0.5)
                                print(lista_atletas[indice]) 
                                #Faz a atualização dos dados
                                atuliza_dicionario(lista_atletas[indice], dicionario_atleta)
                                print('Edição feita com sucesso!\n')

                            #Caso o usário digite 4, é mostrado d opção de editar o situação em relação ao covid-19
                            elif (edicao == 4):
                                #Usa o metódo altera_situacao_covid da calsse cadastro para fazer a atualização do sexo situação em relação ao covid-19
                                lista_atletas[indice].altera_situacao_covid()
                                sleep(0.5)
                                print(lista_atletas[indice]) 
                                atuliza_dicionario(lista_atletas[indice], dicionario_atleta)  
                                print('Edição feita com sucesso!\n')

                            #Caso o usário digite 5, é mostrado d opção de editar o tipo de paralisia
                            elif(edicao == 5):
                                novo_tipo = input('Digite o tipo de paralisia: ').capitalize().strip()
                                print()
                                lista_atletas[indice].alterar_tipo_deficiencia(novo_tipo)
                                sleep(0.5)
                                print(lista_atletas[indice]) 
                                atuliza_dicionario(lista_atletas[indice], dicionario_atleta)  
                            #Caso o usário digite 5, é mostrado d opção de editar a modaliade

                            elif (edicao == 6):
                                #Menu para adcionar ou substituir uma modalidade
                                edita_modalidade = int(input('[1] Adcionar modalidade\n[2] Substituir modalidade\n->'))
                                if edita_modalidade == 1:
                                    #Mostra todas modalidades presentes
                                    mostra_modalidade(todas_modalidades)
                                    #Recebe a nova modalidade
                                    nova_modalidade = int(input('Nova modalidade: '))
                                    print()
                                    #Verifica se a modalidade digitada faz parte de uma das modalidades da paralimpíada
                                    if 0 <= nova_modalidade <= 23:
                                        #Usa o metodo da classe Cadastro para adcionar uma modalidade
                                        lista_atletas[indice].alterar_modalidade(todas_modalidades[nova_modalidade],todas_modalidades)
                                        atuliza_dicionario(lista_atletas[indice], dicionario_atleta)
                                        print(lista_atletas[indice])
                                    else:
                                        print('Modalidade inválida\n')

                                else:
                                    #Mostra as modalidade que o atleta está cadstrado
                                    print('-'*100)
                                    for n,i in enumerate(lista_atletas[indice].modalidade):
                                        print(f'{n} - {i}')
                                    print('-'*100)
                                    #Recebe qual modalidade o usuário deseja substituir
                                    antiga_modalidade = int(input('Modalidade que deseja substituir: '))
                                    #Mostra todas modalidades disponiveis
                                    mostra_modalidade(todas_modalidades)
                                    #Recebe a nova modalidade
                                    nova_modalidade = int(input('Nova modalidade: '))
                                    #Verifica se a nova modalidade está entre as disponiveis
                                    if 0<= nova_modalidade <= 23:
                                        #Usa o metódo da classe Cadastro para substituir a modalidade
                                        lista_atletas[indice].alterar_modalidade(todas_modalidades[nova_modalidade],todas_modalidades, antiga_modalidade)
                                        atuliza_dicionario(lista_atletas[indice], dicionario_atleta)
                                        print(lista_atletas[indice])
                                    else:
                                        print('Entrada inválida!\n')

                            elif (edicao == 7):
                                #Mostra todas modalidades com suas respectivas medalhas ganha pelo alteta
                                for n,k in enumerate(lista_atletas[indice].medalha.items()):
                                    print(f'{n} - {k[0]} [{k[1]}]')
                                print()

                                edita_modalidade = int(input('Modalidade que deseja alterar a medalha: '))
                                print()
                                if 0 <= edita_modalidade <= len(lista_atletas[indice].medalha):
                                    #Usa o metódo altera_medalhas para fazer a alteração
                                    lista_atletas[indice].atlerar_medalhas(list(lista_atletas[indice].medalha.keys())[edita_modalidade])
                                    print(lista_atletas[indice])
                                    atuliza_dicionario(lista_atletas[indice], dicionario_atleta)
                            elif (edicao == 8):
                                break
                #Caso o usuário digite 2, será direcionado para opções de remoção do atleta em determinada modalidade
                elif (menu == 3):
                    #Faz a busca do atleta na lista pelo nome
                    inf_nome = input('Digite seu nome: ').title().strip()
                    indice = buscar_alteas(lista_atletas, inf_nome)

                    #Caso o retorno da função busca atleta seja -1, não está cadastrado
                    if (indice == -1) :
                        print(f'O usuário {inf_nome} ainda não foi cadastrado!')
                    else:
                        
                        print(lista_atletas[indice])
                        molidade_remover = int(input('[1] Remover uma modalidade\n[2] Remover todas modalidades\n->'))
                        if molidade_remover == 1:
                            while True:
                                print()
                                print('-'*100)
                                #Mostra todas modalidades em que o atleta tá cadastrado
                                for n,i in enumerate(lista_atletas[indice].modalidade):
                                    print(f'{n} - {i}')
                                print('-'*100)
                                modalidade = int(input('Modalidade que deseja remover: '))
                                #Verifica se a modalidade que o usário digitou está entre as modalidades disponiveis
                                if 0 <= modalidade <= len(lista_atletas[indice].modalidade):
                                    #Se a lista de modalidades for maior que um a modalidade é deletada
                                    if len(lista_atletas[indice].modalidade) > 1:
                                        #Usa o metódo da classe Cadastro para deletar a modalidade
                                        lista_atletas[indice].excluir_modalidade(modalidade)
                                    else:
                                        #Se só tiver uma modalidade cadastrada, o usário sera deletado do docionário (dicionario_atleta) e da lista (lista_atletas)
                                        prg = input('Caso essa modalidade seja deletada, você será deletado da lista de atleas\nDeseja continuar? [S/N]\n->').upper()
                                        if prg == 'S':
                                            del dicionario_atleta[lista_atletas[indice].nome]
                                            lista_atletas.pop(indice)
                                            print('Atleta deletado com Sucesso!')
                                            #Atualiza os dados no arquivo json
                                            escrever_arquivo(dicionario_atleta)
                                            break
                                        else:
                                            break
                                #Caso o usário queira deletar mais modalidades
                                escrever_arquivo(dicionario_atleta)
                                print('-'*100)
                                for n,i in enumerate(lista_atletas[indice].modalidade):
                                    print(f'{n} - {i}')
                                print('-'*100)
                                opcao_remover = input('Deseja remover mais modalidade?[S/N] ').upper().strip()
                                if opcao_remover == 'S':
                                    continue
                                else:
                                    break
                                    
                        #Caso a opção de excluir de todads modalidades for escolhida, automaticamente o usário será deletado
                        elif (molidade_remover == 2):
                            prg = input('Caso remova todas modalidades, você será deletado da lista de atletas\nDeseja continuar? [S/N]\n->').upper().strip()
                            if prg == 'S':
                                del dicionario_atleta[lista_atletas[indice].nome]
                                lista_atletas.pop(indice)
                                print('Atleta deletado com Sucesso!')
                                escrever_arquivo(dicionario_atleta)

                            else:
                                break
                #Mostra o relatorio
                elif (menu == 4):
                    #Chama a função para produzir o relatório
                    relatório(lista_atletas,todas_modalidades)
                else:
                    break

