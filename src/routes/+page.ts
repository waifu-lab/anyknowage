import axios from 'axios'

export const load = async () => {
	const getposts = async () => {
		try {
			const data = await axios.get('http://localhost:8000/files')
			return data.data
		} catch (e) {
			console.error(e)
			throw new Error(`Failed to fetch posts`)
		}
	}

	const postext = async (text: string) => {
		try {
			if (text.length === 0) return
			if (text === null) return
			const body = {
				text: text
			}
			const data = await axios.post('http://localhost:8000/text', body)
			return data.data
		} catch (e) {
			console.error(e)
			throw new Error(`Failed to post text`)
		}
	}

	return {
		posts: getposts(),
		posttext: postext
	}
}
