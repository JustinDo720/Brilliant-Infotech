import {useDispatch, useSelector} from 'react-redux'
import {inc_num, dec_num} from './actions'

export function App(){
  
  const MyState = useSelector((state)=>state.changeTheNumber)
  const dispatch = useDispatch()

  return <>
    <button onClick={dispatch(inc_num)}>Increment</button>
    <button onClick={dispatch(dec_num)}>Decrement</button>
  </>
}