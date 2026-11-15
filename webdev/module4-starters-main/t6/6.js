"use strict";

// Access the element
let buttonAlert=document.getElementsByTagName("button");
console.log(buttonAlert.length) //getElementsByTagName() always returns an HTMLCollection, even if it contains only one element.

for( let i=0; i<buttonAlert.length;i++){
    if(i==0){
        buttonAlert[0].addEventListener("click", function(){
            alert("Button Clicked");
        });
    }
}



/* 
we can access an HTML element using its **tag name** with `document.getElementsByTagName()`.

For example:

**HTML:**

```
<button>Click Me</button>
```

**JavaScript:**

```
"use strict";

// Access button using its tag name
let myButton = document.getElementsByTagName("button");

// Add click event listener
myButton[0].addEventListener("click", function() {
    alert("Button Clicked");
});
```

### **Why do we use&#x20;**`[0]`**?**

`getElementsByTagName("button")` returns an **HTMLCollection**, which can contain multiple button elements.

- `myButton[0]` → First button.
- `myButton[1]` → Second button.
- `myButton[2]` → Third button.

### **Alternative: querySelector()**

You can also use:

```
let myButton = document.querySelector("button");

myButton.addEventListener("click", function() {
    alert("Button Clicked");
});
```

| Method                           | Returns                            |
| -------------------------------- | ---------------------------------- |
| `getElementsByTagName("button")` | HTMLCollection (multiple elements) |
| `querySelector("button")`        | First matching element             |
| `querySelectorAll("button")`     | NodeList (all matching elements)   |

** Use `document.querySelector("button")` when we want to select only the first button by its tag name. It is simple and convenient.

*/