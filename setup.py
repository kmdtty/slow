try:
  from setuptools import setup, Command
except ImportError:
  from distutils.core import setup, Command

tests = [
  'slow.word.tests',
]

modules = [
  'slow.word',
  'slow.tree'
]

if __name__ == '__main__':
  setup(name='slow',
        author='Tatuya Kamada',
        packages=['slow'] + modules + tests,
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
       )
