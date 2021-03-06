# Copyright 2018 ACSONE SA/NV (<http://acsone.eu>)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name="click-odoo-{{ PROJECT }}",
    description="click-odoo {{ PROJECT }} script",
    long_description="\n".join(
        (
            open(os.path.join(here, "README.rst")).read(),
            open(os.path.join(here, "CHANGES.rst")).read(),
        )
    ),
    use_scm_version=True,
    packages=find_packages(),
    setup_requires=["setuptools-scm"],
    install_requires=["click-odoo>=2.0.0.rc2"],
    dependency_links=[
        "git+https://github.com/xoe-labs/click-odoo.git@2.0.0#egg=click-odoo"
    ],
    license="LGPLv3+",
    author="{{ PACKAGE_AUTHOR }}",
    author_email="{{ PACKAGE_AUTHOR_EMAIL }}",
    url="http://github.com/{{ GITHUBORG }}/click-odoo-{{ PROJECT }}",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: "
        "GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Framework :: Odoo",
    ],
    entry_points="""
        [console_scripts]
        click-odoo-{{ PROJECT }}=src.{{ PROJECT }}:main
    """,
)
