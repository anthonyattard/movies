import fresh_tomatoes
import media

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                   "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIaco")

waking_life = media.Movie("Waking Life",
                          "A man shuffles through a dream meeting various people and discussing the meanings and purposes of the universe.",
                          "https://upload.wikimedia.org/wikipedia/en/9/98/Waking-Life-Poster.jpg",
                          "https://www.youtube.com/watch?v=uk2DeTet98o")

before_sunrise = media.Movie("Before Sunrise",
                          "A young man and woman meet on a train in Europe, and wind up spending one evening together in Vienna. Unfortunately, both know that this will probably be their only night together.",
                          "https://upload.wikimedia.org/wikipedia/en/d/da/Before_Sunrise_poster.jpg",
                          "https://www.youtube.com/watch?v=9v6X-Dytlko")

the_big_short = media.Movie("The Big Short",
                          "Four denizens in the world of high-finance predict the credit and housing bubble collapse of the mid-2000s, and decide to take on the big banks for their greed and lack of foresight.",
                          "https://upload.wikimedia.org/wikipedia/en/e/e3/The_Big_Short_teaser_poster.jpg",
                          "https://www.youtube.com/watch?v=vgqG3ITMv1Q")

the_conjuring = media.Movie("The Conjuring",
                          "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse.",
                          "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg",
                          "https://www.youtube.com/watch?v=DtC1hTw7Rto")

movies = [fight_club, shawshank_redemption, waking_life, before_sunrise, the_big_short, the_conjuring]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
