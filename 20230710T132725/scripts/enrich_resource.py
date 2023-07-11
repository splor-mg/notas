from frictionless import Resource, Pipeline
from dpm.steps import enrich_resource

resource = Resource('fact.yaml')

pipeline = Pipeline(steps=[
    enrich_resource(classificacao = 'uo', key = 'Unidade Orçamentária - Código', column = ['name', 'uo_sigla']),
    enrich_resource(classificacao = 'fonte', key = 'fonte_cod', column = ['name', 'fonte_desc'])
])

resource.transform(pipeline)

print(resource.to_view())