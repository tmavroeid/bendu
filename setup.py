from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name = "bendu",
    version = "1.0.0",
    author = "Thodoris Mavroeidakos",
    description = ("A tool automating operations with docker containers"),
    py_modules=["bendu"],
    install_requires=['docker', 'click', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: Alpha",
        "Topic :: Docker Utilities",
    ],
    #package_dir={"": "src"},
    #packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    entry_points='''
        [console_scripts]
        bendu=bendu:bendu
    ''',

    project_urls={
    'Docker Project': 'https://github.com/tmavroeid/bendu',

},
)
