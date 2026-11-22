
"use strict";

/* ACCESSING THE VALUE OF ELEMENTS */
    const form=document.getElementById("form1");
    const result=document.getElementById("result")
    form.addEventListener("submit", async function(event) {
        /* prevents from reloading */
        event.preventDefault(); 

        /* Getting value from user form */
        let number = document.getElementById("textbox1").value;
        if(number===""){
            result.textContent="Please enter number at first";
            return;
        }
        try{
             /* sending Ajax request to the flask */
        const response=await fetch("/prime",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                number:number
            })
        });

        /* Receive the json response from Flask*/
        const data=await response.json();

        //Display error message first
        if(!response.ok){
            result.textContent=`${data.error}`;
            return;
        }

        /* Display the result*/
        if(data.isPrime){
            document.getElementById("result").textContent=`${data.number} is a Prime Nuber`;
        }
        else{
            document.getElementById("result").textContent=`${data.number} is not a Prime`;
        }

        }catch(error){
            result.textContent="Unable to connect the server";
        }
       
    });
