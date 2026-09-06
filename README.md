# 🩸 Automação de Dados de Saúde — DATASUS

Script em **Python + pandas** que limpa e padroniza uma extração do **DATASUS** sobre
quantidade de bolsas de sangue por município do Paraná e gera uma planilha pronta
para análise.

## 🎯 Problema

A exportação do DATASUS traz o nome do município colado ao código do IBGE
(`410690 CURITIBA`), entre aspas, em caixa alta, e inclui linhas sem valor.
Assim não dá para cruzar com outras bases nem apresentar direto.

## 🔄 O que o script faz

**Entrada:** `raw/municipio.csv` (separado por `;`)

1. Remove o código numérico do IBGE do início do nome do município
2. Remove aspas e espaços sobrando
3. Padroniza o texto para Nome Próprio (`Foz Do Iguacu`)
4. Renomeia a coluna de valor para `Quantidade de Bolsas de Sangue`
5. Converte os valores para número e descarta municípios sem registro (total ≤ 0)

**Saída:** `clean/clean_data.xlsx`

## 🛠️ Tecnologias

- Python 3
- pandas
- openpyxl (escrita do `.xlsx`)

## 📁 Estrutura

```
.
├── raw/
│   ├── extracaohemobanco.py   # script de limpeza
│   └── municipio.csv          # dados brutos do DATASUS
└── clean/
    └── clean_data.xlsx        # resultado
```

## ▶️ Como executar

```bash
pip install pandas openpyxl
python raw/extracaohemobanco.py
```

Os caminhos são resolvidos a partir do próprio script, então funciona de qualquer
diretório. O arquivo `clean/clean_data.xlsx` é sobrescrito a cada execução.

## 📊 Sobre os dados

Dados públicos e **agregados por município** (DATASUS / hemocentros do Paraná).
Não há informação pessoal.

## 👤 Autoria

Desenvolvido por **Giovanna Ribas dos Reis** — projeto individual.

## 🧭 Próximos passos possíveis

- Receber o nome do arquivo de entrada por parâmetro, em vez de fixo no código
- Detectar a coluna de ano automaticamente, em vez do valor `'2026'` fixo

## 🤖 Transparência

O código deste projeto é de autoria própria, sem geração por IA.
