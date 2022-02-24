#Autor: Matheus Mota Santos
#Componente Curricular: EXA854 MI-Algoritmo
#Concluido em: 02/12/2021
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
import os
import pickle
import json

#Classe para cadatro de atletas
class Cadastro:
    #Inicialização de atributos para o cadastro
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.sexo = ''
        self.covid = ''
        self.deficiencia = ''
        self.modalidade = []
        self.medalha = {}

    #Metodo utilizado para imprimir os dados do atleta
    def __str__(self, retorno=False):

        #Faz uma string só com as modalidade, apartir da lista de modalidade
        modalidade = ''
        for i in self.modalidade:
            modalidade += (i.capitalize() + ' | ')

        #Faz um string só com a modalidades e medalhdads, apartir de um dicionário
        medalha = ''
        for k,v in self.medalha.items():
            medalha += (f'{k.capitalize()} - [{v}]\n')
        #Caso o parâmetro retorno não seja passado, retorna o cadastro completa
        if retorno == False:
            return (
                ""
                f'Nome: {self.nome}\n'
                f'Idade: {self.idade}\n'
                f'Sexo: {self.sexo}\n'
                f'Situação Covid : {self.covid}\n'
                f'Tipo de Paralisisa: {self.deficiencia}\n'
                f'Modalidades Cadatradas: [{modalidade}]\n'
                f'Medalhas por modalidade: \n{medalha}'
                ""
            )
        #Caso o parâmetro seja passado como True, retorna o cadastro mas sem as modalidades caadastradas
        elif retorno == True:
            return (
                ""
                f'Nome: {self.nome}\n'
                f'Idade: {self.idade}\n'
                f'Sexo: {self.sexo}\n'
                f'Situação Covid : {self.covid}\n'
                f'Tipo de Paralisia: {self.deficiencia}\n'
                f'Medalhas por modalidade: \n{medalha}'
                ""
            )

         
    #Altera o sexo
    def alterar_sexo(self): 
        # Caso o sexo seja masculino, vai ser alterado para o sexo feminino
        if self.sexo == 'Masculino': 
            self.sexo = 'Feminino'
        # Caso o sexo seja feminino, vai ser alterado para o sexo masculino
        
        else:
            self.sexo = 'Masculino'
        
    #Altera a idade
    def alterar_idade(self,nova_idade: int):
        # Substitui a idade atual por uma nova
        self.idade = nova_idade

    #Altera o nome
    def altera_nome(self,novo_nome: str):
        # Verifica se o novo nome digitado é igual ao atual
        if self.nome == novo_nome:
            print('O nome fornecido é o mesmo!')
        # Caso não seja vai ser substituido por o novo
        else:
            self.nome = novo_nome
    #Altera a situação do atleta em relação ao covid
    def altera_situacao_covid(self):
        #Caso for positivo será alterado para negativo
        if self.covid == 'Positivo':
            self.covid ='Negativo'
        #Caso for negativo será alterado para positivo
        else:
            self.covid = 'Positivo'
    #Aletra o tipo de paralisia
    def alterar_tipo_deficiencia(self, novo_tipo:str):
        #Altera para o tipo novo de paralisia
        self.deficiencia = novo_tipo

    #Exlui uma modalidade
    def excluir_modalidade(self,modalidade:int):
        #Apaga nos dicionário de medalhdas
        del self.medalha[self.modalidade[modalidade]]
        #Apaga na lista de modalidade
        self.modalidade.pop(modalidade)
        

    #Altera adciona ou substitui uma modalidade
    def alterar_modalidade(self,nova_modalidade,modalidades, antiga_modalidade= None ):
        #Se uma modalidade antiga não for passada, a opoção de adcionar modalidade vai ser executada
        if antiga_modalidade == None:
            #Verifica se a moalidade é válida
            if nova_modalidade in modalidades:
                #Caso for adcionar a nova modalidade na lista de modaliddaes
                self.modalidade.append(nova_modalidade)
                while True:
                    #O usário precisa digitar um tipo de medalha para a nova modalidade
                    prg_medalha = int(input(f'Digite a medalha para {nova_modalidade}:\n[0] Nenhuma\n[1] Ouro\n[2] Prata\n[3] Bronze\n ->'))
                    #Verifica se a resposta é válidda
                    if 0 <=  prg_medalha <= 3:
                        #Caso digite 1, a string 'ouro' será adcionada ao dicionario de medalhas, tendo a nova modalidade como chave
                        if prg_medalha == 1:
                            self.medalha[nova_modalidade] =  'ouro'
                            break

                        #Caso digite 2, a string 'prata' será adcionada ao dicionario de medalhas, tendo a nova modalidade como chave
                        elif prg_medalha == 2:
                            self.medalha[nova_modalidade] =  'prata'
                            break

                        #Caso digite 3, a string 'ouro' será adcionada ao dicionario de medalhas, tendo a nova modalidade como chave
                        elif prg_medalha == 3:
                            self.medalha[nova_modalidade] =  'bronze'
                            break

                        #Caso digite 0, a string 'ouro' será adcionada ao dicionario de medalhas, tendo a nova modalidade como chave
                        else:
                            self.medalha[nova_modalidade] =  'nenhuma'
                            break
                    else:
                        print('Por favor selecione uma das quatro opcões!\n')
                        continue

            else:
                print('Essa modalidade não consta')
            
        #Se uma antiga modalidade for passada, a opção de substituir modalidade será executado
        else:
            #Verifica se a nova modaliddade é válida
            if nova_modalidade in modalidades:
                #Deleta os dos da antiga modalidade do dicionario medalhda
                del self.medalha[self.modalidade[antiga_modalidade]]
                #Deleda os dados da antiga modalidade da lista de modalidade
                self.modalidade.pop(antiga_modalidade)
                #Adcionar a nova modalidade na lista de modalidades
                self.modalidade.append(nova_modalidade)

                #Pede o tipo de medalha para a nova modalidade
                while True:
                    prg_medalha = int(input(f'Digite a medalha para {nova_modalidade}:\n[0] Nenhuma\n[1] Ouro\n[2] Prata\n[3] Bronze\n ->'))
                    if 0 <=  prg_medalha <= 3:
                        if prg_medalha == 1:
                            self.medalha[nova_modalidade] =  'ouro'
                            break
                        elif prg_medalha == 2:
                            self.medalha[nova_modalidade] =  'prata'
                            break
                        elif prg_medalha == 3:
                            self.medalha[nova_modalidade] =  'bronze'
                            break
                        else:
                            self.medalha[nova_modalidade] =  'nenhuma'
                            break
                    else:
                        print('Por favor selecione uma das quatro opcões!\n')
            else:
                print('Essa modalidade não consta')
                
    #Altera a medalha de determinado alteta
    def atlerar_medalhas(self,modalidade:str):
       while True:
            prg_medalha = int(input(f'Digite a medalha para {modalidade}:\n[0] Nenhuma\n[1] Ouro\n[2] Prata\n[3] Bronze\n ->'))
            if 0 <=  prg_medalha <= 3:
                if prg_medalha == 1:
                    self.medalha[modalidade] =  'ouro'
                    break
                elif prg_medalha == 2:
                    self.medalha[modalidade] =  'prata'
                    break
                elif prg_medalha == 3:
                    self.medalha[modalidade] =  'bronze'
                    break
                else:
                    self.medalha[modalidade] =  'nenhuma'
                    break
            else:
                print('Por favor selecione uma das quatro opcões!\n')

#Escreve os dados no aquivo json
def escrever_arquivo(arquivo:dict): 
    with open('dados.json', 'w', encoding = 'utf-8') as dados:
        json.dump(arquivo, dados,ensure_ascii = False, indent = 4)

#Recebe os dados do aquivo json
def obter_dados():
    atletas = {}

    #Verifica se o arquivo já existe
    if os.path.exists('dados.json'):
        #Caso exista faz a leitura
        with open('dados.json', 'r', encoding= 'utf-8') as dados:
            try:
                atletas = json.load(dados)
            except:
                pass
    #Caso não exista escreve um dicionário vazio no arquivo json
    else:
        escrever_arquivo(atletas)
    return atletas

#Busca o atleta na lista de objetos pelo nome
def buscar_alteas(lista_atletas,nome:str) -> int:
    for n,i in enumerate(lista_atletas):
        if i.nome == nome:
            #Retorna o objeto quando o usário for encontrado
            return n
    #Caso não encontre retorna -1
    return -1

#Cria objetos da classe cadastro com base nas informações dos usuários, contido no dicinário.
def transforma(diconario_atletas: dict) -> list:
    lista_atletas = []
    #Os atributos receberão os valores contido nas respectivas chaves do dicionário
    for v in diconario_atletas.values():
        atleta = Cadastro()
        atleta.nome = v['nome']
        atleta.idade = v['idade']
        atleta.sexo = v['sexo']
        atleta.covid = v['covid']
        atleta.medalha = v['medalha']
        atleta.modalidade = v['modalidade']
        atleta.deficiencia = v['deficiencia']
        lista_atletas.append(atleta)
    return lista_atletas

#Imprime todas modalidade
def mostra_modalidade(todas_modalidades:list):
    print(f"{'[ Modalidades ]':-^100}")
    for c,i in enumerate(todas_modalidades):
        print(f"{c} - {i.capitalize()}")
    print('-'*100)

#Atualiza o dicionário apartir di objeto
def atuliza_dicionario(atleta:object,dicionario_atleta:dict):
    #A chave será o nome do atleta o valor o atleta como dicionario
    dicionario_atleta[atleta.nome] = atleta.__dict__
    escrever_arquivo(dicionario_atleta)

#Faz a coleta de dados dos atletas
def coleta_dados(atletas: dict,lista_atletas: list) -> object:

    todas_modalidades =[
    'atletismo','badminton','basquetebol em cadeira de rodas','bocha','canoagem','ciclismo de estrada','ciclismo de pista','esgrima em cadeira de rodas','futebol de 5','goalball', 'hipismo','judô','levantamento de peso','natação','remo','rugby em cadeira de rodas','taekwondo','tênis de mesa','tênis em cadeira de rodas','tiro','tiro com arco','triatlo','voleibol sentado',]
    #Cria uma instância da Classe Cadatro
    atleta = Cadastro()
    while True:
        #Recebe nome que o usário deseja cadastrar
        nome = input('Nome: ').title().strip()
        #Verifica de A entrada é válida
        if nome.isnumeric() or nome == '':
            print('Por favor, Digite somente letras. Digite novamente!')
            continue
        else:
            #Verifica se o usário já foi cadastrado
            busca = buscar_alteas(lista_atletas, nome)
            if busca == -1: 
                atleta.nome = nome
                break
            else:
                print('Atleta já cadastrado, Informe outro nome!')

    while True:  
        #Recebe a idade que o usuário deseja cadatrar
        idade = input('Idade: ')
        #Verifica se a idade é um número
        if not idade.isnumeric():
            print('Sua idade deve conte somente números. Digite novamente!')
            continue
        else:
            atleta.idade = int(idade)
            break
    

    while True:
        #Recebe o sexo do usuário
        sexo = input('Sexo[M/F]: ').upper().strip()
        #Verifica se a entrada é válidade
        if sexo.isnumeric() or sexo == '':
            print('Por favor, Informe somente letras. Digite novamente!')
            continue
        else:
            #Se o usuário digitar 'M' o atributo sexo recebera 'Masculino'
            if sexo == 'M':
                atleta.sexo = 'Masculino'
            #Caso digite 'F o atributo seco receberá 'Feminino'
            else:
                atleta.sexo = 'Feminino'  
            break
    
    while True:
        #Recebe a situação do atleta em relaçao ao covid-19
        situacao_covid = input('Você foi infectado pelo Covid-19? [S/N]: ').upper().strip()
        #Verifica a entrada 
        if situacao_covid.isnumeric() or situacao_covid == '':
            print('Por favor, Informe somente letras. Digite novamente!')
            continue
        else:
            if situacao_covid == 'S':
                atleta.covid = 'Positivo'
            else:
                atleta.covid = 'Negativo'
            break
    
    while True:
        tipo_paralisia = input('Digite seu tipo de paralisia: ')
        #Verifica se a entrada é válida
        if tipo_paralisia.isnumeric() or tipo_paralisia == '':
            print('Por favor, Informe somente letras. Digite novamente!')
            continue
        else:
            atleta.deficiencia = tipo_paralisia 
            break
    while True:
        #Mostra todas modalidade disponiveis
        mostra_modalidade(todas_modalidades)

        pergunta_modalidade = int(input('Quantas modalidades deseja cadastrar? '))
        if pergunta_modalidade == 0:
            print('Você precisa cadastrar alguma modalidade!')
            continue
        else:
            #Cadastra as modalidade de acordo com o número que o usário informou
            for i in range(pergunta_modalidade):
                modalidade_temp = int(input(f'{i+1}° Modalidade: '))
                #Verifica se a entrada é válida
                if 0 <= modalidade_temp < len(todas_modalidades):
                    atleta.modalidade.append(todas_modalidades[modalidade_temp])
                else:
                    print('Modalidade não encontrada! ')
                    pergunta_modalidade += 1

            for i in atleta.modalidade:
                while True:
                    #Recebe a medalha de cada modalidade
                    print('-'*100)
                    prg_medalha = int(input(f'Digite a medalha para a modalidade {i}: \n[0] Nenhuma\n[1] Ouro\n[2] Prata\n[3] Bronze\n ->'))
                    print('-'*100)

                    if 0 <= prg_medalha <= 3:
                        if prg_medalha == 1:
                            atleta.medalha[i] = 'ouro'
                            break
                        elif prg_medalha == 2:
                            atleta.medalha[i] = 'prata'
                            break
                        elif prg_medalha == 3:
                            atleta.medalha[i] = 'bronze'
                            break
                        else:
                            atleta.medalha[i] = 'Nenhuma'
                            break
                    else:
                        print('Por favor selecione uma das quatro opcões!\n')
                        continue
            else:
                break
    return atleta

#Faz um relatório geral dos atletas
def relatório(lista_atletas,todas_modalidades):
    total_atletas = len(lista_atletas)
    diagnostico_covidp_masculino = []
    diagnostico_covidn_masculino = []
    diagnosticop_covidp_feminino = []
    diagnosticop_covidn_feminino = []
    modalidade = []
    sem_participacao = []
    quantidade_modalidade = {}
    recorte_covid_modalidade = {}
    quadro_de_medalhas = {}
    medalhas_modalidade = {}

    #Verifica cada modalidade em que os atletas estão cadastrados
    for i in lista_atletas:
        for m in i.modalidade:
            if m not in modalidade:
                #Adciona a lista
                modalidade.append(m)

        #Verfica a se o atleta é masculino, e se teve covid-19 ou não
        if (i.sexo =='Masculino'):
            if i.covid == 'Positivo':
                diagnostico_covidp_masculino.append(i)
            else:
                diagnostico_covidn_masculino.append(i)

        #Verfica a se o atleta é feminino, e se teve covid-19 ou não
        elif (i.sexo == 'Feminino'):
            if i.covid == 'Positivo':
                diagnosticop_covidp_feminino.append(i)
            else:
                diagnosticop_covidn_feminino.append(i)

    #Verifica as modalidades em que os atletas nao participaram
    for i in todas_modalidades:
        if i not in modalidade:
            sem_participacao.append(i)


    for i in modalidade:
        #Adciona ao dicionario um nova chave sendo a modalidade e o valor 0
        #Cria uma lista para cada modalidade no dicionario
        recorte_covid_modalidade[i] = []
        medalhas_modalidade[i] = []

    for i in todas_modalidades:
        quantidade_modalidade[i] = 0
        
        #Faz um recorte por modalidade dos atletas qeu tiveram covid
        for atleta in lista_atletas:
            if (atleta.covid == 'Positivo') and (i in atleta.modalidade):
                recorte_covid_modalidade[i].append(atleta)
            if (i in atleta.modalidade):
                quantidade_modalidade[i] += 1

    for i in todas_modalidades:
            quadro_de_medalhas[i] = {
                'Medalha(s) de ouro' : 0,
                'Medalha(s) de prata' : 0,
                'Medalha(s) de bronze' : 0

            }
    #Verificar a cantidade de medalha por modalidadade
    for atleta in lista_atletas:       
        for i in todas_modalidades:
            if i in atleta.medalha.keys(): 
                if atleta.medalha[i] == 'ouro':
                    quadro_de_medalhas[i]['Medalha(s) de ouro'] += 1
                    medalhas_modalidade[i].append(atleta)
                    
                elif atleta.medalha[i] == 'prata':
                    quadro_de_medalhas[i]['Medalha(s) de prata'] += 1
                    medalhas_modalidade[i].append(atleta)

                elif atleta.medalha[i] == 'bronze':
                    quadro_de_medalhas[i]['Medalha(s) de bronze'] += 1
                    medalhas_modalidade[i].append(atleta)
    
    
    print(f"{'[Relatório Geral]':_^100}\n")
    print(f'Total de Atletas cadastrados: {len(lista_atletas)}')
    print(f'Total de Atletas do sexo feminino cadastrados: {len(diagnosticop_covidp_feminino) + len(diagnosticop_covidn_feminino)}')
    print(f'Total de Atletas do sexo masculino cadastrados: {len(diagnostico_covidp_masculino) + len(diagnostico_covidn_masculino)}\n')
 

    print(f"{'[Diagnostico Covid-19]':_^100}\n")
    print(f'Total de atletas infectados: {len(diagnostico_covidp_masculino) + len(diagnosticop_covidp_feminino)} Alteta(s)')
    print(f'Atleta(s) masculino infectados: {len(diagnostico_covidp_masculino)} Atleta(s)')
    print(f'Atleta(s) feminino infectados: {len(diagnosticop_covidp_feminino)} Atleta(s)\n')

    print(f"{'[Modalidade que os atletas Brasileiros participaram]':_^100}\n")
    print(f'Total de modalidades : {len(modalidade)}')
    for i in sorted(modalidade):
        print(f'+ {i.capitalize()}')
    print()

    print(f"{'[Modalidade que os atletas Brasileiros não participaram]':_^100}\n")
    print(f'Total de modalidades : {len(sem_participacao)}')
    for i in sorted(sem_participacao):
        print(f'- {i.capitalize()}')
    print()
    
    #Imprimi as modalidades por ordem alfabetica
    print(f"{'[Dados por modalidade]':_^100}\n")
    for k,v in sorted(quantidade_modalidade.items()):
        print(f"{'['+k.capitalize()+']':-^100}|")
        print(f"{f'Números de Alteta(s) cadastrado: {v}':^100}")
        print()
        print(f'[Quadro de Medalhas]')
        for i,c in quadro_de_medalhas[k].items():
            print(f'{i} : [{c}]')
        print()

        #Caso a modalidade tenha ganhado medalha vai imprimir as informações mos atletas
        atletas = medalhas_modalidade.get(k,None)
        if atletas != None:
            print(f"{'[Atletas que conquistaram medalha]'}")
            print()
            for i in atletas:
                print(i.__str__(True))
            
        #Caso a modalidade tenha casos de covid, vai imprimir  os atletas que foram infectados
        recorte_covid_mo = recorte_covid_modalidade.get(k,None)
        print(f"{'[Diagnostico Covid-19]'}")

        if recorte_covid_mo != None:
            print(f'Quantidade de altetas Infectados: {len(recorte_covid_mo)}')
            print()
            for i in recorte_covid_mo:
                print(i.__str__(True))
        else:
            print(f'Quantidade de altetas Infectados: 0')
    print()
    print(f"{'[Quadro de medalhas por sexo]':-^100}\n")


    #Quantidade de medalha por sexo masculino
    masculino_temp = []
    cont_masculino = 0
    for i in medalhas_modalidade.values():
        for a in i:
            #Verifica o sexo do altleta
            if a.sexo == 'Masculino':
                #Caso as informações dele ainda não forma mostradas, será imprimido os dados
                #Cada atleta só poderá ser mostrado uma vez
                cont_masculino += 1
                if a not in masculino_temp or not masculino_temp:
                    masculino_temp.append(a)
    
    feminino_temp = []
    cont_feminino = 0
    for i in medalhas_modalidade.values():
        for a in i:
            if a.sexo == 'Feminino':
                cont_feminino += 1
                if a not in feminino_temp or not feminino_temp:
                        feminino_temp.append(a)

    print(f"{'[Sexo Feminino]':_^100}\n")
    print(f"{f'Medalhas conquistados por atletas do sexo feminino: {cont_feminino}':^100}\n")
    if not feminino_temp:
        print('Nenhum atleta do sexo feminino  ganhou medalha!\n')
    else:
        for atleta in feminino_temp:
            print(atleta)          
    print(f"{'[Sexo Masculino]':_^100}\n")
    print(f"{f'Medalhas conquistados por atletas do sexo masculino: {cont_masculino}':^100}\n") 
    if not masculino_temp:
        print('Nenhum atleta do sexo feminino  ganhou medalha!\n')
    else:
        for atleta in masculino_temp:
            print(atleta)                    
    



        










