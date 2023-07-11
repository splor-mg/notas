from frictionless import Step, Resource, Pipeline

class custom_step(Step):
    def transform_resource(self, resource: Resource):
        
        data = [
            ['Número Empenho', 'Unidade Orçamentária - Código', 'Valor Despesa Empenhada', 'Histórico'],
            [1, 2, 3, 'foo'],
            [4, 5, 6, 'bar'],
        ]
        resource.data = data


pipeline = Pipeline(steps=[
    custom_step()
])
source = Resource('fact.yaml')

target = source.transform(pipeline)

print(f'{target.data=}')
print(f'{target.path=}')
print(f'{target.schema=}')
print(target.to_view())
