from conans import ConanFile


class NodConan(ConanFile):
    name = "nod"
    version = "0.5.0"
    license = "Copyright (c) 2015 Fredrik Berggren MIT license"
    url = "https://github.com/Lawrencemm/conan_nod"
    description = "C++ Signals and slots library"
    topics = ("signal", "slot", "event")

    def source(self):
        self.run("git clone https://github.com/fr00b0/nod.git")
        self.run("git checkout 56a9e5a441947f313f062c6147c57f0966ea07a6")

    def package(self):
        self.copy("*.hpp", dst="include", src="nod/include")
