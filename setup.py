from setuptools import find_packages, setup

# parse requirements.txt
with open('requirements.txt') as f:
    install_requires = [_ for _ in f.read().split('\n') 
                        if len(_) and _[0].isalpha()]

# parse README.md
with open('README.md') as f:
    long_description = f.read()

# run setup
setup(
    name='dyneusr-fire',
    version='0.0.3',
    scripts=['dyneusr-fire'],
    description='A command line interface for DyNeuSR',
    long_description=long_description,
    long_description_content_type="text/markdown",	
    author='Caleb Geniesse',
    author_email='geniesse@stanford.edu',
    url='https://braindynamicslab.github.io/dyneusr-fire',
    license='BSD-3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    python_requires='>=3.6',
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords='brain dynamics, topology data analysis, neuroimaging, brain networks, mapper, visualization',
)
