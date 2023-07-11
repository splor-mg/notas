from frictionless import Resource, Pipeline, Step, formats

class custom(Step):
    def transform_resource(self, resource):
        resource.write('data.csv', control=formats.CsvControl(delimiter=';'))

pipeline = Pipeline(
    steps=[
        custom()
    ]
)

source = Resource('dim.yaml')
source.transform(pipeline)