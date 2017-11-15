

import re
line="cats are smarter than dogs"
searchobj=re.search('cats',line,re.M|re.I)
print searchobj.group()



import re
line=" are smarter than dogs cats"
searchobj=re.search('cats',line,re.M|re.I)
print searchobj.group()




import re
line="cats are smarter than dogs"
matchobj=re.match('cats',line,re.M|re.I)
print matchobj.group()



import re
line="cats are smarter than dogs"
searchobj=re.search('^cats',line,re.M|re.I)
print searchobj.group()


import re
line=" are smarter than dogs cats"
matchobj=re.match('cats',line,re.M|re.I)
print matchobj.group()


import re
line="cats are smarter than dogs"
searchobj=re.search('cats$',line,re.M|re.I)
print searchobj.group()

