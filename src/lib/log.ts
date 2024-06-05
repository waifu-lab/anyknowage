type Log = {
	message: string
}

const logs: Log[] = []

export function pushlog(message: Log) {
	logs.push(message)
}

export function get_logs() {
	return logs
}

export default {
	pushlog,
	get_logs
}
