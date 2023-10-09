import setuptools

with open('README.md','r') as f:
    long_description = f.read()
    pass

setuptools.setup(
    name='MyModel', 
    version='0.0.1',
    author='Corbudoier',
    description='Just to Practice Packaging Python Packages',
    long_description=long_description,
    license ='MIT',
    url='https://github.com/YuP2905/MyModel_Test.git',
    author_email='y290575685@gmail.com',
    packages=setuptools.find_packages(exclude=['Tests']))