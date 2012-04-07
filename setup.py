from setuptools import setup, find_packages

setup(
    name="hellojmeter",
    version="1.0.0",
    description="Learn JMeter",
    author="Baiju Muthukadan",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "Flask",
        "gunicorn",
    ],
)
