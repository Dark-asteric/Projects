###########################################
######### Importation des modules #########
###########################################
from PyQt5 import QtWidgets,uic # pour l'IHM et importer de Qtdesigner
import sys # pour sortie et argument en ligne de commande

###########################################
########### variables programme ###########
###########################################
# point décimal mis dans un nombre en cours
pdm=False # initialiser à pas de point décimal mis
# liste contenant les nombres et opérations
# exemple lcop=["12.3","+","56.3"]
lcop=[] # initialiser à vide (pas de calcul en cours
#nombre en cours de saisie
nec="" # initialiser à vide

###########################################
########### fonctions programme ###########
###########################################
def cons_aff ():
    # construite la chaîne de caractère représantant le calcul
    global nec # nombre en cours "95.2"
    global lcop # liste de opérations ["12","+"]
    s=""
    for el in lcop: # pour chaque élément de lcop soit "12" et "+"
        s=s+el
    s=s+nec
    return s # "12+95.2"

def uncalcul (n1,n2,op):
    # effectue le calcul n1 op n2
    # n1 et n2 sont des nombres float
    # op est l'opération "+" ou "-" ou "*" ou "/"
    # retourne le nombre ou "div0" en cas de division par 0
    if op=="+":
        return n1+n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    else:
        if n2==0:
            return "Invalid."
        else:
            return n1/n2

###########################################
######### Fonctions associées IHM #########
###########################################
""" fonction clic9 gérant l'appui sur le bouton du 9 """

def clic9():
    global nec
    if len(lcop)%2 == 0:
        nec += "9"
        dlg.affcalec.setPlainText(cons_aff())

def clic8():
    global nec # on va modifier cette variable donc nécessaire
    if len(lcop)%2==0: # on est en train de traiter un nombre
        nec=nec+"8"
        # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
        dlg.affcalec.setPlainText(cons_aff())

def clic7():
    global nec
    if len(lcop)%2==0:
        nec=nec+"7"
        # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
        dlg.affcalec.setPlainText(cons_aff())

def clic6():
    global nec
    if len(lcop)%2==0:
        nec=nec+"6"
        # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
        dlg.affcalec.setPlainText(cons_aff())

def clic5():
    global nec
    if len(lcop)%2==0:
        nec=nec+"5"
        # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
        dlg.affcalec.setPlainText(cons_aff())

def clic4():
    global nec
    if len(lcop)%2==0:
        nec=nec+"4"
        # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
        dlg.affcalec.setPlainText(cons_aff())

def clic3():
    global nec
    if len(lcop)%2==0:
        nec=nec+"3"
        # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
        dlg.affcalec.setPlainText(cons_aff())

def clic2():
    global nec
    if len(lcop)%2==0:
        nec=nec+"2"
        # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
        dlg.affcalec.setPlainText(cons_aff())

def clic1():
    global nec
    if len(lcop)%2==0:
        nec=nec+"1"
        # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
        dlg.affcalec.setPlainText(cons_aff())

def clic0():
    global nec
    if len(lcop)%2==0:
        nec=nec+"0"
        # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
        dlg.affcalec.setPlainText(cons_aff())

def clicpd():
    global pdm
    global nec
    global lcop
    if len(nec) == 0:
        nec="0."
        pdm=True
    elif not pdm:
        nec=nec+"."
        pdm=True
    # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
    dlg.affcalec.setPlainText(cons_aff())  

def clic_op_eg():
    global pdm
    global nec
    global lcop
    print (len(nec),nec[len(nec)-1])
    if len(lcop)>=2 and len(nec)!=0 and nec[len(nec)-1]!=".":
        print ("calc")
        lcop.append (nec)
        # réalisation du calcul
        res=uncalcul(float(lcop[0]),float(lcop[2]),lcop[1])
        if res=="div0":
            dlg.affres.setText("Div. par 0 impossible")
        for i in range(3,len(lcop),2):
            res=uncalcul(res,float(lcop[i+1]),lcop[i])
            if res=="div0":
                dlg.affres.setText("Div. par 0 impossible")
                break
        lcop=[]
        if res=="div0":
            nec=""
            dlg.affcalec.setPlainText("")
        else:
            nec=str(res)
            # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
        
            dlg.affres.setText(str(res))
        pdm=True
        

def clic_op_pl():
    global pdm
    global nec
    global lcop
    if len(nec)==0 or nec[len(nec)-1]==".":
        nec=nec+"0"
    lcop.append (nec)
    lcop.append ("+")
    nec=""
    # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
    dlg.affcalec.setPlainText(cons_aff())    

def clic_op_mo():
    global pdm
    global nec
    global lcop
    if len(nec)==0 or nec[len(nec)-1]==".":
        nec=nec+"0"
    lcop.append (nec)
    lcop.append ("-")
    nec=""
    # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
    dlg.affcalec.setPlainText(cons_aff())    

def clic_op_mu():
    global pdm
    global nec
    global lcop
    if len(nec)==0 or nec[len(nec)-1]==".":
        nec=nec+"0"
    lcop.append (nec)
    lcop.append ("*")
    nec=""
    # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
    dlg.affcalec.setPlainText(cons_aff())    

def clic_op_di():
    global pdm
    global nec
    global lcop
    if len(nec)==0 or nec[len(nec)-1]==".":
        nec=nec+"0"
    lcop.append (nec)
    lcop.append ("/")
    nec=""
    # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
    dlg.affcalec.setPlainText(cons_aff())    

def clic_op_c(): # clear all
    global pdm
    global nec
    global lcop
    pdm=False
    nec=""
    del lcop
    lcop=[]
    # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
    dlg.affcalec.setPlainText(cons_aff())    

def clic_op_ce(): # clear dernier nombre
    global pdm
    global nec
    pdm=False
    nec="0"
    # affichage de la chaîne retournée par cons_aff() dans élément IHM affcalec
    dlg.affcalec.setPlainText(cons_aff())    

def quitter_prog():
    sys.exit(0)

###########################################
########### Initialisation  IHM ###########
###########################################
def init_dlg ():
    global dlg
    # clic sur le bouton chiffre fonction activée : clicx
    dlg.pb9.clicked.connect(clic8)
    dlg.pb8.clicked.connect(clic8)
    dlg.pb7.clicked.connect(clic7)
    dlg.pb6.clicked.connect(clic6)
    dlg.pb5.clicked.connect(clic5)
    dlg.pb4.clicked.connect(clic4)
    dlg.pb3.clicked.connect(clic3)
    dlg.pb2.clicked.connect(clic2)
    dlg.pb1.clicked.connect(clic1)
    dlg.pb0.clicked.connect(clic0)
    dlg.pbpd.clicked.connect(clicpd)

    # clic sur le bouton opération fonction activée : clic_opx
    dlg.pbeg.clicked.connect(clic_op_eg)
    dlg.pbpl.clicked.connect(clic_op_pl)
    dlg.pbmo.clicked.connect(clic_op_mo)
    dlg.pbmu.clicked.connect(clic_op_mu)
    dlg.pbdi.clicked.connect(clic_op_di)
    dlg.pbc.clicked.connect(clic_op_c)
    dlg.pbce.clicked.connect(clic_op_ce)
    
    # un clic sur le bouton appellera la méthode 'action_quitter'
    dlg.pbq.clicked.connect(quitter_prog)

    #zone affichage (affres, et affcalec) n'est pas modifiable au clavier
    dlg.affres.setReadOnly(True)
    


###########################################
########### Programme principal ###########
###########################################
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    # charge l'IHM faite avec Qtdesigner
    dlg=uic.loadUi("calculatrice.ui")
    # initialisation de l'IHM
    init_dlg ()
    
    dlg.show()
    sys.exit(app.exec_())
