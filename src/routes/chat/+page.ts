import type { PageLoad } from './$types'
import { browser } from '$app/environment'
import axios from 'axios'

export const load = (async () => {
	const getchats = async () => {
		if (browser) {
			try {
				const data = await axios.get('http://localhost:8000/chats')
				return data.data
			} catch (e) {
				console.error(e)
				throw new Error(`Failed to fetch posts`)
			}
		} else {
			return []
		}
	}

	return {
		chats: getchats()
	}
}) satisfies PageLoad
