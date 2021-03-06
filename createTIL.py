''' Simple script to auto-generate the README.md file for a TIL project. 
	Apply as a git hook by running the following command in Linux: 
	cd .git/hooks/ && ln -s ../../createTIL.py pre-commit && cd -
'''
import os

HEADER = '''# TIL   

*Today I Learned*   

A collection of concise write-ups on small things I learn across a variety of 
languages and technologies.   

'''

FOOTER = '''## Usage   
Steps to follow:   

1. Create directories for specific topics.   

2. Inside those directories create a [`Markdown`](https://www.markdownguide.org/basic-syntax/) 
file with your title for example `How_to_autogenerate_a_README.md`, 
`Create_a_simple_App.md` etc. Make sure that the markdown file has a title. 
Spaces in titles are _not_ recommended since different services render markdown differently.   

3. Every Markdown TIL file should start with a `#` i.e h1 heading.   

4. Run `python createTIL.py` to auto-generate the new README file for you   

OR  

If you are using git, you can install this script as a pre-commit git hook so
that it is autogenerated on each commit. Use the following command:  
`cd .git/hooks/ && ln -s ../../createtil.py pre-commit && cd -`   

5. Once satisfied push your changes.   

## About  

Original Idea/Work [thoughtbot/til](https://github.com/thoughtbot/til).   

'''


def get_category_list ():
    ''' Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" in which there are TILs. '''
    dirs = [x for x in os.listdir ('.') if os.path.isdir (x) and '.git' not in x]
    return dirs


def get_title (til_file):
    ''' Read the file until we hit the first line that starts with a #
    indicating a title in markdown.  We'll use that as the title for this
    entry. '''
    with open (til_file) as file:
        for line in file:
            line = line.strip ()
            if line.startswith ('#'):
                return line[1:].lstrip ()  # text after # and whitespace


def get_tils (category):
    ''' For a given category, get the list of TIL titles. '''
    til_files = [x for x in os.listdir (category)]
    titles = []
    for filename in til_files:
        fullname = os.path.join (category, filename)
        if (os.path.isfile (fullname)) and fullname.endswith ('.md'):
            title = get_title (fullname)
            # changing path separator for Windows paths
            # https://mail.python.org/pipermail/tutor/2011-July/084788.html
            titles.append ((title, fullname.replace (os.path.sep, '/')))
    return titles


def get_category_dict (category_names):
    categories = {}
    count = 0
    for category in category_names:
        titles = get_tils (category)
        categories[category] = titles
        count += len (titles)
    return (count, categories)


def print_file (category_names, count, categories):
    ''' Now we have all the information, print it out in markdown format. '''
    with open ('README.md', 'w') as file:
        file.write (HEADER)
        if count == 1:
            file.write ('_{0} TIL and counting..._'.format(count))
        else:
            file.write ('_{0} TILs and counting..._'.format(count))
        file.write ('''   

## Categories   

''')
	# print the list of categories with links
        for category in sorted (category_names):
            file.write ('* [{0}](#{1})\n'.format (category.capitalize (), category))

        if len (category_names) > 0:
            file.write ('''   

---

''')
	# print the section for each category
        for category in sorted (category_names):
            file.write ('### {0}\n'.format (category.capitalize ()))
            file.write ('\n')
            tils = categories[category]
            for (title, filename) in sorted (tils):
                file.write ('- [{0}]({1})\n'.format (title, filename))
            file.write ('\n')

        if len (category_names) > 0:
            file.write ('''---  

''')
        file.write (FOOTER)   


def create_README ():
    ''' Create a TIL README.md file with a nice index for using it directly
    from GitHub. '''
    category_names = get_category_list ()
    count, categories = get_category_dict (category_names)
    print_file (category_names, count, categories)


if __name__ == '__main__':
    create_README ()
