import datetime
def getMaxTimePassed(date):

    dif=datetime.datetime.utcnow()-date

    years=round(dif.days/365)
    months=round(dif.days/30)
    weeks=round(dif.days/7)
    hours=round(dif.seconds/3600)
    minutes=round(dif.seconds/60)

    if years > 0:
        return ("%i years ago"%(round(dif.days/365)))
    elif months > 0:
        return("%i months ago"%(round(dif.days/30)))
    elif weeks > 0:
        return("%i week ago"%(round(dif.days/7)))
    elif dif.days > 0:
        return("%i days ago"%(dif.days))
    elif hours > 0:
        return("%i hours ago"%(round(dif.seconds/3600)))
    elif minutes > 0:
        return("%i minutes ago"%(round(dif.seconds/60)))
    elif dif.seconds > 0:
        return("%i seconds ago"%(dif.seconds))
