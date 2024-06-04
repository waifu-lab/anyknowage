import type { PageLoad } from './$types'
import axios from 'axios'
import toast from 'svelte-french-toast'

export const load = (async () => {
	const getchats = async (pos: number) => {
		try {
			const data = await axios.get('http://localhost:8000/chats')
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
			const data = await axios.post('http://localhost:8000/chat', body)
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
