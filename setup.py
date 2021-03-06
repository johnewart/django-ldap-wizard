from setuptools import setup, find_packages

setup(
    name='django-ldap-wizard',
    version='0.5.0',
    description='A wizard that helps you determine if your LDAP settings are correct and helps you to set them up.',
    long_description=open('README.rst').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='John Ewart',
    author_email='john@johnewart.net',
    url='https://github.com/johnewart/django-ldap-wizard',
    download_url='https://github.com/johnewart/django-ldap-wizard/downloads',
    license='BSD',
    packages=find_packages(exclude=('ez_setup', 'tests', 'example')),
    tests_require=[
        'django>=1.1,<1.4',
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
    zip_safe=False,  # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)