from setuptools import setup

setup(
    name='PySorter',
    version=0.1,
    description='Flask app to sort stuff.',
    long_description="That's all I got.",
    author='Vincent Nguyen',
    author_email='None',
    install_requires=[
        'Flask>=1.0.2',
        'pytest>=4.1.0',
        'schematics==2.1.0'
    ]
)