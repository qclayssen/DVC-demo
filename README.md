# DVC-demo

This repository demonstrates a minimal [DVC](https://dvc.org/) workflow.
It is inspired by Stian Lagstad's blog post about managing large test data
with DVC and custom GitHub Action runners.

## Setup

Install the required tools:

```bash
pip install dvc
```

Initialise the repository and set up a local remote:

```bash
dvc init
dvc remote add -d localremote ./dvc_storage
```

## Pipeline

The repository contains a small example pipeline which converts the contents
of `data/raw.txt` to uppercase. The stage is defined in `dvc.yaml` and can be
reproduced with:

```bash
dvc repro
```

Data is tracked with DVC and stored in the `localremote` directory.

## Running the demo

1. Modify `data/raw.txt` and run `dvc repro` to generate a new
   `data/processed.txt`.
2. Use `dvc push` to store the data in the configured remote.
3. Use `dvc pull` to retrieve the data on a fresh clone.
