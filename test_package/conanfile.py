#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, RunEnvironment, tools
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        os.path.exists(os.path.join("bin", "test_package"))
