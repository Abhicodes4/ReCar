function myFn(){
    fetch('https://catfact.ninja/fact')
      .then(response => response.json())
      .then(data => 
        
        {
            console.log(data)

            document.getElementById("a").innerHTML=data.fact
            
           
         }
         
         )

      
}

function myFn1(){
  fetch('https://dog.ceo/api/breeds/image/random')
    .then(response => response.json())
    .then(data2 => 
      
      {
          console.log(data2.message)

          document.getElementById("b").src=data2.message
          
         
       }
       
       )

    
}