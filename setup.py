from setuptools import setup, find_packages

VERSION = '0.6.0'

setup(
    name='tower',
    version=VERSION,
    description='Pull strings from a variety of sources, collapse whitespace, '
                'support context (msgctxt), and merging .pot files.',
    long_description=open('README.rst').read(),
    author='Wil Clouser',
    author_email='wclouser@mozilla.com',
    url='http://github.com/clouserw/tower',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        # I don't know what exactly this means, but why not?
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
