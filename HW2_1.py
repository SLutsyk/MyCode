python_zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

search = {
    "better": python_zen.count("better"),
    "never": python_zen.count("never"),
    "is": python_zen.count("is"),
}

#print(
    #"",
    #'Count of  "better" is ' + str(search["better"]),
    #'Count of  "never" is ' + str(search["never"]),
    #'Count of  "is" is ' + str(search["is"]),
    #"",
    #sep="\n",
#)

print(python_zen.upper())

python_zen_redacted = python_zen.replace("i", "&")
#print(python_zen_redacted)