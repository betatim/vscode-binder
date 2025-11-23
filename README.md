# VS Code on Binder

[![PyPI](https://img.shields.io/pypi/v/jupyter-vscode-proxy)](https://pypi.org/project/jupyter-vscode-proxy/)
[![Install with conda](https://anaconda.org/conda-forge/jupyter-vscode-proxy/badges/version.svg)](https://github.com/conda-forge/jupyter-vscode-proxy-feedstock)

VS Code on Binder, because sometimes you need a real editor.

Try it: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/betatim/vscode-binder/master?urlpath=lab)

## Configuration

### Environment Variables

| Environment Variable              | Effect                                        | Default Value           | Notes |
|-----------------------------------|-----------------------------------------------|-------------------------|------------------------------------------------------------------------|
| `CODE_WORKINGDIR`                 | Set the working directory for VS Code         | `.` (current directory) | This is `$REPO_DIR` in mybinder or `/home/jovyan` in JupyterHub        |
| `CODE_EXTENSIONSDIR`              | Set a custom extensions directory for VS Code | None                    |                                                                        |
| `CODE_EXECUTABLE`                 | Choose which executable to use                | `code-server`           | Options: `code-server` or `openvscode-server`                          |
| `JUPYTER_VSCODE_PROXY_USE_SOCKET` | Proxy over unix socket instead of a TCP port  | Not set (uses TCP port) | If set to anything but "no" or "false" it will listen on a TCP socket. |
