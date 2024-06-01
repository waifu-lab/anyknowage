import axios from 'axios'

export const load = async () => {
	const getposts = async (pos: number) => {
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

	const addfileunit8 = async (files: Uint8Array, filename: string) => {
		try {
			if (files === null) return
			const body = new FormData()
			body.append('file', new Blob([files]), filename)
			await axios.post('http://localhost:8000/upload', body, {
				headers: {
					'Content-Type': 'multipart/form-data'
				}
			})
		} catch (e) {
			console.error(e)
			throw new Error(`Failed to post file`)
		}
	}

	return {
		posts: getposts,
		posttext: postext,
		addfile: addfileunit8
	}
}
