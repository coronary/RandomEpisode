
import tmdbsimple as tmdb
import random

file = open('key.txt', 'r')
key = file.read()
tmdb.API_KEY = (key)
file.close()

#searches for Tv show on TMDb
def search():
    l = tmdb.Search()
    title = str(input('Show Name: '))
    m = l.tv(query=title)
    seasonInfo(l.results[0]['id'])
'''
    for x in l.results:
        try:
            print (x['original_name'])
        except Exception as error:
            print (error)
'''

#Collects dictionary with each season and the number of episodes in each
def seasonInfo(id):
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
    randomEp(id, dic)

def randomEp(id, dic):
    season = random.randint(1, len(dic))
    ep = random.randint(1, dic['Season {}'.format(season)])
    episodes = tmdb.TV_Seasons(id, season).info()['episodes']
    print ('Season {}, Episode {}, {}'.format(season, ep+1, episodes[ep]['name']))
    print (episodes[ep]['overview'])
'''
    for x in episodes:
        print (x['name'])
'''

search()
