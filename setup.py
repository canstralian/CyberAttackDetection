from setuptools import setup, find_packages

setup(
    name='CyberAttackDetection',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'transformers==4.38.0',
        'torch==2.2.0'
    ],
    entry_points={
        'console_scripts': [
            # Add your console scripts here
        ],
    },
)
