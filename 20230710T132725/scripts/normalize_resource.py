from frictionless import Package, Pipeline
from dpm.steps import normalize_resource_data, normalize_field_names
import typer
import logging
from datetime import datetime

app = typer.Typer(pretty_exceptions_show_locals=False)

@app.callback()
def callback():
    """
    ETL scripts.
    """

def transform_resource(resource):
    pipeline = Pipeline(steps=[
        normalize_field_names(),
        normalize_resource_data(path=f'data/{resource.name}.csv'),
    ])
    resource.transform(pipeline)
    result = resource.to_descriptor()
    return result

def build_package(descriptor):
    package = Package(descriptor)
    package.custom['updated_at'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    return package

@app.command('transform')
def transform_cli(resource_name: str, source_descriptor: str = 'datapackage.yaml', target_descriptor: str = 'datapackage.json'):
    source = Package(source_descriptor)
    target = Package(target_descriptor)
    target.update_resource(resource_name, transform_resource(source.get_resource(resource_name)))
    target.to_json(target_descriptor)

@app.command('build')
def build_cli(descriptor: str = 'datapackage.json'):
    package = build_package(descriptor)
    package.to_json(descriptor)

if __name__ == '__main__':
    LOG_FORMAT = '%(asctime)s %(levelname)-5.5s [%(name)s] %(message)s'
    LOG_DATE_FORMAT = '%Y-%m-%dT%H:%M:%S%z'
    logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT, level=logging.INFO)
    app()
