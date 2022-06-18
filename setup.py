#!/usr/bin/env python

from setuptools import find_packages, setup

import os
import subprocess
import time


def readme():
    with open("README.md", encoding="utf-8") as f:
        content = f.read()
    return content


def get_git_hash():
    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ["SYSTEMROOT", "PATH", "HOME"]:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env["LANGUAGE"] = "C"
        env["LANG"] = "C"
        env["LC_ALL"] = "C"
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(["git", "rev-parse", "HEAD"])
        sha = out.strip().decode("ascii")
    except OSError:
        sha = "unknown"

    return sha


def get_hash():
    if os.path.exists(".git"):
        sha = get_git_hash()[:7]
    else:
        sha = "unknown"

    return sha


def get_requirements(filename="requirements.txt"):
    here = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(here, filename), "r") as f:
        requires = [line.replace("\n", "") for line in f.readlines()]
    return requires


if __name__ == "__main__":
    setup(
        name="facexlib",
        description="Basic face library",
        long_description=readme(),
        version="0.2.24",
        long_description_content_type="text/markdown",
        author="Xintao Wang",
        author_email="xintao.wang@outlook.com",
        keywords="computer vision, face, detection, landmark, alignment",
        url="https://github.com/xinntao/facexlib",
        include_package_data=True,
        packages=find_packages(
            exclude=(
                "options",
                "datasets",
                "experiments",
                "results",
                "tb_logger",
                "wandb",
            )
        ),
        classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        license="Apache License 2.0",
        setup_requires=["cython", "numpy"],
        install_requires=get_requirements(),
        zip_safe=False,
    )
