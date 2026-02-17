from setuptools import setup, find_packages

setup(
    name="file_processor_task",
    version="0.1.0",
    description="A reusable file creation task for generic Airflow DAG execution",
    author="Hariharan",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.8",
)
