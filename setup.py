from setuptools import setup, find_packages

setup(
        name='dailyKana',
        package_dir={'':'src'},
        pakcages=find_packages(where='src'),
        zip_safe=False
)
