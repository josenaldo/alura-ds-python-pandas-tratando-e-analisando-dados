# Python Pandas: Tratando e analisando dados

Esse repositório contém os exercícios e anotações do curso
[Python Pandas: Tratando e analisando dados](https://cursos.alura.com.br/course/introducao-python-pandas), da Alura.

A tarefa referente a esse curso é: [https://github.com/josenaldo/caderno-data-science/issues/21](https://github.com/josenaldo/caderno-data-science/issues/21)

## Ferramentas usadas nesse repositótio

### Autopep8

Autopep8 é uma ferramenta para formatar o código Python de acordo com as
regras de formatação do PEP8.

### MyPy

Mypy é um verificador de tipo estático opcional para o Python, que visa
combinar os benefícios da tipagem dinâmica (ou "duck typing") e da
tipagem estática. Para mais informações, veja
[http://mypy-lang.org/](https://mypy-lang.org/).

Para usar o MyPy, basta instalar o pacote
[mypy-lang](https://pypi.org/project/mypy-lang/) e executar o comando
`mypy .` na pasta do repositório.

```shell
> mypy .
Success: no issues found in 7 source files
```

### Flake8

O Flake8 é um verificador de código Python que verifica padrões de
estilo. Para mais informações, veja
[http://flake8.pycqa.org/](https://flake8.pycqa.org/).

Para usar o flake8, basta instalar o pacote
[flake8](https://pypi.org/project/flake8/) e executar o comando
`flake8` na pasta do repositório.

```shell
flake8 .
```

### Pre-commit

O pre-commit é um gerenciador de pacotes multilíngue para pre-commits
hooks. É através dele que o flake8 é executado. Para mais informações,
veja [https://pre-commit.com/](https://pre-commit.com/)

Pra usar o pre-commit, é preciso primeiro instalar os pré-commits no
git, com o comando

```shell
> pre-commit install
pre-commit installed at .git\hooks\pre-commit
```

Pra testar o pre-commit, use o comando

```shell
> pre-commit run --all-files
flake8..........................................................Passed
```

Se for preciso atualizar o pre-commit, use o comando

```shell
pre-commit autoupdate
```

## Referências

Este trabalho ainda está em desenvolvimento e segue as seguintes
referências.

- [Python Best Practices for a New Project in 2021](https://mitelman.engineering/blog/python-best-practice/automating-python-best-practices-for-a-new-project/)
- (https://realpython.com/python-best-practices-2020/)
- [A Guide to Python Good Practices](https://towardsdatascience.com/a-guide-to-python-good-practices-90598529da35)
- [7 Ways to Make Your Python Project Structure More Elegant](https://www.the-analytics.club/python-project-structure-best-practices)
