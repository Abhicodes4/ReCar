function myFn(){
    fetch('http://127.0.0.1:8000/carsapi/?format=json')
      .then(response => response.json())
      .then(data => 
        
        {
            console.log(data)

            document.getElementById("a").innerHTML=data.name
            document.getElementById('c').src=data.image
            document.getElementById('b').innerHTML=data.company
            document.getElementById('d').innerHTML=data.year
            document.getElementById('d').innerHTML=data.kilometer
            document.getElementById('d').innerHTML=data.ownership
            document.getElementById('d').innerHTML=data.transmission
            document.getElementById('e').innerHTML=data.price
                 
            
           
         }
         
         )

      
}