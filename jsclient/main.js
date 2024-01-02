const ContentContainer = document.getElementById('product-container');
const baseEndpoind = "http://127.0.0.1:8000/api/"
const loginForm = document.getElementById('login-form')
const access = "eyJhbGciOiJIUzI1NiJ9.e30.soPmlTaN7FsJFVYfvFllD69nHLxxTGF-3VmauHW0jxQ"
console.log(ContentContainer)

console.log(baseEndpoind)


// if (loginForm) {

//     loginForm.addEventListener('submit',handleLogin)
// }


function handleLogin(){
    console.log()
    
    const loginEndpoint = `${baseEndpoind}token/`
    
    const loginObjectData = {
            "email" : "fahimuhammedfahimkp@gmail.com",
            "password":"f8921212828"
    }
    console.log(JSON.stringify(loginObjectData)) 

    console.log(loginObjectData)

 
    fetch(loginEndpoint,{
        method : "POST",
        headers : {
            'Content-Type': 'application/json',
        },
        body:JSON.stringify(loginObjectData)
    

    })
    .then(response => {
        if (!response.ok) {


            // writeToContent(error=response.code)

            // throw new Error(`HTTP error! Status: ${response.status}`);
            
        }
        return response.json();
    })
    .then(authData =>{
        handleAuthData(authData,getProduct)
    })
    .catch(error => {
        // Handle errors here
        console.log('Error:', error);
      
    });



}


function handleAuthData(authData,callback){
    localStorage.setItem('access',authData.access)
    localStorage.setItem('refresh',authData.refresh)
    if(callback){
        callback()
    }
}


function writeToContent(data){

    if (ContentContainer) {
        // alert(ContentContainer);
        console.log('hai');
        if (data){
            ContentContainer.innerHTML = "<pre>" + JSON.stringify(data,null,4); + "</pre>"
            // ContentContainer.innerHTML = "<pre>" + data + "</pre>"
        
        }
        else {
            ContentContainer.innerHTML = "";
        }
        // else{
        //     ContentContainer.innerHTML = "";
        // }

        
    }
}


function isTokenNotValid(jsonData){

    if (jsonData.code && jsonData.code === "token_not_valid" ){

        alert('TOKEN NOT VALID ,Please Login Again')
        return false
    }
    return true
}


function getProduct(){
    const endpoint = `http://127.0.0.1:8000/api/user/4af9605d-3960-44c4-b114-8c736c3f02b8/`
    const Options  = getFtechOptions()
    fetch(endpoint,{

        method :  "GET",
        headers: {
            'Content-Type':'application/json',
            'Authorization':`Bearer ${localStorage.getItem('access')}`
        },
       

    })
    .then(response => response.json())
    .then(data =>{
    
        writeToContent(data);
    })
   
}



function validateJWT(){
    const endpoint = `${baseEndpoind}token/verify/`
    const Options  = {
        method: "POST" ,
        headers: {
            "Content-Type":"application/json"
        },
        body: JSON.stringify({
            token: localStorage.getItem('access')
        })
    }
    fetch(endpoint,Options)
    .then(response => response.json())
    .then(expection_data =>{
        console.log(expection_data);
        // refresh 
    })
   
}





// getProduct()
// writeToContent('');


function getFtechOptions(method,jsObject){
    return {
        method :  method === null ? "GET" :method ,
        headers: {
            'Content-Type':'application/json',
            'Authorization':`Bearer ${access}`
        },
        body: jsObject ? JSON.stringify(jsObject)  : null
    }
}

handleLogin()

// getProduct()

// validateJWT();