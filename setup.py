
"""
Created on Thu Apr 25 17:55:14 2019

@author: Rajkumar Shinde
"""

#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = [
    'db-sqlite3==0.0.1',
    'newsapi-python==0.2.3',
    'Click==7.0'
]

#tests_require = [
#    'pytest',
#    ]

setup(
    name='newsapi-python-cli',
    version='1.0',
    author='Rajkumar Shinde',
    author_email='mailrajshinde@gmail.com',
    #license='GENERAL',
    #url='https://github.com/mattlisiv/newsapi-python-cli',
    packages=find_packages(),
    install_requires=install_requires,
    #tests_require=tests_require,
    description='An unofficial Python CLI to export the Top headlines from News API to csv',
    #download_url='https://github.com/mattlisiv/newsapi-python-cli/archive/master.zip',
    keywords=['newsapi','news','newsapicli'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',        
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.7',
    ],
    scripts = ['newsapi_cli/sqlclient.py', 
                'newsapi_cli/const.py',
                'newsapi_cli/news.py',]
    #entry_points={'console_scripts': ['news = newsapi_cli.news:main']}
)