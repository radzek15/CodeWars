"""
Silent Import

As part of your spy training, You were taught to be as stealthy as possible while carrying out missions. This time, you have to silently import modules from a without getting caught. Most of your peers are skeptical if you will be able to do this. But, you are the G.O.A.T and you always have a plan.
Your Task

Write a function silent_thief that will import any module passed in to it and return it.

Your code must NOT:

    Contain the word import
    Contain any double underscores: __
    Use either eval or exec.

Extra info

This is kata 2 of my awesome spy series.
Please take time to give feedback on this kata.
"""


def silent_thief(module_name):
    return globals()['_''_builtins_''_']['_''_impo''rt_''_'](module_name)
