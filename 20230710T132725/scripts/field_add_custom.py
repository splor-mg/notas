from frictionless import Step, Resource, transform, steps, Field
import petl as etl
from rich import print as rprint

class custom_step(Step):
    def transform_resource(self, resource: Resource):
        field = Field.from_descriptor({'name': 'Unidade Orçamentária - Sigla', 'type': 'string', 'title': 'New Field'})
        resource.schema.add_field(field)
        table = resource.to_petl()
        resource.data = etl.addfield(table, 'Unidade Orçamentária - Sigla', lambda d: d['Unidade Orçamentária - Descrição'].lower())


source = Resource('dim.yaml')

rprint('before transformation...')

rprint(f'{source.schema.field_names=}')
rprint(f'{source.path=}')
rprint(f'{source.data=}')

target = transform(source, steps=[
    custom_step()
])

rprint('after transformation...')
rprint(f'{source.schema.field_names=}')
rprint(f'{source.path=}')
rprint(f'{source.data=}')
