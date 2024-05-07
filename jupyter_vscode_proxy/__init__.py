import os
import shutil
from typing import Any, Callable, Dict, List


def _get_inner_vscode_cmd() -> List[str]:
    return [
        "code-server",
        "--auth",
        "none",
        "--disable-telemetry",
    ]


def _get_inner_openvscode_cmd() -> List[str]:
    return [
        "openvscode-server",
        "--without-connection-token",
        "--telemetry-level",
        "off",
    ]


_CODE_EXECUTABLE_INNER_CMD_MAP: Dict[str, Callable] = {
    "code-server": _get_inner_vscode_cmd,
    "openvscode-server": _get_inner_openvscode_cmd,
}


def _get_cmd_factory(executable: str) -> Callable:
    if executable not in _CODE_EXECUTABLE_INNER_CMD_MAP:
        raise KeyError(
            f"'{executable}' is not one of {_CODE_EXECUTABLE_INNER_CMD_MAP.keys()}."
        )

    get_inner_cmd = _CODE_EXECUTABLE_INNER_CMD_MAP[executable]

    def _get_cmd(port: int) -> List[str]:
        if not shutil.which(executable):
            raise FileNotFoundError(f"Can not find {executable} in PATH")

        # Start vscode in CODE_WORKINGDIR env variable if set
        # If not, start in 'current directory', which is $REPO_DIR in mybinder
        # but /home/jovyan (or equivalent) in JupyterHubs
        working_dir = os.getenv("CODE_WORKINGDIR", ".")

        extensions_dir = os.getenv("CODE_EXTENSIONSDIR", None)

        cmd = get_inner_cmd()

        cmd.append("--port=" + str(port))

        if extensions_dir:
            cmd += ["--extensions-dir", extensions_dir]

        cmd.append(working_dir)
        return cmd

    return _get_cmd


def setup_vscode() -> Dict[str, Any]:
    executable = os.environ.get("CODE_EXECUTABLE", "code-server")
    icon = "code-server.svg" if executable == "code-server" else "vscode.svg"
    return {
        "command": _get_cmd_factory(executable),
        "timeout": 300,
        "new_browser_tab": True,
        "launcher_entry": {
            "title": "VS Code",
            "icon_path": os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "icons", icon
            ),
        },
    }
