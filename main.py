from fpdf import FPDF
import tkinter as tk
from tkinter import ttk
import re


def validar_numero_e_letra(texto):
    pattern = r'^[a-zA-Z0-9]+$'
    return re.match(pattern, texto) is not None


def validar_data(data):
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    return re.match(pattern, data)


def validar_valor(valor):
    pattern = r'^\d{1,}\,\d{2}$'
    return re.match(pattern, valor)


def validar_texto(texto):
    pattern = r'^[A-Za-zÀ-ú\s]+$'
    return re.match(pattern, texto)


def validar_numeros(numeros):
    pattern = r'^[\d/-]+$'
    return re.match(pattern, numeros)


class PDF(FPDF):
    def header(self):
        self.set_font('Times', 'B', 10)
        self.cell(0, 6, 'CONTRATO LOCAÇÃO RESIDENCIAL', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Times', 'B', 10)
        self.cell(0, 6, title, 0, 1, 'L')

    def chapter_body(self, body):
        self.set_font('Times', '', 10)
        self.multi_cell(0, 4, body.encode(
            'latin-1', 'replace').decode('latin-1'))
        self.ln(1)


def gerar_contrato():
    try:
        nome_locatario = nome_locatario_entry.get().upper()
        cpf_locatario = cpf_locatario_entry.get().upper()
        identidade_locatario = identidade_locatario_entry.get().upper()
        endereco_locacao = endereco_locacao_entry.get().upper()
        data_inicio = data_inicio_entry.get().upper()
        valor_numeral = valor_numeral_entry.get().upper()
        valor_discurso = valor_discurso_entry.get().upper()
        dia_vencimento = dia_vencimento_entry.get().upper()
        data_assinatura = data_assinatura_entry.get().upper()
        nomearquivo_label = nome_arquivo_entry.get()

        if not validar_numero_e_letra(nomearquivo_label):
            resultado_label.config(
                text="Nome de arquivo inválido , use somente letras e números ")
            return

        if not validar_texto(nome_locatario):
            resultado_label.config(
                text="Nome do Locatario inválido , tente somente texto")
            return

        if not validar_numeros(cpf_locatario):
            resultado_label.config(
                text="CPF do Locatario inválido, tente somente números e símbolos")
            return

        if not validar_numeros(identidade_locatario):
            resultado_label.config(
                text="Identidade do Locatario inválido, tente somente números e símbolos")
            return

        if not validar_data(data_inicio):
            resultado_label.config(
                text="Data errada, tente no formato correto")
            return

        if not validar_numeros(valor_numeral):
            resultado_label.config(
                text="Valor inválido, tente somente números")
            return

        if not validar_texto(valor_discurso):
            resultado_label.config(text="Valor inválido, tente somente texto")
            return

        if not validar_numeros(dia_vencimento):
            resultado_label.config(text="Dia inválido, tente somente números")
            return

        if not validar_data(data_assinatura):
            resultado_label.config(
                text="Data errada, tente no formato correto")
            return

        # Nome do arquivo PDF de saída
        nome_arquivo = f"{nomearquivo_label}.pdf"

        # Criação do PDF com formatação
        pdf = PDF()
        pdf.add_page()

        corpo_contrato = f"""
NOMELOCADORAQUI, CPF CPFLOCADORAQUI, IDENTIDADE IDENTIDADELOCADORAQUI, residente a RUALOCADOR LOTE Nª, BAIRRO , CIDADE  ESTADO PAÍS doravante denominado LOCATARIO: {nome_locatario}  ,CPF {cpf_locatario} , IDENTIDADE {identidade_locatario} doravante denominado LOCATÁRIO, celebram o presente contrato de locação residencial, com as cláusulas e condições seguintes:

1) O LOCADOR cede para locação residencial ao LOCATÁRIO, o imóvel situado à {endereco_locacao},.

2) A locação destina-se ao uso exclusivo como residência e domicílio do LOCATÁRIO.

3) O prazo de locação é de INDETERMINADO, iniciando-se em {data_inicio} e terminando em A COMBINAR, limite de tempo em que o imóvel objeto do presente deverá ser restituído independentemente de qualquer notificação ou interpelação sob pena de caracterizar infração contratual.

4) O aluguel mensal será de (R$ {valor_numeral}  {valor_discurso}), e deverá ser pago até a data de seu vencimento, todo dia {dia_vencimento} do mês seguinte ao vencido, no local do endereço do LOCADOR ou outro que o mesmo venha a designar.

4.1) A impontualidade acarretará juros moratórios na base de 1% (um por cento) ao mês calculado sobre o valor do aluguel. O atraso superior a 30 (trinta) dias implicará em correção monetária do valor do aluguel e encargos de cobrança correspondentes a 10% (dez por cento) do valor assim corrigido.

4.2) O pagamento de qualquer dos aluguéis não implica em renúncia do direito de cobrança de eventuais diferenças de aluguéis, de encargos ou impostos que oportunamente não tiverem sido lançados nos respectivos recibos.

5) O aluguel será reajustado anualmente pela variação do IGPM. Entretanto, se em virtude de lei subsequente vier a ser admitida a correção e periodicidade inferior a prevista na legislação vigente à época de sua celebração, que é anual, concordam as partes desde já e em caráter irrevogável que a correção do aluguel e o seu indexador passará automaticamente a ser feito no menor prazo que for permitido pela lei posterior e pelo maior índice vigente dentre os permitidos pelo Governo Federal e que venha a refletir a variação do período.

6) Havendo prorrogação tácita ou expressa do presente contrato o mesmo será reajustado a preço de mercado sem qualquer relação com o patamar aqui pactuado a ser estabelecido pelo LOCADOR, que poderá ainda estipular, de comum acordo com o LOCATÁRIO, o índice de reajuste e periodicidade.

7) Nas cobranças judiciais e extrajudiciais de aluguéis em atraso os mesmos serão acrescidos de juros de mora, atualização monetária e honorários advocatícios, na base de 20% (vinte por cento ) sendo que qualquer recebimento feitos pela LOCADOR fora dos prazos e condições convencionais neste contrato, será havido como mera tolerância e não induzirá novação bem como resgate de recibos posteriores não significará quitação de aluguéis e outras obrigações contratuais deixadas de quitar nas épocas certas.

8) O imóvel da presente locação destina-se ao uso exclusivo como residência e domicílio do LOCATÁRIO, conforme cláusula 2, não sendo permitida a transferência, sublocação, cessão ou empréstimo no todo ou em parte, sem a prévia e expressa autorização do LOCADOR.

9) Além do aluguel são de responsabilidade do LOCATÁRIO as despesas com consumo de luz, água, esgoto, seguro contra incêndio, imposto predial e todas as demais taxas ou impostos, tributos municipais e encargos da locação, que venham a incidir sobre o imóvel, inclusive taxa de condomínio, que deverão ser pagas diretamente pela mesma, o qual ficará obrigada a apresentar os comprovantes de quitação juntamente com o pagamento do aluguel.

10) Encerrada a locação a entrega das chaves só será processada mediante exibição ao LOCADOR, dos comprovantes de quitação das despesas e encargos da locação referidos nas cláusulas anteriores, inclusive corte final de luz.

11) Fica facultado ao LOCADOR ou ao seu representante legal vistoriar o imóvel sempre que julgar necessário.

12) O LOCATÁRIO se obriga, sob pena de cometer infração contratual, a comunicar por escrito ao LOCADOR, com antecedência mínima de 30 (trinta) dias, a sua intenção de devolver o imóvel antes do prazo aqui previsto.

13) O LOCATÁRIO assume o compromisso de solicitar ao LOCADOR uma vistoria 30 (trinta) dias antes de desocupar o imóvel para ser constatado o estado de conservação do mesmo.

14) Quaisquer modificações no imóvel locado só poderão ser feitas com expressa autorização do LOCADOR. Aderem ao mesmo as benfeitorias sejam elas úteis, necessárias ou voluntárias independente de sua natureza, não cabendo direito de indenização, retenção, compensação ou reembolso.

15) Se no curso da locação vier a ocorrer incêndio ou danos no prédio que demandem obras que impeçam o seu uso normal por mais de 30 (trinta) dias, falência ou insolvência do LOCATÁRIO, bem como desapropriação do imóvel, ficará rescindida de pleno direito a relação locatícia, sem qualquer direito de indenização ou retenção do objeto do presente contrato.

16) O LOCATÁRIO autoriza ao LOCADOR desde já, a proceder a sua citação inicial, interpelação, intimação, notificação, ou qualquer outro ato de comunicação processual mediante correspondência ou aviso de recebimento, mediante telegrama ou fax símile, afora as demais formas previstas em lei.

17) Fica convencionado que a parte que infringir o presente contrato em qualquer dos seus termos, se sujeita ao pagamento em benefício da outra, da multa contratual correspondente a 1 (uma) vez o valor do aluguel vigente à época da infração, tantas vezes forem as infrações praticadas, sem prejuízo da resolução contratual e demais comunicações previstas neste instrumento.

18) Se o LOCATÁRIO vier a usar da faculdade que lhe confere o contido no artigo 4º da Lei n º 8.245/1991 e devolver o imóvel antes do vencimento do prazo ajustado, pagará a multa compensatória equivalente a 02 (duas) vezes o valor do aluguel vigente, reduzido proporcionalmente ao tempo do contrato já cumprido.

19) Salvo declaração escrita do LOCADOR, quaisquer tolerância ou concessões por ela feita não implicam em renúncia de direito ou em alteração contratual, não podendo ser invocada pelo LOCATÁRIO como procedente para se furtar ao cumprimento do contrato.

20) Permanecendo o LOCATÁRIO no imóvel após o prazo de desocupação voluntária nos casos de denúncia condicionada, pagará ele o aluguel pena que vier a ser arbitrado na notificação premonitória na forma de que dispõe o artigo 575 do Novo Código Civil Brasileiro, o mesmo ocorrendo no caso de mútuo acordo nos termos do artigo 9, inciso I da Lei n º 8.245/1991, quando a desocupação não se verificar na data convencionada.

21) O LOCATÁRIO declara, para todos os fins e efeitos de direito, que recebe o imóvel locado em condições plenas de uso, em perfeito estado de conservação, higiene e limpeza, obrigando-se e comprometendo-se a devolvê-lo em iguais condições, independente de qualquer aviso ou notificação prévia, e qualquer que seja o motivo da devolução, sob pena de incorrer nas cominações previstas neste contrato ou estipuladas em lei, além da obrigação de indenizar por danos ou prejuízos decorrentes da inobservância desta obrigação, salvo as deteriorações decorrentes de uso normal do imóvel.

22) Em caso de ausência, interdição, recuperação judicial, falência ou insolvência do fiador, declaradas judicialmente, suas obrigações se transferem aos seus herdeiros e/ou sucessores e o LOCATÁRIO se obriga, dentro de 30 (trinta) dias a dar substituto idôneo, a juízo do LOCADOR, ficando aquele em mora e sujeito à multa contratual e despejo, se não o fizer nesses dias de mera tolerância.

23) Elegem as partes o foro do domicílio do LOCADOR, para dirimir quaisquer dúvidas oriundas do presente contrato, renunciando a qualquer outro por mais privilegiado que seja.

E por estarem LOCADOR e LOCATÁRIO de pleno acordo com o disposto neste instrumento particular, assinam-no na presença das duas testemunhas abaixo, em 02 vias de igual teor e forma, destinando-se uma via para cada uma das partes.
CIDADELOCADOR e Data: {data_assinatura}

LOCADOR : ______________________

LOCATÁRIO : ______________________
"""

        pdf.chapter_body(corpo_contrato)

        # Salvar o PDF
        pdf.output(nome_arquivo)

        # Mostrar uma mensagem de sucesso
        resultado_label.config(text="Contrato gerado com sucesso!")
    except Exception as e:
        resultado_label.config(text=f"Erro: {str(e)}")

# Resto do código para criar a interface tkinter permanece o mesmo


# Iniciar a interface do tkinter
janela = tk.Tk()
janela.title("Gerador de Contrato")
janela.geometry("600x870")

# Centralizar horizontalmente todos os elementos
janela.grid_columnconfigure(0, weight=1)

# Título
titulo_label = tk.Label(janela, text="Gerador de Contrato",
                        font=("Helvetica", 26, "bold"))
titulo_label.pack(pady=20)  # Espaçamento entre o título e os elementos abaixo

# Nome do arquivo
label_nome_arquivo = tk.Label(janela, text="Nome do arquivo:", font=("Helvetica", 12, "bold"))
label_nome_arquivo.pack()
nome_arquivo_entry = ttk.Entry(janela, style="Estilo.TEntry")
nome_arquivo_entry.pack(pady=10)

# Nome do Locatário
label_nome_locatario = tk.Label(janela, text="Nome do Locatário:", font=("Helvetica", 12, "bold"))
label_nome_locatario.pack()
nome_locatario_entry = ttk.Entry(janela, style="Estilo.TEntry")
nome_locatario_entry.pack(pady=10)

# CPF do Locatário
label_cpf_locatario = tk.Label(janela, text="CPF do Locatário:", font=("Helvetica", 12, "bold"))
label_cpf_locatario.pack()
cpf_locatario_entry = ttk.Entry(janela, style="Estilo.TEntry")
cpf_locatario_entry.pack(pady=10)

# Identidade do Locatário
label_identidade_locatario = tk.Label(janela, text="Identidade do Locatário:", font=("Helvetica", 12, "bold"))
label_identidade_locatario.pack()
identidade_locatario_entry = ttk.Entry(janela, style="Estilo.TEntry")
identidade_locatario_entry.pack(pady=10)

# Endereço de Locação
label_endereco_locacao = tk.Label(janela, text="Endereço de Locação:", font=("Helvetica", 12, "bold"))
label_endereco_locacao.pack()
endereco_locacao_entry = ttk.Entry(janela, style="Estilo.TEntry")
endereco_locacao_entry.pack(pady=10)

# Data de Início
label_data_inicio = tk.Label(janela, text="Data de Início (ex: 30/11/2000):", font=("Helvetica", 12, "bold"))
label_data_inicio.pack()
data_inicio_entry = ttk.Entry(janela, style="Estilo.TEntry")
data_inicio_entry.pack(pady=10)

# Valor Numeral
label_valor_numeral = tk.Label(janela, text="Valor Numeral (ex: 1000,00):", font=("Helvetica", 12, "bold"))
label_valor_numeral.pack()
valor_numeral_entry = ttk.Entry(janela, style="Estilo.TEntry")
valor_numeral_entry.pack(pady=10)

# Valor por Extenso
label_valor_discurso = tk.Label(janela, text="Valor por Extenso (ex: MIL REAIS):", font=("Helvetica", 12, "bold"))
label_valor_discurso.pack()
valor_discurso_entry = ttk.Entry(janela, style="Estilo.TEntry")
valor_discurso_entry.pack(pady=10)

# Dia de Vencimento
label_dia_vencimento = tk.Label(janela, text="Dia de Vencimento (ex: 25):", font=("Helvetica", 12, "bold"))
label_dia_vencimento.pack()
dia_vencimento_entry = ttk.Entry(janela, style="Estilo.TEntry")
dia_vencimento_entry.pack(pady=10)

# Data da Assinatura
label_data_assinatura = tk.Label(janela, text="Data da Assinatura (ex: 30/11/2000):", font=("Helvetica", 12, "bold"))
label_data_assinatura.pack()
data_assinatura_entry = ttk.Entry(janela, style="Estilo.TEntry")
data_assinatura_entry.pack(pady=10)

# Botão estilizado
estilo_botao = ttk.Style()
estilo_botao.configure("Estilo.TButton",
                       padding=10,
                       font=("Helvetica", 12),                       
                       borderwidth=0,
                       )


botao = ttk.Button(janela, text="Gerar Contrato",
                   command=gerar_contrato, style="Estilo.TButton")
botao.pack(pady=20)

# Label para mostrar o resultado
resultado_label = tk.Label(janela, text="", font=("Helvetica", 12))
resultado_label.pack()

# Iniciar a interface do tkinter
if __name__ == "__main__":
    janela.mainloop()
    