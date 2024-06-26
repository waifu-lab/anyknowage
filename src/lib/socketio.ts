import { io, Socket } from 'socket.io-client'

let instance: Socket | null = null

export function setup_socketio() {
	if (!instance) {
		instance = io(JSON.parse(localStorage.getItem('default') as string).server_url)
	}
	return instance
}

export function get() {
	return instance
}

export function close() {
	if (instance) {
		instance.close()
	}
}

export default {
	setup_socketio,
	get,
	close
}
