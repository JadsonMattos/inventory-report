# Inventory Report

<details>
<summary><strong>🧑‍💻 O que deverá ser desenvolvido</strong></summary>
  <br />

Neste projeto, irá desenvolver um **gerador de relatórios**. O objetivo é receber arquivos contendo informações sobre um estoque específico e, em seguida, produzir um relatório abrangente com base nesses dados. Esses dados de estoque poderão ser obtidos de duas fontes:

-   Através da importação de um arquivo `CSV`;

-   Através da importação de um arquivo `JSON`;

Além disso, o relatório final possuirá duas versões: **simples** e **completa**.

</details>

<details>
  <summary><strong> 📝 Habilidades a serem trabalhadas </strong></summary>
  <br />

Neste projeto, verificamos se você é capaz de:

-   Aplicar conceitos de Programação Orientada a Objetos em Python;

-   Implementar leitura e escrita de arquivos `CSV` e `JSON` em Python;

</details>

## Orientações específicas deste projeto

<details>
  <summary><strong>🗃️ Arquivos com os dados de entrada</strong></summary><br />
  
Dois formatos de importação estão disponíveis no diretório <code>data</code> dentro do diretório <code>inventory_report</code>. Estes arquivos serão gerados assim que você executar os testes pela primeira vez.


Confira o exemplo de formato eles:

<strong>Arquivos CSV</strong>
Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```CSV
id,product_name,company_name,manufacturing_date,expiration_date,serial_number,storage_instructions
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
```

<strong>Arquivos JSON</strong>
Os arquivos JSON seguem o seguinte modelo:

```json
[
    {
        "id": "1",
        "product_name": "Borracha",
        "company_name": "Papelaria Solar",
        "manufacturing_date": "2021-07-04",
        "expiration_date": "2029-02-09",
        "serial_number": "FR48",
        "storage_instructions": "Ao abrigo de luz solar"
    }
]
```

</details>

1. Crie o ambiente virtual para o projeto

-   `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências

-   `python3 -m pip install -r dev-requirements.txt`

</details>

<details>
  <summary><strong>🐳 Docker</strong></summary>
  <br />
  Caso queria executar os seus testes de projeto via `docker-compose`, ao invés de no ambiente virtual, execute o comando:

```bash
docker-compose run --rm inventory pytest
```

## Requisitos do projeto

### 1. Teste o construtor/inicializador do objeto Produto

> **Crie o teste em:** `tests/product/test_product.py`

<p align="center">
    <img src="/.images/construtor.png " alt="Imagem de construtor em Python"  width="600"/>
</p>

<details>

**<summary>Teste se o construtor do objeto <code>Product</code> contém os atributos corretos.**

</summary>

Ao analisar o código do projeto, você encontrará a classe do objeto produto já implementada no arquivo `inventory_report/product.py`.

Para termos confiança em continuar as implementações, precisamos que você implemente o teste e certifique que o método `__init__` da classe `Product` esteja funcionando corretamente.

O nome deste teste deve ser `test_create_product` e ele deve verificar o correto preenchimento dos seguintes atributos:

-   `id`
-   `company_name`
-   `product_name`
-   `manufacturing_date`
-   `expiration_date`
-   `serial_number`
-   `storage_instructions`

</details>

### 2. Teste o relatório individual gerado por Produto

> **Crie o teste em:** `tests/product_report/test_product_report.py`

<details>

**<summary>Teste se o "método mágico" <code>**str**</code> do objeto <code>Product</code> retorna a frase correta.**

</summary>

Boa notícia! Já implementamos o primeiro relatório no arquivo `inventory_report/product.py`, e também criamos uma frase com as informações do produto, que será útil para etiquetar o estoque. Para desenvolver esse relatório, utilizamos o método `__str__` do Python, que é chamado quando utilizamos a função `str(objeto)`.

Exemplo da frase:

**Trecho 1:** _The product `farinha`,_
**Trecho 2:** _with serial number `TY68 409C JJ43 ASD1 PL2F`,_
**Trecho 3:** _manufactured in `01-05-2021`_
**Trecho 4:** _by the company `Farinini`,_
**Trecho 5:** _valid until `02-06-2023`,_
**Trecho 6:** _must be stored according to the following instructions: `precisa ser armazenado em local protegido da luz`._

Agora, para garantirmos uma boa cobertura de testes, precisamos que você implemente o teste. O nome do teste deve ser `test_product_report`. Ele deve instanciar um objeto `Product` e verificar se a frase retornada está correta.

</details>

### 3. Crie a Interface `Importer`

> **Crie em:** `inventory_report/importers.py`

<details>

**<summary>Crie a classe abstrata <code>Importer</code> com o inicializador implementado e com o método abstrato <code>import_data</code>.**

</summary>
  <br />

Como já temos o arquivo com os produtos, precisamos importar os dados. Em razão dos diversos formatos e para não repetir lógica, vamos criar uma classe abstrata que será responsável por definir como as classes importadoras dos dados dos arquivos serão.

Para isso, crie uma classe abstrata chamada `Importer`, que deve conter um método chamado `import_data`, que recebe o caminho do arquivo e retorna uma lista de produtos:

</details>

### 4. Crie a classe `JsonImporter`

> **Crie em:** `inventory_report/importers.py`

<details>

**<summary>Crie a classe <code>JsonImporter</code> que herda de <code>Importer</code> e implemente o método <code>import_data</code> para ler um arquivo JSON.**

</summary>
  <br />

Agora que temos a interface, precisamos criar a classe que irá implementar o método `import_data` para ler um arquivo JSON. Para isso, crie uma classe chamada `JsonImporter`, que deve herdar da classe `Importer` e implementar o método `import_data`. Esse método, por sua vez, recebe o caminho do arquivo e retorna uma lista de produtos. A lista deve ser retornada como no formato abaixo:

```
[
  Product(
    id='1',
    product_name='Nicotine Polacrilex',
    company_name='Target Corporation',
    manufacturing_date='2021-02-18',
    expiration_date='2024-09-17',
    serial_number='CR25 1551 4467 2549 4402 1',
    storage_instructions='instrucao 1'
  ),

  Product(
    id='2',
    product_name='fentanyl citrate',
    company_name='Target Corporation',
    manufacturing_date='2020-12-06',
    expiration_date='2024-12-25',
    serial_number='FR29 5951 7573 74OY XKGX 6CSG D20',
    storage_instructions='instrucao 2'
  ),
  // ...
]
```

</details>

### 5. Crie a classe `Inventory`

> **Crie em:** `inventory_report/inventory.py`

<details>

**<summary>Crie a classe <code>Inventory</code> que armazenará o estoque e poderá adicionar itens a ele.**

</summary>
  <br />

Com o nosso importador de dados feito, vamos criar a classe que representa um estoque para, a partir dele, gerar o nosso relatório! Atenção para as especificações:

-   A classe `Inventory` deve poder ser instanciada, de forma opcional, com uma lista de produtos.
-   Caso a lista não seja fornecida, a lista da instância deve ser inicializada como vazia.
-   A classe deve conter um método chamado `add_data`, que recebe uma lista de produtos e adiciona todos os produtos à lista de produtos da instância.
-   Além disso, a classe deve ter uma propriedade chamada `data`, que deve ser somente leitura e retornar uma cópia da lista de produtos da instância.

</details>

### 6. Crie o protocolo `Report`

> **Crie em:** `inventory_report/reports/report.py`

<details>

**<summary>Crie o protocolo <code>Report</code>, que deverá ser usado como contrato dos relatórios <code>simple</code> e <code>complete</code>.**

</summary>
  <br />

Feita nossa classe de inventário, vamos usá-la para criar nossos relatórios! Visto que teremos dois formatos dele, primeiro vamos criar um contrato para todos os formatos respeitarem. Usaremos um protocolo para isso. Atenção à especificação:

-   No protocolo `Report` deve haver um método chamado `add_inventory` recebendo um parâmetro `inventory`, do tipo `Inventory`, classe criada no quinto requisito.

-   Deve haver um método chamado `generate` que retorna uma string.

</details>

### 7. Crie o relatório `SimpleReport`

> **Crie a classe em:** `inventory_report/reports/simple_report.py`

<details>

**<summary>Crie a classe <code>SimpleReport</code> que implementa os métodos <code>add_inventory</code> e <code>generate</code> do protocolo <code>Report</code>.**

</summary>
  <br />

A classe `SimpleReport` deve ser inicializada sem parâmetros, contudo, deve ter um atributo para armazenar cada um dos estoques que podem ser adicionados.

O método `add_inventory` deverá seguir o contrato do protocolo `Report` e deve ser capaz de adicionar um estoque ao atributo que armazena cada um dos estoques.

O método `generate` deve ser capaz de gerar o relatório a partir dos produtos que estão presentes em cada um dos estoques armazenados. Atenção às especificações:

-   Ao rodar os testes localmente, você terá um teste para cada validação de cada informação presente no relatório;
-   O método `add_inventory` deve receber um parâmetro que representa um `Inventory`, classe implementada no quinto requisito.
-   O método `generate` deverá retornar uma `string` de saída com o seguinte formato:

```txt
Oldest manufacturing date: YYYY-MM-DD
Closest expiration date: YYYY-MM-DD
Company with the largest inventory: NOME DA EMPRESA
```

-   A data de validade mais próxima considera somente itens que ainda não venceram.

**Dica:** O módulo [datetime](https://docs.python.org/3/library/datetime.html) pode te ajudar.

</details>

## Bônus

### 8. Crie a classe `CsvImporter`

> **Crie em:** `inventory_report/importers.py`

<details>

**<summary>Crie a classe <code>CsvImporter</code> que herda de <code>Importer</code> e implemente o método <code>import_data</code> para ler um arquivo CSV.**

</summary>
  <br />

Para não ficarmos limitados a receber estoques em formato JSON, precisamos criar a classe que irá implementar o método `import_data` para ler um arquivo CSV. Para isso, crie uma classe chamada `CsvImporter`, que deve herdar da classe `Importer` e implementar o método `import_data`, que usa o caminho armazenado em um atributo para retornar uma lista de produtos.

</details>

### 9. Crie o relatório `CompleteReport`

> **Crie em:** `inventory_report/reports/complete_report.py`

<details>

**<summary>Crie a classe <code>CompleteReport</code> que herda de <code>SimpleReport</code> e implementa o método <code>generate</code> do protocolo <code>Report</code>.**

</summary>
  <br />

O relatório completo deve ser gerado através do método `generate` escrito dentro da classe `CompleteReport` e que respeita o contrato criado no protocolo `Report`.

O método `generate` deve usar o atributo que armazena as lista de estoques para a estruturação do relatório e deverá retornar uma string formatada como um relatório. Atenção à especificação:

-   A classe `CompleteReport` deve herdar da classe `SimpleReport` e sobrescrever o método `generate`, de modo a especializar seu comportamento.

-   O método deverá retornar uma saída com o seguinte formato:

```bash
Oldest manufacturing date: YYYY-MM-DD
Closest expiration date: YYYY-MM-DD
Company with the largest inventory: NOME DA EMPRESA
Stocked products by company:
- Empresa 1: 2
- Empresa 2: 1
```

</details>

### 10. Crie a função `process_report_request`

> **Crie em:** `inventory_report/cli/input_handler.py`

<details>

**<summary>Crie a função <code>process_report_request</code>.**

</summary>
  <br />

Está na hora de ajustar a interface de linha de comando (_Command Line Interface_, ou _CLI_) para nossa aplicação que gera relatórios!

No arquivo `inventory_report/cli/__init__.py` já existe uma CLI implementada com a biblioteca [Typer](https://typer.tiangolo.com/) que está configurada para ser chamada da seguinte forma:

```sh
ir -p <caminho_da_pasta> -t <tipo_do_relatorio>
```

A implementação em `inventory_report/cli/__init__.py` (você não precisa alterar esse arquivo) irá chamar a função `process_report_request` que você deve implementar no arquivo `inventory_report/cli/input_handler.py`, com os seguintes argumentos:

- `file_paths: List[str]`: Lista de caminhos de arquivos dentro da pasta informada em `-p`;
- `report_type: str`: Tipo de relatório a ser gerado, informado em `-t`.

A função `process_report_request` deve retornar um relatório do tipo informado contendo os dados de todos os arquivos listados. Atenção às especificações:

-   A função `process_report_request` deve receber dois parâmetros: `file_paths: List[str]` e `report_type: str`;

-   Deverão ser usadas as classes dos requisitos anteriores para gerar o relatório adequado: `Inventory`, `CsvImporter`, `JsonImporter`, `SimpleReport` e `CompleteReport`;

-   Arquivos de extensões não suportadas devem ser ignorados;

-   Caso o tipo de relatório informado não seja suportado, deve ser levantado um `ValueError` com a mensagem `Report type is invalid.`;

</details>
