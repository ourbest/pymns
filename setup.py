import ast
import re
from distutils.core import setup

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pymns/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(name='pymns',
      author='CYH',
      url='https://github.com/ourbest/pymns',
      author_email='chenyonghui@gmail.com',
      version=version,
      description='ali nms simple client',
      packages=['pymns'],
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
      ],
      install_requires=['requests']
      )
