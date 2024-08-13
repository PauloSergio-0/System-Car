from setuptools import setup, find_packages

# cd /caminho para setup.py
# exec terminal: "python setup.py develop"


setup(
    name = 'SistemaVendaCarros',  # Nome do pacote
    version = '1.0',
    packages = find_packages(where = 'src/System'),  # Aponta para o diretório 'System'
    package_dir = {'': 'src/System'},  # Define 'System' como o diretório base para o pacote
)
