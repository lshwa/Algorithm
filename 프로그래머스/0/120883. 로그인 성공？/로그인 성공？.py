def solution(id_pw, db):
    for uid, pwd in db:
        if uid == id_pw[0]:           
            if pwd == id_pw[1]:  
                return "login"
            else:                    
                return "wrong pw"
    return "fail" 