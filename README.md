# Extrator de PDF para JSON
Este projeto fornece um **script Python** para extrair texto estruturado e imagens de qualquer **documento PDF** e convertê-los num **formato JSON**.

## Caraterísticas

- Extrai **texto** e **imagens** de qualquer PDF  
- Estrutura automaticamente **perguntas e respostas** em JSON  
- Funciona com **exames de escolha múltipla, questionários e documentos**  
- Guarda **imagens** extraídas separadamente  

---

## 📂 Estrutura do repositório

```
📦 pdf-to-json-extractor
 ┣ 📂 database-exams/          # Ficheiro PDF original
 ┃ ┗ 📄 rel_3_condutores.pdf
 ┣ 📂 extracted_images/        # Imagens extraídas
 ┃ ┗ 🖼 image_1_1.png (imagem extraída)
 ┣ 📄 extract.py               # Script Python para extração
 ┣ 📄 extracted_output.json    # JSON estruturado final
 ┗ 📄 README.md                # Documentação



```
## Como usar

### 1️. **Clonar este repositório**

```sh
git clone 
cd pdf-to-json-extractor
```

### 2️. **Instalar dependências**

```sh
pip install pymupdf
```

### 3️. **Executar o script**
```sh
python extract.py
```
Isto irá extrair todo o texto e imagens de `rel_3_condutores.pdf` e guardá-los em `extracted_output.json`


---

## Estrutura JSON

Cada pergunta é armazenada no seguinte formato:

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

- **`question`** → O texto da pergunta extraído.  
- **`options`** → Dicionário com opções de resposta.  
- **`image`** → Nome de ficheiro da imagem relacionada (se disponível).
  

---  


## Configuração

Por defeito, o script extrai **todos os textos e imagens**. Se precisar de personalização (e.g., filtrar secções específicas), pode modificar o `extract.py`.


## Contribuir
Quer melhorar este projeto? Sinta-se à vontade para fazer um fork, modificar e enviar um pull request!  


### Licença
Este projeto é de código aberto. Sinta-se à vontade para o usar e modificar. 


---























































