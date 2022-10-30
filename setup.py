from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name = "bendu",
    version = "1.0.0",
    author = "Thodoris Mavroeidakos",
    description = ("A tool automating operations with docker containers"),
    py_modules=["bendu"],
    python_requires='>=3.0',
    install_requires=['docker', 'Click', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: Alpha",
        "Topic :: Docker Utilities",
    ],
    entry_points='''
        [console_scripts]
        bendu=bendu:cli
    ''',

    project_urls={
    'Docker Project': 'https://github.com/tmavroeid/bendu',

},
)
