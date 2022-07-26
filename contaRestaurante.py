import string
from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
formHome = uic.loadUi("homeRestaurante.ui")
verificacao= uic.loadUi("verificacaoRestaurante.ui")
pagamentoFinalizado = uic.loadUi("pagamentoFinalizado.ui")

formHome.show()

def valores():
    valorPrato = float(formHome.lineEdit_valorPrato.text())
    valorSobremesa = float(formHome.lineEdit_valorSobremesa.text())
    valorBebida = float(formHome.lineEdit_valorBebida.text())

    verificacao.show()
    formHome.close()

    pagamentoTotal = (valorPrato + valorSobremesa + valorBebida)

    #Acrescentar os valores informados na verificação#
    verificacao.label_pratoTotal.setText(str(valorPrato))
    verificacao.label_sobremesaTotal.setText(str(valorSobremesa))
    verificacao.label_bebidaTotal.setText(str(valorBebida))

    #Acrescentar o valor final do pagamento#
    pagamentoFinalizado.label_pratoTotal.setText(str(valorPrato))
    pagamentoFinalizado.label_sobremesaTotal.setText(str(valorSobremesa))
    pagamentoFinalizado.label_bebidaTotal.setText(str(valorBebida))
    pagamentoFinalizado.label_valorTotal.setText(str(pagamentoTotal))

def voltar():
    verificacao.close()
    formHome.show()


def confirmar():
    pagamentoFinalizado.show()
    verificacao.close()

def inicio():
    formHome.lineEdit_valorPrato.setText(" ")
    formHome.lineEdit_valorSobremesa.setText(" ")
    formHome.lineEdit_valorBebida.setText(" ")

    pagamentoFinalizado.close()
    formHome.show()

def limparHome():
    formHome.lineEdit_valorPrato.setText(" ")
    formHome.lineEdit_valorSobremesa.setText(" ")
    formHome.lineEdit_valorBebida.setText(" ")


formHome.btConfirmar.clicked.connect(valores)
formHome.btLimpar.clicked.connect(limparHome)
verificacao.btConfirmar.clicked.connect(confirmar)
verificacao.btVoltar.clicked.connect(voltar)
pagamentoFinalizado.btFechar.clicked.connect(inicio)

app.exec()