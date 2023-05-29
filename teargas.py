import spotify
import imdb
import quiz
import chucknorrisjokes
import steam

class Teargas:

    def __init__(self):
        self.spotify_client = spotify.SpotifyClient()
        self.imdb_client = imdb.IMDbClient()
        self.pyquiz_client = pyquiz.PyQuizClient()
        self.chucknorrisjokes_client = chucknorrisjokes.ChuckNorrisJokesClient()
        self.steam_client = steam.SteamClient()

    def recommend_music(self):
        # Get the user's input
        user_input = input("What kind of music do you like? ")

        # Get the user's preferences
        genres = input("What genres do you like? ").split(",")
        artists = input("What artists do you like? ").split(",")
        moods = input("What moods do you like? ").split(",")

        # Make a request to the Spotify API
        recommendations = self.spotify_client.recommend_music(genres, artists, moods)

        # Print the recommendations
        for recommendation in recommendations:
            print(recommendation)

    def recommend_movies(self):
        # Get the user's input
        user_input = input("What kind of movies do you like? ")

        # Get the user's preferences
        genres = input("What genres do you like? ").split(",")
        actors = input("What actors do you like? ").split(",")
        directors = input("What directors do you like? ").split(",")

        # Make a request to the IMDb API
        recommendations = self.imdb_client.recommend_movies(genres, actors, directors)

        # Print the recommendations
        for recommendation in recommendations:
            print(recommendation)

    def take_personality_quiz(self):
        # Get the user's input
        user_input = input("What is your name? ")

        # Make a request to the PyQuiz API
        results = self.pyquiz_client.take_personality_quiz(user_input)

        # Print the results
        for result in results:
            print(result)

    def tell_fun_fact(self):
        # Make a request to the Chuck Norris Jokes API
        fact = self.chucknorrisjokes_client.tell_fun_fact()

        # Print the fact
        print(fact)

    def recommend_games(self):
        # Get the user's input
        user_input = input("What kind of games do you like? ")

        # Get the user's preferences
        genres = input("What genres do you like? ").split(",")
        developers = input("What developers do you like? ").split(",")
        platforms = input("What platforms do you like? ").split(",")

        # Make a request to the Steam API
        recommendations = self.steam_client.recommend_games(genres, developers, platforms)

        # Print the recommendations
        for recommendation in recommendations:
            print(recommendation)

    def say_something_else(self):
        print("I'm not sure what you mean. Can you please rephrase your question?")

    def close(self):
        print("Thank you for using Teargas. Have a nice day!")

# Initialize the chatbot
chatbot = Teargas()

# Get the user's input
user_input = input("What can I help you with? ")

# Process the user's input
if user_input == "music":
    # Recommend music
    chatbot.recommend_music()
elif user_input == "movies":
    # Recommend movies
    chatbot.recommend_movies()
elif user_input == "personality quiz":
    # Take a personality quiz
    chatbot.take_personality_quiz()
elif user_input == "fun facts":
    # Tell a fun fact
    chatbot.tell_fun_fact()
elif user_input == "game recommendations":
    # Recommend games
    chatbot.recommend_games()
else:
    # Say something else
    chatbot.say_something_else()

# Close the chatbot
chatbot.close()
