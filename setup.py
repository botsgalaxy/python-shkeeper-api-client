from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="shkeeper-api-client",  
    version="0.1", 
    author="primeakash", 
    author_email="admin@botsgalaxy.com",
    description="A Python client for the SHKeeper API to manage cryptocurrency invoices.",
    long_description=long_description,  
    long_description_content_type="text/x-rst", 
    url="https://github.com/botsgalaxy/python-shkeeper-api-client",  
    packages=find_packages(),  
    classifiers=[  
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.7', 
    install_requires=[  
        "httpx>=0.23.0",  
    ],
)
