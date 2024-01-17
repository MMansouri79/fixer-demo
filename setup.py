from setuptools import setup

setup(name="fixer-demo",
       version='0.2', 
       description='Fixer service demo package', 
       url="https://github.com/MMansouri79/fixer-demo", 
       author='Mohammad', 
       author_email="mohammadmns1379@gmail.com",
       license='MIT', 
       packages=['fixer'],
       install_requires=['requests'], 
       zip_safe=False
    ) 