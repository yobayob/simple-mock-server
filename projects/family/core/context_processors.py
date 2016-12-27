from django.core.context_processors import request


def git_sha_id(request):
    import subprocess
    label = ''
    try:
        label = subprocess.check_output(["git", "describe"])
    except subprocess.CalledProcessError:
        pass
    try:
        with open('VERSION', 'r') as f:
            label = f.read()
    except IOError:
        pass
    return {
        'git_sha_id': label
    }
