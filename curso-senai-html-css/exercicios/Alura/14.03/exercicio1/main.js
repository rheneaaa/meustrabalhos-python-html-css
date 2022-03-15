var n1 = 0
var n2 = 0
var n3 = 0
var media = (n1 + n2 + n3)/3

if (media > 6) {
    document.write('Aprovado! ')
}else if ((media <= 6 ) && (media >= 5)) {
    document.write('Recuperação! ')
}else {
    document.write('Reprovado!')
}