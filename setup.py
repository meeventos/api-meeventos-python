from setuptools import setup, find_packages

setup(
    name='meeventos-api',
    version='1.0.0',
    description='Client em Python para integração com API da Meeventos.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Thalles Brandão',
    author_email='thalles@meeventos.com.br',
    packages=find_packages(),
    install_requires=[
        'requests'  # Adicione outras dependências necessárias aqui
    ],
    license='Apache-2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='eventos erp api integração',
    url='https://github.com/meeventos/api-meeventos-python'
)
