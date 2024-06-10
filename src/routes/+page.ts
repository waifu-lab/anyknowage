import axios from 'axios'
import toast from 'svelte-french-toast'

export const load = async () => {
	const server_url = JSON.parse(localStorage.getItem('default') as string).server_url
	const getposts = async (pos: number) => {
		try {
			const data = await axios.get(server_url + '/files')
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

	const postext = async (text: string) => {
		try {
			if (text.length === 0) return
			if (text === null) return
			const body = {
				text: text
			}
			const data = await axios.post(server_url + '/text', body)
			toast.success('Post successfully', {
				position: 'top-right',
				style: 'background: var(--background); color: var(--foreground);'
			})
			return data.data
		} catch (e) {
			console.error(e)
			toast.error('upload data failed', {
				position: 'top-right',
				style: 'background: var(--background); color: var(--foreground);'
			})
			throw new Error(`Failed to post text`)
		}
	}

	const addfileunit8 = async (files: Uint8Array, filename: string) => {
		try {
			if (files === null) return
			const body = new FormData()
			body.append('file', new Blob([files]), filename)
			const data = await axios.post(server_url + '/upload', body, {
				headers: {
					'Content-Type': 'multipart/form-data'
				}
			})
			toast.success('Post successfully', {
				position: 'top-right',
				style: 'background: var(--background); color: var(--foreground);'
			})
			return data.data
		} catch (e) {
			console.error(e)
			toast.error('upload data failed', {
				position: 'top-right',
				style: 'background: var(--background); color: var(--foreground);'
			})
			throw new Error(`Failed to post file`)
		}
	}

	return {
		posts: getposts,
		posttext: postext,
		addfile: addfileunit8
	}
}
