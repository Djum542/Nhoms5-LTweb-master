var updateBtns = document.getElementsByClassName('update-cart')
for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productname = this.dataset.product
        var action = this.dataset.action
        console.log('product', productId, 'action', action)
        console.log('USER', user)
        if (user == 'AnonymousUser') {
            console.log('not logged in')
        }else{
            // console.log('User in logged in, sending data')
            updateorder(producdname, action)
        }
    })
}

function updateorder(producdname, action){
    console.log('User in logged in, sending data')
    var url = '/cart/'
    fetch(url, {
        method:'POST',
        headers:{
            'content-Type':'Aplication/json'
        },
        body:JSON.stringify({'productname':producdname, 'action':action})
        .then((respose)=>{
            return respose.json()
        })
        .then((data) =>{
            console.log('data', data)
        })
    })
}