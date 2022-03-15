function nome_funcao() {
    alert('Login ou senha incorreto')
}

function somar(a, b){
    var total = a + b
    alert('O valor da soma de 8 + 3 é ' + total)
}

function desconto(a, b){
    var totalDesc = a - b;
    document.write('O valor com desconto: ' + totalDesc + '<br>')
    return totalDesc
}

var resultTotalDesc = desconto(7,5)
document.write('Valor final com desconto é: ' + resultTotalDesc)

document.write(n1.toLocaleString(`pt-br`,{style:`currency`, currency: `BRL`} ))