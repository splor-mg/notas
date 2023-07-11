from frictionless import Resource, steps, Pipeline, formats

pipeline = Pipeline(steps = [
        steps.table_normalize(),
        # steps.table_write(path = 'data/data.csv'),
        ])

source = Resource('dim.yaml')
target = source.transform(pipeline)
print(target.schema)
print(target.to_petl())

# target.write('data.csv', control=formats.CsvControl(delimiter=';'), encoding='windows-1252')
target.to_petl().tocsv('data.csv')