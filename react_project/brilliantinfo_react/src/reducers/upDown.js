// How to do this action 
// Reducers will update the state (functions that take the ccurr state and actions)

const initialState = 0;

const changeTheNumber = (state=initialState, action)=>{
    switch(action.type){
        case 'INCREMENT':
            return state + 1
        case 'DECREMENT':
            return state - 1
        default:
            return state 
    }
}

export default changeTheNumber