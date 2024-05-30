// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
export const prerender = true

import { browser } from '$app/environment'
import axios from 'axios'

export const load = async () => {
	const getposts = async () => {
		if (browser) {
			try {
				const data = await axios.get('http://localhost:8000/files')
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
		posts: getposts()
	}
}
