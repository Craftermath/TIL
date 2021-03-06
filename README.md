# TIL   

*Today I Learned*   

A collection of concise write-ups on small things I learn across a variety of 
languages and technologies.   

_5 TILs and counting..._   

## Categories   

* [12factor](#12Factor)
* [Github](#Github)
* [Python](#Python)
   

---

### 12factor

- [Logging Like a Pro](12Factor/Logging_like_a_pro.md)
- [The 12 Factors Summarized:](12Factor/12Factor_summarized.md)

### Github

- [An autogenerated README](Github/autogenerated_README.md)

### Python

- [Special Method XOR](Python/special_method_xor.md)
- [Stdout in Pytest](Python/stdout_in_pytest.md)

---  

## Usage   
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

