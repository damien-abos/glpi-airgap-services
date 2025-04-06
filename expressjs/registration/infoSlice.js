import { createSlice } from "@reduxjs/toolkit"
import { readFile } from 'node:fs/promises'
import registrationInfoState from '../data/registrationInfo.json' with { type: 'json' }

const registrationInfoPath = 'data/registrationInfo.json'

// const registrationInfoReadFile = () => readFile(registrationInfoPath, { encoding: 'utf8' })
//         .then((valueBuffer) => {
//             const str = String(valueBuffer)
//             return JSON.parse(str)
//         })

// const registrationInfoWriteFile = createAsyncThunk('registrationInfo/writeFile', () => {
//     return writeFile(registrationInfoPath, state.)
// })

const infoSlice = createSlice({
    name: "registrationInfo",
    initialState: registrationInfoState,
    // initialState: registrationInfoReadFile(),
    reducers: {
        infoUpdated(state, action) {
            state.registrationInfo.key = action.payload.key || state.registrationInfo.key
            state.registrationInfo.is_valid = action.payload.is_valid || state.registrationInfo.is_valid
            state.registrationInfo.owner.name = action.payload.owner.name || state.registrationInfo.owner.name
            state.registrationInfo.subscription.offer_reference = action.payload.subscription.offer_reference || state.registrationInfo.subscription.offer_reference
            state.registrationInfo.subscription.title = action.payload.subscription.title || state.registrationInfo.subscription.title
            state.registrationInfo.subscription.is_running = action.payload.subscription.is_running || state.registrationInfo.subscription.is_running
            state.registrationInfo.subscription.begin_date = action.payload.subscription.begin_date || state.registrationInfo.subscription.begin_date
            state.registrationInfo.subscription.end_date = action.payload.subscription.end_date || state.registrationInfo.subscription.end_date
            state.registrationInfo.subscription.features = action.payload.subscription.features || state.registrationInfo.subscription.features
        }
    }
})

export const { infoUpdated } = infoSlice.actions
export default infoSlice.reducer