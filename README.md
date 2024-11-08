# Using GitHub Pages as Helm Chart Repository
This repository demonstrates creating a Helm chart repository hosted on GitHub Pages and integrating it with GitHub Container Registry for seamless CI/CD in Kubernetes deployments. The setup automates the release of Helm charts by packaging and publishing them on GitHub Pages, enabling version control and easy chart distribution.

## Table of Contents
- [Overview](##overview)
- [Features](##features)
- [Pre-requisites](##pre-requisites)
- [Setup](##setup)
- [Usage](##usage)
- [GitHub Workflow](##github-workflow)

### Overview
This project provides a complete setup for maintaining and distributing Helm charts using GitHub Pages and automating the Helm package release workflow via GitHub Actions. Using GitHub Container Registry as a backend, the solution enables:

- Automated chart versioning
- Chart publishing on GitHub Pages for easy access
- Integration with GitHub Container Registry to push images for the charts

### Features
- **Helm Chart Repository on GitHub Pages**: Host your Helm charts with versioning on GitHub Pages for easy access.
- **Automated CI/CD Workflow**: A GitHub Actions workflow (release.yaml) is set up to automate the chart packaging and publishing process.
- **GitHub Container Registry Integration**: Uses GitHub Container Registry to pull or push Docker images associated with the Helm charts.

### Pre-requisites
- **GitHub Pages**: Enable GitHub Pages for this repository to publish the Helm charts.

### Setup
1. **Clone the Repository**:
```
git clone https://github.com/sarubhai/gh-pages-as-helm-repo.git
cd gh-pages-as-helm-repo
```

2. **Enable GitHub Pages**: Go to **Settings** > **Pages** and set the source to the gh-pages branch.

### Usage
1. **Versioning and Pushing Updates**:
- Commit changes to your application or Helm charts as needed.
- Upon pushing a tagged release, the GitHub Actions workflow (release.yaml) will package the chart and push it to GitHub Pages.
2. **Accessing the Charts**: Access published charts via GitHub Pages at [https://<username>.github.io/gh-pages-as-helm-repo/index.yaml](https://<username>.github.io/gh-pages-as-helm-repo/index.yaml)

### GitHub Workflow
The workflow defined in .github/workflows/release.yaml automates the following steps:

1. **Build and Package the Chart**:
- Packages the Helm chart upon detecting a tagged release.

2. **Authenticate with GitHub Container Registry**:
- Logs into GitHub Container Registry using the GITHUB_TOKEN secret.

3. **Push Helm Chart to GitHub Pages**:
- Publishes the packaged chart files to the gh-pages branch, making it accessible on GitHub Pages.

4. **Update Chart Index**:
- Updates the index.yaml file on GitHub Pages to maintain the latest versions for easy chart retrieval.