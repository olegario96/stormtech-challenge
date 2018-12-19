from setuptools import find_packages, setup

setup(
    name='stormtech-challenge',
    packages=find_packages(),
    entry_points={
        'scripts': [
            'app = app.app:run'
        ],
    },
    install_requires=[
        'flask',
        'python-dotenv',
        'pytest'
    ],
)
