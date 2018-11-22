import re



def Create_hashtags(string):



    pattern=r'[(a-zA-Z)]+'
    find_result=re.findall(pattern,string)
    hash_str= ' '.join(['#{0}'.format(s) for s in find_result])
    hash_str.lower()
    return hash_str.lower()