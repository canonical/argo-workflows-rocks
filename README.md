# ROCKs for Argo Workflows

This repository contains collection of ROCKs for Argo Workflows.

- argocli/ contains Rockcraft project for Argo Workflows CLI (TO BE DEPRECATED?)
- argoexec/ contains Rockcraft project for Argo Workflows executor.
- workflow-controller/ contains Rockcraft project for Argo Workflows controller.

To build ROCK execute the following command in correspomnding directory:

```
rockcraft pack
```

To run sanity tests on the ROCK execute the following command in correspomnding directory:

```
tox -e sanity
```

