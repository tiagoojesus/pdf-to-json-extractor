# Extrator de PDF para JSON

Este projeto fornece um **script Python** para extrair **texto e imagens estruturadas** de qualquer documento **PDF** e convertê-los para um formato **JSON**.

## Funcionalidades

- Extrai **texto** e **imagens** de qualquer PDF  
- Estrutura automaticamente **perguntas e respostas** em JSON  
- Funciona com **exames, testes de código, e outros documentos**  
- Guarda as **imagens extraídas** separadamente  

---

## 📂 Estrutura do Repositório

```
📦 pdf-to-json-extractor
 ┣ 📂 input_pdfs/            # Guardar aqui os PDFs
 ┃ ┗ 📄 exemplo.pdf
 ┣ 📂 extracted_images/      # Imagens extraídas (criadas automaticamente)
 ┃ ┗ 🖼 image_1.png (imagens extraídas)
 ┣ 📄 extract.py             # Script Python para extração
 ┣ 📄 extracted_output.json  # JSON final estruturado
 ┣ 📄 README.md              # Documentação
 ┗ 📄 .gitignore             # Ignorar ficheiros desnecessários
```

---

## Como Usar

### **Clonar este repositório**

```sh
git clone 
cd pdf-to-json-extractor
```

### **Verificar se tens Python 3 instalado**
```sh
python3 --version
```
Se **não estiver instalado**, instala-o da seguinte forma:  
- **Ubuntu/Debian**:  
  ```sh
  sudo apt update && sudo apt install python3 python3-pip
  ```
- **MacOS** (com Homebrew):  
  ```sh
  brew install python
  ```
- **Windows**: [Descarrega Python 3](https://www.python.org/downloads/)

### **Instalar as dependências**
```sh
pip3 install pymupdf
```

### **Colocar o ficheiro PDF na pasta `input_pdfs/`**  
Muda o nome, se necessário (ex: `exame.pdf`).

### **Executar o script**
```sh
python3 extract.py --pdf input_pdfs/exame.pdf
```
Isto irá extrair o texto e imagens e gerar o ficheiro `extracted_output.json`.

---

## Estrutura do JSON

Cada pergunta extraída segue este formato:

```json
[
    {
        "question": "Se o meu motociclo emitir ruídos superiores aos limites máximos fixados, fico sujeito ao pagamento de uma coima?",
        "options": {
            "a": "Sim.",
            "b": "Não."
        },
        "image": "image_1_1.png"
    }
]
```

- **`question`** → O texto da pergunta extraída  
- **`options`** → Dicionário com as opções de resposta  
- **`image`** → Nome do ficheiro da imagem associada (se disponível)  

---

## Configuração

Por defeito, o script extrai **todo o texto e imagens** do PDF. Se precisares de personalizar a extração (ex: filtrar secções específicas), podes editar o ficheiro `extract.py`.

---

## Contribuir
Queres melhorar este projeto? Sente-te à vontade para fazer um **fork**, modificar e enviar um **pull request**!  

### Licença
Este projeto é open-source. Podes usá-lo e modificá-lo livremente. 

---
