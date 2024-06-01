import type { PageLoad } from './$types'
import axios from 'axios'

export const load = (async () => {
	const getchats = async (pos: number) => {
		try {
			console.log(pos)
			const data = await axios.get('http://localhost:8000/chats')
			return data.data
		} catch (e) {
			console.error(e)
			throw new Error(`Failed to fetch posts`)
		}
	}

	const chat = async (question: string) => {
		try {
			const body = {
				model: {
					model: 'gpt-4o'
				},
				question: question
			}
			const data = await axios.post('http://localhost:8000/chat', body)
			return data.data
		} catch (e) {
			console.error(e)
			throw new Error(`Failed to fetch posts`)
		}
	}
	return {
		chats: getchats,
		chat: chat
	}
}) satisfies PageLoad
