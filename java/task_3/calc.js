const firstInput = document.getElementById("firstInput")
const secondInput = document.getElementById("secondInput")
const plus = document.getElementById("plus")
const minus = document.getElementById("minus")
const multiply = document.getElementById("multiply")
const division = document.getElementById("division")
const calculate = document.getElementById("calculate")
const result = document.getElementById("result")
let operation = "+"

// console.log(Number(firstInput.value) + Number(secondInput.value))

plus.onclick = function() {
    operation = "+"
}

minus.onclick = function() {
    operation = "-"
}

multiply.onclick = function() {
    operation = "*"
}

division.onclick = function() {
    operation = "/"
}

function getResult(value) {
    if (value < 0) {
        result.style.color = 'red'
    } else {
        result.style.color = 'green'
    }
    result.textContent = value
}

calculate.onclick = function() {
    if (operation == "+") {
        const sum = Number(firstInput.value) + Number(secondInput.value)
        getResult(sum)
    } else if (operation == "-") {
        const diff = Number(firstInput.value) - Number(secondInput.value)
        getResult(diff)
    } else if (operation == "*") {
        const diff = Number(firstInput.value) * Number(secondInput.value)
        getResult(diff)
    } else if (operation == "/") {
        const diff = Number(firstInput.value) / Number(secondInput.value)
        getResult(diff)
    }
}