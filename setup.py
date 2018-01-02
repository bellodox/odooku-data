from setuptools import setup, find_packages

setup(
    name='odooku-data',
    version='10.0.1005',
    url='https://github.com/odooku/odooku-data',
    author='Raymond Reggers - Adaptiv Design',
    author_email='raymond@adaptiv.nl',
    description=('Odooku Data'),
    license='Apache Software License',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'odooku>=11.0.0,<12.0.0',
        'ijson==2.3'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: Apache Software License',
    ],
)
