import axios from 'axios'

export const load = async () => {
	const getfilelist = async (pos: number) => {
		try {
			const data = await axios.get('http://localhost:8000/files')
			return data.data
		} catch (e) {
			console.error(e)
			throw new Error(`Failed to fetch posts`)
		}
	}

	return {
		posts: getfilelist
	}
}
