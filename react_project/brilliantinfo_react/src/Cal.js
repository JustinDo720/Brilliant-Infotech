import { useState } from 'react'

function Calculator(){
    const [result, updateResult] = useState(0)
    const [num1, updateNum1] = useState('')
    const [num2, updateNum2] = useState('')


    const calculate = (operation, num1, num2)=>{
        switch (operation) {
            case 'add':
                {/* Numer() is basically int() */}
                updateResult(Number(num1) + Number(num2)); // adding 
              break;
            case 'sub':
                updateResult(num1 - num2); // subtracting 
              break;
            case 'mul':
              updateResult(num1 * num2); // multiplying by 
              break;
            case 'div':
              updateResult(num1 / num2); // dividing
              break;
            default:
              console.log('Invalid operation');
        }
    }

    return <>
        <h1> Result: {result} </h1>
        {/* Now because we're using a functoin wtih an argument you must use an arrow function */}
        <input type='number' value={num1} placeholder='First Number' onChange={(n) => {updateNum1(n.target.value)}}/> 
        <input type='number' value={num2} placeholder='Second Number' onChange={(n) => {updateNum2(n.target.value)}}/>

        <button onClick={() => {calculate('add', num1, num2)}}>
            +
        </button>
        <button onClick={() => {calculate('sub', num1, num2)}}>
            -
        </button>
        <button onClick={() => {calculate('mul', num1, num2)}}>
            *
        </button>
        <button onClick={() => {calculate('div', num1, num2)}}>
            /
        </button>
    </>
}

export default Calculator