from setuptools import setup
setup(
    name = 'arch_bwgs_pipeline',
    author = 'Araf Mahmud',
	version = '0.0.1',
    packages = ['app'],
    requires=['pandas'],
    entry_points = {
        'console_scripts': [
            'arch_bwgs_pipeline = app.arch_bwgs_pipeline:main'
        ]
    })
