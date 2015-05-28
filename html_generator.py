contents = [[
    '''
    What computer could do?
    ''',
    '''
    Playing audio and video? Writing article? Surfing internet?
    There is no doubt that modern computer can perfectly do a lot of more things but not limited to above list. Although the computing ability has been improved tremendously 18 months by 18 months, the thing that a computer can do is always the same: 
    The thing that can be computed and solved in limited specific steps.
    '''],
    ['''
    The programming script
    ''',
    '''
    The programming script is a combination of bunch of instructions which could be executed by computer step by step. These instructions are what we people want the computer to do.
    A script is always a plain text file stored in our computer's hard drive. When people run the script, an software called interpreter is called to read and execute the instructions in this script.
    In python language, python is the interpreter, and the *.py files are the executed scripts.
    '''
        ],
    ['''
    About functions
    ''',
    '''
    In the world of developers, nobody like repetition. To avoid this, smart developers like to put some instructions for a particular function into a capsuled text block. Then give a specific name to this block. When such function are needed, developers don't have to rewrite the whole thing again, but only call the name of the text block and all lines in this block would be executed.
    That saves time and life.
    This text block is called a function, or a procedure. Developer could refer to this function by the given name when it was defined.
    Usually, a typical function or procedure might take INPUT date from outside the function. Then the function could manipulate its input as the commands or instructions it has, and return a OUTPUT to the outside world. Such as print some information on the screen, give a calculation result to other functions, etc.
    ''']
        ]

def generate_description(description):
    '''
    generate the long string with multi-paragraphs around by p tags.
    '''
    P_TAG = "<p></p>"
    html_text = '''
        '''
    for line in description.splitlines():
        if line.strip() != '':
            html_text += P_TAG[0:3] + line.strip() + P_TAG[-4:] + "\n"

    return html_text

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title

    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + generate_description(concept_description) 

    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(contents)
