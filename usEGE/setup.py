from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='usEGE',
    version='0.0.1',
    author='max_g',
    author_email='maxkraft06@gmail.com',
    description='This is just a collection of functions that are used in the computer '
                'science section of the Unified State Exam.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/Girday/usEGE',
    packages=find_packages(),
    install_requires=['ipaddress>='],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='EGE functions',
    project_urls={
        'GitHub': 'https://github.com/Girday'
    },
    python_requires='>=3.6'
)
