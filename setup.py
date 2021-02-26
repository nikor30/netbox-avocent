from setuptools import find_packages, setup

from netbox-avocent.version import VERSION

setup(
    name="netbox-avocent",
    version=VERSION,
    author="Nikolas Reitz",
    author_email="nr@gmx.net",
    description="Avocent Plugin",
    url="https://github.com/nikor30/netbox-avocent/",
    license="New BSD",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)
