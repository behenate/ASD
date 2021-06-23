def tank(s,p,bak):
    n = len(s)
    gdzie_jestem = 0 #index
    ile_paliwa = bak-s[0]
    koszt = 0
    while gdzie_jestem != n-1:
        if s[gdzie_jestem]+ile_paliwa >= s[n-1]:
            break
        sem = 0
        i = gdzie_jestem + 1
        # sprawdzam, czy jestem w stanie dojechac na stacje tansza bez dotankowywania
        while i < n and s[i] - s[gdzie_jestem] < ile_paliwa:
            if p[i] < p[gdzie_jestem]:
                ile_paliwa -= s[gdzie_jestem] - s[i]
                gdzie_jestem = i
                sem = 1
                break
            i += 1
        # jesli nie, to czy moge dotankowac tyle, zeby do niej dojechac?
        i = gdzie_jestem + 1
        if sem == 0:
            while i < n and s[i] - s[gdzie_jestem] < bak:
                if p[i] < p[gdzie_jestem]:
                    koszt += (s[i] - s[gdzie_jestem]-ile_paliwa)*p[gdzie_jestem]
                    ile_paliwa=0
                    gdzie_jestem = i
                    sem = 1
                    break
                i += 1
        #jesli tez nie, to tankuje do pelna i jade na kolejna
        if sem == 0:
            if s[n-1]-s[gdzie_jestem] < bak:
                koszt += (s[n-1]-s[gdzie_jestem]-ile_paliwa)*p[gdzie_jestem]
                return koszt
            else:
                koszt += (bak-ile_paliwa)*p[gdzie_jestem]
                ile_paliwa = bak - (s[gdzie_jestem+1]-s[gdzie_jestem])
                gdzie_jestem += 1
    return koszt


