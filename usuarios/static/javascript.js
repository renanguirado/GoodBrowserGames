if(doc.querySelector('.btnCadastro')) {
    let btnDel = doc.querySelectorAll('.btnCadastro');
    for(let i=0; i < btnCadastro.length; i++) {
        btnCadastro[i].addEventListener('click', function(event){
            alert('Usuário cadastrado com sucesso!')
        });
    }
}