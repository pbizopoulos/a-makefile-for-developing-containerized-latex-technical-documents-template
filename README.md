[![template](http://img.shields.io/badge/template-EEE0B1.svg)](https://github.com/pbizopoulos/docker-as-a-development-environment-for-research-papers-template)
[![test-local-reproducibility](https://github.com/pbizopoulos/docker-as-a-development-environment-for-research-papers-template/workflows/test-local-reproducibility/badge.svg)](https://github.com/pbizopoulos/docker-as-a-development-environment-for-research-papers-template/actions?query=workflow%3Atest-local-reproducibility)


# Paper title
This repository contains the code that generates the paper **Paper title**.

## Requirements
- UNIX utilities (cmp, cp, echo, rm, touch)
- [docker](https://docs.docker.com/get-docker/)
- make
- [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit) (required only when using CUDA)

## Instructions
1. `git clone https://github.com/{user}/{paper-title}`
2. `cd {paper-title}`
3. `sudo systemctl start docker`
4. make options
    * `make`             # Generate pdf.
    * `make ARGS=--full` # Generate full pdf.
    * `make clean`       # Remove build and cache directories.
