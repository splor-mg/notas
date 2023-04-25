---
title: Data package manager (dpm)
author: Francisco Alves
categories:
    - spec
    - cli
    - frictionless
---

## Spec

At the basic level a data package manager should allow the installation, update and removal of data packages.

### Installation, update and removal

The data sources[^20230425T102524] of a given project should be specified in a top level data package in the `package.sources` property. To download the source data packages you can run

```bash
dpm install
```

::: {.callout-note collapse=true}

## Example

For the data package

```yaml
name: spreadmart
title: Data mart de dados orçamentários
resources:
  - name: datamart
    path: datamart.db
sources:
  - name: despesa
    title: Despesa Orçamentária
    path: https://dados.mg.gov.br/dataset/despesa
  - name: ppag2023
    title: Plano Plurianual
    path: https://raw.githubusercontent.com/splor-mg/ppag2023-dadosmg/main/datapackage.yaml
```

Running `dpm install` will create or update the `.gitignore` file and store fully dereferenced[^20230425T111627] data packages in their folders:

```
spreadmart/
├── .gitignore
├── datapackage.yaml
└── datapackages
    ├── despesa
    │   ├── data
    │   │   └── data.csv
    │   └── datapackage.json
    └── ppag2023
        ├── data.csv
        └── datapackage.json
```

:::

If you run `dpm install` again, even if there are new versions upstream, nothing will happen. However, if there are new packages listed in `package.sources` they will be downloaded.
In order to update all installed packages overwriting the existing files run:

```bash
dpm update
```

You can also update a specific package with

```bash
dpm update <package-name>
```

Where `<package-name>` corresponds to the `package.sources.name` property[^20230425T112806].

You can remove a data package with

```bash
dpm rm <package-name>
```

This will remove the data package from `package.sources` and also remove the folder `datapackages/<package.sources.name>/`.

### Versioning

When the upstream data package is not under your control, it might be a good idea to inspect the new version of the data package before doing an update. 
Here's how that workflow works with `dpm`.

Firstly you need to download the newer version to a local cache by running:

```bash
dpm fetch # fetch all data packages
```

or

```bash
dpm fetch <package-name>
```

Now you can run 

```bash
dpm diff <package-name>
```

which will show a summary of schema, metadata, and data changes between you current installed and cached version. After you have performed impact analysis on your data sources you can run `dpm update <package-name>`.

[^20230425T102524]: As fontes de dados podem ser data packages ou conjuntos de dados do portal https://dados.mg.gov.br/ que possuem a propriedade `resources_ids` com o mapeamento entre recursos do data package e do conjunto de dados

[^20230425T111627]: Dereferenced

[^20230425T112806]: We don't use the upstream `package.name` because it could change and break lineage between related data packages.