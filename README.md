# VS Code on Binder

[![PyPI](https://img.shields.io/pypi/v/jupyter-vscode-proxy)](https://pypi.org/project/jupyter-vscode-proxy/)
[![Install with conda](https://anaconda.org/conda-forge/jupyter-vscode-proxy/badges/installer/conda.svg)](https://github.com/conda-forge/jupyter-vscode-proxy-feedstock)

VS Code on Binder, because sometimes you need a real editor.

Try it: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/betatim/vscode-binder/master?urlpath=lab)

## Using pre-started code-server

In case code-server is already running (e.g. started in sidecar container with Jupyter running in Kubernetes)
and servig either via TCP port or UNIX socket, it is possible to proxy this already running instance instead
of starting a new one with jupyter-server-proxy. Variables `CODE_EXECUTABLE=none` and `CODE_PRESTARTED_PORT`
or `CODE_PRESTARTED_SOCKET` set `command` to empty list which makes `jupyter-server-proxy` pass requests
to specified port of socket.

To use pre-started code-server:
- set `CODE_EXECUTABLE=none`
    - set `CODE_PRESTARTED_PORT` to TCP port number listened by code-server
    - set `CODE_PRESTARTED_SOCKET` to UNIX socket path code-server is listening to

If none of these environment variables are set, jupyter-code-server starts new code-server process and proxies
requests to its socket.
