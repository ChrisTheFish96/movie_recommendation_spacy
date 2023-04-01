# A program to determine a movie most similar to one described by the user.
# Importing library..
import spacy

# Function to determine similarity by taking in a user description.
def movie_choice(description):
    # Loading the language model needed
    nlp = spacy.load('en_core_web_md')

    # Reading in the file and creating a list from its contents.
    # Use the list to make a dictionary.
    with open("movies.txt", "r") as movie_file:
        movie_dict = {}
        movie_list = []
        movie_lines = movie_file.readlines()
        for index, i in enumerate(movie_lines):
            movie_list_split = i.split(" :")
            movie_list.append(movie_list_split)
            movie_list[index][1] = movie_list[index][1].strip("\n")
            movie_dict = dict(movie_list)
    
    # Add the user description to a variable.
    # Create a list of movie descriptions.
    sentence_to_compare = description
    description_list = []
    for movie in movie_dict:
        descriptions = movie_dict[movie]
        description_list.append(descriptions)

    # Process the user description and determining the similarity to those of known movies from file.
    # Create a separate list for the keys (descriptions) and the values (similarity scores) and then creating a new dictionary from these.
    model_sentence = nlp(sentence_to_compare)
    sim_keys = []
    sim_vals = []
    for sentence in description_list:
        sim_keys.append(sentence)
        similarity = nlp(sentence).similarity(model_sentence)
        sim_vals.append(similarity)
    sim_dict = dict(zip(sim_keys,sim_vals))

    # Find the max the key for the max similarity value in the new dictionary.
    # Use this found key to find the movie named in the original movie dictionary and print it out.
    for entry in sim_dict:
        max_sim = max(sim_dict, key=sim_dict.get)
    keys = [k for k, v in movie_dict.items() if v == max_sim]
    print(f"The most similar movie to the one you described is {keys}")

# Using the function.
movie_choice('Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator')