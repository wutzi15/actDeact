import sys
import ConfigParser
import os
from optparse import OptionParser
import pkg_resources


def main():
    """Entry point for the application script"""
    print("Called actDeact")
    #filename = resource_filename(Requirement.parse("actDeact"),"actDeact.conf")
    print("Got filename: ", pkg_resources.resource_filename(__name__, "actDeact.conf"))
    print("Got filename: ", pkg_resources.resource_filename("actDeact", "actDeact.conf"))


