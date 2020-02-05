import setuptools


with open("README.md", encoding="utf8") as f:
    readme = f.read()


setuptools.setup(
    name="jupyter-vscode-proxy",
    version="0.1",
    url="https://github.com/betatim/vscode-binder",
    author="Tim Head",
    license="BSD",
    description="VS Code extension for Jupyter",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=["Jupyter", "vscode", "vs code", "editor"],
    classifiers=["Framework :: Jupyter"],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        "jupyter_serverproxy_servers": ["vscode = jupyter_vscode_proxy:setup_vscode",]
    },
    package_data={"jupyter_vscode_proxy": ["icons/*"]},
    project_urls={
        "Source": "https://github.com/betatim/vscode-binder/",
        "Tracker": "https://github.com/betatim/vscode-binder/issues",
    },
)
