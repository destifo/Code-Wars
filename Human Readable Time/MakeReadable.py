def make_readable(seconds):
    return f'{0 if seconds//3600 < 10 else ""}{seconds//3600}:{0 if (seconds//60)%60 < 10 else ""}{(seconds//60)%60}:{0 if seconds%60 < 10 else ""}{seconds%60}'