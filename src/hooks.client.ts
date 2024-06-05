import { setup_socketio } from '$lib/socketio'
import toast from 'svelte-french-toast'
const io = setup_socketio()
io.on('connect', () => {
	console.log('connected')
	toast.success('success connect to server', {
		position: 'top-right',
		style: 'background: var(--background); color: var(--foreground);'
	})
})
io.on('connect_error', () => {
	console.error('connect_error')
	if (!io.active) {
		toast.error('Cannot connect to server', {
			position: 'top-right',
			style: 'background: var(--background); color: var(--foreground);'
		})
	}
})
