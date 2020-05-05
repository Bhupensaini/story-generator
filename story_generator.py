import itertools
import sys

first = ['sultry', 'kinky', 'lusty', 'Curvy', 'Streamy', 'crazy',
         'Crazy', 'fleashy']

second = ['cute', 'blonde', 'wild', 'Bold', 'ancient', 'brunette', 'innocent']         

third = ['zombies', 'mummies', 'ghosts', 'Demons', 'Ghargoyles', 'Angles',
         'Reapers', 'Sirens']

titles = []

#generating combinations and add to the titles array         
def gen_titles():
    print('generating titles..........')
    
    for title in itertools.product(first, second, third):
        titles.append(titles)

#show the title list
def show_titles():
    print('Listening ' + str(len(titles)) + ' titles')
    
    for t in titles():
        print(' '.join(t))
        
#run the combination
gen_titles()

#show the lists
show_titles()        