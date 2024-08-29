
function Demo(props){

    let a = 10
    let result = ""
    if(a % 2 ==0){
        result='even'
    } else {
        result = 'odd'
    }

    // condition?output1:output2

    return(
        <>
            <p>This is a Demo Componenet</p>
            <p>{a%2==0?'even':'odd'}</p>
            <p>{a%2==0 && 'Even'}</p>
            <p>{props}</p>
        </>
    )
}
// orr export like this and dont need to use { }
export default Demo
