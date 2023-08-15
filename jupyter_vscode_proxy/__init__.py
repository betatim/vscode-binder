import os
import shutil

def _get_vscode_cmd(port):
    executable = "code-server"
    if not shutil.which(executable):
        raise FileNotFoundError("Can not find code-server in PATH")
    
    # Start vscode in CODE_WORKINGDIR env variable if set
    # If not, start in 'current directory', which is $REPO_DIR in mybinder
    # but /home/jovyan (or equivalent) in JupyterHubs
    working_dir = os.getenv("CODE_WORKINGDIR", ".")

    extensions_dir = os.getenv("CODE_EXTENSIONSDIR", None)
    cmd = [
        executable,
        "--auth",
        "none",
        "--disable-telemetry",
        "--port=" + str(port),
    ]

    if extensions_dir:
        cmd += ["--extensions-dir", extensions_dir]

    cmd.append(working_dir)
    return cmd


def _get_openvscode_cmd(port):
    executable = "openvscode-server"
    if not shutil.which(executable):
        raise FileNotFoundError("Can not find openvscode-server in PATH")

    cmd = [
        executable,
        "--without-connection-token",
        "--telemetry-level off",
        "--port=" + str(port),
    ]

    if (extensions_dir := os.getenv("CODE_EXTENSIONSDIR", None)):
        cmd += ["--extensions-dir", extensions_dir]

    # Start openvscode in CODE_WORKINGDIR env variable if set
    # If not, start in 'current directory'.
    working_dir = os.getenv("CODE_WORKINGDIR", ".")
    cmd.append(working_dir)
    return cmd


_CODE_EXECUTABLE_CMD_MAP = {
    "code-server": _get_vscode_cmd,
    "openvscode-server": _get_openvscode_cmd,
}


def setup_vscode():
    executable = os.environ.get("CODE_EXECUTABLE", "code-server")
    if executable not in _CODE_EXECUTABLE_CMD_MAP:
        raise KeyError(f"'{executable}' is not one of {_CODE_EXECUTABLE_CMD_MAP.keys()}.")
    return {
        "command": _CODE_EXECUTABLE_CMD_MAP[executable],
        "timeout": 300,
        "new_browser_tab": True,
        "launcher_entry": {
            "title": "VS Code",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", "vscode.svg"
            ),
        },
    }
