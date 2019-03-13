#!/usr/bin/env python
import psycopg2
#first top 3 articles execution
def MPArticles():
    conn=psycopg2.connect(dbname="news",user='vagrant',password='vagrant')
    cur=conn.cursor()
    q1= ''' SELECT title, views FROM log_anals_articles INNER JOIN articles ON
    articles.slug = log_anals_articles.slug ORDER BY views desc LIMIT 3; '''
    cur.execute(q1)
    rs=cur.fetchall()
    print(" \n  *What are the most popular three articles of all time ? \n")
    count=1
    for result in rs:
        num='(' + str(count) + ') "'
        tit= result[0]
        views = '"' + str(result[1]) + " views"
        print(num + tit + views)
        count=count+1
        #print('  "{0}"===>{1} views'.format(result[0], result[1]))
#top 4 authors
def MPAuthors():
    
    conn=psycopg2.connect(dbname="news",user='vagrant',password='vagrant')
    cur=conn.cursor()
    q2= '''
    SELECT log_auth_name.name AS author,
    sum(log_anals_articles.views) AS views FROM log_anals_articles INNER JOIN log_auth_name
    ON log_auth_name.slug=log_anals_articles.slug
    GROUP BY log_auth_name.name ORDER BY views desc limit 4;
    '''
    cur.execute(q2)
    rs=cur.fetchall()
    print("\n  **Who are the most popular article authors of all time ? \n")
    count=1
    for result in rs:
        num='(' + str(count) + ') "'
        tit= result[0]
        views = '"Authors' + str(result[1]) + " views"
        print(num + tit + views)
        count=count+1
        #print('  "{0}"====>{1} views'.format(result[0], result[1]))
#lead errors
def LEAnalysis():
    conn=psycopg2.connect(dbname="news",user='vagrant',password='vagrant')
    cur=conn.cursor()
    q3= '''
    SELECT log_err_fail.date ,(log_err_fail.count*100.00 / log_anals_total.count) AS
    percentage FROM log_err_fail INNER JOIN log_anals_total
    ON log_err_fail.date = log_anals_total.date
    AND (log_err_fail.count*100.00 / log_anals_total.count) >1
    ORDER BY (log_err_fail.count*100.00 /log_anals_total.count) desc;
    '''
    cur.execute(q3)
    rs=cur.fetchall()
    print(" \n  ***Days on which more than 1% of requests lead to errors ? ")
    for result in rs:
        print('\n  On ' + str(result[0]) +'   ===>   ' + '%.1f' % result[1] +'% errors\n')
MPArticles()
MPAuthors()
LEAnalysis()


