var porcenDtb = 0.28
var imposto = 0.45
 

var custoFab = prompt('Insira o custo de fabricação do automóvel: ');
custoFab = parseInt(custoFab)
porcenDtb *= custoFab
imposto *= custoFab 
var custoFinal = custoFab + imposto + porcenDtb
custoFinal = parseInt(custoFinal)
document.write('O custo final de um automóvel, com custo de fabricação de R$' + custoFab + ' é R$ ' + custoFinal)