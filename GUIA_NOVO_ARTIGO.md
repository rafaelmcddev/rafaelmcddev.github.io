# Guia interno — Como publicar um novo artigo

> Este arquivo é apenas uma anotação interna do repositório.  
> Ele fica na raiz do projeto e **não aparece no site**, porque não está dentro de `docs/`.

## 1. Escolha a categoria

Categorias atuais:

```text
inteligencia-artificial/
python/
django/
arquitetura/
cloud-devops/
engenharia-software/
produto-colaboracao/
```

Escolha a pasta correspondente ao assunto do artigo.

---

## 2. Copie um artigo existente

A forma mais segura é copiar um artigo já publicado da mesma categoria.

Exemplo:

```bash
cp docs/conteudos/posts/python/pydantic.md \
   docs/conteudos/posts/python/meu-novo-artigo.md
```

Exemplo:

```text
processamento-assincrono-python.md
```

---

## 3. Atualize o front matter

Abra o novo arquivo e altere os metadados que ficam no início, entre `---`.

Use exatamente as mesmas chaves existentes no artigo copiado e altere apenas os valores.

Exemplo:

```yaml
---
title: Processamento assíncrono com Python
description: Entenda quando e como usar processamento assíncrono em aplicações Python.
---
```

Se o artigo copiado possuir outros campos, como categoria, tecnologias, nível ou tempo de leitura, mantenha as mesmas chaves e atualize os valores.

---

## 4. Escreva o conteúdo

Estrutura sugerida:

```markdown
# Título do artigo

Introdução curta explicando o problema e o objetivo do conteúdo.

## O problema

Explique o contexto.

## Como funciona

Apresente os conceitos principais.

## Exemplo prático

Inclua código, diagramas ou casos reais.

## Boas práticas

Liste os principais cuidados.

## Conclusão

Finalize resumindo os aprendizados.
```

Evite repetir o título da página caso o artigo existente usado como modelo já trate o título pelo front matter.

---

## 5. Adicione a imagem

Salve a imagem em:

```text
docs/assets/images/
```

Use um nome descritivo:

```text
processamento-assincrono-python.png
```

No artigo, utilize o mesmo padrão de caminho dos artigos existentes. Exemplo:

```markdown
![Processamento assíncrono com Python](../../../assets/images/processamento-assincrono-python.png)
```

Antes de publicar, confirme localmente se a imagem aparece corretamente.

---

## 6. Não edite a listagem manualmente

Não é necessário adicionar o artigo manualmente em:

```text
docs/conteudos.md
```

Também não é necessário distribuir o novo artigo manualmente pelos cards.

O hook do projeto lê os artigos dentro de:

```text
docs/conteudos/posts/
```

e atualiza automaticamente:

- a página de conteúdos;
- as categorias;
- os links dos artigos;
- a navegação gerada pelo projeto.

---

## 7. Teste localmente

Ative o ambiente virtual, caso ainda não esteja ativo:

```bash
source .venv/bin/activate
```

Inicie o site:

```bash
mkdocs serve
```

Acesse:

```text
http://localhost:8000
```

Confira:

- título;
- imagem;
- formatação;
- blocos de código;
- links;
- categoria;
- página `Conteúdos`;
- menu;
- versão mobile.

---

## 8. Valide o build

Antes de publicar:

```bash
mkdocs build --strict
```

Só continue se o comando terminar sem erros.

---

## 9. Faça commit e push

Veja o que foi alterado:

```bash
git status
```

Depois publique:

```bash
git add . && git commit -m "Adiciona artigo sobre processamento assíncrono em Python" && git push origin main
```

Troque a mensagem do commit pelo assunto real do artigo.

---

## Checklist rápido

```text
[ ] Artigo criado na categoria correta
[ ] Nome do arquivo em kebab-case
[ ] Front matter atualizado
[ ] Imagem salva em docs/assets/images
[ ] Imagem aparecendo no artigo
[ ] Conteúdo aparecendo na página Conteúdos
[ ] Menu e links funcionando
[ ] Layout testado no desktop
[ ] Layout testado no celular
[ ] mkdocs build --strict executado sem erros
[ ] Commit e push realizados
```

## Resumo

Para publicar um novo artigo:

```text
1. Copiar um artigo existente
2. Renomear o arquivo
3. Atualizar os metadados
4. Escrever o conteúdo
5. Adicionar a imagem
6. Testar com mkdocs serve
7. Validar com mkdocs build --strict
8. Fazer commit e push
```
