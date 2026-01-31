from datetime import datetime

def time_ago(dt):
    now = datetime.utcnow()
    diff = now - dt

    seconds = diff.total_seconds()
    minutes = seconds // 60
    hours = minutes // 60
    days = diff.days

    if seconds < 60:
        return "just now"
    elif minutes < 60:
        return f"{int(minutes)} minute{'s' if minutes != 1 else ''} ago"
    elif hours < 24:
        return f"{int(hours)} hour{'s' if hours != 1 else ''} ago"
    elif days < 7:
        return f"{int(days)} day{'s' if days != 1 else ''} ago"
    elif days < 30:
        weeks = days // 7
        return f"{int(weeks)} week{'s' if weeks != 1 else ''} ago"
    else:
        return dt.strftime("%B %d, %Y")
