import axios from 'axios'

type Filetype = {
	fileid: string
	filename: string
	time: Date
	size: number
}

interface Element {
	file_id: string
	name: string
	time: { $date: string }
	filesize: number
}
export const load = async () => {
	const getfilelist = async () => {
		try {
			// 好醜 但算了
			const data = await axios.get('http://localhost:8000/files')
			const files: Filetype[] = []
			data.data.forEach((element: Element) => {
				files.push({
					fileid: element.file_id,
					filename: element.name,
					time: new Date(element.time.$date),
					size: element.filesize
				})
			})
			return files
		} catch (e) {
			console.error(e)
			throw new Error(`Failed to fetch posts`)
		}
	}

	return {
		posts: getfilelist
	}
}
