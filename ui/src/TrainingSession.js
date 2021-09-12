import { useEffect, useState } from 'react'

function TrainingSession() {
	const [flashcards, setFlashcards] = useState([])
	const [session, setSession] = useState()

	useEffect(() => {
		fetch('http://localhost:5000/api/training', {
			method: 'GET',
		})
			.then(resp => resp.json())
			.then(data => {
				setSession(data)
			})
	}, [])

	return (
		<>
			<button
				className="border rounded-lg shadow p-3 bg-green-500 hover:bg-green-700 text-white mt-2"
				onClick={() => createSession()}>
					Create session
			</button>
			<div className="my-4 text-gray-700">
				{session && <h1>Practice session {session.id}.</h1>}
			</div>
		</>
	)

	function createSession() {
		fetch('http://localhost:5000/api/training', {
				method: 'POST'
			})
			.then(resp => resp.json())
			.then(data => {
				setSession(data)
			})
	}
}

export default TrainingSession
