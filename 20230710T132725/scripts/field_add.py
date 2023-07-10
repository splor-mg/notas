from frictionless import Resource, transform, steps

source = Resource('fact.yaml')
target = transform(
    source,
    steps=[
        steps.table_normalize(),
        steps.field_add(
            name="limite",
            function=lambda data: "<1000" if data["Valor Despesa Empenhada"] > 1000 else "1-1000",
            descriptor={'type': 'string'}
        ),
    ],
)
print(target.schema)
print(target.to_petl())