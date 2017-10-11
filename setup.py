from setuptools import setup, find_packages
import bitx

setup(
    name='bitx',
    version=bitx.__version__,
    packages=find_packages(exclude=['tests']),
    description='A BitX API for Python',
    author='',
    scripts=['demo.py'],
    install_requires=[
        'futures>=3.0.3',
        'nose>=1.3.7',
        'requests>=2.8.1',
        'pandas>=0.17.0'
    ],
    license='MIT',
    url='https://github.com/',
    # download_url='https://github.com/CjS77/pybitx/tarball/%s' % (pybitx.__version__, ),
    keywords='BitX Bitcoin exchange API',
    classifiers=[],
    test_suite='tests',
    tests_require=[
        'requests-mock>=0.7.0'
    ]
)