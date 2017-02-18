
import tmdbsimple as tmdb
import random

file = open('key.txt', 'r')
key = file.read()
tmdb.API_KEY = (key)
file.close()

#searches for Tv show on TMDb
def search():
    l = tmdb.Search()
    while True:
        title = str(input('Show Name: '))
        m = l.tv(query=title)
        try:
            seasonInfo(l.results[0]['id'], l.results[0]['original_name'])
            break
        except IndexError as e:
            print('Title not found')
'''
    for x in l.results:
        try:
            print (x['original_name'])
        except Exception as error:
            print (error)
'''

#Collects dictionary with each season and the number of episodes in each
def seasonInfo(id, title):
    dic = {}
    s = 1;
    while True:
        try:
            season = tmdb.TV_Seasons(id, s).info()
            eps = len(season['episodes'])
            dic['Season {}'.format(s)] = eps
            s += 1
        except Exception as e:
            #print (e)
            break
    randomEp(id, dic, title)

#Gives a random episode
def randomEp(id, dic, title):
    season = random.randint(1, len(dic))
    #breaks if there's an empty season
    ep = random.randint(1, dic['Season {}'.format(season)])
    episodes = tmdb.TV_Seasons(id, season).info()['episodes']
    print ('{}: Season {}, Episode {}, {}'.format(title, season, ep+1, episodes[ep-1]['name']))
    print (episodes[ep-1]['overview'])
'''
    for x in episodes:
        print (x['name'])
'''

search()
