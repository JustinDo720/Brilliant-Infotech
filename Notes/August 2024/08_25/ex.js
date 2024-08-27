fac = (num)=>{
    // We're going to multiple this number with it's predecessor 
    let result = 1
    while(num > 1){
        // Because result is 1 by default, it will "become" the number first 
        result *= num
        num--
    }
    return result
}

console.log(fac(5))


prime = (num)=>{
    if(num % 2 == 0){
        return 'Prime'
    } else {
        return 'Odd'
    }
}

console.log(prime(3))