import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from kanren import Relation, fact, facts, var, run, conde
import os


## Creamos las relaciones que existirán
Progenitor = Relation()
Hombre = Relation()
Mujer = Relation()
os.remove("familia.txt")
f = open("familia.txt", "a+")

# Reglas

def Abuela(X, Y):
    Z = var()
    return conde((Progenitor(X, Z), Progenitor(Z, Y), Mujer(X)))

def Abuelo(X, Y):
    Z = var()
    return conde((Progenitor(X, Z), Progenitor(Z, Y), Hombre(X)))

def Abuelos(X, Y):
    Z = var()
    return conde((Progenitor(X, Z), Progenitor(Z, Y)))


def Parejas(X, Y):
    Z = var()
    return conde((Progenitor(Y, Z), Progenitor(X, Z)))


def Hija(X, Y):
    res = conde((Progenitor(Y, X), Mujer(X)))
    return res

def Hijo(X, Y):
    res = conde((Progenitor(Y, X), Hombre(X)))
    return res

def Hijos(X, Y):
    res = conde((Progenitor(Y, X), Hombre(X)), (Progenitor(Y, X), Mujer(X)))
    return res


def Madre(X, Y):
    res = conde((Progenitor(X, Y), Mujer(X)))
    return res

def Padre(X, Y):
    res = conde((Progenitor(X, Y), Hombre(X)))
    return res

def Padres(X, Y):
    res = conde((Progenitor(X, Y), Hombre(X)), (Progenitor(X, Y), Mujer(X)))
    return res


def Hermano(X, Y):
    Z = var()
    return conde((Progenitor(Z, X), Progenitor(Z, Y), Hombre(X)))

def Hermana(X, Y):
    Z = var()
    res = conde((Progenitor(Z, X), Progenitor(Z, Y), Mujer(X)))
    return res

def Hermanos(X, Y):
    Z = var()
    res = conde((Progenitor(Z, X), Progenitor(Z, Y)))
    return res


def Primo(X, Y):
    Z = var()
    W = var()
    return conde((Progenitor(Z, X), Progenitor(W, Y), Hermanos(W, Z), Hombre(X)))

def Prima(X, Y):
    Z = var()
    W = var()
    return conde((Progenitor(Z, X), Progenitor(W, Y), Hermanos(W, Z), Mujer(X)))

def Primos(X, Y):
    Z = var()
    W = var()
    return conde((Progenitor(Z, X), Progenitor(W, Y), Hermanos(W, Z)))


def Tio(X, Y):
    Z = var()
    return conde((Progenitor(Z, Y), Hermano(Z, X)))

def Tia(X, Y):
    Z = var()
    return conde((Progenitor(Z, Y), Hermana(Z, X)))

def Tios(X, Y):
    Z = var()
    return conde((Progenitor(Z, Y), Hermanos(Z, X)))


def Sobrino(X, Y):
    Z = var()
    return conde((Progenitor(Z, X), Hermanos(Z, Y), Hombre(X)))

def Sobrina(X, Y):
    Z = var()
    return conde((Progenitor(Z, X), Hermanos(Z, Y), Mujer(X)))

def Sobrinos(X, Y):
    Z = var()
    return conde((Progenitor(Z, X), Hermanos(Z, Y)))


def Cunado(X, Y):
    Z = var()
    W = var()
    V = var()
    return conde((Progenitor(Z, Y), Progenitor(Z, W), Progenitor(W, V), Progenitor(X, V), Hombre(X)))

def Cunada(X, Y):
    Z = var()
    W = var()
    V = var()
    return conde((Progenitor(Z, Y), Progenitor(Z, W), Progenitor(W, V), Progenitor(X, V), Mujer(Y)))

def Cunados(X, Y):
    Z = var()
    W = var()
    V = var()
    return conde((Progenitor(Z, Y), Progenitor(Z, W), Progenitor(W, V), Progenitor(X, V)))


def Nieta(X, Y):
    Z = var()
    return conde((Progenitor(Y, Z), Progenitor(Z, X), Mujer(X)))

def Nieto(X, Y):
    Z = var()
    return conde((Progenitor(Y, Z), Progenitor(Z, X), Hombre(X)))

def Nietos(X, Y):
    Z = var()
    return conde((Progenitor(Y, Z), Progenitor(Z, X)))


def Suegro(X, Y):
    Z = var()
    W = var()
    return conde((Progenitor(Y, Z), Progenitor(W, Z), Progenitor(X, W), Hombre(X)))

def Suegra(X, Y):
    Z = var()
    W = var()
    return conde((Progenitor(Y, Z), Progenitor(W, Z), Progenitor(X, W), Mujer(X)))

def Suegros(X, Y):
    Z = var()
    W = var()
    return conde((Progenitor(Y, Z), Progenitor(W, Z), Progenitor(X, W)))


def Yerno(X, Y):
    Z = var()
    W = var()
    return conde((Progenitor(Y, Z), Mujer(Z), Progenitor(X, W),Progenitor(Z, W), Hombre(X)))

def Nuera(X, Y):
    Z = var()
    W = var()
    return conde((Progenitor(Y, Z), Hombre(Z), Progenitor(X, W),Progenitor(Z, W), Mujer(X)))

def YerNue(X, Y):
    Z = var()
    W = var()
    return conde((Progenitor(Y, Z), Mujer(Z), Progenitor(X, W),Progenitor(Z, W), Hombre(X)),
                 (Progenitor(Y, Z), Hombre(Z), Progenitor(X, W), Progenitor(Z, W), Mujer(X)))

names = []


class ProjectGui(QMainWindow):
    ## Se inicializa la ui y se asocia los eventos a los botones
    def __init__(self):
        super(ProjectGui, self).__init__()
        uic.loadUi('interfaz.ui', self)
        self.btn_agregar.clicked.connect(self.agregar_fact)
        self.btn_agregar_2.clicked.connect(self.agregar_facts)
        self.btn_preguntar.clicked.connect(self.preguntar)

        fact(Hombre, "Armando")
        fact(Hombre, "Javier")
        fact(Hombre, "Diego")
        fact(Mujer, "Nayeli")
        fact(Mujer, "Alina")
        fact(Mujer, "Elsa")
        fact(Mujer, "Brigitte")
        fact(Hombre, "Leo")
        fact(Hombre, "Porfirio")

        facts(Progenitor, ("Javier", "Armando"))
        facts(Progenitor, ("Javier", "Diego"))
        facts(Progenitor, ("Javier", "Nayeli"))
        facts(Progenitor, ("Javier", "Alina"))

        facts(Progenitor, ("Elsa", "Armando"))
        facts(Progenitor, ("Elsa", "Diego"))
        facts(Progenitor, ("Elsa", "Nayeli"))
        facts(Progenitor, ("Elsa", "Alina"))

        facts(Progenitor, ("Armando", "Leo"))
        facts(Progenitor, ("Brigitte", "Leo"))
        facts(Progenitor, ("Diego", "Porfirio"))

        self.cmb_1.addItem("Armando")
        self.cmb_1.addItem("Leo")
        self.cmb_1.addItem("Brigitte")
        self.cmb_1.addItem("Elsa")
        self.cmb_1.addItem("Nayeli")
        self.cmb_1.addItem("Alina")
        self.cmb_1.addItem("Javier")
        self.cmb_1.addItem("Diego")
        self.cmb_1.addItem("Porfirio")

        self.cmb_2.addItem("Armando")
        self.cmb_2.addItem("Leo")
        self.cmb_2.addItem("Brigitte")
        self.cmb_2.addItem("Elsa")
        self.cmb_2.addItem("Nayeli")
        self.cmb_2.addItem("Alina")
        self.cmb_2.addItem("Javier")
        self.cmb_2.addItem("Diego")
        self.cmb_2.addItem("Porfirio")

        self.cmb_pregunta.addItem("Armando")
        self.cmb_pregunta.addItem("Leo")
        self.cmb_pregunta.addItem("Brigitte")
        self.cmb_pregunta.addItem("Elsa")
        self.cmb_pregunta.addItem("Nayeli")
        self.cmb_pregunta.addItem("Alina")
        self.cmb_pregunta.addItem("Javier")
        self.cmb_pregunta.addItem("Diego")
        self.cmb_pregunta.addItem("Porfirio")

    ## Agrega el hecho simple (Si es hombre o mujer)
    def agregar_fact(self):
        name = str(self.txt_name.text())
        sex = ""
        names.append(name)

        self.cmb_1.addItem(name)
        self.cmb_2.addItem(name)
        self.cmb_pregunta.addItem(name)

        if self.rb_hombre.isChecked():
            fact(Hombre, name)
            sex = "Hombre"
        else:
            fact(Mujer, name)
            sex = "Mujer"

        self.txt_name.setText("")
        print(f"{name} es {sex}")

    ## Agrega los hechos de relaciones de progenitor
    def agregar_facts(self):

        name1 = str(self.cmb_1.currentText())
        name2 = str(self.cmb_2.currentText())

        facts(Progenitor, (name1, name2))

        print(f"La relacion creada fue {name1} es progenitor de {name2}")

    ## Realiza la consulta de las relaciones que tiene según un termino brindado
    def preguntar(self):
        miembro = str(self.cmb_pregunta.currentText())
        if self.rb_abue.isChecked():
            X = var()
            res = run(0, X, Abuelos(X, miembro))

        if self.rb_herm.isChecked():
            X = var()
            res = run(0, X, Hermanos(X, miembro))
            res = list(res)
            if miembro in res:
                res.remove(miembro)
            res = tuple(res)

        if self.rb_tios.isChecked():
            X = var()
            p = var()
            res = run(0, X, Tios(X, miembro))
            padres = run(0, p, Progenitor(p, miembro))
            res = list(res)
            for p in padres:
                if p in res:
                    res.remove(p)
            res = tuple(res)

        if self.rb_primos.isChecked():
            X = var()
            res = run(0, X, Primos(X, miembro))
            res = list(res)
            if miembro in res:
                res.remove(miembro)
            res = tuple(res)

        if self.rb_sobrinos.isChecked():
            X = var()
            p = var()
            res = run(0, X, Sobrinos(X, miembro))
            hijos = run(0, p, Hijos(p, miembro))
            res = list(res)
            for p in hijos:
                if p in res:
                    res.remove(p)
            res = tuple(res)

        if self.rb_cunados.isChecked():
            X = var()
            p = var()
            res = run(0, X, Cunados(X, miembro))
            hermanos = run(0, p, Hermanos(p, miembro)) + run(0, p, Parejas(p, miembro))
            res = list(res)
            for p in hermanos:
                if p in res:
                    res.remove(p)
            res = tuple(res)

        if self.rb_nietos.isChecked():
            X = var()
            res = run(0, X, Nietos(X, miembro))
            ##SE HACE EL GRAFO
            p = var()
            padres = list(names)
            for pa in padres:
                parejas = list(run(0, p, Parejas(p, pa)))
                if pa in parejas:
                    parejas.remove(pa)
                if len(parejas) != 0:
                    for par in parejas:
                        if par in padres:
                            f.write("{0} (id={0}, M)\n".format(pa))
                            f.write("{0} (id={0}, M)\n".format(par))
                            pahijos = list(run(0, p, Hijos(p, pa)))
                            parhijos = list(run(0, p, Hijos(p, par)))
                            for h in pahijos:
                                if(h in parhijos):
                                    f.write("\t{0} (id={0}, M)\n".format(h))
                padres.remove(pa)
            f.close()
            myCmd = 'familytreemaker.py familia.txt | dot -Tpng -o familia.png'
            os.system(myCmd)

        ##NUEVOS
        """
        
        if self.rb_parejas.isChecked():
            X = var()
            res = run(0, X, Parejas(X, miembro))
            res = list(res)
            if miembro in res:
                res.remove(miembro)
            res = tuple(res)

        if self.rb_hijos.isChecked():
            X = var()
            res = run(0, X, Hijos(X, miembro))
            res = list(res)
            if miembro in res:
                res.remove(miembro)
            res = tuple(res)
        
        if self.rb_padres.isChecked():
            X = var()
            res = run(0, X, Padres(X, miembro))
            res = list(res)
            if miembro in res:
                res.remove(miembro)
            res = tuple(res)
        
        if self.rb_suegros.isChecked():
            X = var()
            p = var()
            res = run(0, X, Suegros(X, miembro))
            padres = run(0, p, Padres(p, miembro))
            res = list(res)
            for p in padres:
                if p in res:
                    res.remove(p)
            res = tuple(res)
            
        
        if self.rb_yernue.isChecked():
            X = var()
            res = run(0, X, YerNue(X, miembro))
            res = list(res)
            if miembro in res:
                res.remove(miembro)
            res = tuple(res)
            
        """

        view = self.listView
        model = QStandardItemModel()

        for r in res:
            model.appendRow(QStandardItem(r))

        view.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ProjectGui()
    GUI.show()
    sys.exit(app.exec_())
p = var()
padres = list(names)
for pa in padres:
    parejas = list(run(0, p, Parejas(p, pa)))
    if pa in parejas:
        parejas.remove(pa)
    if len(parejas) != 0:
        for par in parejas:
            if par in padres:
                f.write("{0} (id={0}, M)\n".format(pa))
                f.write("{0} (id={0}, M)\n".format(par))
                pahijos = list(run(0, p, Hijos(p, pa)))
                parhijos = list(run(0, p, Hijos(p, par)))
                for h in pahijos:
                    if(h in parhijos):
                        f.write("\t{0} (id={0}, M)\n".format(h))
    padres.remove(pa)
f.close()
myCmd = 'familytreemaker.py familia.txt | dot -Tpng -o familia.png'
os.system(myCmd)