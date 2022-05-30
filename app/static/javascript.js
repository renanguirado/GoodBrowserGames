(function (win,doc){
    'use strict';
    
    if(doc.querySelector('.btnDel')) {
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++) {
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Tem certeza que deseja apagar?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }

    if(doc.querySelector('.btnSucess')) {
        let btnSucess = doc.querySelectorAll('.btnSucess');
        for(let i=0; i < btnSucess.length; i++) {
            btnSucess[i].addEventListener('click', function(event){
                if(confirm('Tem certeza que deseja avaliar?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }

    
    
})(window, document);