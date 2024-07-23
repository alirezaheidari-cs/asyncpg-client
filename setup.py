from setuptools import setup, find_packages

setup(
    name="asyncpg_client",
    version="0.4.4",
    description="Asyncpg Client is a simple and easy-to-use asyncpg client for Python 3.6+",
    author="Alireza Heidari",
    author_email="alirezaheidari.cs@gmail.com",
    url="https://github.com/alirezaheidari-cs/asyncpg-client",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "asyncpg",
        "sqlalchemy",
        "psycopg2-binary",
        "SQLAlchemy==2.0.0b3",
        "python-decouple",
        "pydantic",
    ],
    license='Apache License 2.0',
    keywords="postgres async-postgres asyncpg asyncpg-client sessionmaker",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    python_requires='>=3.6',
    project_urls={
        "Documentation": "https://github.com/alirezaheidari-cs/asyncpg-client#readme",
        "Source": "https://github.com/alirezaheidari-cs/asyncpg-client",
        "Tracker": "https://github.com/alirezaheidari-cs/asyncpg-client/issues",
    },
)
