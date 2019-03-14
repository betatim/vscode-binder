import os
import shutil


def setup_vscode():
    def _get_vscode_cmd(port):
        executable = 'code-server'
        if not shutil.which(executable):
            raise FileNotFoundError('Can not find code-server in PATH')

        working_dir = os.getenv("CODE_WORKINGDIR", None)
        if working_dir is None:
            working_dir = os.getenv("REPO_DIR", ".")

        cmd = [
            executable,
            '--no-auth',
            '--allow-http',
            '--port=' + str(port),
            working_dir
        ]
        return cmd

    return {
        'command': _get_vscode_cmd,
        'timeout': 20,
        'launcher_entry': {
            'title': 'VS Code',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      'icons',
                                      'vscode.svg')
        }
    }
