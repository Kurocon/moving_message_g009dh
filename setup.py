from setuptools import setup

setup(
    name='moving_message_g009dh',
    version='1.0.0',
    description='This library can help you implement a interface to the Tri Colour Moving Message Sign with USB (G009DH).',
    url='https://github.com/Kurocon/moving_message_g009dh.git',
    author='Kevin Alberts',
    author_email='kevin@kevinalberts.nl',
    packages=['moving_message_g009dh'],
    install_requires=[
        'pyserial',
    ],
    zip_safe=False,
)
