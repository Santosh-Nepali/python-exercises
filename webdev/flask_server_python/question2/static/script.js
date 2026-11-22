
"use strict";

/* ACCESSING THE VALUE OF ELEMENTS */
    const form=document.getElementById("form1");
    const result=document.getElementById("result")
    form.addEventListener("submit", async function(event) {
        /* prevents from reloading */
        event.preventDefault(); 

        /* Getting value from user form */
        let word = document.getElementById("textbox1").value.trim();

        if(word===""){
            result.textContent="Please Enter an English word!!";
            return;
        }

        try{
            /* sending Ajax request to the flask */
            const response=await fetch(`/translateEnglishFinnish/${encodeURIComponent(word)}`);
            
            /* Receive the json response from Flask*/
            const transData=await response.json();

            if(!response.ok){
                result.textContent=`${transData.error}`;
                return;
            }
                 /* Display the result*/
            document.getElementById("result").textContent=``;
            document.getElementById("result").textContent=`Finnish word is : ${transData.finnish}`; 
        }catch(error){
            result.textContent="Unable to connect the server";
        }
    });
