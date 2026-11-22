
"use strict";

/* ACCESSING THE VALUE OF ELEMENTS */
    const form=document.getElementById("form1");
    const result=document.getElementById("result")
    form.addEventListener("submit", async function(event) {
        /* prevents from reloading */
        event.preventDefault(); 

        /* Getting value from user form */
        let number = document.getElementById("textbox1").value;
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

        /* Display the result*/

        if(data.isPrime){
            document.getElementById("result").textContent=`${data.number} is a Prime Nuber`;
        }
        else{
            document.getElementById("result").textContent=`${data.number} is not a Prime`;
        }

        /* if(number<0){
            result.textContent="Please Enter a whole number(0 or more)";
            return;
        }
        try{

            //Sending number to the flask backend
            console.log(number);
            const response=await fetch(`/prime?number=${number}`);
            if(!response.ok){
                throw new Error("server error: " +response.status);
            }
            const data= await response.json(); //parse the json reply

            if (data.isPrime){
                result.textContent=`${data.Number} is a prime number.`;
            }
            else {
                result.textContent=`${data.Number} is not a prime number.`;
            }
        }catch(error){
            result.textContent="Could not reach the Server";
        } */
        console.log(number);
    });
