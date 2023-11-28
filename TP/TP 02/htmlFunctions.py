import random

# Functions adapted from ProgrammingHistorian
# http://niche.uwo.ca/programming-historian/index.php/Tag_clouds

def make_HTML_word(word,cnt,high,low):
    '''
    Make a word with a font size and a random color.
    Font size is scaled between htmlBig and htmlLittle (to be user set).
    high and low represent the high and low counts in the document.
    cnt is the count of the word. 
    Required -- word (string) to be formatted
             -- cnt (int) count of occurrences of word
             -- high (int) highest word count in the document
             -- low (int) lowest word count in the document
    Return -- a string formatted for HTML that is scaled with respect to cnt
    '''
    htmlBig = 96
    htmlLittle = 14
    if high != low:
        ratio = (cnt-low)/float(high-low)
    else:
        ratio = 0
    fontsize = htmlBig*ratio + (1-ratio)*htmlLittle
    fontsize = int(fontsize)
    rgb = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    word_str = '<span style=\"color: rgb{}; font-size:{:s}px;\">{:s}</span>'
    return word_str.format(rgb,str(fontsize), word)

def make_HTML_box(body):
    '''
    Take one long string of words and put them in an HTML box.
    If desired, width, background color & border can be changed in the function
    This function stuffs the "body" string into the the HTML formatting string.

    Required -- body (string), a string of words
    Return -- a string that specifies an HTML box containing the body
    '''
    box_str = """<div style=\"
    width: 560px;
    background-color: rgb(250,250,250);
    border: 1px grey solid;
    text-align: center\" >{:s}</div>
    """
    return box_str.format(body)

def print_HTML_file(body,title):
    '''
    Create a standard html page (file) with titles, header etc.
    and add the body (an html box) to that page. File created is title+'.html'
    Required -- body (string), a string that specifies an HTML box
    Return -- nothing
    '''
    fd = open(title+'.html','w')
    the_str="""
    <html> <head>
    <title>"""+title+"""</title>
    </head>

    <body>
    <h1>"""+title+'</h1>'+'\n'+body+'\n'+"""<hr>
    </body> </html>
    """
    fd.write(the_str)
    fd.close()

# example usage
def main():
    pairs = [('Hai',25),('Monyet',35),(':)',25)]
    high_count=20
    low_count=2
    body=''
    for word,cnt in pairs:
        body = body + " " + make_HTML_word(word,cnt,high_count,low_count)
    box = make_HTML_box(body)  # creates HTML in a box
    print_HTML_file(box,'buka deh')  # writes HTML to file name 'testFile.html'

if __name__ == '__main__':
    main()
