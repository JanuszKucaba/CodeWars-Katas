'''
Write a function that when given a URL as a string, parses out
just the domain name and returns it as a string.
For example:
domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
https://www.codewars.com/kata/514a024011ea4fb54200004b
'''

# 1 solution
def domain_name(url):
    '''Give URL as a string and returns domain name as a string'''
    return url.split("www.")[-1].split("//")[-1].split(".")[0]

# 2 solution
def domain_name2(url):
    '''Give URL as a string and returns domain name as a string'''
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')

    return url[0:url.find('.')]


if __name__ == '__main__':
    print(domain_name("http://github.com/carbonfive/raygun"))
    print(domain_name2("http://github.com/carbonfive/raygun"))

    print(domain_name("http://www.zombie-bites.com"))
    print(domain_name2("http://www.zombie-bites.com"))

    print(domain_name("https://www.cnet.com"))
    print(domain_name2("https://www.cnet.com"))
