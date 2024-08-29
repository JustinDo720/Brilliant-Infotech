export function Upper(props){

    const display = ()=>{
        alert('welcome')
    }

    return(
        <>
            { props.my_str.toUpperCase() }
            <button onclick={display}>Click</button>
            <button onclick={()=>{alert('Alerting')}}>Click Aogain</button>
        </>
    )
}