from setuptools import setup
setup(name='cty-tmp',
  version='0.1',
  description='It show current temprature of big 5 metro city of india',
  author='ls',
  author_email='it4beginner@gmail.com',
  license='MIT',
  packages=['cty-tmp'],
  entry_points = {
    'console_scripts': ['mymood=cty-tmp.command_line:main'],
    },
  zip_safe=False)
