
def detailed_movies(db):
    '''return the list of movies with their genres and director name'''

    query = '''
    SELECT movies.title , movies.genres , directors.name
    FROM movies
    JOIN directors ON movies.director_id = directors.id
    '''
    db.execute(query)
    results = db.fetchall()

    # results in a list (rows) of tuples (columns)
    # print(results)  # Inspect what you get back! Don't guess!
    # Then you'll need to return something.

    list_movies = [results[i][0:3] for i in range(len(results))]

    return list_movies


def late_released_movies(db):
    '''return the list of all movies released after their director death'''

    query = '''
    SELECT movies.title , movies.genres , directors.name
    FROM movies
    JOIN directors ON movies.director_id = directors.id
    WHERE movies.start_year > directors.death_year
    '''
    db.execute(query)
    results = db.fetchall()

    # results in a list (rows) of tuples (columns)
    # print(results)  # Inspect what you get back! Don't guess!
    # Then you'll need to return something.

    list_movies = [results[i][0] for i in range(len(results))]

    return list_movies

def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''

    query = '''
    SELECT COUNT(movies.id) AS number_of_movies, movies.genres , AVG(movies.minutes) AS avg_length
    FROM movies
    WHERE movies.genres = ?
    '''

    db.execute(query, (f'{genre_name}', ))

    result = db.fetchone()

    dict_movies = {'genre': result[1],
              'number_of_movies': result[0],
              'avg_length': round(result[2],2) }

    return dict_movies


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''

    query = '''
    SELECT directors.name, COUNT(movies.id) AS nmb_movies
    FROM movies
    JOIN directors ON movies.director_id = directors.id
    WHERE movies.genres = ?
    GROUP BY directors.name
    ORDER BY nmb_movies DESC, directors.name ASC
    LIMIT 5 '''

    db.execute(query, (f'{genre_name}', ))

    results = db.fetchall()

    list_movies = results

    return list_movies


def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    query = '''
 SELECT
 CASE WHEN movies.minutes >= 0 AND movies.minutes < 30 THEN 30
 	  WHEN movies.minutes >= 30 AND movies.minutes < 60 THEN 60
 	  WHEN movies.minutes >= 60 AND movies.minutes < 90 THEN 90
 	  WHEN movies.minutes >= 90 AND movies.minutes < 120 THEN 120
 	  WHEN movies.minutes >= 120 AND movies.minutes < 150 THEN 150
 	  WHEN movies.minutes >= 150 AND movies.minutes < 180 THEN 180
 	  WHEN movies.minutes >= 180 AND movies.minutes < 210 THEN 210
 	  WHEN movies.minutes >= 210 AND movies.minutes < 240 THEN 240
 	  WHEN movies.minutes >= 240 AND movies.minutes < 270 THEN 270
 	  WHEN movies.minutes >= 270 AND movies.minutes < 300 THEN 300
 	  WHEN movies.minutes >= 300 AND movies.minutes < 330 THEN 330
 	  WHEN movies.minutes >= 330 AND movies.minutes < 360 THEN 360
 	  WHEN movies.minutes >= 360 AND movies.minutes < 390 THEN 390
 	  WHEN movies.minutes >= 390 AND movies.minutes < 420 THEN 420
 	  WHEN movies.minutes >= 420 AND movies.minutes < 450 THEN 450
 	  WHEN movies.minutes >= 450 AND movies.minutes < 480 THEN 480
 	  WHEN movies.minutes >= 510 AND movies.minutes < 540 THEN 540
 	  WHEN movies.minutes >= 540 AND movies.minutes < 570 THEN 570
 	  WHEN movies.minutes >= 570 AND movies.minutes < 600 THEN 600
 	  WHEN movies.minutes >= 600 AND movies.minutes < 630 THEN 630
      WHEN movies.minutes >= 660 AND movies.minutes < 690 THEN 690
      WHEN movies.minutes >= 870 AND movies.minutes < 900 THEN 900
      WHEN movies.minutes >= 990 AND movies.minutes < 1020 THEN 1020
      WHEN movies.minutes >= 1020 AND movies.minutes < 1050 THEN 1050
 END AS max_duration,
 COUNT(movies.id) AS movie_count
 FROM movies
 WHERE max_duration IS NOT NULL
 GROUP BY max_duration
 ORDER BY max_duration ASC '''

    db.execute(query)

    results = db.fetchall()

    list_movies = results

    return list_movies


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''

    query = '''
    SELECT directors.name, (movies.start_year - directors.birth_year) AS age_when_first_time_director
    FROM movies
    JOIN directors ON movies.director_id = directors.id
    WHERE directors.birth_year IS NOT NULL
    GROUP BY age_when_first_time_director, directors.name
    LIMIT 5 '''

    db.execute(query)

    results = db.fetchall()

    list_movies = results

    return list_movies
