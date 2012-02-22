import re
re.DOTALL

hw_folder = '/hw_files'

def get_type(ans):
    name = ans[2:-2]
    if name=='int':
        return int
    elif name=='float':
        return float
    elif name=='str' or name=='string':
        return str
    else:
        raise Exception('Type Not Supported')

class Homework:
    def __init__(self,id,name,questions):
        self.id = id
        self.name = name
        self.questions = questions

class Question:

    # a question has attributes:
    #   - name (string)
    #   - body (string)
    #   - points (int)
    # be sure to implement these fields in all subclasses

    # determines types of each of the answer choices
    def set_types(self):
        answers = re.findall(r'<<\w*?>>',self.body)
        self.types = [get_type(ans) for ans in answers]

    # converts input answers to their appropriate type
    def clean(self,ans):
        for i in range(len(ans)):
            if ans[i]:
                try:
                    ans[i] = self.types[i](ans[i]) # convert ans to its natural type
                except:
                    ans[i] = 'Type Error!'
        return ans

    # converts question body to HTML
    def parse(self):
        # replace <!numeric!> with text box
        html_str = re.sub("<<int>>",
                          "<input type='text' name='ans' size=5>",
                          self.body)
        html_str = re.sub("\n","<br>",html_str)
        return html_str
