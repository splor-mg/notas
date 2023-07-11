from frictionless import Package

def transform_resource(resource):
    resource.custom['bhe'] = 'bar'
    return resource.to_descriptor()
    
if __name__ == '__main__':
    resource_name = 'dim'
    source = Package('datapackage.yaml')
    target = Package('datapackage.json')
    target.update_resource(resource_name, transform_resource(source.get_resource(resource_name)))
    target.to_json('datapackage.json')
