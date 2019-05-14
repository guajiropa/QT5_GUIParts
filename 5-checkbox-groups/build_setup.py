from setuptools import setup, find_packages

setup(
    name="dlgIceCreamShop",
    version="0.1",
    packages=find_packages(),
    scripts=['callDlgIceCream.py', 'dlgIceCreamShop.py', 'main.py'],
    install_requires=['PyQt5>=5.12.1'],
    author="RJP",
    author_email="guajiropa@hotmail.com",
    description="A test of pythons setup tools",
    license="MIT",
    url="http://www.testing.net/icecreamshop"
    )
