import recommendations

dataset = recommendations.critics

# Print the similarity score between Lisa and Gene
sim_distance_01 = recommendations.sim_distance(dataset, 
                                    'Lisa Rose', 'Gene Seymour')
print("The sim_distance of Lisa and Gene: %f" % sim_distance_01, '\n')

# Print the similarity score between Lisa and Gene
sim_pearson_01 = recommendations.sim_pearson(dataset,
                                    'Lisa Rose', 'Gene Seymour')
print("The sim_pearson of Lisa and Gene: %f" % sim_pearson_01, '\n')

# Print the top matches of Toby in the dataset
top_matches = recommendations.topMatches(dataset, 'Toby' , n=3)
print("The top matches of Toby in the dataset: \n", top_matches, '\n')

# Print the recommendations of Toby caculated by sim_pearson
recom_pearson = recommendations.getRecommendations(dataset,'Toby')
print("The recommendations of Toby caculated by sim_pearson: \n", recom_pearson, '\n')

# Print the recommendations of Toby caculated by sim_distance
recom_distance = recommendations.getRecommendations(dataset,'Toby',
                                    similarity=recommendations.sim_distance)
print("The recommendations of Toby caculated by sim_distance: \n", recom_distance, '\n')

prefs = recommendations.loadMovieLens()
# Print recommendations of id87
recom_id87 = recommendations.getRecommendations(prefs, '87')[0:30]
print("The recommendations of movies: \n", recom_id87, '\n')

# Print itemsim
itemsim=recommendations.calculateSimilarItems(prefs,n=50)
recom_itemsim = recommendations.getRecommendedItems(prefs,itemsim,'87')[0:30]
print("itemsim: ", recom_itemsim)



