import setuptools

setuptools.setup(
    name="jupyter-vscode-proxy",
    version="0.1",
    url="https://github.com/betatim/vscode-binder",
    author="Tim Head",
    description="Jupyter extension to proxy VS Code",
    packages=setuptools.find_packages(),
    keywords=["Jupyter"],
    classifiers=["Framework :: Jupyter"],
    install_requires=[
        #'jupyter-server-proxy'
    ],
    entry_points={
        "jupyter_serverproxy_servers": ["vscode = jupyter_vscode_proxy:setup_vscode",]
    },
    package_data={"jupyter_vscode_proxy": ["icons/*"],},
)
