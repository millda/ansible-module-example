# !/usr/bin/python
"""
Example module code, as basic as possible
"""

# Ansible needs to have the class copied over and path to classes set
import sys
sys.path.append('/tmp')
from example_class import Automation

from ansible.module_utils.basic import AnsibleModule


def run_module():
    """ Run a minimal module """

    # define available arguments/parameters a user can pass to the module
    module_args = {"destination": {"required": True, "type": "str"}}

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # Set the original state. Our code will fill this object
    result = {"changed": False, "message": ""}

    # Custom module logic here!
    automation = Automation(destination=module.params['destination'])
    is_error, result = automation.do_something()

    # Custom logic has completed. Return the result - failure or success
    if is_error:
        module.fail_json(msg='Something went wrong!', **result)
    else:
        module.exit_json(**result)


def main():
    """ call ansible module code """
    run_module()


if __name__ == '__main__':
    main()
