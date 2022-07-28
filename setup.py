from setuptools import setup, find_packages


setup(
    name='example_publish_pypi_devterminal',
    version='0.0',
    license='MIT',
    author="Ahmad Almohammad",
    author_email='almohammedahmed23@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[],

)