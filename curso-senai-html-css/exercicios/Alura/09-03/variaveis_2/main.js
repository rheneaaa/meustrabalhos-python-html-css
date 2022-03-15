var para = document.querySelector('p')
para.addEventListener('click', atualizaNome)

function atualizaNome() {
    var nome = prompt('Insira um novo nome')
    para.textContent = 'aluno: ' + nome
}