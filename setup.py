from setuptools import setup, find_packages


setup(
    name='example_publish_pypi_devterminal',
    version='1.1',
    license='MIT',
    author="Ahmad Almohammad",
    author_email='almohammedahmed23@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Eng-Ahmad-Almohammad/pypi-test',
    keywords='example project',
    install_requires=[],

)