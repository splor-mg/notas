# Base de conhecimento

Esse repositório armazena a base de conhecimento da Assessoria de Dados da [Subsecretaria de Planejamento e Orçamento/SEPLAG](https://www.mg.gov.br/planejamento/pagina/geral/quem-e-quem#subsecretaria-de-planejamento-e-orcamento) e representa uma iniciativa de organização e disseminação de conhecimento.

Organização do conhecimento porque torna explícito o conhecimento tácito dos servidores e disseminação porque as notas são lidas por todos antes de serem incorporadas a [base de conhecimento permanente](https://splor-mg.github.io/notas/main).

## Instalação e configuração

Essa instalação é necessária somente para a visualização local das notas.

- Git
- GNU Make
- Docker Desktop

## Uso

Cada nota[^20230411T151431] (arquivo `index.md`, `index.qmd` ou `index.ipynb`) e seu material de referência (eg. imagens, csvs, xlsx, etc) deve ser armazenada em uma pasta `YYYYDDMMThhmmss`. Por exemplo:

[^20230411T151431]: A nota é a unidade de armazenamento de conhecimento e pode ter conteúdo variado. A renderização das notas utiliza a ferramenta [quarto](https://quarto.org/). A syntaxe do markdown utilizada pelo quarto está disponível em [https://quarto.org/docs/authoring/markdown-basics.html](https://quarto.org/docs/authoring/markdown-basics.html). Cabe destacar a necessidade de inclusão de um cabeçalho de _YAML frontmatter_ para armazenamento de metadados sobre a nota (no mínimo `title`). No formato `*.ipynb` o cabeçalho deve ser a [primeira célula do notebook no formato _raw_](https://quarto.org/docs/tools/jupyter-lab.html#yaml-front-matter).

```bash
.
├── 20230327T162719
│ └── index.md
└── README.md
```

Toda nota deve ser elaborada em um branch específico[^20230411T153215] e ser revisada pelos demais membros não autores via pull request (PR). 

[^20230411T153215]: As notas em produção, ou seja, que ainda não foram aprovadas e mergiadas no branch main estão disponíveis em <https://splor-mg.github.io/notas/main/<branch>

Se não houver nenhum comentário, dúvida ou sugestão, um :1: como comentário no PR sinaliza a aprovação. O merge é realizado pelo autor principal após a aprovação de todos os servidores. 

Para visualizar o conteúdo da nota de forma interativa execute:

```bash
make preview
```

Para renderizar a base de conhecimento completa localmente execute:

```bash
make render
```

## Manutenção

O gerenciamento de dependências é realizado por meio dos arquivos `DESCRIPTION` para o R e `requirements.txt` para o Python. 
Se uma nota precisar de um pacote não listado, o mesmo deve ser inserido.

Se o pacote tiver dependências de sistema, pode ser necessário realizar alterações no arquivo `Dockerfile`.

## Projetos relacionados

A principal inspiração para essa iniciativa é de um [Zettelkasten](https://zettelkasten.de/posts/overview/) adaptado para o contexto organizacional de produção de documentação técnica.
