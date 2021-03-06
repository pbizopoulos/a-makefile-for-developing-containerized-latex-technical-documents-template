[![template](http://img.shields.io/badge/template-EEE0B1.svg)](https://github.com/pbizopoulos/a-makefile-for-developing-containerized-latex-technical-documents-template)
[![test-draft-version-document-reproducibility](https://github.com/pbizopoulos/a-makefile-for-developing-containerized-latex-technical-documents-template/workflows/test-draft-version-document-reproducibility/badge.svg)](https://github.com/pbizopoulos/a-makefile-for-developing-containerized-latex-technical-documents-template/actions?query=workflow%3Atest-draft-version-document-reproducibility)

# A Makefile for Developing Containerized LaTeX Technical Documents Template
This repository contains the code that generates **A Makefile for Developing Containerized LaTeX Technical Documents Template**.

## Requirements
- [Docker](https://docs.docker.com/get-docker/)
    - [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#setting-up-nvidia-container-toolkit) (Optional)
- [Make](https://www.gnu.org/software/make/)

## Instructions
1. `git clone https://github.com/{user}/a-makefile-for-developing-containerized-latex-technical-documents-template`
2. `cd a-makefile-for-developing-containerized-latex-technical-documents-template/`
3. `sudo systemctl start docker`
4. make options
    - `make` # Generate the draft (fast) version document.
    - `make VERSION=--full` # Generate the full (slow) version document.
    - `make clean` # Remove the tmp/ directory.
