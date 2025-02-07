from flask import Flask, render_template, request, send_file
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Receber arquivos do formulário
        file1 = request.files["file1"]
        file2 = request.files["file2"]
        reference_column = int(request.form["reference_column"]) - 1
        start_row = int(request.form["start_row"]) - 1

        # Salvar arquivos temporariamente
        path1 = os.path.join(UPLOAD_FOLDER, file1.filename)
        path2 = os.path.join(UPLOAD_FOLDER, file2.filename)
        file1.save(path1)
        file2.save(path2)

        # Ler arquivos
        ex1 = pd.read_excel(path1, header=None, skiprows=start_row)
        ex2 = pd.read_excel(path2, header=None, skiprows=start_row)

        ex1 = ex1.astype(str)
        ex2 = ex2.astype(str)

        updated_rows = []
        inserted_rows = []

        ex1_references = set(ex1[reference_column])

        for _, row2 in ex2.iterrows():
            ref_value = row2[reference_column]
            if ref_value in ex1_references:
                row1 = ex1[ex1[reference_column] == ref_value].iloc[0]
                if not row1.equals(row2):
                    updated_rows.append(row1.tolist() + ["→"] + row2.tolist())
            else:
                inserted_rows.append(row2.tolist())

        output_path = os.path.join(UPLOAD_FOLDER, "Resultado.xlsx")

        with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
            if updated_rows:
                df_updated = pd.DataFrame(updated_rows, dtype=object)
                df_updated = df_updated.map(lambda x: np.nan if x == "nan" else x)
                df_updated.dropna(axis=1, how="all", inplace=True)
                df_updated.to_excel(writer, sheet_name="Dados Atualizados", index=False, header=False)

            if inserted_rows:
                df_inserted = pd.DataFrame(inserted_rows, dtype=object)
                df_inserted = df_inserted.map(lambda x: np.nan if x == "nan" else x)
                df_inserted.dropna(axis=1, how="all", inplace=True)
                df_inserted.to_excel(writer, sheet_name="Dados Inseridos", index=False, header=False)

        return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
