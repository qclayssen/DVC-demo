# DVC-demo

This repository demonstrates a minimal [DVC](https://dvc.org/) workflow on
Linux and macOS. It provides a tiny bioinformatics-style pipeline that
converts a FASTQ file to a BAM-like file and then to a VCF-like file.

The example is inspired by [Stian Lagstad's blog post](https://stianlagstad.no/2024/10/efficient-management-of-large-test-data-for-nextflow-pipelines-using-dvc-and-custom-github-actions-runners/).

## Setup

Install DVC (works on Linux and macOS):

```bash
pip install dvc
```

Initialise the repository and set up a local remote:

```bash
dvc init
dvc remote add -d localremote ./dvc_storage
```

## Pipeline

The pipeline has two stages defined in `dvc.yaml`:

1. `fastq_to_bam` – converts `data/sample.fastq` to a simple BAM-like
   representation stored in `data/sample.bam`.
2. `bam_to_vcf` – converts the BAM file to a tiny VCF-like file
   `data/sample.vcf`.

Reproduce the pipeline with:

```bash
dvc repro
```

## Running the demo

After running `dvc repro`, use `dvc push` to store the data in the
configured remote and `dvc pull` to retrieve it in a fresh clone.
