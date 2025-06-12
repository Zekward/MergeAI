MERGE AI (DJ Compatibility APP)
MVP Build Log



6/11/25

Goal: Build MVP that queries a song and prints out its audio features using Spotify API

Accomplishments:
- Researched and understood Spotify's Web API authentication model (client credentials flow)
- Authenticated using access tokens
- Requests to Spotify's /v1/search endpoint to retrieve track metadata
- Built and tested API interactions
- Prased JSON responses to comfirm end-to-end query flow works

Challenges:
- Troubleshot Spotify invalid_client error (resolved with correct base64 encoding and included missing syntax for f string)

Todo:
- Given song name, extract Spotify track ID
- use ID to query and fetch
    - tempo
    - energy
    - danceability
- input two songs, compare features
- create simple scoring function (id. Euclidean distance)
- print "compatibility score"