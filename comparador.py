import pandas as pd
import numpy as np

# Função para detectar colunas de data e formatá-las corretamente
def format_dates(df):
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.strftime('%d/%m/%Y')  # Formato brasileiro
    return df

# Solicitar ao usuário a escolha da coluna de referência e da linha inicial
reference_column = int(input("Informe o número da coluna de referência (começando do 1 | Exemplo: 1 = A, 2 = B, 3 = C, etc...): ")) - 1
start_row = int(input("Informe a linha inicial da verificação (começando do 1): ")) - 1

# Carregar os arquivos
file_ex1_path = 'Ex1.xls'
file_ex2_path = 'Ex2.xls'

ex1 = pd.read_excel(file_ex1_path, header=None, skiprows=start_row)
ex2 = pd.read_excel(file_ex2_path, header=None, skiprows=start_row)

# Converter todos os valores para string
ex1 = ex1.astype(str)
ex2 = ex2.astype(str)

# Criar dataframes para armazenar os resultados
updated_rows = []
inserted_rows = []

# Criar um conjunto de referências para ex1
ex1_references = set(ex1[reference_column])

# Iterar pelas linhas do ex2 para identificar atualizações e inserções
for _, row2 in ex2.iterrows():
    ref_value = row2[reference_column]
    if ref_value in ex1_references:
        row1 = ex1[ex1[reference_column] == ref_value].iloc[0]
        if not row1.equals(row2):
            updated_rows.append(row1.tolist() + ["→"] + row2.tolist())
    else:
        inserted_rows.append(row2.tolist())

# Criar um DataFrame para salvar no Excel
with pd.ExcelWriter("Resultado.xlsx", engine="xlsxwriter") as writer:
    if updated_rows:
        df_updated = pd.DataFrame(updated_rows, dtype=object)
        df_updated = df_updated.map(lambda x: np.nan if x == "nan" else x)
        df_updated.dropna(axis=1, how='all', inplace=True)  # Remover colunas vazias
        df_updated.to_excel(writer, sheet_name="Dados Atualizados", index=False, header=False)
    
    if inserted_rows:
        df_inserted = pd.DataFrame(inserted_rows, dtype=object)
        df_inserted = df_inserted.map(lambda x: np.nan if x == "nan" else x)
        df_inserted.dropna(axis=1, how='all', inplace=True)  # Remover colunas vazias
        df_inserted.to_excel(writer, sheet_name="Dados Inseridos", index=False, header=False)

print("Comparação concluída. Resultado salvo em 'Resultado.xlsx'.")
