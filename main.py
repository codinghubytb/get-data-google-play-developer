from google_play_scraper import app

# App Id
result = app('com.example.app')

print(f"{result['installs']}")


