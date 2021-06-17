import random # biblioteca que gera número aleatório


record = []
def insert(idade, peso, altura, olhos_cor, cabelo_cor):
    """       
        coluna      0     1        2          3               4 
                | idade | peso | altura | cor dos olhos | cor do cabelo |
        linha 0 |   18  | 90   | 186    | c             |    c          |
        linha 1 |   18  | 86   | 186    | c             |    c          |

        Para acessar um valor da matriz é necessário digitar a linha e a coluna.
        Por exemplo quero acessa o primeiro registo(linha 0) e o peso(coluna 1): record[0][1]
    """
    tupla  = []
    tupla.append(idade) # idade
    tupla.append(peso) # peso
    tupla.append(altura) # altura em centimetro
    tupla.append(olhos_cor) # cor dos olhos
    tupla.append(cabelo_cor) # cor do cabelo
    
    return tupla


def record_add(tupla):
    record.append(tupla)
    

def get_column(record, column_number):
    column = []
    for i in range(len(record)):
        column.append(record[i][column_number])
    return column


def mean(column):
    return float(sum(column)) / len(column)
    
    
if __name__ == "__main__" :
    QUANTIDADE_DE_REGISTRO = 2 # quantidade de tuplas do registro

    for i in range(QUANTIDADE_DE_REGISTRO):
        tuple_iterator = insert(
            (random.randint(18,65)), # idade
            (random.randint(40,180)), # peso
            (random.randint(140,210)), # altura em centimetro
            ('a'), # cor dos olhos
            ('c'), # cor do cabelo
        )
        record_add(tuple_iterator)
        
    print("todo o registro:", record)

    peso = get_column(record, 0)
    print(mean(peso))
    