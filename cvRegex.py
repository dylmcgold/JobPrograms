import re
import subprocess 


coverLetter = """Dear xvar, 

I am interested in xvar's yvar position."""


x = "Company Here"
y = "Job Title Here"

if (x[len(x) - 1]) == "s":

    temp = re.sub("xvar\'s", x + "\'", coverLetter)
    temp = re.sub("xvar", x, temp)
    temp = re.sub("yvar", y, temp)
    subprocess.run("pbcopy", text=True, input=temp)
else:
    temp = re.sub("xvar", x, coverLetter)
    temp = re.sub("yvar", y, temp)
    subprocess.run("pbcopy", text=True, input=temp)