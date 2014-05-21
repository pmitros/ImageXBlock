"""Setup for image XBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='image-xblock',
    version='0.1',
    description='image XBlock',   # TODO: write a better description.
    packages=[
        'image',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'image = image:ImageXBlock',
        ]
    },
    package_data=package_data("image", "static"),
)