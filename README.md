# Nativium - Nano GUI

<p align="center">
    <a href="https://github.com/paulo-coutinho/nativium-nanogui" target="_blank" rel="noopener noreferrer">
        <img src="extras/images/screenshot.png" alt="Nativium HTTP Server Screenshot">
    </a>
</p>

<br>

<p align="center">
    <a href="https://github.com/paulo-coutinho/nativium-nanogui/actions/workflows/linux.yml"><img src="https://github.com/paulo-coutinho/nativium-nanogui/actions/workflows/linux.yml/badge.svg"></a>
    <a href="https://github.com/paulo-coutinho/nativium-nanogui/actions/workflows/macos.yml"><img src="https://github.com/paulo-coutinho/nativium-nanogui/actions/workflows/macos.yml/badge.svg"></a>
    <a href="https://github.com/paulo-coutinho/nativium-nanogui/actions/workflows/windows.yml"><img src="https://github.com/paulo-coutinho/nativium-nanogui/actions/workflows/windows.yml/badge.svg"></a>    
    <a href="https://github.com/paulo-coutinho/nativium-nanogui/actions/workflows/wasm.yml"><img src="https://github.com/paulo-coutinho/nativium-nanogui/actions/workflows/wasm.yml/badge.svg"></a>
</p>

<br>

<p align="center">This is a sample that show how to use Nano GUI and Nativium architecture with custom install.</p>

<br>

# General

First of all you need to do the steps of the original [Nativium](https://github.com/paulo-coutinho/nativium) project.

Visit:

https://github.com/paulo-coutinho/nativium

# Build for Linux

Execute the following commands to build for Linux:

```
git clone https://github.com/paulo-coutinho/nativium.git nativium
cd nativium
python nativium.py custom install --path=../custom
python nativium.py target linux prepare
python nativium.py target linux build
python nativium.py target linux run
```

# Build for macOS

Execute the following commands to build for macOS:

```
git clone https://github.com/paulo-coutinho/nativium.git nativium
cd nativium
python nativium.py custom install --path=../custom
python nativium.py target macos prepare
python nativium.py target macos build
python nativium.py target macos run
```

# Build for Windows

Execute the following commands to build for Windows:

```
git clone https://github.com/paulo-coutinho/nativium.git nativium
cd nativium
python nativium.py custom install --path=../custom
python nativium.py target windows prepare
python nativium.py target windows build
python nativium.py target windows run
```

Obs: On Windows the terminal needs to be opened as `administrator`, otherwise the `symlinks` will not be created.

# Build for WASM

Execute the following commands to build for Web Assembly (WASM):

```
git clone https://github.com/paulo-coutinho/nativium.git nativium
cd nativium
python nativium.py custom install --path=../custom
python nativium.py target wasm prepare
python nativium.py target wasm build
python nativium.py target wasm serve
```

# Web Assembly Demo

Visit:

[https://nativium-nanogui.s3.amazonaws.com/demo/1.0.0/index.html](https://nativium-nanogui.s3.amazonaws.com/demo/1.0.0/index.html)
