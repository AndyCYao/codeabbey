try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'My Project',
    'author': 'Andy Test 47',
    'url': 'Andy Test.',
    'download_url': 'Where to download it.',
    'author_email': 'andyyao@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'Ex47TestCase'
}

setup(**config)

