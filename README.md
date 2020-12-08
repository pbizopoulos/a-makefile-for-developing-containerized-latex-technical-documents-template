[![template](http://img.shields.io/badge/template-EEE0B1.svg)](https://github.com/pbizopoulos/latex-technical-documents-with-docker-and-make-template)
[![test-fast-draft-reproducibility](https://github.com/pbizopoulos/latex-technical-documents-with-docker-and-make-template/workflows/test-fast-draft-reproducibility/badge.svg)](https://github.com/pbizopoulos/latex-technical-documents-with-docker-and-make-template/actions?query=workflow%3Atest-fast-draft-reproducibility)

# LaTeX Technical Documents with Docker and Make Template
This repository contains the code that generates **LaTeX Technical Documents with Docker and Make Template**.

## Requirements
- [POSIX-oriented operating system](https://en.wikipedia.org/wiki/POSIX#POSIX-oriented_operating_systems)
- [Docker](https://docs.docker.com/get-docker/)
- [Make](https://www.gnu.org/software/make/)
- [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit) (required only when using CUDA)

## Instructions
1. `git clone https://github.com/{user}/latex-technical-documents-with-docker-and-make-template`
2. `cd latex-technical-documents-with-docker-and-make-template/`
3. `sudo systemctl start docker`
4. make options
    * `make`             # Generate the fast/draft version document.
    * `make ARG=--full`  # Generate the slow/final version document.
    * `make clean`       # Remove the tmp directory.
