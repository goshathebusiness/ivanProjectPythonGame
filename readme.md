ненавижу блять жирного

    for i in moveObj1:
        i.y-=frame*1000
        if i.y<=-900:
            background1.image=backgroundImages[random.randint(0,len(backgroundImages)-1)]
            i.y=1800
            
    for i in moveObj2:
        i.y-=frame*1000
        if i.y<=-900:
            background2.image=backgroundImages[random.randint(0,len(backgroundImages)-1)]
            i.y=1800

    for i in moveObj3:
        i.y-=frame*1000
        if i.y<=-900:
            background3.image=backgroundImages[random.randint(0,len(backgroundImages)-1)]
            i.y=1800
    

        for i in decor:
        i.y-=frame*1000
        if i.y<=-900:
            i.y=1500
            decorRandomizer(i)

            