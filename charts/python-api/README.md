# Python API Demo Helm Chart

This Helm chart provides a Kubernetes deployment for a Python-based API. It allows easy deployment and configuration of a Python API on Kubernetes clusters using Helm. The chart is designed to simplify the deployment process by encapsulating best practices for Kubernetes resource definitions and configurations for Python-based applications.

## Repository

This Helm chart is part of the [gh-pages-as-helm-repo](https://github.com/sarubhai/gh-pages-as-helm-repo) GitHub repository, which is configured as an exclusive Helm repository hosted on GitHub Pages and using GitHub Container Registry (GCR) for storing the chart images.

## Prerequisites

- Helm 3.x or newer
- Kubernetes 1.19+ with cluster-admin permissions

## Installation

To install this chart with the release name `my-python-api`:

1. First, add the repository to Helm (if not already added):

```
helm repo add my-helm-repo https://sarubhai.github.io/gh-pages-as-helm-repo
```

2. Update the Helm repository to fetch the latest charts:

```
helm repo update
```

3. Install the chart:

```
helm install my-python-api my-helm-repo/python-api
```

## Configuration
The following table lists the configurable parameters of the python-api chart and their default values.
| Parameter                            | Description                                | Default                                  |
|--------------------------------------|--------------------------------------------|------------------------------------------|
| `image.repository`                   | Docker image repository for the Python API | `ghcr.io/sarubhai/gh-pages-as-helm-repo` |
| `image.tag`                          | Docker image tag for the Python API        | `<github.sha>`                           |
| `image.pullPolicy`                   | Image pull policy                          | `IfNotPresent`                           |
| `imagePullSecrets`                   | Image pull secrets                         | `[]`                                     |
| `replicaCount`                       | Number of replicas for the deployment      | `1`                                      |
| `resources`                          | Resource requests and limits               | `{}`                                     |
| `service.type`                       | Kubernetes service type                    | `ClusterIP`                              |
| `service.port`                       | Port on which the service is exposed       | `80`                                     |
| `ingress.enabled`                    | Enable or disable ingress                  | `false`                                  |
| `ingress.className`                  | Ingress class name                         | `""`                                     |
| `ingress.annotations`                | Additional annotations for the ingress     | `{}`                                     |
| `ingress.hosts[0].host`              | Hostname for the ingress                   | `python-api.local`                       |
| `ingress.hosts[0].paths[0].path`     | Path within the host for the ingress       | `/`                                      |
| `ingress.hosts[0].paths[0].pathType` | Path type for the ingress                  | `Prefix`                                 |
| `ingress.tls`                        | TLS configuration for the ingress          | `[]`                                     |
| `ingress.tls[0].hosts[0]`            | TLS hostname for the ingress               | `python-api.local`                       |
| `ingress.tls[0].secretName`          | TLS secret name for the ingress            | `python-api-tls`                         |



## Customization
You can specify each parameter directly on the command line using the --set flag or by providing a values.yaml file.

### Example: Setting Parameters

```
helm install my-python-api my-helm-repo/python-api \
    --namespace backend-api --create-namespace \
    --set replicaCount=2 \
    --set ingress.enabled=true \
    --set ingress.className=nginx \
    --set ingress.annotations."nginx\.ingress\.kubernetes\.io/backend-protocol"=HTTP \
    --set-string ingress.annotations."nginx\.ingress\.kubernetes\.io/force-ssl-redirect"=true \
    --set "ingress.hosts[0].host=python-api.local" \
    --set "ingress.hosts[0].paths[0].path=/,ingress.hosts[0].paths[0].pathType=Prefix" \
    --set "ingress.tls[0].hosts[0]=python-api.local" \
    --set "ingress.tls[0].secretName=python-api-tls"
```

### Example: Using a Custom values.yaml file
1. Create a custom values.yaml file with your desired values:

```
replicaCount: 2
ingress:
  enabled: true
  className: nginx
  annotations:
    nginx.ingress.kubernetes.io/backend-protocol: HTTP
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
  hosts:
    - host: python-api.local
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: python-api-tls
      hosts:
        - python-api.local
```

2. Install the chart using your custom values.yaml:

```
helm install my-python-api my-helm-repo/python-api -f values.yaml
```

## Upgrading the Chart

```
helm upgrade my-python-api my-helm-repo/python-api
```

## Uninstallation

```
helm uninstall my-python-api
```

This command will remove all Kubernetes components associated with the release, including the deployment and service.
