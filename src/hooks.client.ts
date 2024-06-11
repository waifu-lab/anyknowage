import { setup_socketio } from '$lib/socketio'
import toast from 'svelte-french-toast'
if (localStorage.getItem('default') === null) {
	localStorage.setItem(
		'default',
		JSON.stringify({
			server_url: 'http://localhost:8000',
			username: 'user',
			avatar: 'https://cdn.discordapp.com/avatars/762484891945664542/a3d0e4d30b78ce30a2ed22b51bf80df4.png?size=1024',
			botavatar:
				'https://cdn.discordapp.com/avatars/762484891945664542/a3d0e4d30b78ce30a2ed22b51bf80df4.png?size=1024'
		})
	)
}
if (localStorage.getItem('chat') === null) {
	localStorage.setItem(
		'chat',
		JSON.stringify({
			model: 'gpt-4o',
			maxtoken: 2000,
			openaikey: ''
		})
	)
}
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
