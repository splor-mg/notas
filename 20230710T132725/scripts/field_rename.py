from frictionless import Resource, Pipeline, steps

pipeline = Pipeline(steps=[
        steps.field_update(
            name="Número Empenho",
            descriptor={'name': 'id'}
        ),
    ])

source = Resource('fact.yaml')
target = source.transform(pipeline)

print(f'{source.schema.field_names=}')
