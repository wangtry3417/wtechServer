from setuptools import setup, find_packages

setup(
    name='tcplib',
    version='0.3',
    description='That a tcp maker.',
    author='WTech',
    author_email='wangtry3417@gmail.com',
    packages=find_packages(),
    license='MLT',
    license_files=('LICENSE'),
    install_requires=[
        'cryptography',
        'requests',
        'random2',
    ],
)
