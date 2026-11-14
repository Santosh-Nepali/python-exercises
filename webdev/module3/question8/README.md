Let's break this code into small parts so you understand exactly how `addEventListener()` works.

```
addBtn.addEventListener("click", function () {
    // Your code here
});
```

## **1. What does&#x20;**`addEventListener()`**&#x20;mean?**

`addEventListener()` is a JavaScript method that waits for a specific event to happen on an HTML element.

In your example, it waits for the user to click the Add String button.

## **2. Understand each part**

```
addBtn.addEventListener("click", function () {
```

| Code                 | Explanation                                                 |
| -------------------- | ----------------------------------------------------------- |
| `addBtn`             | A variable that references your HTML button.                |
| `.`                  | Accesses a method or property of an object.                 |
| `addEventListener()` | Registers an event handler.                                 |
| `"click"`            | The event JavaScript should listen for.                     |
| `function ()`        | An anonymous function that executes when the event happens. |
| `{ }`                | Contains the code that executes after the click.            |

## **3. How does it work in your application?**

First, you select the HTML button:

```
const addBtn = document.getElementById("addBtn");
```

Your HTML:

```
<button id="addBtn">Add String</button>
```

Then you attach an event listener:

```
addBtn.addEventListener("click", function () {
    console.log("Button clicked!");
});
```

**Try it yourself**

# **0**

Button clicks

Click Me!Reset

Each click triggers the event handler and increases the counter.

## **4. Why use&#x20;**`function ()`**&#x20;instead of calling a function directly?**

There are two ways to write an event listener.

**Method 1: Anonymous function**

```
addBtn.addEventListener("click", function () {
    console.log("Hello!");
});
```

**Method 2: Named function**

```
function addString() {
    console.log("Hello!");
}

addBtn.addEventListener("click", addString);
```

Both work.

Notice the difference:

- `addString` passes the function to the event listener.
- `addString()` calls the function immediately.

This is a very important concept in JavaScript.

## **5. Other common events**

| Event         | When it happens                      |
| ------------- | ------------------------------------ |
| `"click"`     | User clicks an element               |
| `"input"`     | User changes input text              |
| `"change"`    | Input value is changed and committed |
| `"mouseover"` | Mouse moves over an element          |
| `"mouseout"`  | Mouse leaves an element              |
| `"keydown"`   | User presses a keyboard key          |
| `"submit"`    | User submits a form                  |

## **Short summary**

Remember this structure:

```
element.addEventListener("event", function () {
    // Code to execute
});
```

Think of `addEventListener()` as telling JavaScript:

**"Wait for this event. When it happens, execute this function."**

This is one of the most important concepts for building interactive websites with JavaScript.
