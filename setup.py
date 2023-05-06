from setuptools import setup, find_packages
import site

setup(
    name='directory_browser_using_ipydatagrid',
    version='0.0.1',
    description='A Jupyter directory browser widget using ipydatagrid.',
    url='http://github.com/mister-average/directory_browser_using_ipydatagrid',
    author='mister-average',
    author_email='mister_person@averageaddress.com',
    license='BSD',
    data_files=[('/', ['directory_browser_using_ipydatagrid.ipynb'])],
    python_requires='>=3.9'
)
