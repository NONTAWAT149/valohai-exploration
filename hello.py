import valohai
import pandas as pd

my_parameters = {
    'epoch': 5,
    'learningrate': 0.01,
    'name': 'Bruce',
    'save': False
}

valohai.prepare(step="hello-job", default_parameters=my_parameters)

print("Hello Valohai")

name = valohai.parameters('name').value
print(f"and hello {name}!")
