const logs: string[] = []

export function pushlog(message: string) {
	logs.push(message)
}

export function get_logs() {
	return logs
}

export default {
	pushlog,
	get_logs
}
