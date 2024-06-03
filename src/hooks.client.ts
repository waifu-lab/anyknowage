import { setup_socketio } from '$lib/socketio'

const io = setup_socketio()
io.on('connect', () => {
	console.log('connected')
})
// export const handle = async ({ event, resolve }) => {}
