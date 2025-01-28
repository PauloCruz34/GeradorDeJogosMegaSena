
import random
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from collections import Counter

# Simulação dos dados dos sorteios do último ano (substitua por dados reais se disponível)
sorteios_ultimo_ano = [
    [7, 15, 23, 34, 45, 56],
    [5, 12, 23, 34, 45, 59],
    [7, 14, 21, 36, 42, 59],
    [3, 18, 25, 37, 49, 60],
    # Adicione mais sorteios aqui...
]

# Contar a frequência de cada número
frequencia_numeros = Counter()
for sorteio in sorteios_ultimo_ano:
    frequencia_numeros.update(sorteio)

# Selecionar os 45 números mais frequentes
numeros_mais_frequentes = [num for num, _ in frequencia_numeros.most_common(45)]

def gerar_jogo(numeros_mais_frequentes):
    # Escolhe 6 números aleatórios entre os 45 mais frequentes
    return sorted(random.sample(numeros_mais_frequentes, 7))

def gerar_jogos_mega_sena(quantidade, numeros_mais_frequentes):
    jogos = []
    for _ in range(quantidade):
        jogo = gerar_jogo(numeros_mais_frequentes)
        jogos.append(jogo)
    return jogos

def criar_pdf(jogos, filename="jogos_mega_sena.pdf"):
    # Configurações do PDF
    pdf = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    conteudo = []

    # Título do PDF
    titulo = Paragraph("Jogos da Mega-Sena (Baseados nos 45 números mais frequentes)", styles['Title'])
    conteudo.append(titulo)
    conteudo.append(Spacer(1, 12))

    # Preparar os dados para a tabela
    dados = []
    for i, jogo in enumerate(jogos, start=1):
        dados.append([f"Jogo {i}:", ", ".join(map(str, jogo))])

    # Criar a tabela
    tabela = Table(dados, colWidths=[50, 300])
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    conteudo.append(tabela)
    pdf.build(conteudo)

# Definir a quantidade de jogos (até 500)
quantidade_jogos = 500

# Gerar os jogos usando os 45 números mais frequentes
jogos_gerados = gerar_jogos_mega_sena(quantidade_jogos, numeros_mais_frequentes)

# Criar o PDF
criar_pdf(jogos_gerados)
print(f"PDF criado com sucesso: jogos_mega_sena.pdf (Baseado nos 45 números mais frequentes)")
