import type { PageLoad } from './$types'
import axios from 'axios'
import toast from 'svelte-french-toast'

export const load = (async () => {
	const server_url = JSON.parse(localStorage.getItem('default') as string).server_url
	const getchats = async (pos: number) => {
		try {
			const data = await axios.get(server_url + '/chats')
			return data.data
		} catch (e) {
			console.error(e)
			toast.error('Cannot connect to server', {
				position: 'top-right',
				style: 'background: var(--background); color: var(--foreground);'
			})
			throw new Error(`Failed to fetch posts`)
		}
	}

	const chat = async (question: string) => {
		try {
			const setting = JSON.parse(localStorage.getItem('chat') as string)
			const body = {
				model: {
					model: setting.model
				},
				question: question,
				maxtoken: setting.maxtoken,
				token: setting.openaikey
			}
			const data = await axios.post(server_url + '/chat', body)
			return data.data
		} catch (e) {
			console.error(e)
			toast.error('Cannot connect to server', {
				position: 'top-right',
				style: 'background: var(--background); color: var(--foreground);'
			})
			throw new Error(`Failed to post text`)
		}
	}
	return {
		chats: getchats,
		chat: chat
	}
}) satisfies PageLoad
