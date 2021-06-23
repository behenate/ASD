def tank(p,s,bak):
    n = len(s)
    gdzie_jestem = 0 #index
    ile_paliwa = bak-s[0]
    koszt = 0
    sem = 0
    while gdzie_jestem != len(s):
        i = gdzie_jestem + 1
        # sprawdzam, czy jestem w stanie dojechac na stacje tansza bez dotankowywania
        while s[i] - s[gdzie_jestem] < ile_paliwa:
            if p[i] < p[gdzie_jestem]:
                ile_paliwa -= s[gdzie_jestem] - s[i]
                gdzie_jestem = i
                sem = 1
                break
        # jesli nie, to czy moge dotankowac tyle, zeby do niej dojechac?
        i = gdzie_jestem + 1
        if sem == 0:
            while s[i] - s[gdzie_jestem] < bak:
                if p[i] < p[gdzie_jestem]:
                    koszt += (s[i] - s[gdzie_jestem]-ile_paliwa)*p[gdzie_jestem]
                    ile_paliwa=0
                    gdzie_jestem = i
                    break
        #jesli tez nie, to tankuje do pelna i jade na kolejna
        if sem == 0:
            koszt += (bak-ile_paliwa)*p[gdzie_jestem]
            ile_paliwa = bak - (s[gdzie_jestem+1]-s[gdzie_jestem])
            gdzie_jestem += 1