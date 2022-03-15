var n1 = prompt('Informe um número: ')
var n2 = prompt('Informe outro número: ')
var n3 = prompt('Informe mais um número: ')

n1 = parseInt(n1)
n2 = parseInt(n2)
n3 = parseInt(n3)

if ((n1 < n2) && (n1 < n3)) {
    document.write('A soma dos 2 maiores valores é: ' + (n2 + n3))
}else if (n2 < n3) {
    document.write('A soma dos 2 maiores valores é: ' + (n1 + n3))
}else {
    document.write('A soma dos 2 maiores valores é: ' + (n1 + n2))
}