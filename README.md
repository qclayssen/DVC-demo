# DVC-demo

This repository demonstrates a minimal [DVC](https://dvc.org/) workflow.
It is inspired by [Stian Lagstad's blog post](https://stianlagstad.no/2024/10/efficient-management-of-large-test-data-for-nextflow-pipelines-using-dvc-and-custom-github-actions-runners/).

It contains two tiny example pipelines:

1. **Text processing** – converts `data/raw.txt` to uppercase in `data/processed.txt`.
2. **Bioinformatics demo** – converts a FASTQ file to a BAM-like file and then to a VCF-like file.

## Setup

Install DVC:

```bash
pip install dvc
```

Initialise the repository and set up a local remote:

```bash
dvc init
dvc remote add -d localremote ./dvc_storage
```

## Pipeline

The `dvc.yaml` file defines three small stages:

1. `process` – converts `data/raw.txt` to uppercase in `data/processed.txt`.
2. `fastq_to_bam` – converts `data/sample.fastq` to a simple BAM-like file `data/sample.bam`.
3. `bam_to_vcf` – converts the BAM file to a tiny VCF-like file `data/sample.vcf`.

Reproduce the full pipeline with:

```bash
dvc repro
```

Data is tracked with DVC and stored in the `localremote` directory.

## Running the demo

1. Modify `data/raw.txt` or `data/sample.fastq` and run `dvc repro` to generate new outputs.
2. Use `dvc push` to store the data in the configured remote.
3. Use `dvc pull` to retrieve the data on a fresh clone.
