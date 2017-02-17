import tmdbsimple as tmdb

tmdb.API_KEY = ('')

l = tmdb.Search()
m = l.movie(query='Ace Ventura')
for x in l.results:
    print (x['title'])
