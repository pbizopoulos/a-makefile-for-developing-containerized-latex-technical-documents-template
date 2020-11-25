[![template](http://img.shields.io/badge/template-EEE0B1.svg)](https://github.com/pbizopoulos/docker-as-a-development-environment-for-documenting-results-template)
[![test-local-reproducibility](https://github.com/pbizopoulos/docker-as-a-development-environment-for-documenting-results-template/workflows/test-local-reproducibility/badge.svg)](https://github.com/pbizopoulos/docker-as-a-development-environment-for-documenting-results-template/actions?query=workflow%3Atest-local-reproducibility)


# Document Title
This repository contains the code that generates **Document Title**.

## Requirements
- [POSIX](https://en.wikipedia.org/wiki/POSIX)-oriented operating system
- [docker](https://docs.docker.com/get-docker/)
- [make](https://www.gnu.org/software/make/)
- [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit) (required only when using CUDA)

## Instructions
1. `git clone https://github.com/{user}/{document-title}`
2. `cd {document-title}`
3. `sudo systemctl start docker`
4. make options
    * `make`             # Generate pdf.
    * `make ARGS=--full` # Generate full pdf.
    * `make clean`       # Remove build and cache directories.
