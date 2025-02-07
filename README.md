# 📊 Comparador de Arquivos para Excel *(FCEx 1.0)*

## 🔎 Um sistema que compara dois arquivos **Excel** e identifica:
✔️ **Alterações** feitas nos dados.  
✔️ **Novos itens adicionados** ao segundo arquivo.  
✔️ **Saída organizada** em um novo Excel.  
✔️ **Interface Web** para facilitar o uso.  

---

## **📌 Funcionalidades**
✅ O usuário escolhe **dois arquivos Excel** para comparar.  
✅ O sistema verifica **qual coluna será usada como referência**.  
✅ Identifica **diferenças linha por linha e coluna por coluna**.  
✅ Gera um **arquivo Excel com os resultados** da comparação.  
✅ Interface web simples usando **Flask** para facilitar o uso.  

---

## **📂 Estrutura do Projeto**

```
📁 fcex
│── 📁 templates
│   ├── index.html      # Página da interface web
│── app.py              # Código principal (Flask + Lógica de comparação)
│── comparador.py       # Código para execução sem interface web
│── LICENSE             # Informações referente a licença MIT
│── README.md           # Este arquivo
```
* **Obs.:** *O script via intarface web, cria uma nova pasta nomeada "uploads" ao iniciar a verificação dos arquivos. É nessa pasta que ele armazena os arquivos em analise.*
---

## **💻 Como Rodar o Projeto**

### 🔹 **Rodar via Terminal (Modo CLI)**
Se quiser rodar o comparador direto pelo terminal (sem interface gráfica):  

1️⃣ **Instale as dependências**  
```sh
pip install pandas numpy xlsxwriter
```
2️⃣ **Execute o script**  
```sh
python comparador.py
```
3️⃣ **Informe os parâmetros solicitados**.

* **Obs.:** *Ao usar o script via terminal, os arquivos devem ser lançados na mesma pasta e renomeados, o arquivo original para “Ex1.xls” e o arquivo atualizado para “Ex2.xls”. O script gera um novo arquivo, “Resultado.xls”, na mesma pasta com o resultado da análise.*

---

### 🔹 **Rodar via Interface Web (Flask)**
Se preferir usar a **interface web**, siga os passos abaixo:  

1️⃣ **Instale as dependências**  
```sh
pip install flask pandas numpy xlsxwriter
```
2️⃣ **Execute o servidor Flask**  
```sh
python app.py
```
3️⃣ **Acesse no navegador**  
```
http://127.0.0.1:5000
```
4️⃣ **Envie os arquivos Excel e clique para comparar!**

5️ **Ao finalizar a analise, para encerrar o sistema, tecle no terminal CTRL + C.**

---

## **📊 Exemplo de Saída**
Após a verificação, o sistema gera um **arquivo Excel** com **duas abas**:  

- 📄 **"Dados Atualizados"** → Exibe as **alterações** linha por linha.  
- 📄 **"Dados Inseridos"** → Exibe os **novos itens adicionados**.  

---

## **⚠ Lembretes**
✔️ *Para a leitura correta dos arquivos é importante se certificar que os dois arquivos tenham os mesmos parâmetros. Ou seja, os dados têm que iniciar na mesma linha, além de ser analisadas as mesmas colunas em ambas.*     
✔️ *Caso seja necessário, remova as colunas, ou linha extras, que não fazem parte da análise.*  
✔️ *Se o arquivo contém várias abas, uma alternativa é salvar os dados da aba em analise em um arquivo à parte.* 
 

---

## **🛠 Tecnologias Usadas**
✔️ **Python**  
✔️ **Flask** (para interface web)  
✔️ **Pandas** (para manipulação de dados)  
✔️ **XlsxWriter** (para gerar arquivos Excel)  

---

## **📌 Melhorias Futuras** 
🔹 Melhorar a interface web.    
🔹 Habilitar a função para escolher a origem dos arquivos no script “comparador.py”.    
🔹 Alterar o formato da data, e valores monetários, para o padrão brasileiro.   
🔹 Criar uma terceira aba no arquivo de retorno, “Resultado.xls”, para exibir os dados que foram removidos do arquivo original.      
🔹 Adicionar suporte para arquivos CSV.     


---

## **🖥 Créditos**
🤖 "Durante o desenvolvimento deste projeto, utilizei o **ChatGPT** como assistente para o código, estruturar a documentação e esclarecer dúvidas técnicas. A *IA* ajudou especialmente na automação da comparação de arquivos Excel e na criação da interface web com Flask." Contribuiu com insights e sugestões para melhorar o código e a documentação deste projeto!" 

---

## **🤝 Contribuição**
💡 Se quiser contribuir com o projeto:  
1. Faça um **Fork** do repositório.  
2. Crie uma nova **branch** (`git checkout -b minha-melhoria`).  
3. Faça as melhorias e **commite as mudanças**.  
4. Envie um **Pull Request**!  

---

## **📜 Licença**
📖 Este projeto está sob a licença **MIT**.