"""

"""

from setuptools import setup, find_namespace_packages

tests_require = ["pytest", "pytest-cov"]

setup(
    name="mypkg-module1",
    author="Me",
    author_email="jason@entos.ai",
    url="www.entos.ai",
    description="Just a test 1",
    packages=find_namespace_packages(include=["mypkg"]),
    include_package_data=True,
    # platforms=['Linux',
    #            'Mac OS-X',
    #            'Unix',
    #            'Windows'],            # Valid platforms your code works on, adjust to your flavor
    python_requires=">=3.9",  # Python version restrictions
    zip_safe=False,
)
