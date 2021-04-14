import re

"""
Program: Regex Practice
Author: rickyg3
Date: 04/13/21
"""


if __name__ == "__main__":
    # sample_text = "Use of python in Machine Learning"
    # sample_regex = re.search(r'^Use.*Learning$', sample_text)
    # if sample_regex:
    #     print("Match Found!")
    # else:
    #     print("No Match")
    '''
    .---------------.    
    | Regex methods |
    '---------------'
    ------------------------------------------------------------------
       1. findall: returns list of all matches
       2. search: returns Match obj if found
       3. split: returns list where string has been split by each match 
       4. sub: replaces one or many matches with a string
    ------------------------------------------------------------------
    
    '''
    '''
    .----------------.
    | Metacharacters |
    '----------------'
    ------------------------------------------------------------------
    []: [a-m], set of chars
     .: any character except newline character
     ^: starts with
     $: ends with
     *: 0 or more occurrences
     +: 1 or more occurrences
    {}: a{2} -> aa, exactly that many occurrences
     |: long|short, either or
    (): group
    ------------------------------------------------------------------
    '''
    '''
    .-------------------.
    | Special Sequences |
    '-------------------'
    ------------------------------------------------------------------
    \\A: returns match if at beginning of a string
    \\b: returns match if at start or end of word
    \\B: returns match if present but not at the start or the end
    \\d: returns a match if the string contains digits
    \\D: returns a match if the string does not contain digits
    \\s: returns a match if string contains a whitespace char
    \\S: returns a match if string does not contain a whitespace char
    \\w: returns a match if string contains any word char (a-z, digits, and underscore '_')
    \\W: returns a match if string does not contain any word char (a-z, digits, and underscore '_')
    \\Z: returns a match if specified characters are at the end
    ------------------------------------------------------------------
    '''
    '''
    .------.
    | Sets |
    '------'
    ------------------------------------------------------------------
    [abc]: returns match if specified characters are present
    [a-r]: returns match if any lowercase letter between a-r is present
    [^abc]: returns match for any character except those specified
    [0123]: returns match if any of the specified digits are present 
    [0-9]: returns match if any digit between 0-9 is present 
    
    [0-3] 
    [0-3]: returns match for any two-digit numbers between 00 and 38
     
    [a-zA-Z]: returns match for any alph char between a-z and A-Z
    [+]: return match for any + char in string
    ------------------------------------------------------------------
    '''

    practice_text = '''
1-(833)-423-3245
my_num: (833) 468-5293, my@gmail.com
batman: (157) 456 6125, batman@wayne_industries.com
jer bear: 173 835 7214, jerry@parksandrec.gov
ash: 133 486-5796, gotta_catch_em123@poke_league.net
colonel sanders: 1314753697, 23flavors@kfc.com
    '''

    # Regex Patterns
    basic_phone_reg = r'([0-9]|{3})'
    phone_reg = r'[0-9]*[- ]*[(]*[0-9]{3}[)]*[- ]*[0-9]{3}[- ]*[0-9]{4}'
    email_reg = r''

    find_numbers = re.findall(phone_reg, practice_text)

    print(find_numbers)

    replace_numbers = re.sub(phone_reg, "[private_number]", practice_text)

    print(replace_numbers)

    template = '''
    
Dear [recipient_name],

My name is [user_name], and I am in your 
[class_name] class, Section [section_name], at [meeting_time] on [meeting_day].

Thank you for your help!

Best,
[user_name]   
    '''

    recipient_name = "Professor Xavier"
    user_name = "Clark Kent"
    class_name = "Math 120"
    section_name = "1E"
    meeting_time = "10:00 am"
    meeting_day = "Tuesday"

    template_map = {
        r'\[recipient_name\]': recipient_name,
        r'\[user_name\]': user_name,
        r'\[class_name\]': class_name,
        r'\[section_name\]': section_name,
        r'\[meeting_time\]': meeting_time,
        r'\[meeting_day\]': meeting_day,
    }

    print(template)
    print("\n")
    new_product = template
    for regex_pattern, variable in template_map.items():
        new_product = re.sub(regex_pattern, variable, new_product)

    print(new_product)