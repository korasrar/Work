def v_contravention(vlimite,vvoiture):
    vdep = vlimite-vvoiture
    if vdep == 20:
        if vlimite > 50:
            amende = 68
            ppoints = 1
            spermis = 0
        else :
            amende = 135
            ppoints = 1
            spermis = 0
    if vdep > 20 and vdep <= 30 :
        amende = 135
        ppoints = 2
        spermis = 0
        
    if vdep > 30 and vdep <= 40:
        amende = 135
        ppoints = 3
        spermis = 3  
    if vdep > 40 and vdep <= 50:
        amende = 135
        ppoints = 4
        spermis = 3      
    if vdep > 50:
        amende = 1500
        ppoints = 6
        spermis = 3      
    return()
            