#! /usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import datetime
    import sys
    reload(sys).setdefaultencoding("UTF-8")
except:
    pass

try:
    from setuptools import setup, find_packages
except ImportError:
    print 'Please install or upgrade setuptools or pip to continue.'
    sys.exit(1)

kwargs = {}
kwargs = dict(
    version='0+d' + datetime.date.today().strftime('%Y%m%d'),
    setup_requires=['pytest-runner'],
)

TEST_REQUIRES = ['pytest-cov', 'pytest-xdist']

INSTALL_REQUIRES = [
    'pytest>=2.8.0',
    'numpy',
    'pandas>=0.20.1, <=0.20.3',
    'scipy',
    'tables',
    'matplotlib',
    'click',
    'uncertainties',
    'lmfit',
] + TEST_REQUIRES

setup(
    name='sca_tools',
    description='Scalability Analysis Tools',
    author='Bhaskar Mookerji',
    author_email='mookerji@gmail.com',
    maintainer='Bhaskar Mookerji',
    maintainer_email='mookerji@gmail.com',
    url='https://github.com/mookerji/sca_tools',
    keywords='',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ],
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    tests_require=TEST_REQUIRES,
    platforms="Linux,Windows,Mac",
    use_2to3=False,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'usl=sca_tools.sca_fit:main',
        ],
    },
    **kwargs)
