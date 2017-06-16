from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name='dictator',
        version='0.2.2',
        packages=find_packages(),
        url='https://github.com/amka/dictator',
        license='MIT',
        author='andrey.maksimov',
        author_email='meamka@ya.ru',
        description=(
            'Dictator is a tiny library for Robots'
            'to work with Redis as a Dict.'
        ),
        install_requires=[
            'redis',
            'six',
        ],
        setup_requires=[
            'pytest-runner',
        ],
        tests_require=[
            'pytest',
        ],
        zip_safe=False,
        include_package_data=True,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
