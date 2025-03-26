#### Prerequisites

* Conan version >=2.0.11

#### How to install dependencies

```bash
conan install . --output-folder=build --build=missing
```

#### How to build

```bash
cd build

cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_TOOLCHAIN_FILE=build/Release/generators/conan_toolchain.cmake

cmake --build . --config Release

./bin/Project
```

#### How to install

```bash
cmake --install .
```

#### How to test

```bash
ctest
```