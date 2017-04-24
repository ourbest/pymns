from distutils.core import setup

import pymns

setup(name='pymns',
      author='CYH',
      url='https://github.com/ourbest/pynms',
      author_email='chenyonghui@gmail.com',
      version=pymns.__version__,
      description='ali mns simple client',
      packages=['pynms'],
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
      ],
      install_requires=['requests'],
      )
