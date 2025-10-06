#Renaming

#change the name of the points columns to score

data.rename(columns={'points': 'score'})

#also ken change by row too

data.rename(index={0:"first_entry",1:"secondEntry"})

#row itself can have its own name and coloumns have its own name

data.rename_axis("wines",axis="rows").rename_axis("fields",axis="columns")



#Combining

canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')
