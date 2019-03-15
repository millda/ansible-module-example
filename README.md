# Basic Ansible Example

a very basic ansible module without a lot of documentation. See the reference links before for more detailed explanations.

## Files
+-- ansible.cfg: Add the path to your module here
+-- playbook.yml: Example call to your custom module
+-- roles
|   +-- demo
|   |   +-- library
|   |   |   +-- __init__.py
|   |   |   +-- demo.py: Ansible tasks calls this file by name
|   |   |   +-- example_class.py: Class for custom logic
|   |   |   +-- tasks
|   |   |   |   +-- main.yml: Ansible task called when the role is imported
|   |   +-- test.yml

## References

- [Ansible Module Docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html)
