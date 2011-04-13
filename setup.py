from setuptools import setup, find_packages

setup(
    name='django-uploadify',
    version='0.1',
    description='A Django re-usable app to integrate Uploadify.',
    author='tstone',
    author_email='tstone',
    url='https://github.com/tstone/django-uploadify',
    packages=find_packages(),
    package_data={
        'uploadify': [
	    'templates/uploadify/multi_file_upload.html'
	]
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
