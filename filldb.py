from app.models import *
df = pd.read_excel(r"C:\Users\User\Documents\repos\fred-jehle-spanish-verbs\12000verbs\master_verbs_10.7.20.xlsx")[['verbo', 'trad_en', 'form']].fillna('')
for i in df.index:
    verb, def_, form = df.loc[i]
    u = Nocab( words_es = verb, form = form, def_es = def_)
    db.session.add(u)
    
db.session.commit()
    

