import atexit
import re
from subprocess import Popen, PIPE
import sys

test_results = []


def add_result(name, error=None):
    result = {"name": name, "error": error}
    report_result(result)
    test_results.append(result)


def report_result(result):
    print("%s: %s" % (result['name'], result['error'] or 'OK'))


def will(name, command, input='', output='', error='', status=0):
    full_command = ['python', 'commander.py'] + command
    process = Popen(full_command, stdout=PIPE, stderr=PIPE)
    actual_output, actual_error = process.communicate(input)
    errors = []
    if not re.match(output, actual_output):
        errors.append('Expected output "%s", got "%s"' % (output, actual_output))
    if not re.match(error, actual_error):
        errors.append('Expected error "%s", got "%s"' % (error, actual_error))
    if process.returncode != status:
        errors.append('Expected status "%s", got "%s"' % (status, process.returncode))
    if errors:
        errors.append('Command: ' + ' '.join(full_command))
    add_result(name, "\n  ".join(errors))


def fail_on_failures():
    failures = filter(lambda result: result['error'], test_results)
    if failures:
        sys.stderr.write("Failures: %d\n" % len(failures))
        sys.exit(1)

atexit.register(fail_on_failures)
