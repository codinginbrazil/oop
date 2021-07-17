import math


class Cpf(object):
    """ Etapas:
        - Primeira: Verificar se o CPF informado contém todos os dígidos nem são repetidos
        - Segunda: Confirmar se o primeiro dígito do verificador está correto
        - Terceira: Confirmar se o segundo dígito do verificador está correto
        - Quarta: Validar o CPF
        - Quinta: Informar o estado emissor do CPF
    """

    _cpf = []

    def __init__(self, cpf):
        self._cpf = self.str2int(cpf)
        if(not self.verificar()):
            self._cpf = False

    def str2int(self, string):
        inteiro = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(string)):
            inteiro[i] = int(string[i])
        return inteiro

    def verificar_valores_heterogenicos(self):
        controle = False
        for i in range(11):
            if (self._cpf[1] != self._cpf[i]):
                controle = True
        return controle

    def verificar_digito(self, digito):
        quociente = sum = 0
        resto_divisao = None

        for i in range(8 + digito):
            """ # Dígito verificador
                # Primeiro Dígito
                # Distribua os 9 primeiros dígitos em um quadro (Ex.: cpf[i]);
                # Atribuindo pesos respectivos a eles: seguindo a fórmula: 8 + 1 - i;
                # Multiplique os valores de cada coluna (Ex.: sum += (cpf[i] * (9 + 1 - i)))
                # Esquematizando:
                #             01	01	01	04	04	04	07	07	07
                #          x  10	09	08	07	06	05	04	03	02
                #             ------------------------------------
                #             10	09	08	28	24	20	28	21	14
                # Segundo Dígito
                # Distribua os 10 primeiros dígitos em um quadro (Ex.: cpf[i]);
                # Atribuindo pesos respectivos a eles: seguindo a fórmula: 8 + 2 - i;
                # Multiplique os valores de cada coluna (Ex.: sum += (cpf[i] * (9 + 2- i)))
                # Esquematizando:
                #             01	01	01	04	04	04	07	07	07  03
                #          x  11	10	09	08	07	06	05	04	03	02
                #             -----------------------------------------
                #             11	10	09	32	28	24	35	28	21	06
            """
            sum += (self._cpf[i] * (9 + digito - i))
        sum /= 11

        quociente = int(sum)
        resto_divisao = math.ceil((sum - quociente) * 10)

        if (resto_divisao < 2):
            return (0)
        else:
            return (11 - resto_divisao)

    def verificar(self):
        return (
            (len(self._cpf) == 11) and
            (self.verificar_valores_heterogenicos) and
            (self._cpf[9] == self.verificar_digito(1)) and
            (self._cpf[10] == self.verificar_digito(2))
        )

    def estado_emissor(self):
        estado = self._cpf[8]
        if estado == 0:
            return 'Rio Grande do Sul'
        elif estado == 1:
            return 'Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins;'
        elif estado == 2:
            return 'Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima'
        elif estado == 3:
            return 'Ceará, Maranhão ou Piauí'
        elif estado == 4:
            return 'Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas'
        elif estado == 5:
            return 'Bahia ou Sergipe'
        elif estado == 6:
            return 'Minas Gerais'
        elif estado == 7:
            return 'Rio de Janeiro ou Espírito Santo'
        elif estado == 8:
            return 'São Paulo'
        elif estado == 9:
            return 'Paraná ou Santa Catarina'
        else: 
            return 'Error: Emissor do CPF desconhecido'