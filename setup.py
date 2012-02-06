from setuptools import setup, find_packages

setup(name="django-paypal",
           version="0.1",
           description="Interface to Django interface to Paypal",
           author="johnboxall",
           author_email="john@mobify.com",
           packages=find_packages(),
           include_package_data=True,
)
