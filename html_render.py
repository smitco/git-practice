# lesson 07 html render
# !/usr/bin/env python3

"""
Restart with:
class Element(object):

    def __init__(self, content=None):
        pass

    def append(self, new_content):
        pass

    def render(self, out_file):
        out_file.write("just something as a place holder...")
"""

# link to exercise: https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/html_renderer.html#html-primer

import pdb
#Step 1
class Element(object):
    def __init__(self, content=None):
        self.tag_name = ""
        if content is None:
            self.content = []
        else:
            self.content = [content]
    def append(self, new_content):
        self.content.append(new_content)
    def render(self, out_file, cur_ind=""):
        out_file.write("<" + self.tag_name + ">\n")
        pdb.set_trace()
        for c in self.content:
            out_file.write(str(c) + "\n")
        out_file.write("</" + self.tag_name + ">")

#Step 2 Part A
class Html(Element):
    def __init__(self, content=None):
        super(Html, self).__init__(content=content)
        self.tag_name = "html"

class Body(Element):
    def __init__(self, content=None):
        super(Body, self).__init__(content=content)
        self.tag_name = "body"

class P(Element):
    def __init__(self, content=None):
        super(P, self).__init__(content=content)
        self.tag_name = "p"
