import { Axios } from 'axios'
import { useEffect } from 'react'

export function API(){
    useEffect(()=>{
        Axios.get("https://sampleapis.com/futurama/api/characters").then((rep)=>{
            console.log(rep)
        })
    })
}