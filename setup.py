from setuptools import setup, find_packages

setup(
    name='api_send_email',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        # Otras dependencias de tu aplicación
    ],
)