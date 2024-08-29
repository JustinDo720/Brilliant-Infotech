const display2= async()=>{
    let data = await fetch('api_link')
    return data
}

console.log(1)
console.log(display2())
console.log(2)