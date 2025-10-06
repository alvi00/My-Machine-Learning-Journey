#so there are functions they are map and apply
#that take value, do something to that,then return
#map works on one coloum
#apply can work on multiple coloum

#map
review_points_mean = reviews.points.mean()


def subtract_mean(p):
    return p - review_points_mean

reviews.points.map(subtract_mean)


#apply

def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')
