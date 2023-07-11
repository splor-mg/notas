from frictionless import Package, Pipeline
from dpm.steps import normalize_field_names

dp = Package('datapackage.yaml')

pipeline = Pipeline(steps=[
    normalize_field_names()
])

for resource in dp.resources:
    resource.transform(pipeline)

print(dp.get_resource('dim'))