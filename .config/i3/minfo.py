# -*- coding: utf-8 -*-
"""
Fetch Cmus <song> - <artist>

Multi-line description followed by an empty line.

Configuration parameters:
    - cache_timeout : how often we refresh this module in seconds

@author (github: juanvallejo) juan.vallejo.12@cnu.edu
@license BSD
"""

# import your useful libs here
from time import time
from subprocess import Popen, PIPE


class Py3status:
    """
    The Py3status class name is mandatory.

    Below you list all the available configuration parameters and their
    default value for your module which can be overwritten by users
    directly from their i3status config.

    This examples features only one parameter which is 'cache_timeout'
    and is set to 10 seconds (0 would mean no cache).
    """
    # available configuration parameters
    cache_timeout = 5

    def __init__(self):
        """
        This is the class constructor which will be executed once.
        """
        pass

    def kill(self, i3s_output_list, i3s_config):
        """
        This method will be called upon py3status exit.
        """
        pass

    def on_click(self, i3s_output_list, i3s_config, event):
        """
        This method should only be used for ADVANCED and very specific usages.

        Read the 'Handle click events directly from your i3status config'
        article from the py3status wiki:
            https://github.com/ultrabug/py3status/wiki/

        This method will be called when a click event occurs on this module's
        output on the i3bar.

        Example 'event' json object:
        {'y': 13, 'x': 17, 'button': 1, 'name': 'example', 'instance': 'first'}
        """
        pass

    def fetch_cmus_songinfo(self, i3s_output_list, i3s_config):
        """
        This method will return an empty text message
        so it will NOT be displayed on your i3bar.

        If you want something displayed you should write something
        in the 'full_text' key of your response.

        See the i3bar protocol spec for more information:
        http://i3wm.org/docs/i3bar-protocol.html
        """
        
        p = Popen(['minfo'], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        res = p.communicate()[0]

        response = {
            'cached_until': time() + self.cache_timeout,
            'full_text': (str(res[:-1])[2:-1] if res != None else '')
        }
        return response

if __name__ == "__main__":
    """
    Test this module by calling it directly.
    This SHOULD work before contributing your module please.
    """
    from time import sleep
    x = Py3status()
    config = {
        'color_bad': '#FF0000',
        'color_degraded': '#FFFF00',
        'color_good': '#00FF00'
    }
    while True:
        print(x.fetch_cmus_songinfo([], config))
        sleep(1)
