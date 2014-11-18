#!/usr/bin/env python
from pip.req import parse_requirements
from setuptools import setup

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_requires = [str(requirement.req)
                    for requirement
                    in parse_requirements('requirements.txt')]

setup(name="Simple Dockployment",
      version="0.0.1",
      description="Simple daemon to watch Docker for new tagged containers, and deploy them",
      author="Ricky Cook",
      author_email="mail@thatpanda.com",
      py_modules=['simple-dockployment'],
      scripts=['simple-dockployment'],
      install_requires=install_requires,
      )
