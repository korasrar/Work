def v_contravention(vlimite,vvoiture):
    vdep = vvoiture-vlimite
    res =(0,0,0)
    if vdep <= 20 and vdep > 0:
        if vlimite > 50:
            res =(68,1,0)
        else :
            res =(135,1,0)
    if vdep > 20 and vdep <= 30 :
        res =(135,2,0)  
    if vdep > 30 and vdep <= 40:
        res =(135,3,3)
    if vdep > 40 and vdep <= 50:
        res =(135,4,3)     
    if vdep > 50:
        res =(1500,6,3)    
    return res

def test_v_contravention():
    assert v_contravention(50,70) == 3
    assert v_contravention(50,70) == 1
    assert v_contravention(50,70) ==1
    assert v_contravention(50,70) ==1

            