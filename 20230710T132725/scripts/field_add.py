from frictionless import Resource
from scripts.pipeline import pipeline

source = Resource('fact.yaml')

target = source.transform(pipeline)
print(target.schema)
print(target.to_petl())
target.write('data/field_add.csv')
