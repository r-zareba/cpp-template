
"""Conan package definition for Interview Practice Questions"""

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.build import check_min_cppstd


CPP_VERSION_REQUIRED = '17'


class MyProjectSetup(ConanFile):
    
    name = 'my_project_setup'
    version = '1.0'
    label = 'my project dependencies package'

    settings = (
        'os',
        'arch',
        'compiler',
        'build_type'
    )

    exports_sources = (
        'CMakeLists.txt',
        'cmake/*',
        'src/*',
        'test/*'
    )

    def build_requirements(self):
        self.tool_requires('cmake/[>=3.27.0]')
        self.tool_requires('ccache/[>=4.8.3]')
        self.tool_requires('cppcheck/[>=2.12.1]')
        self.test_requires('gtest/[>=1.14.0]')

    def validate(self):
        check_min_cppstd(self, CPP_VERSION_REQUIRED)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        CMakeToolchain(self).generate()
        CMakeDeps(self).generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
