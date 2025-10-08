import json
f = open("/mnt/d/imdb/imdb_movies.json", mode='r')
movies_data = json.load(f)
f.close()
print(movies_data)
print(type(movies_data))


director_movie_count={}
for j in movies_data:
    if j['director'] not in director_movie_count:
        director_movie_count[j['director']]=1
    else:
        director_movie_count[j['director']]+=1

# print(director_movie_count)
top_director=max(director_movie_count.items(), key=lambda x:x[1])[1]
# print(top_director)
for rec_one in director_movie_count:
    if director_movie_count[rec_one]==top_director:
        print(rec_one)

#2.
gener_data_count={}
for j in movies_data:
    for m in j['genre']:
        print(m)
        if m.strip() not in gener_data_count:
            gener_data_count[m.strip()]=1
        else:
            gener_data_count[m.strip()]+=1

most_gener=max(gener_data_count.items(),key=lambda x:x[1])
print(most_gener)


# 3.
empty_dic={}
for k in movies_data:
    if 'name' not in empty_dic:
        empty_dic[k["name"]]= k["imdb_score"]

# print(empty_dic)
top_movies=sorted(empty_dic.items(), key=lambda x:x[1],reverse=True)
top_10_movies=top_movies[0:11]
# print(top_movies)
print(top_10_movies)


# 4.
top_movies=sorted(empty_dic.items(), key=lambda x:x[1])
print(top_movies[0])


# 5.
end_dict={}
for i in movies_data:
    if 'director' not in end_dict:
        end_dict[i['director']]=i['99popularity']