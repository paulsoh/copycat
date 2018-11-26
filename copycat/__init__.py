from fabric.api import local, abort
from .inquirer import get_answers

def run():
    answers = get_answers()
    dest_hostname = answers.get('dest_hostname')
    source_path = answers.get('source_path')
    dest_path = answers.get('dest_path')

    result = local("scp -r {} {}:{}".format(
        source_path,
        dest_hostname,
        dest_path
    ))

    if result.failed:
        abort("Failed copy")
    else:
        print("Upload from {} to {}:{} is complete!".format(source_path, dest_hostname, dest_path))

if __name__ == "__main__":
    copycat()
