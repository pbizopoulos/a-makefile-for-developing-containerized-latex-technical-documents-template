[![template](http://img.shields.io/badge/template-EEE0B1.svg)](https://github.com/pbizopoulos/documenting-results-generation-using-latex-and-docker-template)
[![test-local-reproducibility](https://github.com/pbizopoulos/documenting-results-generation-using-latex-and-docker-template/workflows/test-local-reproducibility/badge.svg)](https://github.com/pbizopoulos/documenting-results-generation-using-latex-and-docker-template/actions?query=workflow%3Atest-local-reproducibility)

# Documenting Results Generation using LaTeX and Docker Template
This repository contains the code that generates **Documenting Results Generation using LaTeX and Docker Template**.

## Requirements
- [POSIX-oriented operating system](https://en.wikipedia.org/wiki/POSIX#POSIX-oriented_operating_systems)
- [docker](https://docs.docker.com/get-docker/)
- [make](https://www.gnu.org/software/make/)
- [nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit) (required only when using CUDA)

## Instructions
1. `git clone https://github.com/{user}/documenting-results-generation-using-latex-and-docker-template`
2. `cd documenting-results-generation-using-latex-and-docker-template`
3. `sudo systemctl start docker`
4. make options
    * `make`             # Generate pdf.
    * `make ARGS=--full` # Generate full pdf.
    * `make clean`       # Remove results and tmp directories.
