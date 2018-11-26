from setuptools import setup

setup(
    name="copycat",
    version="0.1",
    description="copy data among machines with ease",
    author="Yongseok Paul Soh",
    author_email="yongseok@linewalks.com",
    license="MIT",
    packages=["copycat"],
    install_requires=[
        "fabric3",
        "pyinquirer",
    ],
    scripts=[
        "bin/copycat",
    ],
    zip_safe=False
)
