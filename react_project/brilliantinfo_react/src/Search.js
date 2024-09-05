import {useState} from "react";

export function Search(){
    /* Important that state starts as a String to use the toLowerCase() string function during the comparison phase */
    const [searched_term, searching] = useState('')
    // List of available items to search for
    const names = ['Muffin', 'Blue', 'Logan', 'Jacob', 'Snow', 'Thy',]

    return <>
        Searched Term: { searched_term }
        <br/>
        <input type='text' value={searched_term}
               onChange={(e)=>{searching(e.target.value)}}
               placeholder="Searched Term"
        />

        {/* Displaying an array */}
        {/*<ul style={{listStyleType:'none', marginLeft: 0}}>*/}
        {/*    {names.map(name => <li> {name} </li>)}*/}
        {/*</ul>*/}
        {/* Filtering Item */}
        {/*<ul>*/}
        {/*    {names.filter(name => {*/}
        {/*        if(name.toLowerCase().includes(searched_term.toLowerCase())){*/}
        {/*            return <li>{name}</li>*/}
        {/*        }*/}
        {/*    }).map((name, index) => (*/}
        {/*        <ul style={{listStyleType:'none', marginLeft: 0}}>*/}
        {/*            {names.map(name => <li> {name} </li>)}*/}
        {/*        </ul>*/}
        {/*    ))}*/}
        {/*</ul>*/}
        { names.filter(name =>
            name.toLowerCase().includes(searched_term.toLowerCase())).map((name,index)=>(
                <li key={index}> {name } </li>
        ))}

    </>
}