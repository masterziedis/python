playlist = {
    'title': 'alus',
    'author': 'radzi',
    'songs': [
        { 'title': 'ka daryt', 'artist': ['radzi'], 'duration': 120},
        { 'title': 'ka daryt(remix)', 'artist': ['radzi', 'katunskyte'], 'duration': 100}
    ]
}

total_length = 0

for song in playlist['songs']:
    total_length += song['duration']

print(total_length)
