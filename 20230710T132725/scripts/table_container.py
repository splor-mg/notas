from frictionless import Step, Resource, Pipeline

class custom_step(Step):
    def transform_resource(self, resource: Resource):
        current = resource.to_copy()
        resource.schema.update_field('Unidade Orçamentária - Descrição', {'name': 'Unidade Orçamentária - Sigla'})
        def foo():
            with current:
                for row in current.row_stream:
                    output = row.to_dict()
                    output['Unidade Orçamentária - Sigla'] = row['Unidade Orçamentária - Descrição'].lower()
                    yield output

        resource.data = foo
        

pipeline = Pipeline(steps=[custom_step()])

source = Resource('dim.yaml')
target = source.transform(pipeline)
target.write('data.csv')

print(source.to_view())
