#!/usr/bin/python
"""
Example class for demo purposes
"""


class Automation:
    """
    Tells you who automation is for
    """

    def __init__(self, destination=None):
        self.destination = destination

    def do_something(self):
        ''' Example function '''
        if self.destination:
            return False, {
                'changed': True,
                'message': 'Automation for ' + self.destination + '!'
            }
        return True, {
            'changed': True,
            'message': 'Error with do_something function'
        }
