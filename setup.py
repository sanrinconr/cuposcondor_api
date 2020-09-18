import setuptools

setuptools.setup(
    name="Api cupos condor",
    version="1.0",
    author="Santiago Rincon",
    author_email="sanrinconr@correo.udistrital.edu.co",
    description="Api para la busqueda de cupos en condor",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://gitlab.com/cupos-condor/api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[("config", ["config/local.py"]), (".", ["entrypoint.py"])],
)
